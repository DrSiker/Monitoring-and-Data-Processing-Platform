from pydantic import BaseModel
from typing import Dict, Any

class MetadataSchema(BaseModel):
    filename: str
    schema: Dict[str, str]

class DataSchema(BaseModel):
    data: Dict[str, Any]
