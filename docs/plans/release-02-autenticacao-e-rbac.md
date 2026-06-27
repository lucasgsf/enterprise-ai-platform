# Release 2 — Autenticação & RBAC

> **Status:** esboço leve (será detalhado ao iniciar o release)
> **Bounded context:** Identidade & Acesso

## Objetivo
Permitir login corporativo seguro (SSO) e controle de acesso por papéis, servindo de
base para todos os releases que precisam saber *quem* é o usuário e *o que pode fazer*.

## Escopo
- Login via OAuth2/OIDC com padrão **BFF no Next.js** (tokens em cookies httpOnly,
  nunca expostos ao JS do browser).
- Emissão/validação de sessão entre Next.js (BFF) e FastAPI.
- **RBAC**: papéis (ex: admin, analista, viewer) e permissões por módulo.
- Proteção de rotas no backend (dependências FastAPI) e no front.

## Conceitos-chave a explicar antes de implementar
OAuth2 vs OIDC; fluxo Authorization Code + PKCE; por que BFF > token no browser;
JWT vs sessão opaca; RBAC vs ABAC; onde validar autorização (gateway vs serviço).

## Critério de "pronto"
- [ ] Usuário faz login/logout via provedor de identidade.
- [ ] Rotas protegidas rejeitam não autenticados.
- [ ] Permissões por papel barram ações não autorizadas.

## Depende de
R1 (fundação).
