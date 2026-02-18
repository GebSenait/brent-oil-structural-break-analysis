# Contributing & Setup

**Remote:** No `origin`? `git remote add origin https://github.com/USER/REPO.git` then `git push -u origin main`. Push rejected (behind remote)? `git pull origin main` then push, or `git push --force origin main` to overwrite remote.

**Branches:** `main` (production, PR only); `task-1-dev` (Task-1); `task-23-dev` (Task-2 + Task-3).

**Commits:** One logical change per commit; no direct push to `main` (use PRs).

**CI:** `.github/workflows/unittest.yml` — lint (ruff), `pytest tests/`, Task-1 pipeline. Before push: `ruff check .`, `ruff format .`, `pytest tests/`.

**Setup:** Python 3.10+. `py -m venv .venv`, `.\.venv\Scripts\Activate.ps1`, `pip install -r requirements.txt`. Task-1: notebook or `python notebooks/run_diagnostics.py`. Task-2: run notebook (kernel .venv or `scripts\register_kernel.ps1`; `jupyter.kernelStartupTimeout` ≥ 120). Task-3: `python -m backend.app` then `cd frontend`, `npm install`, `npm run dev` (Node required; CMD on other drive: `cd /d` or `scripts\run_frontend.cmd`). See [task-3/README.md](task-3/README.md) for frontend details.

**Hygiene:** `data/raw` = inputs, `data/processed` = outputs. Before commit: `ruff check .`, `ruff format .`, `pytest tests/`.
