# Tests

- **Structure**: `test_repo_structure.py` — required directories and files (per README and Task-1).
- **Task-1 deliverables**: `test_task1_deliverables.py` — event CSV schema (columns, count, categories), docs content (workflow, causation, diagnostic results).
- **CI**: `.github/workflows/unittest.yml` runs `pytest tests/` plus lint (ruff) and the Task-1 diagnostics pipeline.

Run locally (from repo root, with venv activated):

```bash
pip install -r requirements-dev.txt
pytest tests/ -v
```
