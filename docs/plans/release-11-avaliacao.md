# Release 11 — Avaliação

> **Status:** esboço leve
> **Bounded context:** Quality

## Objetivo
Medir objetivamente a qualidade das respostas, do RAG e dos agentes — sair do "parece
bom" para métricas reprodutíveis.

## Escopo
- **Ragas** para avaliar RAG (faithfulness, relevância, etc.).
- **DeepEval** para avaliar respostas/agentes.
- Datasets de avaliação e execução no CI (regressão de qualidade).
- Ligação com prompt versioning (R5) para comparar versões.

## Conceitos-chave a explicar antes de implementar
Por que avaliar LLM é difícil; LLM-as-judge; métricas de RAG; eval offline vs online;
regressão de qualidade; datasets de avaliação.

## Critério de "pronto"
- [ ] Suite de eval roda e produz métricas comparáveis entre versões.
- [ ] Regressão de qualidade detectável no CI.

## Depende de
R8 (RAG), R9 (agentes).
