# Release 7 — MCP (Model Context Protocol)

> **Status:** light outline
> **Bounded context:** External integration

## Goal
Integrate the platform with external systems (Acme's fictional GitHub, Jira, Slack) via
**MCP**, standardizing how the model accesses external context and tools.

## Scope
- MCP client in the platform.
- One or more **MCP servers** exposing Acme resources/tools.
- Map MCP tools to the R6 tool-calling loop.

## Key concepts to explain before implementing
What MCP is and what problem it solves; servers vs clients; resources vs tools vs
prompts in MCP; MCP vs "native" tool calling; security at the external boundary.

## Definition of Done
- [ ] Platform consumes an MCP server and uses its tools in chat/agent.

## Depends on
R6 (tool calling).
