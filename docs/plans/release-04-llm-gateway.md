# Release 4 — LLM Gateway

> **Status:** light outline
> **Bounded context:** Model Gateway

## Goal
Abstract multiple LLM providers behind a single interface, with model routing and cost
tracking.

## Scope
- Single interface (port) for OpenAI, Anthropic, Gemini, Llama.
- **Model routing**: choose a model by criteria (cost, latency, capability, task).
- Initial **cost tracking**: tokens and cost per request.
- Error handling / retries / fallback between providers.

## Key concepts to explain before implementing
Adapter/Strategy pattern for providers; response normalization; multi-provider
streaming; routing trade-offs; fallback and circuit breaker; token counting and cost
calculation.

## Definition of Done
- [ ] Switch provider without changing the calling code.
- [ ] Routing by configurable policy.
- [ ] Cost per request recorded.

## Depends on
R3 (initial consumer of the gateway).
