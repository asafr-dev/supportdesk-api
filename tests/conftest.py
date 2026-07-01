from __future__ import annotations

import os
import tempfile
from collections.abc import Generator
from contextlib import suppress

import pytest
from fastapi.testclient import TestClient

from app.config import get_settings
from app.db import get_engine, init_engine
from app.factory import create_app
from app.models import Base


@pytest.fixture(autouse=True)
def _env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LOG_LEVEL", "WARNING")
    monkeypatch.setenv("AUTO_CREATE_DB", "true")
    monkeypatch.setenv("SEED_DEMO_DATA", "true")

    get_settings.cache_clear()  # type: ignore[attr-defined]


@pytest.fixture()
def client() -> Generator[TestClient, None, None]:
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    os.environ["DATABASE_URL"] = f"sqlite:///{path}"
    get_settings.cache_clear()  # type: ignore[attr-defined]

    init_engine(os.environ["DATABASE_URL"])
    Base.metadata.create_all(bind=get_engine())

    app = create_app()
    with TestClient(app) as c:
        yield c

    with suppress(OSError):
        os.remove(path)
