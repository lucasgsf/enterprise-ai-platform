# Release 3 — Chat & Streaming

> **Status:** light outline
> **Bounded context:** Conversation

## Goal
First AI feature: conversation with an LLM, with **streaming** responses and persistent
per-user history.

## Scope
- Chat endpoint with **token streaming** (SSE) from backend to frontend.
- Incremental rendering in Next.js (SSR/token streaming).
- Persistence of conversations and messages (Postgres).
- Conversation context (history window).

## Key concepts to explain before implementing
Streaming via SSE vs WebSocket; backpressure; tokens vs messages; context window
management; conversation/message modeling; send idempotency.

## Definition of Done
- [ ] User sends a message and sees the response token by token.
- [ ] History persists and reloads across sessions.

## Depends on
R1, R2 (needs to know who the user is).
