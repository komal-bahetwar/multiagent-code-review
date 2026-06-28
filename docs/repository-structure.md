# Repository Structure

# Multi-Agent Code Review & Auto-Debugging System

This project follows a **Monorepo (Monolithic Repository)** approach, where all project components are maintained in a single Git repository.

The project uses a **single Python workspace** managed by **uv**. Both the FastAPI backend and the Streamlit user interface share the same virtual environment and dependency management, simplifying development and onboarding.

This allows all team members and AI coding agents to have complete visibility into the project, making development, testing, documentation, and deployment significantly easier.

---

## Why Monorepo?

A monorepo provides several advantages for this project:

- Single source of truth
- Easier collaboration across a 10-member team
- Shared documentation
- Single Python environment using `uv`
- Consistent coding standards
- Simplified dependency management
- Simplified CI/CD
- Better support for AI coding assistants (Cursor, Claude Code, GitHub Copilot, Codex, etc.)
- Centralized version control

---

## Repository Structure

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
│   ├── pyproject.toml
│   ├── uv.lock
│   ├── .python-version
│   ├── app/
│   ├── agents/
│   ├── graph/
│   ├── rag/
│   ├── tools/
│   ├── models/
│   ├── services/
│   ├── api/
│   ├── prompts/
│   ├── ui/
│   │   └── streamlit/
│   │       ├── Home.py
│   │       └── pages/
│   ├── tests/
│   └── evaluation/
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
| design | Technical design documents |
| diagrams | Architecture and workflow diagrams |
| meeting-notes | Weekly meeting notes |
| decisions | Architecture Decision Records (ADRs) |
| reports | Evaluation reports and final documentation |
| references | Research papers and useful resources |
| screenshots | UI screenshots and demo images |

---

# backend/

The backend is the core of the project and is managed as a single **Python project** using **uv**.

Both the FastAPI REST API and the Streamlit user interface share the same Python environment and dependencies.

| Folder | Purpose |
|---------|----------|
| pyproject.toml | Python project configuration |
| uv.lock | Locked dependency versions |
| .python-version | Python version used by uv |
| app | FastAPI application entry point |
| agents | AI agents (Security, Bug, Style, Patch, Test) |
| graph | LangGraph workflows and orchestration |
| rag | Retrieval-Augmented Generation pipeline |
| tools | Utility modules and integrations |
| models | Pydantic models and schemas |
| services | Business logic |
| api | REST API endpoints |
| prompts | Prompt templates for LLMs |
| ui/streamlit | Streamlit dashboard and user interface |
| tests | Unit and integration tests |
| evaluation | Evaluation scripts and metrics |

---

# datasets/

Contains all datasets used during development and evaluation.

| Folder | Purpose |
|---------|----------|
| raw | Original datasets |
| processed | Cleaned datasets |
| synthetic | AI-generated datasets |
| samples | Small demo datasets |

---

# knowledge-base/

Contains documents indexed by the RAG pipeline.

| Folder | Purpose |
|---------|----------|
| owasp | OWASP Top-10 documentation |
| cwe | CWE knowledge base |
| pep8 | Python coding standards |
| python | Python reference documentation |
| indexed | Documents prepared for vector indexing |

---

# scripts/

Utility scripts used throughout the project.

| Script | Purpose |
|--------|----------|
| setup.py | Project initialization |
| ingest_docs.py | Load documents into the knowledge base |
| build_index.py | Build vector indexes |
| run_tests.py | Execute automated tests |
| benchmark.py | Benchmark performance |

---

# infrastructure/

Infrastructure and deployment configuration.

| Folder | Purpose |
|---------|----------|
| docker | Dockerfiles and Docker configuration |
| github-actions | CI/CD templates |
| deployment | Deployment manifests and scripts |

---

# experiments/

Contains experimental features, prototypes, and proof-of-concepts.

---

# notebooks/

Jupyter notebooks for:

- Data exploration
- Prompt engineering
- Embedding analysis
- Model evaluation
- Research experiments

---

# evaluation/

Stores evaluation reports and benchmark results.

Examples include:

- RAGAS scores
- Precision / Recall
- F1 Score
- Patch Success Rate
- Latency reports
- Benchmark comparisons

---

# .github/

GitHub-specific configuration.

| Folder | Purpose |
|---------|----------|
| workflows | GitHub Actions CI/CD pipelines |

---

# Development Workflow

The project uses a **single Python environment** managed by **uv**.

Initialize the environment:

```bash
cd backend
uv sync
```

Run the FastAPI server:

```bash
uv run uvicorn app.main:app --reload
```

Run the Streamlit dashboard:

```bash
uv run streamlit run ui/streamlit/Home.py
```

---

# Repository Principles

The team should follow these principles throughout development:

- Maintain a single Python environment using `uv`
- Keep documentation updated
- Use feature branches for all development
- Never commit secrets or API keys
- Write tests for new functionality
- Version control all LLM prompts
- Store datasets separately from source code
- Keep modules loosely coupled and independently testable
- Follow clean architecture and modular design principles

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

# Summary

This repository is organized to support:

- Multi-agent AI development
- FastAPI backend services
- Streamlit dashboard
- LangGraph orchestration
- Retrieval-Augmented Generation (RAG)
- Evaluation and benchmarking
- CI/CD automation
- Team collaboration
- AI-assisted software development
- Production-quality engineering practices