# Release 12 — Kubernetes Deployment

> **Status:** light outline
> **Bounded context:** Platform / Infra

## Goal
Take the platform to a realistic production environment on Kubernetes, with
infrastructure as code.

## Scope
- **Terraform** to provision infrastructure (cloud TBD: Azure/AWS).
- Manifests/Helm for the services (api, web, dependencies).
- Per-environment configuration, secrets, scaling.
- Deployment pipeline (continuation of the R1 CI → CD).

## Key concepts to explain before implementing
IaC with Terraform; K8s objects (Deployment, Service, Ingress, ConfigMap, Secret);
deployment strategies; HPA/scaling; in-cluster observability; when (and whether) to
extract modules from the monolith into their own services.

## Definition of Done
- [ ] Platform runs on a K8s cluster with versioned IaC.
- [ ] Automated deployment from the pipeline.

## Depends on
All previous releases.
