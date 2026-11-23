# AI Security Engineering

A hands-on learning repository following the **AI Security Engineer Curriculum v2.2**.

The goal is to progress from Python foundations through machine learning, adversarial ML, deep learning, LLMs, agentic systems, and AI application security—by building, testing, documenting, and evaluating practical projects.

> This is a public learning workspace. It contains original exercises and synthetic-data experiments. Assessed CS50P problem-set solutions are intentionally excluded.

## Learning path

1. **Python foundations** — Python, data structures, files, testing, APIs, and small security utilities.
2. **Mathematics, data science, and classical ML** — NumPy, pandas, statistics, probability, supervised learning, tree models, and anomaly detection.
3. **Cybersecurity ML** — feature engineering, reproducible datasets, detection baselines, generalization, and adversarial ML.
4. **Deep learning and robustness** — PyTorch, neural networks, autoencoders, evaluation, and adversarial robustness.
5. **LLMs and RAG** — transformers, tokenization, embeddings, inference, and retrieval evaluation.
6. **Agentic AI and MCP** — tool calling, agent orchestration, state, approvals, and secure tool integration.
7. **AI security and capstone** — security testing, threat modelling, and final evaluation.

The curriculum is planned as 31 calendar weeks, including four dedicated slack/recovery weeks. Progress is based on working deliverables and independent skill checks—not just watching course material.

## Repository structure

```text
AI-Security-Engineering/
├── phase-01-python/
│   ├── week-01/
│   │   ├── session-01/
│   │   ├── session-02/
│   │   ├── session-03/
│   │   ├── session-04/
│   │   └── session-05/
│   ├── week-02/
│   │   └── session/
│   └── ...
├── documentation/
│   ├── archives/
│   ├── decisions/
│   ├── learning-journal/
│   ├── security/
│   └── weekly-reports/
├── requirements.txt
└── .gitignore
```

Exercises are grouped by curriculum week and session. New folders and files use lowercase names and zero-padded session numbers. Historical exercise content is retained when paths are normalized.

## Getting started

### Requirements

- Python 3
- Git
- VS Code or another Python editor
- Kali Linux or another suitable Linux environment

### Set up the environment

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Activate the virtual environment again whenever opening a new terminal:

```bash
source .venv/bin/activate
```

### Run an exercise

Run a Python file from the repository root using its relative path. Examples:

```bash
python phase-01-python/week-01/session-04/ip_counter_and_validator.py
python phase-01-python/week-02/session/cli_v2.py
```

Some exercises import sibling modules. Run them from the documented working directory or configure the project root on the Python path.

## Development and security practices

- Use a project virtual environment; do not install project packages into system Python.
- Keep functions focused and reusable. Separate reusable logic from demonstration or command-line entry points.
- Use `if __name__ == "__main__":` to guard code that should run only when a module is executed directly.
- Test normal inputs, boundary cases, malformed inputs, and empty inputs.
- Treat log contents and other external input as untrusted data. Never pass log content to `eval`, `exec`, unsafe deserialization, or shell execution.
- Never commit passwords, API keys, access tokens, raw PCAP files, private data, or large datasets.
- Do not publish CS50P problem-set or assessment solutions in this public repository.

## Current progress

| Area | Status |
|---|---|
| Python environment and project setup | Completed |
| Week 1 — Python fundamentals and security exercises | Completed (reported) |
| Week 2 — Control flow, collections and 1,000-event processing | Core exercises implemented; final gate pending |
| Later curriculum phases | Not started |

Progress is updated as weekly deliverables and assessment gates are completed.

## Learning and reporting

- Learning notes: `documentation/learning-journal/`
- Weekly reports: `documentation/weekly-reports/`
- Technical decisions: `documentation/decisions/`
- Security notes: `documentation/security/`

Each weekly report distinguishes completed work, learner-reported results, independently verified checks, and remaining gaps.

## Tools used

- Python and the Python standard library
- pytest
- pip-audit
- Bandit
- Git and GitHub
- VS Code

Additional libraries and tools will be introduced when the curriculum requires them.

## Disclaimer

This repository documents an educational learning path. Security examples are intended for controlled learning and defensive experimentation. Validate code, dependencies, datasets, and experimental results before using anything in a real environment.
