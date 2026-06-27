"""Typed application configuration.

Settings are read from environment variables (prefixed with ``APP_``) or a local
``.env`` file. ``get_settings`` is cached so the configuration is parsed once.
"""

from functools import lru_cache
from importlib.metadata import version as distribution_version

from pydantic_settings import BaseSettings, SettingsConfigDict

# Name of this package's distribution, as declared in pyproject.toml.
DISTRIBUTION_NAME = "enterprise-ai-platform-api"


class Settings(BaseSettings):
    """Application settings, validated and typed via pydantic-settings."""

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file=".env",
        extra="ignore",
    )

    app_name: str = "Enterprise AI Platform API"
    environment: str = "development"

    # Async SQLAlchemy URL. Defaults to the local Compose Postgres (published port);
    # inside Compose the API overrides the host via APP_DATABASE_URL.
    database_url: str = "postgresql+asyncpg://app:app@localhost:5432/app"

    @property
    def version(self) -> str:
        """Application version.

        Derived from the installed package metadata (single source of truth:
        ``pyproject.toml``). It is a build artifact, not runtime configuration, so it
        is intentionally not overridable via the ``APP_`` environment layer.
        """
        return distribution_version(DISTRIBUTION_NAME)


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()
