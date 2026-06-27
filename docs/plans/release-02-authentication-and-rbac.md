# Release 2 — Authentication & RBAC

> **Status:** light outline (to be detailed when the release starts)
> **Bounded context:** Identity & Access

## Goal
Enable secure corporate login (SSO) and role-based access control, providing the
foundation for every release that needs to know *who* the user is and *what* they can do.

## Scope
- Login via OAuth2/OIDC using the **BFF pattern in Next.js** (tokens in httpOnly
  cookies, never exposed to browser JS).
- Session issuance/validation between Next.js (BFF) and FastAPI.
- **RBAC**: roles (e.g. admin, analyst, viewer) and per-module permissions.
- Route protection on the backend (FastAPI dependencies) and the frontend.

## Key concepts to explain before implementing
OAuth2 vs OIDC; Authorization Code + PKCE flow; why BFF > token in the browser; JWT vs
opaque session; RBAC vs ABAC; where to validate authorization (gateway vs service).

## Definition of Done
- [ ] User can log in/out via the identity provider.
- [ ] Protected routes reject unauthenticated requests.
- [ ] Per-role permissions block unauthorized actions.

## Depends on
R1 (foundation).
