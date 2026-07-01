# Stack

FastAPI + Postgres service for SupportDesk (Dockerized; deployable to Railway).

| Area             | Technologies                                           | Evidence                               |
| ---------------- | ------------------------------------------------------ | -------------------------------------- |
| Language/runtime | Python 3.12                                            | `.python-version`, `pyproject.toml`    |
| Web/API          | FastAPI • Uvicorn                                      | `pyproject.toml`, `app/`               |
| Data             | SQLAlchemy 2.x • PostgreSQL • psycopg                  | `pyproject.toml`, `docker-compose.yml` |
| Config/logging   | Pydantic Settings • python-json-logger        | `pyproject.toml`                       |
| Migrations       | Alembic (dev)                                          | `pyproject.toml`                       |
| Testing/QA       | pytest • pytest-cov • ruff • mypy • pre-commit • httpx | `pyproject.toml`, `tests/`             |
| Local dev        | Dockerfile • docker-compose (API + Postgres)           | `Dockerfile`, `docker-compose.yml`     |
| Dev env          | VS Code Dev Container / Codespaces                     | `.devcontainer/`                       |
| CI/Security      | GitHub Actions • CodeQL                                | `.github/workflows/*`                  |
| Deployment       | Railway (Dockerfile builder)                           | `railway.toml`                         |
