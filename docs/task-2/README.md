# Task-2: Bayesian Change Point Modeling

**Objective:** Detect structural breaks in Brent oil returns using a Bayesian change point model (PyMC), interpret the posterior distribution of the switch point and regime parameters, and quantify before/after impacts for decision support. No causal claims are made; we align detected breaks with a curated event list for narrative context.

---

## 1. Objective

- Fit a **single discrete change point model** to Brent daily returns (from Task-1 processed data).
- Estimate the **posterior distribution** of the switch index τ (tau), and of the pre- and post-regime means and standard deviations.
- Perform **MCMC diagnostics** (Rhat, ESS) and interpret results.
- **Quantify impacts**: mean return and volatility before vs after the estimated break.
- **Align** posterior break date(s) with the curated geopolitical/economic/OPEC event list for hypothesis-forming and stakeholder narrative (correlation/consistency only).

---

## 2. Data Preparation & EDA

- **Source:** `data/processed/brent_returns.csv` (Date, price) — the "price" column is the daily log or simple return from Task-1.
- **Events:** `data/processed/events_aligned.csv` (event_id, date, category, short_name, description, trading_date).
- **Preparation:** Parse dates, drop any NaNs, and use the return series as the observed data. EDA (e.g. time plot, rolling mean/volatility) is in the notebook.

---

## 3. Bayesian Change Point Model (PyMC)

- **Likelihood:** For observation index \(t = 1, \ldots, T\),  
  - \(y_t \sim \mathcal{N}(\mu_1, \sigma_1)\) if \(t < \tau\),  
  - \(y_t \sim \mathcal{N}(\mu_2, \sigma_2)\) if \(t \geq \tau\).
- **Parameters:**  
  - \(\tau\) (tau): discrete change point index in \(\{1, 2, \ldots, T-1\}\).  
  - \(\mu_1, \mu_2\): regime means (e.g. Normal priors).  
  - \(\sigma_1, \sigma_2\): regime standard deviations (e.g. HalfNormal or HalfStudentT).
- **Implementation:** PyMC model with `pm.Categorical` or index-based switch for τ; observed likelihood via `pm.Normal` with mean and sigma selected by segment. See `notebooks/task-2-change-point-analysis.ipynb`.

---

## 4. Sampling & Diagnostics

- **Sampler:** NUTS (default in PyMC) for continuous parameters; discrete τ is handled by PyMC (e.g. marginalization or discrete sampling).
- **Diagnostics:**  
  - **Rhat** < 1.01 for all parameters.  
  - **ESS** (bulk/tail) sufficiently large (e.g. > 400 per chain).  
  - Trace plots and posterior distributions for τ, μ₁, μ₂, σ₁, σ₂.
- **Documentation:** Summary table and plots are produced in the notebook and referenced here.

---

## 5. Results & Quantified Impacts

- **Posterior summary:** Mean/median and credible intervals for τ (converted to date), μ₁, μ₂, σ₁, σ₂.
- **Quantified impacts:**  
  - Change in mean return: μ₂ − μ₁ (posterior mean and interval).  
  - Change in volatility: σ₂ vs σ₁ (e.g. ratio or difference).  
- **Decision-ready narrative:** e.g. “The posterior places the single break at [date]; the post-break regime shows [higher/lower] mean return and [higher/lower] volatility, consistent with [event list].”

---

## 6. Event Alignment & Hypotheses

- Map posterior break date(s) to the nearest events in `events_aligned.csv` (by trading_date).
- State alignment as **consistency/correlation**, not causation: e.g. “The estimated break is consistent with the timing of [Event X].”
- Note any events that fall inside the posterior credible interval for the break date.

---

## 7. Limitations & Future Work

- **Single change point:** The model assumes one break; the series may have multiple regimes. Extensions: multiple change points, or hierarchical models.
- **Causality:** We do not infer that any event “caused” the break; we only assess timing consistency.
- **Prior sensitivity:** Results can be checked under alternative priors (e.g. different σ priors).
- **Future:** Add macro variables (e.g. VIX, spreads) as covariates; extend to multi-break or time-varying variance models.

---

## 8. Execution

Run the Jupyter notebook **`notebooks/task-2-change-point-analysis.ipynb`** (Run All) with the project’s Python environment. Ensure `data/processed/brent_returns.csv` and `data/processed/events_aligned.csv` exist (from Task-1). The notebook writes posterior summaries and, if configured, exports JSON/artifacts for the Task-3 dashboard API.
