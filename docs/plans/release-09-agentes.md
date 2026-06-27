# Release 9 — Agentes

> **Status:** esboço leve
> **Bounded context:** Orquestração

## Objetivo
Orquestrar fluxos agênticos: o modelo planeja, usa tools/RAG, reflete e, quando
necessário, pede confirmação humana.

## Escopo
- **LangGraph** para orquestrar grafos de estados/decisões.
- **Memory** (curto e longo prazo), **planning**, **reflection**.
- **Human-in-the-loop** (HITL): pontos de aprovação.
- Guardrails reforçados para ações de alto impacto.

## Conceitos-chave a explicar antes de implementar
Agente vs pipeline; LangGraph (nós, estado, arestas condicionais); tipos de memória;
planning/reflection; HITL e checkpoints; controle de loops e custo; segurança de
agentes.

## Critério de "pronto"
- [ ] Agente resolve uma tarefa multi-step usando tools + RAG.
- [ ] HITL bloqueia ações sensíveis até aprovação.

## Depende de
R6 (tools), R8 (RAG).
