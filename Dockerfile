FROM python:3.12.13-slim-trixie AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN set -eux; \
    for sources_file in /etc/apt/sources.list /etc/apt/sources.list.d/*.list /etc/apt/sources.list.d/*.sources; do \
        [ -e "$sources_file" ] || continue; \
        sed -i \
            -e 's|http://deb.debian.org|https://deb.debian.org|g' \
            -e 's|http://security.debian.org|https://security.debian.org|g' \
            "$sources_file"; \
    done; \
    apt-get update -o Acquire::Retries=3; \
    apt-get install -y --no-install-recommends git; \
    rm -rf /var/lib/apt/lists/*

RUN python -m pip install --no-cache-dir -U pip

COPY pyproject.toml README.md requirements.txt requirements-dev.txt ./
COPY app ./app

FROM base AS test
RUN python -m pip install --no-cache-dir -r requirements-dev.txt \
    && python -m pip install --no-cache-dir --no-deps .
COPY tests ./tests
CMD ["python", "-m", "pytest"]

FROM base AS runtime
RUN python -m pip install --no-cache-dir -r requirements.txt \
    && python -m pip install --no-cache-dir --no-deps .

EXPOSE 8080
CMD ["sh", "-c", "python -m uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080} --ws websockets-sansio"]
