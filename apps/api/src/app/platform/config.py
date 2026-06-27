"""Typed application configuration.

Settings are read from environment variables (prefixed with ``APP_``) or a local
``.env`` file. ``get_settings`` is cached so the configuration is parsed once.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings, validated and typed via pydantic-settings."""

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file=".env",
        extra="ignore",
    )

    app_name: str = "Enterprise AI Platform API"
    environment: str = "development"
    version: str = "0.1.0"


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()
