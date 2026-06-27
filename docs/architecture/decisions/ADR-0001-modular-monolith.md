# ADR-0001 — Modular Monolith as the starting point

- **Status:** Accepted
- **Date:** 2026-06-27
- **Deciders:** Lucas (author), Tech Lead (mentoring)
- **Technical context:** Release 1 — Architecture & Foundation

---

## Context and Problem

The Enterprise AI Platform will be made of several independent domains (identity,
conversation, LLM gateway, RAG, agents, etc. — see `00-roadmap.md`). We need to decide
the **initial architectural style**: how are these domains packaged and deployed?

Two forces pull in opposite directions:

1. The author comes from **microservices in C#/.NET** — the instinct is to slice early.
2. The core goal of the project is to **learn Generative AI**, not distributed systems
   engineering. Every hour spent on distributed plumbing is an hour not spent on LLMs,
   RAG, and agents.

## Considered Options

### Option A — Modular Monolith (chosen)
A single FastAPI application, organized into **modules with explicit domain
boundaries** (internal bounded contexts). Inter-module communication happens only
through **public interfaces** (service/contract layer), never importing internals.

- ➕ Simple to run, debug, and test (one process, one deploy).
- ➕ Refactoring boundaries is cheap — we are still *discovering* the right limits.
- ➕ Keeps focus on learning AI.
- ➕ Well-designed boundaries allow **future extraction** into services.
- ➖ Scaling limit: everything scales together, in a single process.
- ➖ Boundary discipline relies on convention (no network barrier enforcing it).

### Option B — Microservices from day 1
Each bounded context is its own service, communicating over network/RabbitMQ.

- ➕ Independent scaling and failure isolation.
- ➕ Independent teams (irrelevant: we are a single author).
- ➖ High complexity: networking, eventual consistency, distributed observability,
  multi-service deploy, versioned contracts between services.
- ➖ That complexity **steals focus** from the real goal (AI).
- ➖ High risk of **getting the boundary wrong** too early (and a wrong boundary
  between services is very expensive to fix).

### Option C — Hybrid (monolith + 1-2 extracted services)
Start as a monolith and already extract, e.g., RAG workers.

- ➕ Extract only what hurts.
- ➖ Deciding *now* what to extract is guesswork; we would likely get it wrong.

## Decision

We adopt **Option A — Modular Monolith**.

The folder structure reflects the bounded contexts from the start
(`app/modules/<context>`), with inter-module communication only through public
interfaces. This gives us the organizational benefits of microservices **without** the
distributed cost.

## Evolution criteria (when to reconsider)

We extract a module into its own service (via RabbitMQ/events) **only** when there is
**real, measured pain**, for example:

- a proven need to **scale** a module independently of the others
  (e.g. RAG ingestion saturating CPU);
- a **failure-isolation** requirement for a critical component;
- divergent **deploy/lifecycle** constraints.

Not before. When it happens, it will be recorded in a new ADR.

## Consequences

- ➕ High development speed and operational simplicity early on.
- ➕ Freedom to refactor boundaries while we learn the domains.
- ➖ We need **discipline** to avoid leaking dependencies between modules — mitigated
  by the public-interface convention and, later, CI enforcement.
- ➖ If discipline fails, the monolith turns into a "big ball of mud". Risk accepted and
  monitored.

## Related

- `docs/plans/release-01-architecture-and-foundation.md`
- `docs/architecture/c4/level-1-context.md`
