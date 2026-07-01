from __future__ import annotations

import tomllib
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as pkg_version
from pathlib import Path


def get_version() -> str:
    try:
        return pkg_version("supportdesk-api")
    except PackageNotFoundError:
        pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
        if pyproject.exists():
            data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
            v = (data.get("project") or {}).get("version")
            if isinstance(v, str) and v:
                return v
            v = ((data.get("tool") or {}).get("poetry") or {}).get("version")
            if isinstance(v, str) and v:
                return v
        return "0.0.0"
