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

## CI/CD (GitHub Actions)

- **Workflow**: `.github/workflows/unittest.yml` runs on every push and pull request to `main` and `task-1-dev`.
- **Jobs**:
  1. **Lint**: `ruff check` and `ruff format --check` for code quality.
  2. **Test**: `pytest tests/` for repository structure and Task-1 deliverables (required dirs/files, event schema, docs content).
  3. **Task-1 pipeline**: Runs `notebooks/run_diagnostics.py` and checks that `docs/task-1/DIAGNOSTIC-RESULTS.md` and `data/processed/*.csv` are produced.
- **Local**: Before pushing, run `ruff check .`, `ruff format .`, and `pytest tests/` (use `requirements-dev.txt`).

## Repo hygiene

- Keep `data/raw` for raw inputs; `data/processed` for derived datasets.
- Document all assumptions in `docs/`; link from README.
- Run linters and tests before committing: `ruff check .`, `ruff format .`, `pytest tests/`.
