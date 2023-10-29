from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

from lib import settings

__all__ = [
    "Base",
    "local_async_session_maker",
    "remote_async_session_maker",
    "get_async_session",
    "startup",
]

local_engine = create_async_engine(settings.db.LOCAL_URL, connect_args={}, echo=settings.db.ECHO)
remote_engine = create_async_engine(settings.db.REMOTE_URL, connect_args={}, echo=settings.db.ECHO)

local_async_session_maker = async_sessionmaker(local_engine, expire_on_commit=False)
remote_async_session_maker = async_sessionmaker(remote_engine, expire_on_commit=False)

Base = declarative_base()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with local_async_session_maker() as session:
        yield session


async def startup():
    async with local_engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    pass
