from pathlib import Path
from DEMON_AI._common.logging.logger_config import logger
from DEMON_AI._common.schemas.voice_schemas import AudioInputSchema

def main():
    logger.info("Testing started")
    try:
        # Absolute path use karo (Windows ke liye)
        test_file = Path("D:/DEMON/test.wav").resolve()
        
        # Validate schema
        AudioInputSchema(file_path=str(test_file), language="hi")
        logger.success("Schema validation passed")
    except Exception as e:
        logger.error(f"Schema failed: {str(e)}")
    
if __name__ == "__main__":
    main()