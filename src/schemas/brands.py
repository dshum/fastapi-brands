from typing import Optional, Dict, Any

from pydantic import BaseModel, Field


class BrandDTO(BaseModel):
    name: str
    hosts: str
    settings: Optional[Dict[str, Any]] = None
    db_name: str
    created_at: str = Field()

    class Config:
        from_attributes = True
