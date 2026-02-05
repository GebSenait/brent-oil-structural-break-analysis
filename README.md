# Change Point Analysis and Statistical Modeling of Time Series Data

**Birhan Energies** — Brent oil price analysis for decision support in a volatile global market.

---

## Project title

**Change Point Analysis and Statistical Modeling of Time Series Data** (Brent crude oil).

---

## Business purpose

Understand how **major geopolitical, economic, and policy-driven events** influence Brent oil prices. Results support **investors, policymakers, and energy companies** by:

- Identifying when price or volatility regimes have shifted.
- Aligning those shifts with a curated set of known events for interpretation.
- Providing a statistically rigorous, reproducible foundation for scenario analysis and risk communication.

*We do not claim to prove causation; we aim to detect structural breaks and to inform narrative and strategy with evidence.*

---

## Business needs

- **Reproducible workflow**: From raw data to insights, with clear documentation so new analysts can onboard quickly and audits are straightforward.
- **Event context**: A structured list of major events (OPEC, geopolitics, macro) so that detected change points can be discussed in business terms.
- **Statistical soundness**: Time series diagnostics before modeling so that choices (e.g. returns vs. levels, variance structure) are justified.
- **Scalability**: Foundation that supports future Bayesian change point models, dashboards, and scenario tools without redoing core design.

---

## Data description

- **Primary series**: Brent crude oil price (spot or cash), daily or monthly. Source to be documented in `data/raw/` (e.g. EIA, ICE).
- **Event dataset**: Curated 10–15 major events (geopolitical, economic, OPEC-related) with date, category, and short description. Schema and assumptions: `data/events/README.md` and `docs/task-1/event-assumptions.md`.

---

## Technical architecture / workflow (textual)

```
[Raw data: Brent prices + Event list]
           |
           v
    +------+------+
    |   Ingest    |  Validate schema, date ranges
    +------+------+
           |
           v
    +------+------+
    | Clean &     |  Missing values, frequency alignment,
    | Align       |  event date → first trading day rule
    +------+------+
           |
           v
    +------+------+
    | Diagnose    |  Trend, stationarity (ADF/KPSS),
    |             |  volatility, autocorrelation
    +------+------+
           |
           v
    +------+------+
    | Document    |  docs/task-1/, notebooks, handoff
    +------+------+
           |
           v
    [Processed series + event windows] --> Task-2 (Bayesian CP) / Dashboards
```

All steps are implemented in code (e.g. `src/`, notebooks) and documented so the pipeline is reproducible.

---

## Task-1 overview

**Task-1: Laying the foundation**

- Define and document the end-to-end workflow (ingest → clean → diagnose → document → prepare for modeling).
- Build the event dataset (10–15 events, CSV + schema + timing assumptions).
- Specify and run time series diagnostics (trend, stationarity, volatility) and document how they inform modeling.
- Explain change point models (purpose, outputs, limitations) for stakeholders and analysts.
- Document assumptions, limitations, and correlation vs. causation.

**Deliverables**: Repo structure, main README, Task-1 docs (`docs/task-1/`), event dataset (`data/events/`), assumptions and limitations, and a clear handoff for Task-2.

---

## Task-1: Test results, execution, and recommendations

### Execution

- **Notebook**: Run **`notebooks/task1_ingest_clean_diagnose.ipynb`** (Run All) with the project’s Python environment. The notebook runs: **Ingest** (Brent + events) → **Clean & align** (trading-day rule) → **Diagnose** (trend, ADF/KPSS, volatility, ACF/PACF) → **Document** (writes `docs/task-1/DIAGNOSTIC-RESULTS.md` and figures) → **Prepare** (saves `data/processed/` for Task-2).
- **Outputs**: `docs/task-1/DIAGNOSTIC-RESULTS.md`, `diagnostic_trend_volatility.png`, `diagnostic_acf_pacf_returns.png`, and processed series in `data/processed/` (cleaned prices, returns, events aligned to trading days).

### Test results (from latest run)

| Item | Result |
|------|--------|
| **Brent series** | ~9,011 daily observations (1987-05-20 to 2022-11-14). |
| **Returns** | ~9,010 observations after first difference. |
| **Events aligned** | 12 of 14 events mapped to first trading day on or after calendar date (2 outside price range). |
| **ADF (levels)** | Cannot reject unit root (p ≈ 0.29) → **levels non-stationary**. |
| **ADF (returns)** | Reject unit root (p ≈ 0.00) → **returns stationary**. |
| **KPSS (levels)** | Reject level stationarity → **levels non-stationary**. |
| **KPSS (returns)** | Do not reject level stationarity → **returns stationary**. |

### Analysis

- **Levels vs returns**: Brent **price levels** are treated as **non-stationary**; **returns** are treated as **stationary**. Change point and volatility modeling in Task-2 should use **returns** (or a stationary transform), not raw levels.
- **Volatility**: Rolling volatility is **time-varying** (e.g. spikes around 2008 and 2020). Task-2 should allow **heteroskedastic or regime-switching variance**, not constant variance.
- **Events**: The curated event list (geopolitical, economic, OPEC) is aligned to the price timeline; it will be used to **interpret** detected break dates (narrative only, no causal claim).

### Recommendations

- **For Task-2**: Use `data/processed/brent_returns.csv` and `events_aligned.csv`; model returns with time-varying or regime-dependent variance; compare posterior break dates to event dates for consistency.
- **For stakeholders**: Use Task-1 deliverables as the single source of truth for event definitions and alignment. When reporting Task-2 results, phrase findings as “structural break is consistent with the timing of event X,” not “event X caused the break.”
- **For reproducibility**: Re-run the notebook after any change to raw data or event list; `DIAGNOSTIC-RESULTS.md` and figures will update. See `docs/task-1/README.md` and `docs/task-1/ASSUMPTIONS-AND-LIMITATIONS.md` for full context.

---

## Repository structure

| Path | Purpose |
|------|---------|
| `.github/workflows/` | CI/CD: `unittest.yml` (lint, tests, Task-1 pipeline). |
| `data/raw/` | Unaltered Brent price series and external inputs. |
| `data/processed/` | Cleaned, derived series for modeling. |
| `data/events/` | Geopolitical/economic/OPEC event dataset (CSV + README). |
| `docs/` | Project and task documentation; `docs/task-1/` for Task-1. |
| `notebooks/` | Exploratory and Task-1 workflows; future Bayesian/dashboard work. |
| `src/` | Data loaders, diagnostics, and (later) models. |
| `tests/` | Pytest: repo structure, Task-1 deliverables, pipeline checks. |

See `data/README.md`, `notebooks/README.md`, `src/README.md`, and `docs/CONTRIBUTING.md` (CI/CD) for details.

---

## Technologies & tools

- **Language**: Python 3.x (recommend 3.10+).
- **Key libraries**: pandas, numpy, scipy/statsmodels (e.g. ADF), matplotlib/seaborn. Future: PyMC/Stan or similar for Bayesian change point.
- **Version control**: Git; branching strategy and commit guidelines in `docs/CONTRIBUTING.md`.
- **Environment**: Use a virtual environment and a requirements file (e.g. `requirements.txt`) for reproducibility.

---

## Getting started

1. Clone the repo; switch to `task-1-dev` for Task-1 work.
2. **Create and activate a Python virtual environment**, then install dependencies. See **`docs/SETUP.md`** for step-by-step instructions. Use Python **3.10+**; install from `requirements.txt`.
3. Place Brent price data in `data/raw/` and document the source (or use existing `BrentOilPrices.csv`).
4. Follow the workflow in `docs/task-1/README.md` (ingest → diagnose → document).
5. Run **`notebooks/task1_ingest_clean_diagnose.ipynb`** with the venv kernel selected; diagnostics are recorded in `docs/task-1/`.

For contribution and commit strategy, see `docs/CONTRIBUTING.md`.