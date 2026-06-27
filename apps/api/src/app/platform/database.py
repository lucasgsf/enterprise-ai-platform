"""Database access: async engine, session factory, and the FastAPI dependency.

We use SQLAlchemy 2.0's async API with the asyncpg driver. One session is created
per request (unit of work) and closed when the request ends, via the ``get_db``
dependency.
"""

from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app.platform.config import get_settings


class Base(DeclarativeBase):
    """Declarative base for ORM models. Its metadata is the target for Alembic."""


_settings = get_settings()

# ``pool_pre_ping`` checks a connection is alive before using it, avoiding errors
# from connections dropped by the database or a proxy.
engine = create_async_engine(_settings.database_url, pool_pre_ping=True)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> AsyncIterator[AsyncSession]:
    """Yield a database session scoped to a single request."""
    async with async_session_maker() as session:
        yield session
