# ADR-0001 — Monólito Modular como ponto de partida

- **Status:** Aceito
- **Data:** 2026-06-27
- **Decisores:** Lucas (autor), Tech Lead (mentoria)
- **Contexto técnico:** Release 1 — Arquitetura & Fundação

---

## Contexto e Problema

A Enterprise AI Platform será composta por vários domínios independentes
(identidade, conversação, gateway de LLMs, RAG, agentes, etc. — ver `00-roadmap.md`).
Precisamos decidir o **estilo arquitetural inicial**: como esses domínios são
empacotados e implantados?

Duas forças puxam em direções opostas:

1. O autor vem de **microsserviços em C#/.NET** — o instinto é fatiar cedo.
2. O objetivo central do projeto é **aprender IA Generativa**, não engenharia de
   sistemas distribuídos. Cada hora gasta com encanamento distribuído é uma hora
   não gasta com LLMs, RAG e agentes.

## Opções Consideradas

### Opção A — Monólito Modular (escolhida)
Um único aplicativo FastAPI, organizado em **módulos com fronteiras de domínio
explícitas** (bounded contexts internos). Comunicação entre módulos apenas por
**interfaces públicas** (camada de serviço/contratos), nunca importando internals.

- ➕ Simples de rodar, debugar e testar (um processo, um deploy).
- ➕ Refatorar fronteiras é barato — ainda estamos *descobrindo* os limites certos.
- ➕ Mantém o foco no aprendizado de IA.
- ➕ Fronteiras bem desenhadas permitem **extração futura** para serviços.
- ➖ Limite de escala: tudo escala junto, num processo só.
- ➖ Disciplina de fronteira depende de convenção (não há barreira de rede forçando).

### Opção B — Microsserviços desde o dia 1
Cada bounded context é um serviço próprio, comunicando por rede/RabbitMQ.

- ➕ Escala e isolamento de falha independentes.
- ➕ Times independentes (irrelevante: somos um autor só).
- ➖ Complexidade alta: rede, consistência eventual, observabilidade distribuída,
  deploy multi-serviço, contratos versionados entre serviços.
- ➖ Essa complexidade **rouba o foco** do objetivo real (IA).
- ➖ Alto risco de **errar a fronteira** cedo demais (e fronteira errada entre
  serviços é caríssima de corrigir).

### Opção C — Híbrido (monólito + 1-2 serviços extraídos)
Começar monólito e já extrair, p.ex., workers de RAG.

- ➕ Extrai só o que dói.
- ➖ Decidir *agora* o que extrair é adivinhação; provavelmente erraríamos.

## Decisão

Adotamos a **Opção A — Monólito Modular**.

A estrutura de pastas reflete os bounded contexts desde já
(`app/modules/<contexto>`), com comunicação inter-módulos apenas por interfaces
públicas. Isso nos dá os benefícios de organização de microsserviços **sem** o custo
distribuído.

## Critério de evolução (quando reconsiderar)

Extraímos um módulo para serviço próprio (via RabbitMQ/eventos) **somente** quando
houver **dor real e medida**, por exemplo:

- necessidade comprovada de **escalar** um módulo independente dos demais
  (ex.: ingestão de RAG saturando CPU);
- requisito de **isolamento de falha** de um componente crítico;
- limites de **deploy/ciclo de vida** divergentes.

Não antes. Quando acontecer, será registrado em um novo ADR.

## Consequências

- ➕ Velocidade de desenvolvimento e simplicidade operacional altas no início.
- ➕ Liberdade para refatorar fronteiras enquanto aprendemos os domínios.
- ➖ Precisamos de **disciplina** para não vazar dependências entre módulos —
  mitigado por convenção de interfaces públicas e, futuramente, checagem em CI.
- ➖ Se a disciplina falhar, o monólito vira "big ball of mud". Risco aceito e
  monitorado.

## Relacionados

- `docs/plans/release-01-arquitetura-e-fundacao.md`
- `docs/architecture/c4/level-1-context.md`
