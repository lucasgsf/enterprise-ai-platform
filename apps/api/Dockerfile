# syntax=docker/dockerfile:1

# ----------------------------------------------------------------------------
# Stage 1 — builder: install dependencies and the project into a virtualenv.
# Uses the official uv image (Debian slim + uv preinstalled).
# ----------------------------------------------------------------------------
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

# Compile .pyc ahead of time; copy (not hardlink) into the venv so it can be
# moved to the runtime stage cleanly.
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# Install ONLY dependencies first, so this layer is cached and not rebuilt when
# application source changes. --no-dev excludes pytest/ruff/mypy from the image.
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

# Now copy the source and install the project itself.
COPY src ./src
COPY README.md ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# ----------------------------------------------------------------------------
# Stage 2 — runtime: slim Python image with only the venv and source. No uv,
# no build tools, no dev dependencies. Runs as a non-root user.
# ----------------------------------------------------------------------------
FROM python:3.12-slim-bookworm AS runtime

# Non-root user (least privilege).
RUN groupadd --system app && useradd --system --gid app --create-home app

WORKDIR /app

# Bring over the prebuilt virtualenv and the application source.
COPY --from=builder --chown=app:app /app/.venv /app/.venv
COPY --from=builder --chown=app:app /app/src /app/src

# Put the venv on PATH and make Python logs unbuffered (better container logs).
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

USER app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
