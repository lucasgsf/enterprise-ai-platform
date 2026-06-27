# Release 6 — Tool Calling

> **Status:** esboço leve
> **Bounded context:** Tooling

## Objetivo
Permitir que o LLM invoque ferramentas/funções da plataforma de forma controlada e
segura.

## Escopo
- Definição de tools (schema) e registro.
- Loop de tool calling (modelo pede → executa → devolve resultado).
- **Guardrails** iniciais: validação de entrada/saída, allowlist de tools.
- Primeiras defesas contra **prompt injection**.

## Conceitos-chave a explicar antes de implementar
Function/tool calling; JSON schema de tools; loop ReAct simplificado; guardrails de
entrada/saída; superfície de ataque de prompt injection; princípio do menor privilégio.

## Critério de "pronto"
- [ ] LLM invoca uma tool real e usa o resultado na resposta.
- [ ] Tools inválidas/perigosas são bloqueadas por guardrails.

## Depende de
R4 (gateway com suporte a tool calling).

## Cross-cutting
Guardrails e prompt injection começam aqui e são reforçados no R9.
