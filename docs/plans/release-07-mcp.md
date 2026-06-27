# Release 7 — MCP (Model Context Protocol)

> **Status:** esboço leve
> **Bounded context:** Integração externa

## Objetivo
Integrar a plataforma a sistemas externos (GitHub, Jira, Slack fictícios da Acme) via
**MCP**, padronizando como o modelo acessa contexto e ferramentas externas.

## Escopo
- Cliente MCP na plataforma.
- Um ou mais **MCP servers** expondo recursos/tools da Acme.
- Mapear tools MCP para o loop de tool calling do R6.

## Conceitos-chave a explicar antes de implementar
O que é MCP e que problema resolve; servers vs clients; resources vs tools vs prompts
no MCP; MCP vs tool calling "nativo"; segurança na fronteira externa.

## Critério de "pronto"
- [ ] Plataforma consome um MCP server e usa suas tools no chat/agente.

## Depende de
R6 (tool calling).
