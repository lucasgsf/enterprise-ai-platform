# Architecture

This folder holds the **architecture on paper** for the Enterprise AI Platform.

## Structure

```
architecture/
  decisions/   ← ADRs (Architecture Decision Records), MADR format
  c4/          ← C4 diagrams (Context, Containers, Components)
```

## ADRs — Architecture Decision Records

Each relevant architectural decision becomes an `ADR-NNNN-title.md` file under
`decisions/`. Rules:

- **One ADR per decision.**
- **Immutable:** we do not edit a decision after it is accepted. If we change our mind,
  we create a new ADR with status `Accepted` that **supersedes** the previous one
  (which moves to `Superseded by ADR-XXXX`).
- **Sequential numbering**, starting at `0001`.
- Format: **MADR** (Markdown Any Decision Record), simplified — Context, Options,
  Decision, Consequences.

Possible statuses: `Proposed`, `Accepted`, `Rejected`, `Superseded`, `Deprecated`.

## C4

Diagrams at 4 zoom levels (we use the first 3 as needed):

1. **Context** — system + users + external systems.
2. **Containers** — executable apps and databases.
3. **Components** — modules inside a container.

Diagrams are written in **Mermaid** so they render directly on GitHub.
