<div align="center">

# API Spec Generator

[![Python Version](https://img.shields.io/badge/python-3.10%2 | 3.11%2 | 3.12-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Pydantic v2](https://img.shields.io/badge/Pydantic-v2-E92063.svg?logo=pydantic)](https://docs.pydantic.dev/)
[![CI Status](https://github.com/daily-project-factory/api-spec-generator/actions/workflows/ci.yml/badge.svg)](https://github.com/daily-project-factory/api-spec-generator/actions)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An elite, automated utility that analyzes legacy controller code, database schemas, and sample payloads to generate compliant OpenAPI 3.0 documentation. It leverages local and hosted language models with strict Pydantic parsing to draft detailed endpoint descriptions, response schemas, and error codes with minimal developer intervention.

</div>

---

## 📋 Problem Statement

Engineering teams frequently struggle to keep API documentation synchronized with rapidly changing backend codebases. Manual documentation upkeep consistently leads to stale specifications, undocumented endpoints, integration friction for frontend consumers, and wasted engineering hours during onboarding and releases. 

**API Spec Generator** solves this by bridging the gap between raw source code and standardized OpenAPI 3.0 documentation using automated AST parsing and strict AI-driven schema inference.

### Target Audience
* **Backend Engineers** looking to automatically generate and maintain OpenAPI specifications without manual YAML/JSON writing.
* **DevOps & Platform Teams** enforcing strict API documentation standards across microservices.
* **Frontend Developers** requiring up-to-date, reliable contracts to accelerate integration cycles.

---

## ✨ Key Features

* **AST Source Code Analysis**: Parses source code directories and route definitions to extract endpoint paths, HTTP methods, and parameter structures reliably.
* **AI-Powered Schema Inference**: Uses structured LLM prompting and Pydantic validation to infer request/response schemas, parameter types, and generate descriptive docstrings.
* **Asynchronous FastAPI Backend**: Exposes a robust FastAPI backend service for asynchronous batch documentation generation and direct OpenAPI JSON/YAML export.
* **Developer-Friendly CLI**: Provides a command-line interface (CLI) powered by Typer for scanning local code repositories and outputting instant validation reports.

---

## 🏗️ Architecture & System Design

The application follows a modular, decoupled architecture separating static analysis, AI orchestration, validation, and delivery interfaces.

```
                  +-----------------------------------+
                  |          src/main.py              |
                  |     (Unified Entrypoint)          |
                  +-----------------+-----------------+
                                    |
            +-----------------------+-----------------------+
            |                                               |
            v                                               v
  +-------------------+                           +-------------------+
  |    src/cli.py     |                           |    src/api.py     |
  |  (Typer CLI App)  |                           | (FastAPI Service) |
  +---------+---------+                           +---------+---------+
            |                                               |
            +-----------------------+-----------------------+
                                    |
                                    v
                  +-----------------------------------+
                  |          src/core.py              |
                  |  (AST Parser & LLM Orchestrator)  |
                  +-----------------+-----------------+
                                    |
                                    v
                  +-----------------------------------+
                  |         src/models.py             |
                  |  (Pydantic V2 Schemas & Contracts)|
                  +-----------------------------------+
```

### Core Modules

| Module | Purpose |
| :--- | :--- |
| `src/models.py` | Pydantic models representing AST route metadata, OpenAPI 3.0 specification objects, generation job payloads, and validation results. |
| `src/core.py` | Static AST code parser, prompt orchestration engine, LLM client interfacing with strict Pydantic response validation, and OpenAPI 3.0 spec synthesizer. |
| `src/api.py` | FastAPI HTTP server handling asynchronous batch generation jobs, schema uploads, status polling, and OpenAPI JSON/YAML exports. |
| `src/cli.py` | Typer CLI application providing commands for local repository AST scanning, offline spec generation, and compliance validation reports. |
| `src/main.py` | Unified runtime entrypoint enabling execution of the Typer CLI commands and launching the Uvicorn-hosted FastAPI server. |

---

## 💻 Technology Stack

* **Language**: Python 3.10+
* **Framework**: FastAPI (Async Web & REST)
* **Validation**: Pydantic v2 (Strict data parsing & model validation)
* **CLI**: Typer (Modern command-line interfaces)
* **AI / LLM Integration**: OpenAI / LangChain compatible interfaces with structured output parsing
* **Vector & Retrieval**: ChromaDB (Context augmentation for large codebases)
* **Testing**: Pytest & Pytest-Asyncio

---

## 🚀 Installation & Virtual Environment Setup

Clone the repository and set up an isolated Python virtual environment:

```bash
# 1. Clone the repository
git clone https://github.com/daily-project-factory/api-spec-generator.git
cd api-spec-generator

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🔐 Environment Variables Configuration

Copy the example environment configuration file and populate your API keys and configuration settings:

```bash
cp .env.example .env
```

### Configuration Options (`.env`)

| Variable | Description | Default |
| :--- | :--- | :--- |
| `OPENAI_API_KEY` | Your OpenAI API key for LLM-based inference | `sk-...` |
| `LLM_MODEL_NAME` | Model identifier to use for parsing | `gpt-4o-mini` |
| `API_HOST` | Host address for the FastAPI server | `0.0.0.0` |
| `API_PORT` | Port for the FastAPI server | `8000` |
| `LOG_LEVEL` | Application logging level | `INFO` |

---

## 📦 Usage

The application can be run either via the Command Line Interface (CLI) or through the FastAPI REST API service.

### CLI Commands

Execute commands via the unified entrypoint `src/main.py`:

* **Scan a code repository and generate an OpenAPI spec**:
  ```bash
  python src/main.py generate --path ./path/to/legacy/code --output ./openapi.json
  ```

* **Validate an existing codebase against OpenAPI compliance rules**:
  ```bash
  python src/main.py validate --path ./path/to/legacy/code --spec ./openapi.json
  ```

### API Endpoints

Start the FastAPI server:
```bash
python src/main.py serve --port 8000
```

Once running, access the interactive Swagger documentation at `http://localhost:8000/docs`.

#### Key API Routes:
* `POST /api/v1/jobs` - Submit an asynchronous batch documentation generation job.
* `GET /api/v1/jobs/{job_id}` - Poll status and retrieve generated OpenAPI specifications.
* `GET /api/v1/specs/export` - Export synthesized specs directly in JSON or YAML format.

---

## 🧪 Automated Testing

The project uses `pytest` for comprehensive unit and integration testing. Run the test suite with:

```bash
# Run all tests with verbose output
pytest -v

# Run tests with coverage reporting
pytest --cov=src --cov-report=term-missing
```

---

## 📁 Project Structure

```text
api-spec-generator/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── api.py          # FastAPI server & batch job endpoints
│   ├── cli.py          # Typer CLI application definitions
│   ├── core.py         # AST parser, LLM orchestration & spec synthesizer
│   ├── main.py         # Unified runtime entrypoint (CLI & API server)
│   └── models.py       # Pydantic V2 models & data contracts
└── tests/
    ├── __init__.py
    ├── test_api.py     # FastAPI endpoint and async job tests
    └── test_core.py    # AST parsing and schema inference tests
```

---

## 🗺️ Roadmap / Future Enhancements

- [ ] **Multi-Language AST Support**: Expand static code parsing beyond Python to support Node.js/Express, Go (Gin/Fiber), and Java (Spring Boot).
- [ ] **ChromaDB Context Retrieval**: Implement semantic code indexing to supply large codebases into local LLM contexts effectively.
- [ ] **Web Dashboard**: Build a lightweight React dashboard for visualizing generated endpoint maps and editing schemas visually.
- [ ] **CI/CD Action**: Publish a GitHub Action wrapper enabling automated doc generation PRs on code push.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<div align="center">
Maintained with ❤️ by <a href="https://github.com/daily-project-factory">Daily Project Factory</a>.
</div>