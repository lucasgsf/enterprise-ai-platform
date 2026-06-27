"""Application entry point.

Uses the application-factory pattern (`create_app`) so the app can be built with
different configurations in tests and at runtime.
"""

from fastapi import FastAPI

from app.platform.config import get_settings
from app.platform.health import router as health_router


def create_app() -> FastAPI:
    """Build and configure the FastAPI application."""
    settings = get_settings()
    app = FastAPI(title=settings.app_name, version=settings.version)
    app.include_router(health_router)
    return app


app = create_app()
