from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager, suppress

from fastapi import FastAPI

from .config import get_settings
from .db import get_engine, init_engine, session_scope
from .logging import configure_logging
from .middleware import RequestLoggingMiddleware
from .models import Base
from .routes.health import router as health_router
from .routes.tickets import router as tickets_router
from .seed import seed_if_empty
from .version import get_version


def create_app() -> FastAPI:
    configure_logging()
    settings = get_settings()

    @asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncIterator[None]:
        init_engine(settings.database_url)
        if settings.auto_create_db:
            Base.metadata.create_all(bind=get_engine())

        if settings.seed_demo_data:
            with session_scope() as db:
                seed_if_empty(db)

        yield

        with suppress(Exception):
            get_engine().dispose()

    app = FastAPI(
        title="SupportDesk API",
        version=get_version(),
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    app.add_middleware(RequestLoggingMiddleware)
    app.include_router(health_router)
    app.include_router(tickets_router)
    return app
