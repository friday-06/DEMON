from pydantic import BaseModel, Field, FilePath
from typing import Optional
import re  # Add this import

class AudioInputSchema(BaseModel):
    """Production validation schema for voice processing"""
    file_path: FilePath = Field(..., description="Absolute path to audio file")
    sample_rate: int = Field(16000, ge=8000, le=48000)
    bit_depth: int = Field(16, ge=8, le=32)
    language: str = Field(
        default="en",
        pattern=r"^(en|hi)$", 
        examples=["en", "hi"]
    )
    metadata: Optional[dict] = Field(None, example={"user_id": "DEMON_001"})