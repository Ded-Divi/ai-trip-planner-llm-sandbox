# AI Trip Planner — LLM Engineering Fundamentals Sandbox

This is a deliberately small, CLI-only Python project for learning the
primitives of LLM application engineering before using frameworks.

The trip planner is the vehicle, not the destination. Each phase introduces
one mechanism, first in isolation and then in the planner.

## Learning route

| Phase | What you will build | Arpit Bhayani course bridge |
| --- | --- | --- |
| 0 | Project setup and environment configuration | Foundation |
| 1 | One direct LLM API request | API / SDK fundamentals |
| 2 | System and user prompt experiments | Prompt LLMs Reliably |
| 3 | Validated `TripPlan` structured output | Prompt LLMs Reliably |
| 4–6 | Token experiments, streaming, errors and retries | AI application reliability |
| 7–9 | Tools, schemas, and a hand-written agent loop | Tool Use / Single Agent Systems |
| 10–14 | Embeddings, cosine similarity, retrieval and RAG | RAG |
| 15–18 | Combined planner, async calls, logs and small evals | System design / Observability / Evals |

Do not skip ahead: each folder starts empty on purpose, so its code can be
written only after its underlying concept is clear.

## Project map

```text
src/
  config.py                 # Environment/configuration, introduced in Phase 1
  main.py                   # CLI entry point, introduced in Phase 1
  llm/                      # Direct SDK calls, prompts, structured output
  tools/                    # Python functions the model may request
  embeddings/               # Text-to-vector and manual cosine similarity
  rag/                      # Documents, chunks, retrieval, RAG prompt
  agent/                    # Small explicit tool-calling loop
data/
  travel_knowledge.txt      # Tiny local knowledge base, introduced in Phase 10
```

## Setup

Use a virtual environment so this sandbox's packages do not affect another
Python project:

```powershell
cd C:\Users\divya\Documents\Codex\2026-08-22\make\outputs\ai-trip-planner
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Do not add a real API key to `.env` until Phase 1. `.env` is ignored by Git;
`.env.example` is safe to commit because it contains only the variable name.

## Phase 0 checkpoint

Before continuing, be able to answer:

1. Why is the API key kept outside Python source code?
2. What is the difference between `.env` and `.env.example`?
3. Why use a virtual environment for one small project?

Next: Phase 1 — one API request, viewed both through the official SDK and as
the HTTP/JSON request the SDK performs on your behalf.
