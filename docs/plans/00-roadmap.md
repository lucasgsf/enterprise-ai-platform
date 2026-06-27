# Roadmap — Enterprise AI Platform (Acme Corporation)

> Índice mestre do projeto. Este documento dá a visão macro dos 12 releases.
> Cada release tem (ou terá) seu próprio plano em `docs/plans/release-NN-*.md`.

---

## Filosofia de planejamento: camadas (just-in-time)

Não escrevemos 12 planos detalhados de uma vez. Por quê?

- **Planejamento prematuro envelhece mal.** Decisões concretas tomadas hoje para o
  Release 9 estarão erradas quando chegarmos lá, porque o que aprendemos nos
  releases anteriores muda o desenho dos posteriores.
- **Custo de manutenção.** Documento detalhado e desatualizado é pior que documento
  ausente.

Por isso, a profundidade dos planos é **em camadas**:

| Camada | Documento | Profundidade |
|--------|-----------|--------------|
| Macro | `00-roadmap.md` (este) | Índice mestre |
| Próximo passo | `release-01-*.md` | **Detalhado** |
| Futuro | `release-02..12-*.md` | Esboço leve, aprofundado no momento certo |

**Regra prática:** ao iniciar um release, seu esboço é promovido a plano detalhado
(seguindo o fluxo brainstorming → spec → plano do `AI_CONTEXT.md`).

---

## Decisão arquitetural central: Monólito Modular

A plataforma começa como **um único aplicativo FastAPI**, organizado em **módulos com
fronteiras de domínio explícitas** (bounded contexts internos). **Não** começamos com
microsserviços.

**Por quê (resumo — detalhe em `release-01`):**
- Foco no aprendizado de **IA**, não em encanamento distribuído (rede, consistência
  eventual, observabilidade distribuída).
- Refatorar fronteiras dentro de um monólito é barato; quebrar serviços cedo demais
  e errar a fronteira é caro.
- As fronteiras são desenhadas para permitir **extração futura** de serviços via
  RabbitMQ/eventos, *quando e se* houver dor real de escala.

Cada release abaixo corresponde, em geral, a **um bounded context**.

---

## Stack confirmada

| Camada | Tecnologia | Status |
|--------|-----------|--------|
| Backend | Python **3.12** + FastAPI + Pydantic + SQLAlchemy (async) | ✅ definido |
| Tooling Python | **uv** (deps + venv + execução) | ✅ definido |
| Frontend | **Next.js** + TypeScript (BFF para SSO + SSR/streaming) | ✅ definido |
| Banco relacional | PostgreSQL | ✅ definido |
| Cache / filas leves | Redis | ✅ definido |
| Mensageria | RabbitMQ | quando houver extração de serviços |
| Banco vetorial | pgvector → Qdrant | Release 8 |
| Containers | Docker / Docker Compose → Kubernetes | R1 / R12 |

---

## Os 12 releases

| # | Release | Bounded Context | Aprende-se | Depende de |
|---|---------|-----------------|------------|------------|
| 1 | Arquitetura & Fundação | Plataforma / Infra base | C4, monólito modular, FastAPI, uv, Docker, CI | — |
| 2 | Autenticação & RBAC | Identidade & Acesso | OAuth/OIDC, SSO via BFF, RBAC, JWT | R1 |
| 3 | Chat & Streaming | Conversação | SSE/streaming de tokens, histórico, persistência | R1, R2 |
| 4 | Gateway de LLMs | Model Gateway | Abstração multi-provider, model routing, cost tracking | R3 |
| 5 | Prompt Versioning | Prompt Management | Versionamento, registry de prompts, rollout | R4 |
| 6 | Tool Calling | Tooling | Function/tool calling, guardrails, validação | R4 |
| 7 | MCP | Integração externa | Model Context Protocol, servers/clients MCP | R6 |
| 8 | RAG & Banco Vetorial | Knowledge | Embeddings, chunking, retrieval, hybrid search, reranking | R4 |
| 9 | Agentes | Orquestração | LangGraph, memory, planning, reflection, human-in-the-loop | R6, R8 |
| 10 | Observabilidade | Cross-cutting | OpenTelemetry, Langfuse, tracing de LLM, cost tracking | R4+ |
| 11 | Avaliação | Quality | DeepEval, Ragas, eval de RAG e agentes | R8, R9 |
| 12 | Deploy Kubernetes | Plataforma / Infra | Terraform, K8s, manifests, escalonamento | todos |

> **Cross-cutting (atravessam vários releases):** Guardrails e Prompt Injection
> (começam no R6, reforçados no R9), Cost Tracking (R4, consolidado no R10),
> Model Routing (R4, refinado no R10).

---

## Como navegar

1. Comece sempre pelo plano do release **atual**.
2. Ao concluir um release, faça uma **revisão** e promova o esboço do próximo a
   plano detalhado.
3. Mantenha este roadmap como fonte de verdade da visão macro — atualize a coluna
   "Status" e dependências conforme a realidade muda.
