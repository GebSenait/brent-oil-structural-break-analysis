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

## Tasks overview

| Task | Description |
|------|-------------|
| **Task-1** | Ingest, clean, diagnose; event dataset; handoff to Task-2. |
| **Task-2** | Bayesian change point model (PyMC); posterior diagnostics; quantified impacts; event alignment. |
| **Task-3** | Flask API + React dashboard; event highlighting and filtering; decision-ready visualizations. |

---

## Task-2: Table of contents

- **Objective and model:** [docs/task-2/README.md](docs/task-2/README.md)
- **Notebook:** [notebooks/task-2-change-point-analysis.ipynb](notebooks/task-2-change-point-analysis.ipynb) — PyMC single change point on Brent returns, MCMC diagnostics, export for dashboard.

**Execution:** Run the notebook (Run All) after Task-1. Outputs: posterior summary, trace plots, `data/processed/change_point_posterior.json` for Task-3.

---

## Task-3: Table of contents

- **Objective and architecture:** [docs/task-3/README.md](docs/task-3/README.md)
- **Backend:** [backend/](backend/) — Flask app, [backend/app.py](backend/app.py), [backend/routes/](backend/routes/), [backend/services/](backend/services/).
- **Frontend:** [frontend/](frontend/) — React (Vite), [frontend/src/](frontend/src/), components and [Dashboard](frontend/src/pages/Dashboard.jsx).

**Execution:** Start Flask (`python -m backend.app`), then `cd frontend && npm install && npm run dev`. Open http://localhost:3000. Ensure `change_point_posterior.json` exists (run Task-2 notebook) for full dashboard.

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
| `data/processed/` | Cleaned series, returns, events aligned, change point posterior (Task-2 export). |
| `data/events/` | Geopolitical/economic/OPEC event dataset (CSV + README). |
| `docs/` | Task docs: `docs/task-1/`, `docs/task-2/`, `docs/task-3/`. |
| `notebooks/` | Task-1 ingest/diagnose; **Task-2** change point analysis (PyMC). |
| `backend/` | **Task-3** Flask API (app, routes, services). |
| `frontend/` | **Task-3** React dashboard (Vite, components, pages). |
| `src/` | Data loaders, diagnostics. |
| `tests/` | Pytest: repo structure, Task-1 deliverables. |

See `data/README.md`, `notebooks/README.md`, `docs/task-2/README.md`, `docs/task-3/README.md`, and `docs/CONTRIBUTING.md` for details.

---

## Insights summary (expected)

- **Statistically significant regime shifts:** Posterior distribution of the change point (τ) and 95% credible interval for break date.
- **Quantified impacts:** Change in mean return (μ₂ − μ₁) and volatility (σ₂ vs σ₁ or ratio) before vs after the break.
- **Event alignment:** Detected break date(s) compared with curated geopolitical, economic, and OPEC events for narrative context (no causal claim).
- **Decision support:** Dashboard enables exploration of returns, prices, events by category, and posterior summary for investment timing, policy planning, and operational strategy.

---

## Technologies & tools

- **Language**: Python 3.10+.
- **Task-1/2**: pandas, numpy, scipy, statsmodels, matplotlib, seaborn, **PyMC**, **ArviZ**.
- **Task-3**: **Flask**, Flask-CORS (backend); **React**, Vite, Recharts (frontend).
- **Version control**: Git; branches `main` (stable), `task-23-dev` (Task-2 + Task-3); see `docs/CONTRIBUTING.md`.
- **Environment**: Python venv + `requirements.txt`; Node.js for frontend (`frontend/package.json`).

---

## Execution instructions

1. **Setup:** Clone the repo; create and activate a Python 3.10+ venv; `pip install -r requirements.txt`. See `docs/SETUP.md`.
2. **Task-1:** Run `notebooks/task1_ingest_clean_diagnose.ipynb` (Run All). Outputs in `data/processed/` and `docs/task-1/`.
3. **Task-2:** Run `notebooks/task-2-change-point-analysis.ipynb` (Run All). Outputs in `docs/task-2/` and `data/processed/change_point_posterior.json`.
4. **Task-3:** Start API: `python -m backend.app` (port 5000). Then: `cd frontend && npm install && npm run dev`; open http://localhost:3000.
5. **Branch:** Task-2 and Task-3 development on **`task-23-dev`**; merge to `main` when stable.

For contribution and commit strategy, see `docs/CONTRIBUTING.md`.