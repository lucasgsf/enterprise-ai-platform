# Release 11 — Evaluation

> **Status:** light outline
> **Bounded context:** Quality

## Goal
Objectively measure the quality of answers, RAG, and agents — move from "looks good" to
reproducible metrics.

## Scope
- **Ragas** to evaluate RAG (faithfulness, relevance, etc.).
- **DeepEval** to evaluate answers/agents.
- Evaluation datasets and CI execution (quality regression).
- Link with prompt versioning (R5) to compare versions.

## Key concepts to explain before implementing
Why evaluating LLMs is hard; LLM-as-judge; RAG metrics; offline vs online eval; quality
regression; evaluation datasets.

## Definition of Done
- [ ] Eval suite runs and produces comparable metrics across versions.
- [ ] Quality regression detectable in CI.

## Depends on
R8 (RAG), R9 (agents).
