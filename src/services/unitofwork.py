from abc import ABC, abstractmethod

from lib.database import local_async_session_maker, remote_async_session_maker
from lib.repository import AbstractRepository
from repositories.brands import BrandRepository


class IUnitOfWork(ABC):
    brands: AbstractRepository

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError


class LocalUnitOfWork:
    def __init__(self):
        self.session_factory = local_async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()
        self.brands = BrandRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()


class RemoteUnitOfWork:
    def __init__(self):
        self.session_factory = remote_async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()
        self.brands = BrandRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
