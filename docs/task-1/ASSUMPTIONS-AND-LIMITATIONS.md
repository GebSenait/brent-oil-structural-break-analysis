# Assumptions and limitations

This document states the main assumptions and limitations of the Task-1 foundation and of the overall change point analysis. It is intended to prevent overinterpretation and to align stakeholders and analysts on what the analysis can and cannot support.

---

## 1. Data limitations

- **Single price series**: We rely primarily on one Brent price series (spot or cash). Other benchmarks (WTI, Dubai) or regional prices may behave differently; we do not model cross-market relationships in Task-1.
- **Frequency and history**: Results depend on the chosen frequency (daily vs. monthly) and the length of history. Shorter samples may miss earlier regimes; longer samples may mix structural changes with different market eras.
- **Data quality**: Missing values, corrections, and source changes (e.g. methodology) can affect diagnostics and change point estimates. We assume raw data is validated and documented in `data/raw/`.
- **Event dataset**: The event list is curated, not exhaustive. Omitted or misdated events can affect the interpretation of detected breaks.

---

## 2. Methodological limitations

- **Change point detection**: Algorithms estimate *when* the distribution (e.g. mean or variance) may have changed, not *why*. Different methods (Bayesian vs. frequentist, mean vs. variance, number of breaks) can yield different answers; we will document and compare in Task-2.
- **Stationarity and structure**: Conclusions assume that the chosen transformation (e.g. returns) and model form are appropriate. If the true process is more complex (e.g. long memory, multiple regimes), our summaries are approximate.
- **Event alignment**: We use a simple rule (first trading day on or after event date). We do not estimate lead/lag or reaction windows in Task-1; that can be added later.
- **No formal causality**: We do not run causal inference (e.g. difference-in-differences, synthetic control). Coincidence in time between an event and a detected break is **correlational**, not proof of causation.

---

## 3. Correlation vs. causation

- **Correlation**: We can observe that a structural break in Brent prices occurs around the same time as a known event (e.g. OPEC decision, invasion). That is a **temporal association**.
- **Causation**: To claim that event *E* *caused* break *B*, we would need to rule out confounding, reverse causality, and omitted factors—which we do not do here. Multiple events often cluster; markets also react to expectations and to information that predates the “official” event date.
- **How we use the event list**: The event dataset supports **narrative and consistency checks**: “Did we see a break near this event? Is the direction of the break consistent with the event?” It does **not** support statements such as “This event caused X% of the price move.”

Stakeholders should treat change point results as **evidence for when dynamics changed**, and use events as **context for discussion**, not as established causal drivers.

---

## 4. Risks of misinterpretation

- **Over-attribution**: Assuming a single event “explains” a break when other factors (e.g. global demand, financial flows) are also at play.
- **Ignoring uncertainty**: Reported break dates have uncertainty (posterior or confidence intervals); treating them as exact can be misleading.
- **Extrapolation**: Past breaks and event associations do not guarantee future behavior; regime structure can change.

---

## 5. Scalability and future work

- The workflow and event schema are designed so that **Task-2** (Bayesian change point, scenario analysis) and **dashboards** can consume the same processed data and event list without redefining foundations.
- New events can be added to the CSV with versioning; new diagnostics (e.g. additional tests) can be appended to the plan in `docs/task-1/README.md` and linked from here.
