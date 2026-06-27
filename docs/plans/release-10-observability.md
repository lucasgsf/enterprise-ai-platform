# Release 10 — Observability

> **Status:** light outline
> **Bounded context:** Cross-cutting (Operational quality)

## Goal
See what happens inside the AI platform: tracing, cost, and quality in production.

## Scope
- **OpenTelemetry** for distributed application tracing.
- **Langfuse** for LLM-specific tracing (prompts, tokens, latency, cost).
- Consolidated **cost tracking** (evolves what started in R4).
- Basic dashboards and alerts.

## Key concepts to explain before implementing
Observability vs monitoring; traces/spans/metrics/logs; LLM tracing (why it is
different); cost attribution; end-to-end correlation.

## Definition of Done
- [ ] Every LLM call traceable with cost and latency.
- [ ] End-to-end trace of an agentic request.

## Depends on
R4+ (instruments the gateway and existing flows).
