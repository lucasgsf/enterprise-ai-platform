# Release 1 — Arquitetura & Fundação

> **Status:** plano detalhado (próximo passo)
> **Objetivo:** desenhar a arquitetura no papel e construir a fundação executável
> da plataforma — antes de qualquer feature de IA.
> **Princípio condutor:** *desenhar antes de construir.*

---

## 1. Por que este release existe

Toda a plataforma será empilhada sobre as decisões deste release. Errar a fundação
significa retrabalho caro em todos os releases seguintes. Por isso o R1 tem duas
fases distintas e nessa ordem:

1. **Arquitetura no papel** — modelo C4, bounded contexts, decisões registradas.
2. **Fundação executável** — monorepo, esqueletos, Docker, CI mínimo.

Só passamos para a fase 2 depois que a fase 1 estiver clara.

---

## 2. Fase 1 — Arquitetura no papel

### 2.1 Decisão: Monólito Modular (e por que não microsserviços)

Você vem de microsserviços em C#/.NET, então o instinto seria já fatiar a plataforma.
Vamos **desafiar isso conscientemente**.

| Abordagem | Prós | Contras | Veredito |
|-----------|------|---------|----------|
| **Monólito modular** | Simples de rodar/debugar; refatorar fronteiras é barato; deploy único; foco em IA | Limite de escala num processo só | ✅ **Escolhido** |
| Microsserviços desde o dia 1 | Escala/falha isoladas | Complexidade distribuída rouba foco do aprendizado de IA | ❌ Cedo demais |
| Híbrido (monólito + 1-2 serviços) | Extrai só o que dói | Decidir cedo o que extrair costuma errar | ⏳ Talvez no futuro |

**Regra de evolução:** extraímos um módulo para serviço próprio (via RabbitMQ/eventos)
**somente** quando houver dor real e medida — escala independente, isolamento de
falha, ou time separado. Não antes.

### 2.2 Modelo C4 (níveis 1 e 2)

**Nível 1 — Contexto:** A *Enterprise AI Platform* da Acme serve usuários internos
(funcionários) que interagem com IA sobre dados corporativos fictícios (ERP, CRM,
RH, etc.). Atores externos: provedores de LLM (OpenAI, Anthropic, Gemini) e sistemas
da Acme (GitHub, Jira, Slack — via MCP no R7).

**Nível 2 — Contêineres:**
- **Frontend (Next.js):** UI + BFF (auth/SSO, proxy seguro para a API).
- **API (FastAPI):** o monólito modular — todos os bounded contexts.
- **PostgreSQL:** dados relacionais + pgvector (R8).
- **Redis:** cache, sessões, rate limiting.
- **(futuro) RabbitMQ, Qdrant, workers** — entram quando os respectivos releases os exigirem.

> Diagramas C4 detalhados (com ferramenta) são uma **tarefa** desta fase — ver §4.

### 2.3 Mapa de Bounded Contexts → Releases

Os módulos do monólito nascem alinhados aos releases (ver `00-roadmap.md`). A
estrutura de pastas do backend reflete esse mapa desde o R1, mesmo que a maioria
comece vazia:

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

**Regra de fronteira:** um módulo só conversa com outro por uma **interface pública
explícita** (camada de serviço/contratos), nunca importando internals diretamente.
Isso é o que torna a futura extração para microsserviço barata.

### 2.4 Decisões de stack a registrar (com trade-offs)

- **Python 3.12** — estável, boa tipagem; 3.13 ainda tem libs de IA correndo atrás.
- **uv** (vs Poetry/pip-tools) — velocidade e padrão emergente; lockfile reprodutível.
- **Next.js + TypeScript** — BFF para SSO seguro (cookies httpOnly) + SSR/streaming
  de tokens no chat.
- **SQLAlchemy async + Alembic** — ORM maduro + migrations versionadas.
- **Pydantic v2 / pydantic-settings** — validação e config tipada por ambiente.

---

## 3. Fase 2 — Fundação executável (escopo)

Só código de **infraestrutura/esqueleto**. Nada de feature de IA ainda.

- **Monorepo** com `apps/api` (FastAPI) e `apps/web` (Next.js), mais `docs/`.
- **Esqueleto FastAPI:** `main.py`, healthcheck (`/health`), config tipada,
  estrutura de módulos vazia (§2.3), logging estruturado.
- **Esqueleto Next.js:** projeto base TypeScript, página inicial, healthcheck.
- **Docker Compose:** serviços `api`, `web`, `postgres`, `redis` subindo juntos.
- **CI mínimo (GitHub Actions):** lint + type-check + testes (mesmo que poucos) +
  build das imagens. Roda em cada PR.
- **Qualidade:** `ruff` (lint+format) no Python, `eslint`/`prettier` no front,
  `mypy` para tipagem, `pytest` para testes.

---

## 4. Tarefas (ordem sugerida)

1. **[Arquitetura]** Escrever os diagramas C4 (níveis 1-2) e ADRs das decisões
   (monólito modular, stack). Salvar em `docs/architecture/`.
2. **[Setup]** Inicializar git + monorepo + estrutura de pastas.
3. **[Backend]** Esqueleto FastAPI com `uv`, config, `/health`, módulos vazios.
4. **[Backend]** Postgres + Redis via Compose; conexão async + Alembic.
5. **[Frontend]** Esqueleto Next.js + TypeScript + healthcheck consumindo a API.
6. **[Infra]** `docker-compose.yml` orquestrando os 4 serviços.
7. **[CI]** Workflow do GitHub Actions: lint, type-check, test, build.
8. **[Qualidade]** Configurar ruff/mypy/pytest e eslint/prettier.

---

## 5. Critério de "pronto" (Definition of Done)

- [ ] ADRs e diagramas C4 escritos e revisados.
- [ ] `docker compose up` sobe API, Web, Postgres e Redis sem erro.
- [ ] `GET /health` responde OK; front consegue chamar a API.
- [ ] CI verde num PR (lint + type-check + test + build).
- [ ] README explica como rodar localmente.

---

## 6. O que NÃO entra neste release

Autenticação, chat, LLMs, RAG, agentes — tudo isso é dos próximos releases.
Resistir ao escopo aqui é parte do exercício de arquitetura.
