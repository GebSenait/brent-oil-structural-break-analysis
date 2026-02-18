"""
Generate a small sample/synthetic Brent-style price series for fast testing of
Task 1, Task 2, and run_diagnostics.py (and thus the React dashboard).

Usage (from repo root):
  python scripts/generate_sample_data.py

Output:
  data/sample/BrentOilPrices_sample.csv  (~1,100 rows, Date,Price)

Then run with sample data:
  set USE_SAMPLE_DATA=1
  python notebooks/run_diagnostics.py
  (and run task1/task2 notebooks with USE_SAMPLE_DATA=1)

Same sample is used across Task 1 → processed outputs → Task 2 → run_diagnostics → Task 3 dashboard.
"""

from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
SAMPLE_DIR = ROOT / "data" / "sample"
SAMPLE_CSV = SAMPLE_DIR / "BrentOilPrices_sample.csv"

# Date range: ~4.5 years of trading days (aligns with several events in events CSV)
START = "2018-01-02"
END = "2022-06-30"
# Initial price level (Brent was in this range in 2018)
INITIAL_PRICE = 65.0
# Daily return drift and volatility (roughly consistent with historical Brent)
DRIFT = 0.0001
VOLATILITY = 0.018
SEED = 42


def main():
    np.random.seed(SEED)
    SAMPLE_DIR.mkdir(parents=True, exist_ok=True)

    # Trading days only
    dates = pd.bdate_range(start=START, end=END, freq="B")
    n = len(dates)
    # Geometric random walk
    log_returns = np.random.normal(DRIFT, VOLATILITY, size=n)
    prices = INITIAL_PRICE * np.exp(np.cumsum(log_returns))
    prices = np.round(prices, 2)

    df = pd.DataFrame({"Date": dates, "Price": prices})
    # Match late-format from full CSV: "MMM DD, YYYY"
    df["Date"] = df["Date"].dt.strftime("%b %d, %Y")

    df.to_csv(SAMPLE_CSV, index=False)
    print("Written:", SAMPLE_CSV)
    print("Rows:", len(df))
    print("Date range:", df["Date"].iloc[0], "to", df["Date"].iloc[-1])
    print("Use with: set USE_SAMPLE_DATA=1 then run task1 notebook or run_diagnostics.py")


if __name__ == "__main__":
    main()
