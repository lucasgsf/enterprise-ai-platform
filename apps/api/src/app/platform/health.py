"""Health check endpoint.

A liveness probe used by Docker, Kubernetes, and load balancers to know the service
is up. Kept dependency-free on purpose: it must not touch the database or external
services, so it stays fast and reliable.
"""

from fastapi import APIRouter
from pydantic import BaseModel

from app.platform.config import get_settings

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    """Response schema for the health endpoint."""

    status: str
    service: str
    environment: str
    version: str


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Return basic service liveness information."""
    settings = get_settings()
    return HealthResponse(
        status="ok",
        service=settings.app_name,
        environment=settings.environment,
        version=settings.version,
    )
