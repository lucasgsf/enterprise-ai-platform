# Release 1 — Architecture & Foundation

> **Status:** detailed plan (next step)
> **Goal:** design the architecture on paper and build the executable foundation of
> the platform — before any AI feature.
> **Guiding principle:** *design before building.*

---

## 1. Why this release exists

The entire platform will be stacked on the decisions made here. Getting the
foundation wrong means expensive rework in every later release. That is why R1 has two
distinct phases, in this order:

1. **Architecture on paper** — C4 model, bounded contexts, recorded decisions.
2. **Executable foundation** — monorepo, skeletons, Docker, minimal CI.

We only move to phase 2 once phase 1 is clear.

---

## 2. Phase 1 — Architecture on paper

### 2.1 Decision: Modular Monolith (and why not microservices)

The author comes from microservices in C#/.NET, so the instinct is to slice the
platform early. We **consciously challenge that.**

| Approach | Pros | Cons | Verdict |
|----------|------|------|---------|
| **Modular monolith** | Simple to run/debug; cheap to refactor boundaries; single deploy; AI focus | Scaling limit in a single process | ✅ **Chosen** |
| Microservices from day 1 | Independent scale/failure | Distributed complexity steals focus from AI learning | ❌ Too early |
| Hybrid (monolith + 1-2 services) | Extract only what hurts | Deciding early what to extract usually gets it wrong | ⏳ Maybe later |

**Evolution rule:** we extract a module into its own service (via RabbitMQ/events)
**only** when there is real, measured pain — independent scaling, failure isolation, or
a separate team. Not before.

### 2.2 C4 model (levels 1 and 2)

**Level 1 — Context:** Acme's *Enterprise AI Platform* serves internal users
(employees) who interact with AI over fictional corporate data (ERP, CRM, HR, etc.).
External actors: LLM providers (OpenAI, Anthropic, Gemini) and Acme systems
(GitHub, Jira, Slack — via MCP in R7).

**Level 2 — Containers:**
- **Frontend (Next.js):** UI + BFF (auth/SSO, secure proxy to the API).
- **API (FastAPI):** the modular monolith — all bounded contexts.
- **PostgreSQL:** relational data + pgvector (R8).
- **Redis:** cache, sessions, rate limiting.
- **(future) RabbitMQ, Qdrant, workers** — added when the relevant releases require them.

> Detailed C4 diagrams (with tooling) are a **task** of this phase — see §4.

### 2.3 Bounded Contexts → Releases map

The monolith modules are born aligned with the releases (see `00-roadmap.md`). The
backend folder structure reflects this map from R1, even if most start empty:

```
app/
  modules/
    identity/        # R2
    conversation/    # R3
    model_gateway/   # R4
    prompts/         # R5
    tooling/         # R6
    mcp/             # R7
    knowledge/       # R8 (RAG)
    agents/          # R9
  platform/          # cross-cutting: config, db, logging, observability, errors
  main.py
```

**Boundary rule:** a module talks to another only through an **explicit public
interface** (service/contract layer), never importing internals directly. This is what
makes future extraction into a microservice cheap.

### 2.4 Stack decisions to record (with trade-offs)

- **Python 3.12** — stable, good typing; 3.13 still has AI libraries catching up.
- **uv** (vs Poetry/pip-tools) — speed and emerging standard; reproducible lockfile.
- **Next.js + TypeScript** — BFF for secure SSO (httpOnly cookies) + SSR/token
  streaming in chat.
- **SQLAlchemy async + Alembic** — mature ORM + versioned migrations.
- **Pydantic v2 / pydantic-settings** — validation and typed config per environment.

---

## 3. Phase 2 — Executable foundation (scope)

Only **infrastructure/skeleton** code. No AI feature yet.

- **Monorepo** with `apps/api` (FastAPI) and `apps/web` (Next.js), plus `docs/`.
- **FastAPI skeleton:** `main.py`, healthcheck (`/health`), typed config, empty module
  structure (§2.3), structured logging.
- **Next.js skeleton:** base TypeScript project, home page, healthcheck.
- **Docker Compose:** services `api`, `web`, `postgres`, `redis` coming up together.
- **Minimal CI (GitHub Actions):** lint + type-check + tests (even if few) + image
  build. Runs on every PR.
- **Quality:** `ruff` (lint+format) for Python, `eslint`/`prettier` for the front,
  `mypy` for typing, `pytest` for tests.

---

## 4. Tasks (suggested order)

1. **[Architecture]** Write the C4 diagrams (levels 1-2) and ADRs for the decisions
   (modular monolith, stack). Save under `docs/architecture/`.
2. **[Setup]** Initialize git + monorepo + folder structure.
3. **[Backend]** FastAPI skeleton with `uv`, config, `/health`, empty modules.
4. **[Backend]** Postgres + Redis via Compose; async connection + Alembic.
5. **[Frontend]** Next.js + TypeScript skeleton + healthcheck consuming the API.
6. **[Infra]** `docker-compose.yml` orchestrating the 4 services.
7. **[CI]** GitHub Actions workflow: lint, type-check, test, build.
8. **[Quality]** Configure ruff/mypy/pytest and eslint/prettier.

---

## 5. Definition of Done

- [ ] ADRs and C4 diagrams written and reviewed.
- [ ] `docker compose up` brings up API, Web, Postgres, and Redis without errors.
- [ ] `GET /health` returns OK; the frontend can call the API.
- [ ] CI green on a PR (lint + type-check + test + build).
- [ ] README explains how to run locally.

---

## 6. What is NOT in this release

Authentication, chat, LLMs, RAG, agents — all of that belongs to later releases.
Resisting scope creep here is part of the architecture exercise.
