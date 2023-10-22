from typing import Optional, List

from sqlalchemy import select, column
from sqlalchemy.dialects.postgresql import JSONB

from lib.repository import SQLAlchemyRepository
from models.brands import Brand


class BrandRepository(SQLAlchemyRepository):
    model = Brand

    async def list_with_params(self, params: Optional[List[str]] = None):
        if params is None:
            params = []
        columns = [
            self.model.name,
            self.model.hosts,
            self.model.db_name,
            self.model.created_at
        ]
        for param in params:
            columns.append(self.model.settings['settings'][param].astext)
        query = select(*columns).order_by(self.model.name.asc())
        res = await self.session.execute(query)
        return res.all()

    async def list_with_settings(self):
        query = select(self.model.settings['settings']).order_by(self.model.name.asc())
        res = await self.session.execute(query)
        return res.all()

    async def get_by_name(self, name: str):
        query = select(self.model).where(self.model.name == name)
        res = await self.session.scalar(query)
        return res
