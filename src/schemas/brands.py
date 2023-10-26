from typing import Optional, Dict, Any

from pydantic import BaseModel, Field


class BrandDTO(BaseModel):
    name: str
    hosts: str
    status: str
    db_name: str
    created_at: str = Field()
    updated_at: str = Field()
    settings: Optional[Dict[str, Any]] = None

    class Config:
        from_attributes = True
