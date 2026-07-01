# Repository structure

Purpose: a fast map of this repo for onboarding and “where does X go?”

## Directory map (trimmed)

```text
.
├── README.md  # Main entrypoint (what it is + quickstart + links)
├── LICENSE
├── Makefile
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── app/  # FastAPI application package
│   ├── factory.py
│   ├── main.py
│   ├── routes/
│   └── ...
├── docs/  # Longer-form docs
│   ├── STRUCTURE.md  # Repo map (you are here)
│   ├── API.md
│   ├── ARCHITECTURE.md
│   └── RELATIONSHIP_TO_SUPPORTDESK_APP.md
├── tests/  # Automated tests
│   └── conftest.py
└── .github/  # GitHub metadata (CI, automation)
    ├── workflows/
    ├── dependabot.yml
    └── CODEOWNERS
```

## Conventions (what goes where)

- `docs/`: canonical docs; README links here.
- `app/`: Python application package (FastAPI); treat as the import root.
- `tests/`: tests (unit/integration).
- `.github/`: CI + automation; keep workflow logic out of README.
