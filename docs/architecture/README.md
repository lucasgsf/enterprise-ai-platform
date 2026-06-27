# Arquitetura

Esta pasta contém a **arquitetura no papel** da Enterprise AI Platform.

## Estrutura

```
architecture/
  decisions/   ← ADRs (Architecture Decision Records), formato MADR
  c4/          ← diagramas C4 (Contexto, Contêineres, Componentes)
```

## ADRs — Architecture Decision Records

Cada decisão arquitetural relevante vira um arquivo `ADR-NNNN-titulo.md` em
`decisions/`. Regras:

- **Um ADR por decisão.**
- **Imutáveis:** não editamos a decisão depois de aceita. Se mudarmos de ideia,
  criamos um novo ADR com status `Aceito` que **supersede** o anterior (que passa a
  `Substituído por ADR-XXXX`).
- **Numeração sequencial**, começando em `0001`.
- Formato: **MADR** (Markdown Any Decision Record) simplificado — Contexto, Opções,
  Decisão, Consequências.

Status possíveis: `Proposto`, `Aceito`, `Rejeitado`, `Substituído`, `Obsoleto`.

## C4

Diagramas em 4 níveis de zoom (usamos os 3 primeiros, conforme necessário):

1. **Contexto** — sistema + usuários + sistemas externos.
2. **Contêineres** — apps e bancos executáveis.
3. **Componentes** — módulos dentro de um contêiner.

Diagramas escritos em **Mermaid** para renderizarem direto no GitHub.
