# Enterprise AI Platform

[![CI](https://github.com/lucasgsf/enterprise-ai-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/lucasgsf/enterprise-ai-platform/actions/workflows/ci.yml)

Corporate AI platform for **Acme Corporation** (a fictional company) — a portfolio
project and learning lab for Generative AI, software architecture, and platform
engineering.

> This project is **not** an MVP or a tutorial. The goal is to represent an
> application that could exist in a real company, demonstrating mastery of
> architecture, Generative AI, cloud, and engineering best practices.

## Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.12 · FastAPI · Pydantic · SQLAlchemy (async) · uv |
| Frontend | Next.js · TypeScript (BFF for SSO + streaming) |
| Data | PostgreSQL (+ pgvector) · Redis |
| Infra | Docker · Docker Compose → Kubernetes · Terraform |
| AI | OpenAI · Anthropic · Gemini · Llama · LangGraph · MCP · RAG |

## Architecture

Initial style: **modular monolith** (see
[ADR-0001](docs/architecture/decisions/ADR-0001-modular-monolith.md)).

- 📐 Decisions and diagrams: [`docs/architecture/`](docs/architecture/)
- 🗺️ Roadmap and plans: [`docs/plans/`](docs/plans/)

The project evolves across **12 releases**, each one mapping to a *bounded context*.
See the [roadmap](docs/plans/00-roadmap.md).

## Contributing (workflow)

- **Branching:** GitHub Flow — `main` always stable; feature/release work in a
  branch → PR.
- **Commits:** [Conventional Commits](https://www.conventionalcommits.org/)
  (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`...).
