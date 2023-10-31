from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def list(self):
        raise NotImplementedError

    @abstractmethod
    async def get(self, id: int):
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: int, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: int):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, data: dict):
        query = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(query)
        return res.scalar()

    async def list(self):
        query = select(self.model).order_by(self.model.id.desc())
        res = await self.session.scalars(query)
        return [row for row in res.all()]

    async def get(self, id: int):
        res = await self.session.get(self.model, id)
        return res

    async def update(self, id: int, data: dict):
        query = update(self.model).values(**data).filter_by(id=id)
        res = await self.session.execute(query)
        return res

    async def delete(self, id: int):
        query = delete(self.model).filter_by(id=id)
        res = await self.session.execute(query)
        return None
