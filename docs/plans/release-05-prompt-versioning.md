# Release 5 — Prompt Versioning

> **Status:** light outline
> **Bounded context:** Prompt Management

## Goal
Treat prompts as versioned artifacts (not loose strings in code), enabling controlled
evolution and rollback.

## Scope
- Prompt registry with versions and metadata.
- Template rendering with (typed) variables.
- Rollout strategy (which version is active per environment/usage).
- History and comparison between versions.

## Key concepts to explain before implementing
Prompt as code vs as data; safe templating; semantic versioning of prompts; prompt A/B
testing; relationship with evaluation (R11).

## Definition of Done
- [ ] Prompts versioned and referenced by id+version.
- [ ] Switch the active version without a code deploy.

## Depends on
R4 (prompts feed the gateway).
