# Release 12 — Deploy Kubernetes

> **Status:** esboço leve
> **Bounded context:** Plataforma / Infra

## Objetivo
Levar a plataforma a um ambiente de produção realista em Kubernetes, com
infraestrutura como código.

## Escopo
- **Terraform** para provisionar infraestrutura (cloud à escolher: Azure/AWS).
- Manifests/Helm para os serviços (api, web, dependências).
- Configuração por ambiente, secrets, escalonamento.
- Pipeline de deploy (continuação do CI do R1 → CD).

## Conceitos-chave a explicar antes de implementar
IaC com Terraform; objetos K8s (Deployment, Service, Ingress, ConfigMap, Secret);
estratégias de deploy; HPA/escalonamento; observabilidade em cluster; quando (e se)
extrair módulos do monólito para serviços próprios.

## Critério de "pronto"
- [ ] Plataforma roda em cluster K8s com IaC versionada.
- [ ] Deploy automatizado a partir do pipeline.

## Depende de
Todos os releases anteriores.
