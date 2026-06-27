# Enterprise AI Platform

Plataforma corporativa de IA da **Acme Corporation** (empresa fictícia) — um projeto
de portfólio e laboratório de aprendizado em IA Generativa, arquitetura de software e
engenharia de plataformas.

> Este projeto **não** é um MVP nem um tutorial. O objetivo é representar uma
> aplicação que poderia existir em uma empresa real, demonstrando domínio de
> arquitetura, IA Generativa, cloud e boas práticas de engenharia.

## Stack

| Camada | Tecnologia |
|--------|-----------|
| Backend | Python 3.12 · FastAPI · Pydantic · SQLAlchemy (async) · uv |
| Frontend | Next.js · TypeScript (BFF para SSO + streaming) |
| Dados | PostgreSQL (+ pgvector) · Redis |
| Infra | Docker · Docker Compose → Kubernetes · Terraform |
| IA | OpenAI · Anthropic · Gemini · Llama · LangGraph · MCP · RAG |

## Arquitetura

Estilo inicial: **monólito modular** (ver
[ADR-0001](docs/architecture/decisions/ADR-0001-monolito-modular.md)).

- 📐 Decisões e diagramas: [`docs/architecture/`](docs/architecture/)
- 🗺️ Roadmap e planos: [`docs/plans/`](docs/plans/)

O projeto evolui em **12 releases**, cada um correspondendo a um *bounded context*.
Veja o [roadmap](docs/plans/00-roadmap.md).

## Como contribuir (workflow)

- **Branching:** GitHub Flow — `main` sempre estável; feature/release em branch → PR.
- **Commits:** [Conventional Commits](https://www.conventionalcommits.org/)
  (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`...).
