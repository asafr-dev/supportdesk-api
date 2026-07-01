<h1 align="center">SupportDesk API</h1>

<p align="center">
  FastAPI + Postgres service (demo) powering <a href="https://github.com/asafr-dev/supportdesk-admin-ui">SupportDesk Admin UI</a> — demonstrating service separation from <a href="https://github.com/asafr-dev/supportdesk-app">SupportDesk App</a> via a minimal reimplementation of the app’s ticketing slice as a standalone ticketing API.
</p>

<p align="center">
  <a href="https://codespaces.new/asafr-dev/supportdesk-api?quickstart=1"><img alt="Open in GitHub Codespaces" src="https://img.shields.io/badge/Open%20in-GitHub%20Codespaces-3e3e3e?logo=github&style=for-the-badge"></a>
  <a href="https://github.com/asafr-dev/supportdesk-api/actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/asafr-dev/supportdesk-api/ci.yml?branch=main&style=for-the-badge&label=CI"></a>
  <a href="https://github.com/asafr-dev/supportdesk-api/actions/workflows/codeql.yml"><img alt="CodeQL" src="https://img.shields.io/github/actions/workflow/status/asafr-dev/supportdesk-api/codeql.yml?branch=main&style=for-the-badge&label=CODEQL"></a>
  <a href="https://codecov.io/gh/asafr-dev/supportdesk-api"><img alt="Coverage" src="https://img.shields.io/codecov/c/github/asafr-dev/supportdesk-api/main.svg?style=for-the-badge&logo=codecov&label=coverage"></a>
  <a href="https://www.codefactor.io/repository/github/asafr-dev/supportdesk-api"><img alt="CodeFactor" src="https://img.shields.io/codefactor/grade/github/asafr-dev/supportdesk-api?branch=main&style=for-the-badge"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/github/license/asafr-dev/supportdesk-api?style=for-the-badge"></a>
</p>

## 🚀 Quickstart

### Requirements

- Linux
- Python 3.12+
- Docker

### Run locally

```bash
docker compose up --build
```

API docs: [http://localhost:8080/docs](http://localhost:8080/docs)

### Run via Codespaces

This repo ships a `.devcontainer` that uses the existing `docker-compose.yml`:

- DB and API start automatically
- Port 8080 is forwarded
- Dev dependencies are installed in the devcontainer

Open the repo in Codespaces, then hit: [http://localhost:8080/docs](http://localhost:8080/docs)

## 🧪 How to test

### Test locally

```bash
docker compose run --rm --build api-test
```

### Test via Codespaces

```bash
python -m pip install -r requirements-dev.txt
python -m pip install --no-deps .
python -m pytest
```

## 🗂️ Project structure

For the full directory map and “what goes where” conventions, see
[STRUCTURE.md](docs/STRUCTURE.md).

- `app/` – FastAPI app
- `app/routes/` – endpoints
- `tests/` – API tests
- `docker-compose.yml` – local DB + API
- `docs/` – longer-form documentation (architecture, API, etc)

## 📚 Documentation

See [documentation](docs/)

## 🤝 Contributing

See the [contributing guidelines](https://github.com/asafr-dev/.github/blob/main/CONTRIBUTING.md)

## 🔒 Security

See the [security policy](https://github.com/asafr-dev/.github/blob/main/SECURITY.md)

## 📄 License

See [LICENSE](LICENSE)
