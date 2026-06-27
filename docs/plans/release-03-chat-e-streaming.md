# Release 3 — Chat & Streaming

> **Status:** esboço leve
> **Bounded context:** Conversação

## Objetivo
Primeira feature de IA: conversa com LLM, com resposta **em streaming** e histórico
persistente por usuário.

## Escopo
- Endpoint de chat com **streaming de tokens** (SSE) do backend ao front.
- Renderização incremental no Next.js (SSR/streaming de tokens).
- Persistência de conversas e mensagens (Postgres).
- Contexto de conversa (janela de histórico).

## Conceitos-chave a explicar antes de implementar
Streaming via SSE vs WebSocket; backpressure; tokens vs mensagens; gestão de
janela de contexto; modelagem de conversa/mensagem; idempotência de envio.

## Critério de "pronto"
- [ ] Usuário envia mensagem e vê resposta token a token.
- [ ] Histórico persiste e recarrega entre sessões.

## Depende de
R1, R2 (precisa saber quem é o usuário).
