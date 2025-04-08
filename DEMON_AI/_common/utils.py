import psutil  
from typing import Optional  
from loguru import logger  
import sys

class ResourceManager:  
    """Optimized resource handling for low-RAM environments"""  
    
    @staticmethod  
    def enforce_ram_limit(max_usage: float = 0.85):  
        """Hard killswitch for memory management"""  
        current_usage = psutil.virtual_memory().percent / 100  
        if current_usage > max_usage:  
            logger.critical(f"Memory overuse detected: {current_usage:.0%}")  
            raise MemoryError("DEMON AI: System resources exceeded")  

    @staticmethod  
    def clear_memory_cache():  
        """Aggressive cache clearing for Python/Numpy"""  
        import numpy as np  
        np.savez_compressed("cache.npz")  # Force flush  
        if "torch" in sys.modules:  
            import torch  
            if torch.cuda.is_available():  
                torch.cuda.empty_cache()  