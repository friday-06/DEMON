"""  
DEMON AI Core Package
"""  
from pathlib import Path  

__version__ = "0.1.0-alpha"  
ROOT_DIR = Path(__file__).resolve().parent.parent  

__all__ = ["utils", "schemas", "logging"]  