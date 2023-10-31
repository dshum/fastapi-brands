from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update, delete, cast
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):

    @abstractmethod
    async def list(self):
        raise NotImplementedError

    @abstractmethod
    async def get_settings(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def list(self):
        columns = []
        for column in self.model.__table__.columns:
            if column.key == 'settings':
                column = cast(column, JSONB)['settings'].label('settings')
            columns.append(column)

        query = select(*columns).order_by(self.model.name.asc())
        res = await self.session.execute(query)
        return res.mappings().all()

    async def get_settings(self):
        query = select(cast(self.model.settings, JSONB)['settings']).order_by(self.model.name.asc())
        res = await self.session.execute(query)
        return res.all()
