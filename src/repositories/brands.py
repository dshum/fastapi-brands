from typing import Optional, List

from sqlalchemy import select, column
from sqlalchemy.dialects.postgresql import JSONB

from lib.repository import SQLAlchemyRepository
from models.brands import Brand


class BrandRepository(SQLAlchemyRepository):
    model = Brand

    async def list(self):
        columns = []
        for column in self.model.__table__.columns:
            if column.key == 'settings':
                column = column['settings'].label('settings')
            columns.append(column)

        query = select(*columns).order_by(self.model.name.asc())
        res = await self.session.execute(query)
        return res.mappings().all()

    async def get_settings(self):
        query = select(self.model.settings['settings']).order_by(self.model.name.asc())
        res = await self.session.execute(query)
        return res.all()
