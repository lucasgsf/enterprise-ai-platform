"""Application entry point.

Uses the application-factory pattern (`create_app`) so the app can be built with
different configurations in tests and at runtime. A lifespan handler disposes the
database engine on shutdown so connections are closed gracefully.
"""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.platform.config import get_settings
from app.platform.database import engine
from app.platform.health import router as health_router


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    """Manage startup/shutdown. On shutdown, dispose the engine's connection pool."""
    yield
    await engine.dispose()


def create_app() -> FastAPI:
    """Build and configure the FastAPI application."""
    settings = get_settings()
    app = FastAPI(title=settings.app_name, version=settings.version, lifespan=lifespan)
    app.include_router(health_router)
    return app


app = create_app()
