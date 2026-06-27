"""Tests for the health endpoints."""

from collections.abc import AsyncIterator
from typing import Any

from fastapi.testclient import TestClient
from sqlalchemy.exc import SQLAlchemyError

from app.main import app
from app.platform.database import get_db

client = TestClient(app)


def test_health_returns_ok() -> None:
    """Liveness: no database, always reports the service is alive."""
    response = client.get("/health")

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["service"]
    assert body["environment"]
    assert body["version"]


class _FakeSession:
    """Minimal stand-in for AsyncSession whose SELECT 1 succeeds."""

    async def execute(self, *args: Any, **kwargs: Any) -> None:
        return None


class _FailingSession:
    """Stand-in whose query raises, simulating a DB outage."""

    async def execute(self, *args: Any, **kwargs: Any) -> None:
        raise SQLAlchemyError("database down")


async def _ok_db() -> AsyncIterator[_FakeSession]:
    yield _FakeSession()


async def _failing_db() -> AsyncIterator[_FailingSession]:
    yield _FailingSession()


def test_ready_returns_ready_when_db_ok() -> None:
    app.dependency_overrides[get_db] = _ok_db
    try:
        response = client.get("/health/ready")
        assert response.status_code == 200
        assert response.json()["status"] == "ready"
    finally:
        app.dependency_overrides.clear()


def test_ready_returns_503_when_db_down() -> None:
    app.dependency_overrides[get_db] = _failing_db
    try:
        response = client.get("/health/ready")
        assert response.status_code == 503
    finally:
        app.dependency_overrides.clear()
