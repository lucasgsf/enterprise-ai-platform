# Release 6 — Tool Calling

> **Status:** light outline
> **Bounded context:** Tooling

## Goal
Let the LLM invoke platform tools/functions in a controlled and safe way.

## Scope
- Tool definition (schema) and registration.
- Tool-calling loop (model requests → execute → return result).
- Initial **guardrails**: input/output validation, tool allowlist.
- First defenses against **prompt injection**.

## Key concepts to explain before implementing
Function/tool calling; tool JSON schema; simplified ReAct loop; input/output
guardrails; prompt injection attack surface; principle of least privilege.

## Definition of Done
- [ ] LLM invokes a real tool and uses the result in its response.
- [ ] Invalid/dangerous tools are blocked by guardrails.

## Depends on
R4 (gateway with tool-calling support).

## Cross-cutting
Guardrails and prompt injection start here and are reinforced in R9.
