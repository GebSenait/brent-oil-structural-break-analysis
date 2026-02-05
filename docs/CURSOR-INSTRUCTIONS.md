# Cursor-friendly instructions (this repo)

Concise but deep guidance for analysts and AI working in Cursor on this project.

---

## Repo role and scope

- **Project**: Change point analysis and statistical modeling of **Brent oil** time series for Birhan Energies. Business goal: understand how major events (geopolitical, economic, OPEC) align with structural breaks in prices; support investors and policymakers with evidence-based narrative—**not** causal claims.
- **Task-1**: Foundation only (workflow, event dataset, diagnostics plan, documentation). No Bayesian model yet; that is Task-2.

---

## Conventions to follow

- **Business vs. technical**: Keep `docs/` and READMEs in business-friendly language; keep implementation details in `src/`, notebooks, and technical subsections of `docs/task-1/`.
- **Events**: Event dates in `data/events/` use **calendar date**; when merging with prices use **first trading day on or after** that date. Do not add events without updating `data/events/README.md` or `docs/task-1/event-assumptions.md` if assumptions change.
- **Causation**: Never state that an event "caused" a break. Use "consistent with," "aligns with," "temporal association."
- **Reproducibility**: Every analysis step (load, clean, diagnose) should be runnable from code; document data source and version. Use `requirements.txt` and a single supported Python version (e.g. 3.10+).

---

## Where to put what

- **New event or schema change** → `data/events/` CSV + note in `data/events/README.md` or `docs/task-1/event-assumptions.md`.
- **Diagnostic results** (ADF, plots, regime comments) → `docs/task-1/` and/or notebooks; link from `docs/task-1/README.md`.
- **New code** (loaders, tests, diagnostics) → `src/` with clear module names; keep business logic separate from generic utils.
- **Assumptions or limitations** → Extend `docs/task-1/ASSUMPTIONS-AND-LIMITATIONS.md` and mention correlation vs. causation where relevant.

---

## Workflow order

1. Ingest raw Brent + events → validate schema and dates.  
2. Clean and align to trading days; merge events.  
3. Run diagnostics (trend, stationarity, volatility); document implications for modeling.  
4. Only then run change point models (Task-2); interpret breaks with event list and uncertainty.

---

## When adding code or docs

- Prefer clarity and interpretability over complexity.  
- Explain *why* a step exists (e.g. "ADF so we know whether to model returns").  
- Tie statistics to real-world oil market behavior where possible.  
- Ensure a new analyst can onboard in &lt;30 minutes using README and `docs/task-1/`.
