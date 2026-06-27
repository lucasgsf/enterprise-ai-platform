# Roadmap — Enterprise AI Platform (Acme Corporation)

> Master index for the project. This document gives the macro view of the 12 releases.
> Each release has (or will have) its own plan in `docs/plans/release-NN-*.md`.

---

## Planning philosophy: layered (just-in-time)

We do not write 12 detailed plans up front. Why?

- **Premature planning ages badly.** Concrete decisions made today for Release 9 will
  be wrong by the time we get there, because what we learn in earlier releases
  reshapes the design of the later ones.
- **Maintenance cost.** A detailed, out-of-date document is worse than no document.

So plan depth is **layered**:

| Layer | Document | Depth |
|-------|----------|-------|
| Macro | `00-roadmap.md` (this one) | Master index |
| Next step | `release-01-*.md` | **Detailed** |
| Future | `release-02..12-*.md` | Light outline, deepened at the right time |

**Rule of thumb:** when a release starts, its outline is promoted to a detailed plan
(following the brainstorming → spec → plan flow from `AI_CONTEXT.md`).

---

## Central architectural decision: Modular Monolith

The platform starts as **a single FastAPI application**, organized into **modules with
explicit domain boundaries** (internal bounded contexts). We do **not** start with
microservices.

**Why (summary — full detail in `release-01`):**
- Focus on learning **AI**, not distributed plumbing (networking, eventual
  consistency, distributed observability).
- Refactoring boundaries inside a monolith is cheap; splitting services too early and
  getting the boundary wrong is expensive.
- Boundaries are designed to allow **future extraction** into services via
  RabbitMQ/events, *when and if* there is real scaling pain.

Each release below generally corresponds to **one bounded context**.

---

## Confirmed stack

| Layer | Technology | Status |
|-------|-----------|--------|
| Backend | Python **3.12** + FastAPI + Pydantic + SQLAlchemy (async) | ✅ decided |
| Python tooling | **uv** (deps + venv + execution) | ✅ decided |
| Frontend | **Next.js** + TypeScript (BFF for SSO + SSR/streaming) | ✅ decided |
| Relational DB | PostgreSQL | ✅ decided |
| Cache / light queues | Redis | ✅ decided |
| Messaging | RabbitMQ | when services are extracted |
| Vector store | pgvector → Qdrant | Release 8 |
| Containers | Docker / Docker Compose → Kubernetes | R1 / R12 |

---

## The 12 releases

| # | Release | Bounded Context | What you learn | Depends on |
|---|---------|-----------------|----------------|------------|
| 1 | Architecture & Foundation | Platform / Base infra | C4, modular monolith, FastAPI, uv, Docker, CI | — |
| 2 | Authentication & RBAC | Identity & Access | OAuth/OIDC, SSO via BFF, RBAC, JWT | R1 |
| 3 | Chat & Streaming | Conversation | SSE/token streaming, history, persistence | R1, R2 |
| 4 | LLM Gateway | Model Gateway | Multi-provider abstraction, model routing, cost tracking | R3 |
| 5 | Prompt Versioning | Prompt Management | Versioning, prompt registry, rollout | R4 |
| 6 | Tool Calling | Tooling | Function/tool calling, guardrails, validation | R4 |
| 7 | MCP | External integration | Model Context Protocol, MCP servers/clients | R6 |
| 8 | RAG & Vector Store | Knowledge | Embeddings, chunking, retrieval, hybrid search, reranking | R4 |
| 9 | Agents | Orchestration | LangGraph, memory, planning, reflection, human-in-the-loop | R6, R8 |
| 10 | Observability | Cross-cutting | OpenTelemetry, Langfuse, LLM tracing, cost tracking | R4+ |
| 11 | Evaluation | Quality | DeepEval, Ragas, RAG and agent evaluation | R8, R9 |
| 12 | Kubernetes Deployment | Platform / Infra | Terraform, K8s, manifests, scaling | all |

> **Cross-cutting (span several releases):** Guardrails and Prompt Injection (start in
> R6, reinforced in R9), Cost Tracking (R4, consolidated in R10), Model Routing (R4,
> refined in R10).

---

## How to navigate

1. Always start from the **current** release's plan.
2. When a release is done, run a **review** and promote the next outline to a detailed
   plan.
3. Keep this roadmap as the source of truth for the macro view — update the "Status"
   column and dependencies as reality changes.
