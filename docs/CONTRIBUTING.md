# Contributing & Commit Strategy

## Branching

- **main**: Production-ready code and documentation. Protected; only merged via PR.
- **task-1-dev**: Development for Task-1 (Foundation). All Task-1 work happens here first.
- **task-N-dev**: Future tasks (e.g. task-2-dev for Bayesian modeling) branch from `main` after Task-1 is merged.

## Commit Strategy

- **Atomic commits**: One logical change per commit (e.g. "Add event dataset schema", "Document ADF test plan").
- **Conventional-style messages** (optional but encouraged):
  - `docs: add Task-1 objectives and workflow`
  - `data: add geopolitical events CSV and schema`
  - `fix: correct event date for OPEC+ 2020 cut`
- **No direct pushes to main**: Use Pull Requests; require review for main.

## Repo hygiene

- Keep `data/raw` for raw inputs; `data/processed` for derived datasets.
- Document all assumptions in `docs/`; link from README.
- Run linters/formatters before committing (e.g. `black`, `ruff`).
