# API — Enterprise AI Platform

Backend of the platform: a **modular monolith** built with Python 3.12 + FastAPI,
managed by [uv](https://docs.astral.sh/uv/).

## Layout

```
apps/api/
├── src/app/
│   ├── main.py            # application factory (create_app)
│   ├── platform/          # cross-cutting: config, health, (db/logging later)
│   └── modules/           # bounded contexts (mostly empty placeholders)
├── tests/
└── pyproject.toml
```

We use the **src layout**: the package lives under `src/`, so tests run against the
*installed* package, not files that happen to be in the current directory.

## Requirements

- Python 3.12
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Getting started

```bash
# from apps/api
uv sync                       # create venv and install deps (incl. dev group)
uv run uvicorn app.main:app --reload   # run the API at http://127.0.0.1:8000
```

Check it: <http://127.0.0.1:8000/health> and the docs at `/docs`.

## Health probes

- `GET /health` — **liveness** (no dependencies).
- `GET /health/ready` — **readiness** (runs `SELECT 1` against the database).

## Database & migrations

Async SQLAlchemy (asyncpg) + Alembic. Start a database first (`docker compose up -d
postgres` from the repo root), then:

```bash
# from apps/api
uv run alembic upgrade head      # apply migrations
uv run alembic revision -m "add X"   # create a new migration (autogenerate-ready)
uv run alembic downgrade -1       # roll back one revision
```

## Quality

```bash
uv run pytest        # tests
uv run ruff check .  # lint
uv run ruff format . # format
uv run mypy          # type-check
```
