PYTHON ?= python
HOST ?= 127.0.0.1
PORT ?= 8080
PIP = $(PYTHON) -m pip

.PHONY: venv install dev host-test docker-test lint type docker-up docker-down format format-check check host-check

venv:
	$(PYTHON) -m venv .venv

install:
	$(PIP) install -U pip
	$(PIP) install -r requirements-dev.txt
	$(PIP) install --no-deps .

dev:
	$(PYTHON) -m uvicorn app.main:app --reload --host $(HOST) --port $(PORT) --ws websockets-sansio

host-test:
	$(PYTHON) -m pytest

docker-test:
	docker compose run --rm --build api-test

lint:
	$(PYTHON) -m ruff check .

type:
	$(PYTHON) -m mypy

docker-up:
	docker compose up -d --build

docker-down:
	docker compose down -v

format:
	$(PYTHON) -m ruff format .

format-check:
	$(PYTHON) -m ruff format --check .

host-check: format-check lint type host-test

check: docker-test
