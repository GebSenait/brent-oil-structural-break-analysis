# Testing with Sample Data

To avoid long runtimes or out-of-memory errors when using the full **Brent oil** series (`data/raw/BrentOilPrices.csv`, ~9,000 rows), you can use a **small sample/synthetic dataset** for testing Task 1, Task 2, `run_diagnostics.py`, and the Task 3 React dashboard.

## What is the sample?

- **File:** `data/sample/BrentOilPrices_sample.csv`
- **Size:** ~1,170 rows (Jan 2018 – Jun 2022, business days)
- **Format:** Same as raw: `Date,Price` (dates as `"MMM DD, YYYY"`)
- **Content:** Synthetic prices from a geometric random walk (realistic level and volatility) so diagnostics and change-point logic run the same way.

Events still come from `data/events/geopolitical_economic_opec_events.csv`; Task 1 aligns only events whose calendar date falls within the sample’s trading range, so you get a subset of events automatically.

## Generate the sample

From the **repo root**:

```bash
python scripts/generate_sample_data.py
```

This creates or overwrites `data/sample/BrentOilPrices_sample.csv`. Re-run anytime to regenerate.

## Use the sample in runs

Set the environment variable **`USE_SAMPLE_DATA=1`** (or `true` / `yes`, case-insensitive), then run as usual.

### Task 1 notebook

1. Set `USE_SAMPLE_DATA=1` in your environment (or in the notebook’s env / first cell).
2. **Run All** on `notebooks/task1_ingest_clean_diagnose.ipynb`.

The notebook will read `data/sample/BrentOilPrices_sample.csv` and write to the same places: `data/processed/` and `docs/task-1/`.

### run_diagnostics.py (Task 1 pipeline)

From repo root:

```bash
# Windows (PowerShell)
$env:USE_SAMPLE_DATA=1; python notebooks/run_diagnostics.py

# Windows (cmd)
set USE_SAMPLE_DATA=1
python notebooks/run_diagnostics.py

# Linux / macOS
USE_SAMPLE_DATA=1 python notebooks/run_diagnostics.py
```

This produces the same outputs as Task 1 but using the sample series.

### Task 2 notebook

Task 2 does **not** read the raw CSV. It reads:

- `data/processed/brent_returns.csv`
- `data/processed/events_aligned.csv`
- (and optionally `brent_prices_cleaned.csv` if used)

So:

1. Run **Task 1** (or `run_diagnostics.py`) **with `USE_SAMPLE_DATA=1`** so that `data/processed/` is filled with sample-based series and events.
2. Run **Task 2** notebook **Run All** as usual. It will use the sample-based processed files and write `data/processed/change_point_posterior.json` and other Task 2 outputs.

No change to the Task 2 notebook is required; it automatically uses whatever is in `data/processed/`.

### Task 3 (React dashboard)

1. Run Task 1 and Task 2 with the sample as above so that `data/processed/change_point_posterior.json` (and any other artifacts the backend uses) exist and are based on the sample.
2. Start the API and frontend as in the main [Execution instructions](README.md#execution-instructions). The dashboard will show results from the sample run.

## Flow summary

| Step | Use sample? | What runs |
|------|-------------|-----------|
| 1 | `USE_SAMPLE_DATA=1` | Task 1 notebook or `run_diagnostics.py` → reads `data/sample/BrentOilPrices_sample.csv` → writes `data/processed/` and `docs/task-1/` |
| 2 | (automatic) | Task 2 notebook → reads `data/processed/*` → writes `change_point_posterior.json` etc. |
| 3 | (automatic) | `run_diagnostics.py` (if used) / Task 3 dashboard → use same `data/processed/` and docs |

One sample dataset is used across all three tasks for a consistent, fast test path.

## Switching back to full data

Unset the variable and re-run Task 1 (or `run_diagnostics.py`):

```bash
# Windows PowerShell
Remove-Item Env:USE_SAMPLE_DATA -ErrorAction SilentlyContinue
python notebooks/run_diagnostics.py

# Linux / macOS
unset USE_SAMPLE_DATA
python notebooks/run_diagnostics.py
```

Then run Task 2 again so `data/processed/` and the dashboard reflect the full series.
