import json
from datetime import datetime
from typing import Dict

from sqlalchemy import String, Text, DateTime, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from lib.database import Base
from schemas.brands import BrandDTO


class Brand(Base):
    __tablename__ = "brands"

    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    settings: Mapped[str] = mapped_column(JSONB)
    hosts: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(255))
    db_name: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def to_dto(self) -> BrandDTO:
        return BrandDTO(
            name=self.name,
            hosts=self.hosts,
            status=self.status,
            db_name=self.db_name,
            created_at=self.created_at.strftime("%Y-%m-%d"),
            settings=self.settings,
        )
