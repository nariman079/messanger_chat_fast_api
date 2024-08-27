from typing import AsyncGenerator, Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from config.settings import DB_USER, DB_PASSWORD, DB_PORT, DB_HOST, DB_NAME

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(
    DATABASE_URL,
    future=True,
    echo=True
)
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """ Dependency for getting async session """
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()



async def get_object(
        db: AsyncSession,
        obj: Base,
        by_field: str,
        search_value: str | int | float | bool
) -> Base:
    query = await db.execute(
        select(obj)
        .where(
            getattr(obj, by_field) == search_value
        )
    )
    db_object = query.scalar()
    return db_object

