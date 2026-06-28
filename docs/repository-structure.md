# Repository Structure

# Multi-Agent Code Review & Auto-Debugging System

This project follows a **Monorepo (Monolithic Repository)** approach, where all project components are maintained in a single Git repository.

This allows all team members and AI coding agents to have complete visibility into the project, making development, testing, documentation, and deployment significantly easier.

---

## Why Monorepo?

A monorepo provides several advantages for this project:

- Single source of truth
- Easier collaboration across a 10-member team
- Shared documentation
- Consistent coding standards
- Simplified CI/CD
- Better support for AI coding assistants (Cursor, Claude Code, GitHub Copilot, Codex, etc.)
- Easier dependency management
- Centralized version control

---

# Repository Structure

```text
multiagent-code-review/
│
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── docker-compose.yml
├── Makefile
│
├── docs/
│   ├── architecture/
│   ├── api/
│   ├── design/
│   ├── diagrams/
│   ├── meeting-notes/
│   ├── decisions/
│   ├── reports/
│   ├── references/
│   └── screenshots/
│
├── backend/
│   ├── app/
│   ├── agents/
│   ├── graph/
│   ├── rag/
│   ├── tools/
│   ├── models/
│   ├── services/
│   ├── api/
│   ├── tests/
│   ├── prompts/
│   ├── evaluation/
│   └── requirements.txt
│
├── frontend/
│   ├── streamlit/
│   └── assets/
│
├── datasets/
│   ├── raw/
│   ├── processed/
│   ├── synthetic/
│   └── samples/
│
├── knowledge-base/
│   ├── owasp/
│   ├── cwe/
│   ├── pep8/
│   ├── python/
│   └── indexed/
│
├── scripts/
│   ├── setup.py
│   ├── ingest_docs.py
│   ├── build_index.py
│   ├── run_tests.py
│   └── benchmark.py
│
├── infrastructure/
│   ├── docker/
│   ├── github-actions/
│   └── deployment/
│
├── experiments/
│
├── notebooks/
│
├── evaluation/
│
└── .github/
    └── workflows/
```

---

# Folder Explanation

## Root Directory

Contains project-wide configuration and documentation.

| File | Purpose |
|------|----------|
| README.md | Project overview, setup instructions, architecture and usage guide |
| LICENSE | Open-source license |
| .gitignore | Files and folders excluded from Git |
| .env.example | Sample environment variables |
| docker-compose.yml | Local development environment |
| Makefile | Common developer commands |

---

# docs/

Contains all project documentation.

| Folder | Purpose |
|---------|----------|
| architecture | High-level architecture documents |
| api | API specifications |
| design | Design documents and technical notes |
| diagrams | System diagrams and flowcharts |
| meeting-notes | Weekly meeting notes |
| decisions | Architecture Decision Records (ADRs) |
| reports | Evaluation reports and final documentation |
| references | Research papers and useful links |
| screenshots | UI screenshots and demo images |

---

# backend/

Contains the complete backend implementation.

| Folder | Purpose |
|---------|----------|
| app | FastAPI application entry point |
| agents | AI agents (Security, Bug, Style, Patch, Test) |
| graph | LangGraph workflow definitions |
| rag | Retrieval-Augmented Generation pipeline |
| tools | Helper utilities and external integrations |
| models | Pydantic models and schemas |
| services | Business logic |
| api | REST API endpoints |
| tests | Unit and integration tests |
| prompts | LLM prompts |
| evaluation | Backend evaluation scripts |
| requirements.txt | Python dependencies |

---

# frontend/

Contains the user interface.

| Folder | Purpose |
|---------|----------|
| streamlit | Streamlit application |
| assets | Images, CSS, icons and static resources |

---

# datasets/

Contains all datasets used during development and evaluation.

| Folder | Purpose |
|---------|----------|
| raw | Original datasets |
| processed | Cleaned datasets |
| synthetic | AI-generated samples |
| samples | Small demo datasets |

---

# knowledge-base/

Stores documents used by the RAG pipeline.

| Folder | Purpose |
|---------|----------|
| owasp | OWASP Top-10 documentation |
| cwe | CWE knowledge base |
| pep8 | Python style guide |
| python | Python reference documentation |
| indexed | Vector database source files |

---

# scripts/

Automation scripts.

| Script | Purpose |
|--------|----------|
| setup.py | Project setup |
| ingest_docs.py | Import RAG documents |
| build_index.py | Build vector indexes |
| run_tests.py | Execute automated tests |
| benchmark.py | Performance benchmarking |

---

# infrastructure/

Infrastructure-as-Code and deployment resources.

| Folder | Purpose |
|---------|----------|
| docker | Dockerfiles |
| github-actions | CI/CD workflow templates |
| deployment | Deployment configuration |

---

# experiments/

Contains prototypes and experimental features that are not yet production-ready.

---

# notebooks/

Jupyter notebooks used for:

- Data exploration
- Prompt experimentation
- Embedding analysis
- Model evaluation
- Research

---

# evaluation/

Stores evaluation outputs.

Examples:

- RAGAS scores
- Precision / Recall
- F1 Score
- Patch Success Rate
- Latency Reports
- Benchmark Results

---

# .github/

GitHub-specific configuration.

| Folder | Purpose |
|---------|----------|
| workflows | GitHub Actions CI/CD pipelines |

---

# Repository Principles

The team should follow these principles throughout development:

- Keep documentation updated.
- Use feature branches for all development.
- Never commit secrets or API keys.
- Write tests for new functionality.
- Keep AI prompts version controlled.
- Store datasets separately from source code.
- Maintain a clean and modular architecture.
- Ensure every component is independently testable.

---

# Future Enhancements

As the project evolves, additional directories may be added:

- `mobile/` – Mobile application
- `terraform/` – Infrastructure provisioning
- `monitoring/` – Logging and observability
- `kubernetes/` – Kubernetes deployment
- `benchmark-results/` – Performance reports
- `docs/demo/` – Demo videos and presentations

---

## Summary

This repository is organized to support:

- Multi-agent AI development
- FastAPI backend services
- Streamlit frontend
- Retrieval-Augmented Generation (RAG)
- LangGraph orchestration
- CI/CD automation
- Team collaboration
- AI-assisted development
- Production-quality software engineering practices