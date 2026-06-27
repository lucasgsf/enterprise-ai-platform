# Release 8 — RAG & Banco Vetorial

> **Status:** esboço leve
> **Bounded context:** Knowledge

## Objetivo
Dar à plataforma memória de conhecimento: indexar documentos da Acme e responder com
base neles (Retrieval-Augmented Generation).

## Escopo
- **Embeddings** + **chunking** de documentos corporativos fictícios.
- Banco vetorial: **pgvector** primeiro, **Qdrant** depois (comparar).
- **Retrieval** + **hybrid search** (semântico + keyword) + **reranking**.
- Pipeline de ingestão e pipeline de consulta.

## Conceitos-chave a explicar antes de implementar
Embeddings; estratégias de chunking; cosine similarity; retrieval top-k; hybrid
search (BM25 + vetorial); reranking; pgvector vs Qdrant (trade-offs); avaliação de
retrieval (liga ao R11).

## Critério de "pronto"
- [ ] Pergunta é respondida citando documentos recuperados.
- [ ] Hybrid search + reranking medidos contra retrieval simples.

## Depende de
R4 (gateway para gerar embeddings e respostas).
