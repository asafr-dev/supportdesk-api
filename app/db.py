from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

_engine: Engine | None = None
_session_maker: sessionmaker[Session] | None = None
_current_url: str | None = None


def init_engine(database_url: str) -> None:
    global _engine, _session_maker, _current_url
    if _engine is not None and _current_url == database_url:
        return

    connect_args: dict[str, Any] = {}
    if database_url.startswith("sqlite"):
        connect_args = {"check_same_thread": False}

    _engine = create_engine(database_url, pool_pre_ping=True, connect_args=connect_args)
    _session_maker = sessionmaker(
        bind=_engine, autoflush=False, autocommit=False, expire_on_commit=False
    )
    _current_url = database_url


def get_engine() -> Engine:
    if _engine is None:
        raise RuntimeError("DB engine not initialized. Call init_engine() at startup.")
    return _engine


@contextmanager
def session_scope() -> Iterator[Session]:
    if _session_maker is None:
        raise RuntimeError("DB engine not initialized. Call init_engine() at startup.")
    db = _session_maker()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def get_db() -> Iterator[Session]:
    with session_scope() as db:
        yield db
