"""Health endpoints.

Two distinct probes (see Kubernetes semantics):

- **Liveness** (`GET /health`): "is the process alive?" — must NOT touch the database,
  so a transient DB outage never triggers a pointless container restart.
- **Readiness** (`GET /health/ready`): "is it ready to serve traffic?" — runs
  ``SELECT 1`` against the database; if it fails, the instance reports not-ready
  (503) and is pulled from the load balancer, but is NOT restarted.
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.platform.config import get_settings
from app.platform.database import get_db

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    """Response schema for the liveness endpoint."""

    status: str
    service: str
    environment: str
    version: str


class ReadyResponse(BaseModel):
    """Response schema for the readiness endpoint."""

    status: str
    database: str


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Liveness probe: basic service info, no external dependencies."""
    settings = get_settings()
    return HealthResponse(
        status="ok",
        service=settings.app_name,
        environment=settings.environment,
        version=settings.version,
    )


@router.get("/health/ready", response_model=ReadyResponse)
async def ready(session: Annotated[AsyncSession, Depends(get_db)]) -> ReadyResponse:
    """Readiness probe: verify the database is reachable with a trivial query."""
    try:
        await session.execute(text("SELECT 1"))
    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="database unavailable",
        ) from exc
    return ReadyResponse(status="ready", database="ok")
