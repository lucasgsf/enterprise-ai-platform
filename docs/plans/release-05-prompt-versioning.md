# Release 5 — Prompt Versioning

> **Status:** esboço leve
> **Bounded context:** Prompt Management

## Objetivo
Tratar prompts como artefatos versionados (não strings soltas no código), permitindo
evolução controlada e rollback.

## Escopo
- Registry de prompts com versões e metadados.
- Renderização de templates com variáveis (tipadas).
- Estratégia de rollout (qual versão está ativa por ambiente/uso).
- Histórico e comparação entre versões.

## Conceitos-chave a explicar antes de implementar
Prompt como código vs como dado; templating seguro; versionamento semântico de
prompts; A/B de prompts; relação com avaliação (R11).

## Critério de "pronto"
- [ ] Prompts versionados e referenciados por id+versão.
- [ ] Trocar versão ativa sem deploy de código.

## Depende de
R4 (prompts alimentam o gateway).
