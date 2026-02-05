# Source code

- **data**: Loaders, validation, event alignment (e.g. `load_brent.py`, `load_events.py`).
- **diagnostics**: Time series diagnostics (stationarity tests, volatility metrics, trend checks).
- **models** (future): Change point detection, Bayesian models.
- **utils**: Shared helpers (logging, paths, constants). Keep business logic in `data/` and `models/`.
