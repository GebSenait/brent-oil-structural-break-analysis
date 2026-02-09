# Change Point Analysis and Statistical Modeling of Time Series Data

**Birhan Energies** — Brent crude oil price analysis for decision support in a volatile global market. This repository detects structural breaks in Brent prices using Bayesian change point modeling and aligns them with major geopolitical, economic, and OPEC events.

---

## Table of contents

| Section | Links |
|--------|--------|
| **Project** | [Project title](#project-title) · [Business purpose](#business-purpose) · [Business needs](#business-needs) · [Data description](#data-description) · [Technical architecture](#technical-architecture) |
| **Task-1** | [Description](#task-1-description) · [Implementation](#task-1-implementation) · [Test results](#task-1-test-results) · [Insights](#task-1-insights) |
| **Task-2** | [Description](#task-2-description) · [Implementation](#task-2-implementation) · [Test results](#task-2-test-results) · [Insights](#task-2-insights) |
| **Task-3** | [Description](#task-3-description) · [Implementation](#task-3-implementation) · [Test results](#task-3-test-results) · [Insights](#task-3-insights) |
| **Reference** | [Repository structure](#repository-structure) · [Insights summary](#insights-summary) · [Technologies & tools](#technologies--tools) · [Execution instructions](#execution-instructions) |

---

## Project title

**Change Point Analysis and Statistical Modeling of Time Series Data** — Brent crude oil. Ingest → clean → diagnose (Task-1); Bayesian single change point (Task-2); Flask API and React dashboard (Task-3).

---

## Business purpose

Understand how **major geopolitical, economic, and policy-driven events** influence Brent oil prices. Results support **investors, policymakers, and energy companies** by:

- Identifying when price or volatility regimes have shifted.
- Aligning those shifts with a curated set of known events for interpretation.
- Providing a statistically rigorous, reproducible foundation for scenario analysis and risk communication.

*We do not claim causation; we detect structural breaks and inform narrative and strategy with evidence.*

---

## Business needs

- **Reproducible workflow**: Raw data to insights with clear documentation for onboarding and audits.
- **Event context**: Structured list of major events (OPEC, geopolitics, macro) for discussing change points in business terms.
- **Statistical soundness**: Time series diagnostics before modeling to justify choices (returns vs levels, variance structure).
- **Scalability**: Foundation for Bayesian change point models, dashboards, and scenario tools.

---

## Data description

- **Primary series**: Brent crude oil price (spot/cash), daily. Source documented in `data/raw/` (e.g. EIA, ICE).
- **Event dataset**: Curated 10–15 events (geopolitical, economic, OPEC) with date, category, and description. Schema: [data/events/README.md](data/events/README.md) and [docs/task-1/event-assumptions.md](docs/task-1/event-assumptions.md).

---

## Technical architecture

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
    [Processed series + event windows] --> Task-2 (Bayesian CP) / Task-3 (Dashboard)
```

All steps are implemented in code (`src/`, notebooks) and documented for reproducibility.

---

## Tasks overview

| Task | Description |
|------|-------------|
| **Task-1** | Ingest, clean, diagnose; event dataset; handoff to Task-2. |
| **Task-2** | Bayesian change point model (PyMC); posterior diagnostics; quantified impacts; event alignment. |
| **Task-3** | Flask API + React dashboard; event highlighting and filtering; decision-ready visualizations. |

---

## Task-1: Description

**Objective:** Lay the foundation for change point analysis with a clear, reproducible workflow and a curated event dataset.

- Define and document the end-to-end workflow: **ingest → clean → diagnose → document → prepare for modeling**.
- Build the event dataset: 10–15 events (CSV + schema + timing assumptions) in `data/events/`.
- Run time series diagnostics (trend, stationarity, volatility) and document how they inform modeling.
- Explain change point models (purpose, outputs, limitations) for stakeholders and analysts.
- Document assumptions, limitations, and the distinction between correlation and causation.

**Deliverables:** Repo structure, Task-1 docs in [docs/task-1/](docs/task-1/), event dataset in [data/events/](data/events/), and processed series in `data/processed/` for Task-2.

---

## Task-1: Implementation

| Item | Location |
|------|----------|
| **Notebook** | [notebooks/task1_ingest_clean_diagnose.ipynb](notebooks/task1_ingest_clean_diagnose.ipynb) |
| **Workflow** | Ingest (Brent + events) → Clean & align (trading-day rule) → Diagnose (trend, ADF/KPSS, volatility, ACF/PACF) → Document → Prepare |
| **Outputs** | [docs/task-1/DIAGNOSTIC-RESULTS.md](docs/task-1/DIAGNOSTIC-RESULTS.md), diagnostic figures, [data/processed/](data/processed/) (cleaned prices, returns, events aligned) |
| **Docs** | [docs/task-1/README.md](docs/task-1/README.md), [docs/task-1/ASSUMPTIONS-AND-LIMITATIONS.md](docs/task-1/ASSUMPTIONS-AND-LIMITATIONS.md) |

**Execution:** Run the notebook **Run All** with the project Python environment. Outputs are written to `docs/task-1/` and `data/processed/`.

---

## Task-1: Test results

| Item | Result |
|------|--------|
| **Brent series** | ~9,011 daily observations (1987-05-20 to 2022-11-14). |
| **Returns** | ~9,010 observations after first difference. |
| **Events aligned** | 12 of 14 events mapped to first trading day on or after calendar date (2 outside price range). |
| **ADF (levels)** | Cannot reject unit root (p ≈ 0.29) → **levels non-stationary**. |
| **ADF (returns)** | Reject unit root (p ≈ 0.00) → **returns stationary**. |
| **KPSS (levels)** | Reject level stationarity → **levels non-stationary**. |
| **KPSS (returns)** | Do not reject level stationarity → **returns stationary**. |

---

## Task-1: Insights

- **Levels vs returns:** Brent **price levels** are **non-stationary**; **returns** are **stationary**. Task-2 change point and volatility modeling use **returns**, not raw levels.
- **Volatility:** Rolling volatility is **time-varying** (e.g. spikes around 2008 and 2020). Task-2 uses **regime-dependent variance** (σ₁, σ₂), not constant variance.
- **Events:** The curated event list is aligned to the price timeline and used to **interpret** detected break dates (narrative only; no causal claim).
- **Recommendations:** Use `data/processed/brent_returns.csv` and `events_aligned.csv` in Task-2; phrase findings as “structural break is consistent with the timing of event X,” not “event X caused the break.” See [docs/task-1/INSIGHTS-AND-RECOMMENDATIONS.md](docs/task-1/INSIGHTS-AND-RECOMMENDATIONS.md).

---

## Task-2: Description

**Objective:** Detect structural breaks in Brent oil returns using a Bayesian change point model (PyMC), interpret the posterior distribution of the switch point and regime parameters, and quantify before/after impacts.

- Fit a **single change point model** to Brent daily returns (from Task-1 processed data).
- Estimate the **posterior distribution** of the switch index τ (tau) and of pre- and post-regime means (μ₁, μ₂) and standard deviations (σ₁, σ₂).
- Perform **MCMC diagnostics** (Rhat, ESS) and interpret results.
- **Quantify impacts:** change in mean return (μ₂ − μ₁) and volatility (σ₂ vs σ₁).
- **Align** posterior break date(s) with the curated event list for narrative context (correlation/consistency only).

**Deliverables:** Posterior summary, trace plots, break date with 95% credible interval, quantified impacts, event alignment, and export to `data/processed/change_point_posterior.json` for Task-3.

---

## Task-2: Implementation

| Item | Location |
|------|----------|
| **Notebook** | [notebooks/task-2-change-point-analysis.ipynb](notebooks/task-2-change-point-analysis.ipynb) |
| **Model** | Single break: observations t < τ from N(μ₁, σ₁), t ≥ τ from N(μ₂, σ₂). Continuous τ in [1, T−1] with NUTS. |
| **Outputs** | Posterior summary, trace plots, [data/processed/change_point_posterior.json](data/processed/change_point_posterior.json), figures in [docs/task-2/](docs/task-2/) |
| **Docs** | [docs/task-2/README.md](docs/task-2/README.md) |

**Execution:** Run the notebook **Run All** after Task-1. Ensure `data/processed/brent_returns.csv` and `data/processed/events_aligned.csv` exist. The notebook writes `change_point_posterior.json` for the Task-3 dashboard.

---

## Task-2: Test results

| Item | Result |
|------|--------|
| **Rhat** | All parameters < 1.01 (convergence). |
| **ESS (bulk)** | Minimum ESS meets diagnostic threshold (e.g. > 400 per chain). |
| **Break date** | Posterior mean/median and 95% credible interval converted to date. |
| **Regime means** | μ₁, μ₂ with credible intervals; Δμ = μ₂ − μ₁. |
| **Regime volatilities** | σ₁, σ₂ with credible intervals; ratio or difference reported. |

Full diagnostics (trace plots, posterior distributions) are in the notebook. Summary and event alignment are exported to `change_point_posterior.json`.

---

## Task-2: Insights

- **Statistically significant regime shift:** Posterior distribution of τ yields a break date with 95% credible interval; narrative is decision-ready (e.g. “The posterior places the single break at [date]”).
- **Quantified impacts:** Post-break regime shows higher/lower mean return and higher/lower volatility; Δμ and σ₂/σ₁ (or difference) quantify the change.
- **Event alignment:** Estimated break date is compared with events in `events_aligned.csv`; findings stated as consistency/correlation, not causation.
- **Limitations:** Single change point assumed; prior sensitivity and causality are documented in [docs/task-2/README.md](docs/task-2/README.md).

---

## Task-3: Description

**Objective:** Expose Task-2 change point results and Task-1 event context through a Flask API and React frontend so stakeholders can explore regime shifts, filter events by category, and view decision-ready summaries without running notebooks.

- Provide **REST APIs** for returns, prices, events (with optional category filter), and the change point posterior summary.
- Build an **interactive React dashboard** that visualizes returns and price levels, highlights the posterior break date, and lists/filters events.
- Ensure **responsive layout** and **clear, probabilistic narratives** (no causal claims).

**Deliverables:** Flask backend ([backend/](backend/)), React frontend ([frontend/](frontend/)), API documentation, and setup/run instructions in [docs/task-3/README.md](docs/task-3/README.md).

---

## Task-3: Implementation

| Item | Location |
|------|----------|
| **Backend** | [backend/app.py](backend/app.py), [backend/routes/api.py](backend/routes/api.py), [backend/services/data_service.py](backend/services/data_service.py) |
| **Frontend** | [frontend/src/App.jsx](frontend/src/App.jsx), [frontend/src/pages/Dashboard.jsx](frontend/src/pages/Dashboard.jsx), [frontend/src/components/](frontend/src/components/) (ReturnsChart, ChangePointSummary, EventsTable) |
| **API** | GET `/api/health`, `/api/returns`, `/api/prices`, `/api/events?category=`, `/api/change-point` — see [docs/task-3/README.md](docs/task-3/README.md) |
| **Docs** | [docs/task-3/README.md](docs/task-3/README.md) |

**Execution:** From project root: `python -m backend.app` (port 5000). Then `cd frontend && npm install && npm run dev`; open http://localhost:3000. Ensure `data/processed/change_point_posterior.json` exists (run Task-2 notebook) for full dashboard.

---

## Task-3: Test results

| Item | Result |
|------|--------|
| **Health** | GET `/api/health` returns `{ "status": "ok" }`. |
| **Returns/Prices** | GET `/api/returns` and `/api/prices` return `{ "data": [...], "count": N }`. |
| **Events** | GET `/api/events` and `/api/events?category=geopolitical` return filtered events. |
| **Change point** | GET `/api/change-point` returns posterior summary or 404 if Task-2 output is missing. |
| **Dashboard** | Loads returns/prices charts, break date summary, events table with category filter; responsive layout, dark theme. |

---

## Task-3: Insights

- **Decision support:** Dashboard enables exploration of returns, prices, events by category, and posterior summary for investment timing, policy planning, and operational strategy.
- **No code required:** Stakeholders view regime shifts and event context without running notebooks or Python.
- **Single source of truth:** Backend reads from `data/processed/` and Task-2 export; frontend presents consistent, probabilistic narratives.

---

## Repository structure

| Path | Purpose |
|------|---------|
| `.github/workflows/` | CI/CD: `unittest.yml` (lint, tests, Task-1 pipeline). |
| `data/raw/` | Unaltered Brent price series and external inputs. |
| `data/processed/` | Cleaned series, returns, events aligned, change point posterior (Task-2 export). |
| `data/events/` | Geopolitical/economic/OPEC event dataset (CSV + README). |
| `docs/` | Task docs: [docs/task-1/](docs/task-1/), [docs/task-2/](docs/task-2/), [docs/task-3/](docs/task-3/). |
| `notebooks/` | Task-1 ingest/diagnose; Task-2 change point analysis (PyMC). |
| `backend/` | Task-3 Flask API (app, routes, services). |
| `frontend/` | Task-3 React dashboard (Vite, components, pages). |
| `src/` | Data loaders, diagnostics. |
| `tests/` | Pytest: repo structure, Task-1 deliverables. |

See [data/README.md](data/README.md), [notebooks/README.md](notebooks/README.md), and [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for details.

---

## Insights summary

- **Regime shifts:** Posterior distribution of the change point (τ) and 95% credible interval for break date.
- **Quantified impacts:** Change in mean return (μ₂ − μ₁) and volatility (σ₂ vs σ₁ or ratio) before vs after the break.
- **Event alignment:** Detected break date(s) compared with curated geopolitical, economic, and OPEC events for narrative context (no causal claim).
- **Decision support:** Dashboard enables exploration of returns, prices, events by category, and posterior summary for strategy and communication.

---

## Technologies & tools

| Layer | Stack |
|-------|--------|
| **Language** | Python 3.10+ |
| **Task-1/2** | pandas, numpy, scipy, statsmodels, matplotlib, seaborn, **PyMC**, **ArviZ** |
| **Task-3 backend** | **Flask**, Flask-CORS |
| **Task-3 frontend** | **React**, Vite, Recharts |
| **Version control** | Git; branches `main` (stable), `task-23-dev` (Task-2 + Task-3); see [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) |
| **Environment** | Python venv + [requirements.txt](requirements.txt); Node.js for frontend ([frontend/package.json](frontend/package.json)) |

---

## Execution instructions

1. **Setup:** Clone the repo; create and activate a Python 3.10+ venv; `pip install -r requirements.txt`. See [docs/SETUP.md](docs/SETUP.md).
2. **Task-1:** Run [notebooks/task1_ingest_clean_diagnose.ipynb](notebooks/task1_ingest_clean_diagnose.ipynb) (Run All). Outputs in `data/processed/` and `docs/task-1/`.
3. **Task-2:** Run [notebooks/task-2-change-point-analysis.ipynb](notebooks/task-2-change-point-analysis.ipynb) (Run All). Outputs in `docs/task-2/` and `data/processed/change_point_posterior.json`.
4. **Task-3:** Start API: `python -m backend.app` (port 5000). Then: `cd frontend && npm install && npm run dev`; open http://localhost:3000.
5. **Branch:** Task-2 and Task-3 development on **`task-23-dev`**; merge to `main` when stable.

For contribution and commit strategy, see [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).
