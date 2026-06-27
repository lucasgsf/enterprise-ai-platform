# Release 10 — Observabilidade

> **Status:** esboço leve
> **Bounded context:** Cross-cutting (Qualidade operacional)

## Objetivo
Enxergar o que acontece dentro da plataforma de IA: tracing, custo e qualidade em
produção.

## Escopo
- **OpenTelemetry** para tracing distribuído da aplicação.
- **Langfuse** para tracing específico de LLM (prompts, tokens, latência, custo).
- **Cost tracking** consolidado (evolui o que começou no R4).
- Dashboards e alertas básicos.

## Conceitos-chave a explicar antes de implementar
Observabilidade vs monitoração; traces/spans/metrics/logs; tracing de LLM (por que é
diferente); atribuição de custo; correlação ponta a ponta.

## Critério de "pronto"
- [ ] Cada chamada de LLM rastreável com custo e latência.
- [ ] Trace ponta a ponta de uma requisição agêntica.

## Depende de
R4+ (instrumenta o gateway e os fluxos existentes).
