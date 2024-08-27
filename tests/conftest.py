import pytest_asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from src.main import app
from src.database import Base, get_db
from fastapi.testclient import TestClient

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)


# Фикстура для базы данных
@pytest_asyncio.fixture(scope="module")
async def db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session = TestingSessionLocal()
    try:
        yield async_session
    finally:
        await async_session.close()
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)


# Фикстура для клиента API
@pytest_asyncio.fixture(scope="module")
async def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()