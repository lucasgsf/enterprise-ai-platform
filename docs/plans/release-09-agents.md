# Release 9 — Agents

> **Status:** light outline
> **Bounded context:** Orchestration

## Goal
Orchestrate agentic flows: the model plans, uses tools/RAG, reflects, and — when needed
— asks for human confirmation.

## Scope
- **LangGraph** to orchestrate state/decision graphs.
- **Memory** (short and long term), **planning**, **reflection**.
- **Human-in-the-loop** (HITL): approval points.
- Reinforced guardrails for high-impact actions.

## Key concepts to explain before implementing
Agent vs pipeline; LangGraph (nodes, state, conditional edges); memory types;
planning/reflection; HITL and checkpoints; loop and cost control; agent security.

## Definition of Done
- [ ] Agent solves a multi-step task using tools + RAG.
- [ ] HITL blocks sensitive actions until approval.

## Depends on
R6 (tools), R8 (RAG).
