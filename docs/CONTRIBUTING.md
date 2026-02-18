# Contributing & Setup

## Branching

- **main**: Production-ready code and documentation. Protected; only merged via PR.
- **task-1-dev**: Development for Task-1 (Foundation). All Task-1 work happens here first.
- **task-23-dev**: Development for Task-2 (Bayesian change point) and Task-3 (Flask + React dashboard). Combined branch; merge to `main` when stable.
- **task-N-dev**: Other future tasks branch from `main` as needed.

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
- **Local**: Before pushing, run `ruff check .`, `ruff format .`, and `pytest tests/` (use `requirements.txt`).

## Setup & running

- **Python**: 3.10+. Create and activate a venv from repo root: `py -m venv .venv` then `.\.venv\Scripts\Activate.ps1` (PowerShell) or `.\.venv\Scripts\activate.bat` (Cmd). Optional: `.\scripts\setup_venv.ps1` to create venv and install deps.
- **Dependencies**: `pip install -r requirements.txt`. Verify: `python scripts/verify_task2_env.py`.
- **Task-1**: Run `notebooks/task1_ingest_clean_diagnose.ipynb` (Run All) or `python notebooks/run_diagnostics.py`. Outputs: `docs/task-1/`, `data/processed/`.
- **Task-2**: Run `notebooks/task-2-change-point-analysis.ipynb` (Run All). Needs `data/processed/brent_returns.csv`. Writes `data/processed/change_point_posterior.json`, `docs/task-2/`. Kernel: use .venv or run `scripts\register_kernel.ps1` and select **Python (brent-task2)**; set `jupyter.kernelStartupTimeout` ≥ 120 if needed.
- **Task-3**: Backend: `python -m backend.app` (port 5000). Frontend: Node.js required; in a second terminal run `cd frontend` then `npm install` then `npm run dev`, or `scripts\run_frontend.cmd` from project root (Windows CMD use `cd /d` if project is on another drive). Open http://localhost:3000. Cursor terminal: `.vscode/settings.json` adds default Node paths on Windows; open a new terminal. Custom Node install: set **NODE_HOME**. See [docs/task-3/README.md](task-3/README.md) for full execution plan.
- **Troubleshooting**: PowerShell script execution: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`. "npm not recognized": install Node from nodejs.org, restart terminal/Cursor. "Could not read package.json": use `cd /d "drive:\path\to\frontend"` in CMD or `scripts\run_frontend.cmd`. Kernel timeout: register kernel (above), increase Jupyter kernel startup timeout to 120+.

## Repo hygiene

- Keep `data/raw` for raw inputs; `data/processed` for derived datasets.
- Document all assumptions in `docs/`; link from README.
- Run linters and tests before committing: `ruff check .`, `ruff format .`, `pytest tests/`.
