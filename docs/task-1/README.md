# Task-1: Laying the Foundation for Analysis

## 1. Objectives

- **Define a clear, reproducible data analysis workflow** from raw data ingestion to insight generation, so that all downstream modeling (Bayesian change point, scenario analysis) is statistically sound and aligned with business needs.
- **Research and compile 10–15 major geopolitical, economic, and OPEC-related events** into a structured dataset with explicit assumptions on event timing and classification.
- **Analyze time series properties** (trend, stationarity, volatility) of Brent oil prices and document how these properties inform modeling choices (e.g. differencing, prior choice, windowing).
- **Explain change point models**—purpose, expected outputs, and limitations—in business and technical terms so stakeholders and future analysts share a common understanding.
- **Document assumptions, constraints, and the distinction between correlation and causation** to avoid overinterpretation and to set expectations for what the analysis can and cannot support.

## 2. Analysis Workflow

High-level flow (each step is documented and reproducible):

1. **Ingest**  
   Load raw Brent price series and event dataset; validate schema and date ranges.

2. **Clean & align**  
   Handle missing values, align frequency (e.g. business days), and merge events to the price timeline with a defined rule (e.g. event date = first trading day on or after the calendar date).

3. **Diagnose**  
   Run time series diagnostics:
   - **Trend**: Visual inspection, simple linear/rolling trend; decide if we model levels or returns.
   - **Stationarity**: ADF (and optionally KPSS) tests; document whether differencing is required.
   - **Volatility**: Rolling variance, regime shifts; inform priors and likelihood choice (e.g. heteroskedasticity).

4. **Document**  
   Record results in `docs/task-1/` and in notebooks; link diagnostics to modeling implications.

5. **Prepare for modeling**  
   Produce processed series (e.g. returns, volatility proxy) and event windows for Task-2 (Bayesian change point and scenario analysis).

*Why this order:* Diagnostics before modeling avoids misspecification (e.g. using a level model when the series is non-stationary) and ensures that event timing assumptions are explicit before we attribute breaks to events.

## 3. Time Series Diagnostics Plan

| Check            | Tool / approach              | Purpose |
|------------------|------------------------------|---------|
| **Trend**        | Plot levels; rolling mean; simple regression of price on time | Decide level vs. return modeling; inform structural break interpretation. |
| **Stationarity** | ADF test (and KPSS if needed) on levels and returns | Choose differencing; validate that returns are suitable for many change point methods. |
| **Volatility**   | Rolling std, squared returns; visual inspection of volatility clusters | Inform variance structure (constant vs. time-varying) and priors in Bayesian models. |
| **Autocorrelation** | ACF/PACF of returns          | Guide AR/MA components if we add them later; check for simple dependencies. |

Results are summarized in **`docs/task-1/DIAGNOSTIC-RESULTS.md`** and in the notebook. Run **`notebooks/task1_ingest_clean_diagnose.ipynb`** to execute the full ingest → clean → diagnose workflow and regenerate that summary and figures. Clear statements include “Brent returns are treated as stationary for the change point model” or “Volatility is time-varying; we will use a heteroskedastic specification.”

## 4. Change Point Model — Purpose, Outputs, Limitations

### Purpose

- **Change point models** identify dates (or periods) where the *data-generating process* of the series (e.g. mean, variance, or both) shifts. In the Brent context, we use them to detect when price dynamics or volatility regimes change, and to align those changes with known events (e.g. OPEC decisions, geopolitical shocks) for interpretation—**not** to prove that an event “caused” the break.

### Expected outputs

- **Number and location of change points** (with uncertainty, e.g. posterior distributions or confidence intervals).
- **Regime characteristics**: e.g. mean and variance before/after each break.
- **Alignment with event dataset**: comparison of estimated break dates with event dates; discussion of consistency and outliers.

### Limitations

- **Correlation, not causation**: Coincidence in time does not imply that a specific event caused the break; confounding and omitted factors are possible.
- **Uncertainty**: Estimated break dates are uncertain; overlapping events make attribution harder.
- **Model choice**: Different algorithms (Bayesian vs. frequentist, mean vs. variance breaks) can yield different break counts and locations; we will document and compare.
- **Data quality**: Garbage-in, garbage-out; results depend on clean, correctly timed data and explicit event assumptions.

A concise technical note on the exact models to be used (e.g. Bayesian offline change point) will be added in Task-2; here we only establish the *purpose* and *expectations* so that stakeholders and analysts are aligned.

## 5. Expected Outputs (Task-1)

- **Repository structure** and README as the single entry point for the project.
- **Event dataset**: CSV with 10–15 events, schema, and an assumptions document (see `data/events/`).
- **Task-1 documentation**: This file plus any linked notes (assumptions, limitations, correlation vs. causation).
- **Diagnostics**: Run **`notebooks/task1_ingest_clean_diagnose.ipynb`** to perform ingest → clean → diagnose; results are recorded in **`docs/task-1/DIAGNOSTIC-RESULTS.md`** and optional figures in this folder.
- **Clear handoff**: Processed series in `data/processed/` and documentation ready for Task-2 (Bayesian modeling) and future dashboards.
