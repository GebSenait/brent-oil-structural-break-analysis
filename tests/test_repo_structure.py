"""Ensure repository code structure meets project standards."""
import pytest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Required directories (per README and Task-1)
REQUIRED_DIRS = [
    "data",
    "data/raw",
    "data/processed",
    "data/events",
    "docs",
    "docs/task-1",
    "notebooks",
    "src",
    "tests",
]

# Required files for Task-1 and project hygiene
REQUIRED_FILES = [
    "README.md",
    "requirements.txt",
    "requirements-dev.txt",
    ".gitignore",
    "data/README.md",
    "data/raw/README.md",
    "data/processed/README.md",
    "data/events/README.md",
    "data/events/geopolitical_economic_opec_events.csv",
    "docs/CONTRIBUTING.md",
    "docs/SETUP.md",
    "docs/task-1/README.md",
    "docs/task-1/ASSUMPTIONS-AND-LIMITATIONS.md",
    "docs/task-1/event-assumptions.md",
    "notebooks/README.md",
    "notebooks/task1_ingest_clean_diagnose.ipynb",
    "notebooks/run_diagnostics.py",
    "src/__init__.py",
    "src/README.md",
]


@pytest.mark.parametrize("rel_path", REQUIRED_DIRS)
def test_required_directories_exist(repo_root, rel_path):
    """Required directories must exist."""
    path = repo_root / rel_path
    assert path.is_dir(), f"Missing required directory: {rel_path}"


@pytest.mark.parametrize("rel_path", REQUIRED_FILES)
def test_required_files_exist(repo_root, rel_path):
    """Required files must exist."""
    path = repo_root / rel_path
    assert path.is_file(), f"Missing required file: {rel_path}"


def test_raw_data_readme_documents_brent(repo_root):
    """data/raw/README should reference Brent or raw data."""
    readme = (repo_root / "data" / "raw" / "README.md").read_text(encoding="utf-8")
    assert "raw" in readme.lower() or "brent" in readme.lower()


def test_contributing_mentions_branching(repo_root):
    """CONTRIBUTING must document branching strategy (main, task-1-dev)."""
    contrib = (repo_root / "docs" / "CONTRIBUTING.md").read_text(encoding="utf-8")
    assert "main" in contrib and "task-1-dev" in contrib
