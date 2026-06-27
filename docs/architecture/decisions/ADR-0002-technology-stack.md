# ADR-0002 — Core Technology Stack

- **Status:** Accepted
- **Date:** 2026-06-27
- **Deciders:** Lucas (author), Tech Lead (mentoring)
- **Technical context:** Release 1 — Architecture & Foundation

---

## Context and Problem

With the architectural style decided (modular monolith, ADR-0001), we need to choose
the concrete technologies for the foundation. These choices are **interdependent** —
backend language, web framework, frontend, and data stores are picked together — so
they are recorded in a single ADR rather than fragmented across many tiny ones.

> Note on granularity: the canonical rule is *one decision per ADR*. Here we bundle a
> cohesive set of stack choices made at the same time. If a single choice later needs
> revisiting (e.g. replacing the package manager), a focused ADR will **supersede** only
> that part of this one.

## Considered Options and Decisions

### Backend language — **Python 3.12** ✅
- Why: the Generative AI ecosystem is Python-first (LLM SDKs, LangGraph, Ragas,
  DeepEval, embeddings, MCP). The project's goal is to learn AI, so we go where the
  tooling is mature.
- Why 3.12 (not 3.13): 3.12 is stable with strong typing and performance; on 3.13 some
  AI libraries are still catching up.
- Rejected: staying on C#/.NET — would fight the ecosystem and miss the target job
  market.

### Python tooling — **uv** ✅
- Why: very fast dependency resolution and virtualenv management, single tool, lockfile
  for reproducible builds; it is becoming the community standard.
- Alternatives: **Poetry** (mature, slower, heavier), **pip-tools** (minimal, more
  manual). uv wins on speed and DX.
- Trade-off: younger than Poetry; ecosystem still maturing. Accepted — easy to migrate
  if needed.

### Web framework — **FastAPI** ✅
- Why: async-first, Pydantic-based validation, automatic OpenAPI docs, excellent for
  streaming (SSE) needed in Release 3.
- Alternatives: **Django** (batteries-included but heavier, sync-first heritage),
  **Flask** (minimal, less async/typing support). FastAPI fits an async AI API best.

### Frontend — **Next.js + TypeScript** ✅
- Why: a server runtime enables the **BFF (Backend-for-Frontend)** pattern for secure
  SSO (httpOnly cookies) and **SSR + token streaming** for chat (Release 3).
- Rejected: a pure SPA (Vite/React) — would force storing tokens in the browser (worse
  security) and lacks server-side streaming ergonomics.
- Note: SEO is **not** a reason here — the platform is internal and authenticated.

### Relational + vector store — **PostgreSQL (+ pgvector)** ✅
- Why: a single, battle-tested store for relational data, with the **pgvector**
  extension adding vector search (Release 8) without a new container.
- Alternatives: a dedicated vector DB from day one (**Qdrant**) — deferred until real
  need is measured (consistent with ADR-0001).

### Cache / sessions — **Redis** ✅
- Why: standard for sessions, caching, and rate limiting; also a lightweight queue if
  needed before RabbitMQ.

### Persistence layer — **SQLAlchemy (async) + Alembic** ✅
- Why: mature async ORM + versioned, reviewable database migrations.

### Validation / config — **Pydantic v2 + pydantic-settings** ✅
- Why: typed request/response models and typed, per-environment configuration.

## Consequences

- ➕ A coherent, modern, async, Python-first stack aligned with the AI job market.
- ➕ pgvector and Redis keep the container count low early on (see
  [C4 Level 2](../c4/level-2-container.md)).
- ➖ Some choices (uv, pgvector at scale) are less battle-tested than the most
  conservative alternatives. Accepted and revisitable via superseding ADRs.

## Related

- `docs/architecture/decisions/ADR-0001-modular-monolith.md`
- `docs/architecture/c4/level-2-container.md`
- `docs/plans/release-01-architecture-and-foundation.md`
