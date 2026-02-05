"""Pytest fixtures: repo root and paths."""

import pytest
from pathlib import Path

# Repo root = parent of tests/
REPO_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture
def repo_root():
    return REPO_ROOT
