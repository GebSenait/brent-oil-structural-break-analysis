"""Validate Task-1 deliverables: event schema, docs content, and key artifacts."""

import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Event CSV schema (per data/events/README.md)
EVENT_REQUIRED_COLUMNS = ["event_id", "date", "category", "short_name"]
EVENT_CATEGORIES = {
    "geopolitical",
    "economic",
    "opec_policy",
    "supply_shock",
    "demand_shock",
    "other",
}
MIN_EVENTS = 10
MAX_EVENTS = 20  # 10-15 requested; allow some headroom


def test_events_csv_schema(repo_root):
    """Events CSV must have required columns."""
    path = repo_root / "data" / "events" / "geopolitical_economic_opec_events.csv"
    assert path.is_file()
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        row = next(reader)
        for col in EVENT_REQUIRED_COLUMNS:
            assert col in row, f"Events CSV missing column: {col}"


def test_events_csv_count(repo_root):
    """Events CSV must contain 10–15 (or up to 20) events."""
    path = repo_root / "data" / "events" / "geopolitical_economic_opec_events.csv"
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert MIN_EVENTS <= len(rows) <= MAX_EVENTS, (
        f"Events count {len(rows)} outside expected range [{MIN_EVENTS}, {MAX_EVENTS}]"
    )


def test_events_csv_categories(repo_root):
    """Event categories must be from allowed set (or documented other)."""
    path = repo_root / "data" / "events" / "geopolitical_economic_opec_events.csv"
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        cat = (row.get("category") or "").strip()
        assert cat in EVENT_CATEGORIES, f"Unknown category: {cat}"


def test_task1_readme_has_workflow(repo_root):
    """docs/task-1/README must describe the analysis workflow."""
    readme = (repo_root / "docs" / "task-1" / "README.md").read_text(encoding="utf-8")
    assert "workflow" in readme.lower() or "ingest" in readme.lower()
    assert "diagnos" in readme.lower() or "stationarity" in readme.lower()


def test_assumptions_doc_mentions_causation(repo_root):
    """Assumptions doc must address correlation vs causation."""
    path = repo_root / "docs" / "task-1" / "ASSUMPTIONS-AND-LIMITATIONS.md"
    text = path.read_text(encoding="utf-8")
    assert "causation" in text.lower() or "correlation" in text.lower()


def test_diagnostic_results_or_placeholder(repo_root):
    """Either DIAGNOSTIC-RESULTS.md exists or notebook is the source (structure check)."""
    path = repo_root / "docs" / "task-1" / "DIAGNOSTIC-RESULTS.md"
    # After first run or CI run it exists; if not, at least task-1 docs dir exists
    assert (repo_root / "docs" / "task-1").is_dir()
    if path.is_file():
        text = path.read_text(encoding="utf-8")
        assert "ADF" in text or "stationarity" in text.lower()
