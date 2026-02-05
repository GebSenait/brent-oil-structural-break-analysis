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

## Repository structure

| Path | Purpose |
|------|---------|
| `data/raw/` | Unaltered Brent price series and external inputs. |
| `data/processed/` | Cleaned, derived series for modeling. |
| `data/events/` | Geopolitical/economic/OPEC event dataset (CSV + README). |
| `docs/` | Project and task documentation; `docs/task-1/` for Task-1. |
| `notebooks/` | Exploratory and Task-1 workflows; future Bayesian/dashboard work. |
| `src/` | Data loaders, diagnostics, and (later) models. |

See `data/README.md`, `notebooks/README.md`, and `src/README.md` for details.

---

## Technologies & tools

- **Language**: Python 3.x (recommend 3.10+).
- **Key libraries**: pandas, numpy, scipy/statsmodels (e.g. ADF), matplotlib/seaborn. Future: PyMC/Stan or similar for Bayesian change point.
- **Version control**: Git; branching strategy and commit guidelines in `docs/CONTRIBUTING.md`.
- **Environment**: Use a virtual environment and a requirements file (e.g. `requirements.txt`) for reproducibility.

---

## Getting started

1. Clone the repo; switch to `task-1-dev` for Task-1 work.
2. Create a virtual environment and install dependencies from `requirements.txt`.
3. Place Brent price data in `data/raw/` and document the source.
4. Follow the workflow in `docs/task-1/README.md` (ingest → diagnose → document).
5. Run notebooks in order where dependencies exist; record diagnostics in `docs/task-1/`.

For contribution and commit strategy, see `docs/CONTRIBUTING.md`.
