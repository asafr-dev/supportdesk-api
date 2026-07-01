from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # keep a default for smooth local dev
    env: str = "local"
    database_url: str = "postgresql+psycopg://app:app@db:5432/supportdesk_api"
    log_level: str = "INFO"
    auto_create_db: bool = True
    seed_demo_data: bool = True


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    # Settings instantiated here (Pydantic v2 validation runs on instantiation).
    return Settings()  # type: ignore[call-arg]
