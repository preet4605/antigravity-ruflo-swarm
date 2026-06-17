---
name: android-rag-local
description: "Implement local Retrieval-Augmented Generation using Room and Vector embeddings."
category: ai-native
risk: high
source: community
date_added: "2026-04-07"
metadata:
  triggers:
    - "@rag"
    - "vector database"
    - "local search"
---

# Android Local RAG & Vector Databases 🔎

Retrieval-Augmented Generation (RAG) on Edge devices provides privacy-first, low-latency contextual intelligence. Instead of using cloud Pinecone/Weaviate, this skill enforces local vector embeddings via Room or SQLite.

## ⚡ When to Use
- When tasked with "RAG", "semantic search", or "vector embeddings".
- Building highly private AI features.

## 🏗️ Core Rules / Pillars

### 1. Vector Search in Room
- **Pattern**: Standard Room does not have native vector similarity out of the box in stable. Use L2 distance extensions or `sqlite-vss`.
- **Implementation**: Avoid pulling unmaintained third-party vector DBs. Use SQLite virtual tables with FTS or simple cosine similarity functions if embeddings are small.

## 🚧 Critical Anti-Hallucination Guards
- **Trap**: Do NOT hallucinate that Room natively supports `SELECT * FROM tbl ORDER BY VECTOR_DISTANCE()` securely out of the box without specific extensions.
