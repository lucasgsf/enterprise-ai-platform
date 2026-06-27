# Release 8 — RAG & Vector Store

> **Status:** light outline
> **Bounded context:** Knowledge

## Goal
Give the platform knowledge memory: index Acme documents and answer based on them
(Retrieval-Augmented Generation).

## Scope
- **Embeddings** + **chunking** of fictional corporate documents.
- Vector store: **pgvector** first, **Qdrant** later (compare).
- **Retrieval** + **hybrid search** (semantic + keyword) + **reranking**.
- Ingestion pipeline and query pipeline.

## Key concepts to explain before implementing
Embeddings; chunking strategies; cosine similarity; top-k retrieval; hybrid search
(BM25 + vector); reranking; pgvector vs Qdrant (trade-offs); retrieval evaluation (ties
into R11).

## Definition of Done
- [ ] A question is answered citing retrieved documents.
- [ ] Hybrid search + reranking measured against simple retrieval.

## Depends on
R4 (gateway to generate embeddings and answers).
