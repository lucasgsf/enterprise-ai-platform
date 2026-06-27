# Release 4 — Gateway de LLMs

> **Status:** esboço leve
> **Bounded context:** Model Gateway

## Objetivo
Abstrair múltiplos provedores de LLM atrás de uma interface única, com roteamento de
modelo e rastreio de custo.

## Escopo
- Interface única (porta) para OpenAI, Anthropic, Gemini, Llama.
- **Model routing**: escolher modelo por critério (custo, latência, capacidade, tarefa).
- **Cost tracking** inicial: tokens e custo por requisição.
- Tratamento de erros/ret/ fallback entre providers.

## Conceitos-chave a explicar antes de implementar
Padrão Adapter/Strategy para providers; normalização de respostas; streaming
multi-provider; trade-offs de roteamento; fallback e circuit breaker; contagem de
tokens e cálculo de custo.

## Critério de "pronto"
- [ ] Trocar de provider sem mudar o código de quem chama o gateway.
- [ ] Roteamento por política configurável.
- [ ] Custo por requisição registrado.

## Depende de
R3 (consumidor inicial do gateway).
