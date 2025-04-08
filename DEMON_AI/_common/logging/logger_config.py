from loguru import logger
import sys
from pathlib import Path

def configure_logging(log_dir: str = "logs"):
    """Fixed logging configuration for Windows"""
    try:
        log_path = Path(log_dir)
        log_path.mkdir(exist_ok=True, parents=True)
        
        # Remove default handler
        logger.remove()
        
        # Console handler
        logger.add(
            sink=sys.stderr,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{module}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
            level="INFO"
        )
        
        # File handler (Windows compatible filename)
        logger.add(
            sink=log_path / "demon_{time:YYYY-MM-DD_HH-mm-ss}.log",  # Colon replaced with -
            rotation="10 MB",
            compression="zip",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{function} - {message}",
            enqueue=True,
            backtrace=True,
            diagnose=True
        )
        
        logger.success("Logging initialized successfully")
    except Exception as e:
        logger.error(f"Failed to configure logging: {e}")
        raise

# Initialize with error handling
try:
    configure_logging()
except Exception as e:
    print(f"CRITICAL ERROR: {str(e)}")
    sys.exit(1)