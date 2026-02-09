"""
Load processed Brent data and change point posterior for the dashboard API.
Paths are relative to project root (parent of backend/).
"""
import json
from pathlib import Path

import pandas as pd

# Project root: parent of this file -> backend -> project root
ROOT = Path(__file__).resolve().parent.parent.parent
PROCESSED_DIR = ROOT / "data" / "processed"
EVENTS_RAW = ROOT / "data" / "events" / "geopolitical_economic_opec_events.csv"


def get_returns():
    """Return Brent returns as list of {date, value} for charting."""
    path = PROCESSED_DIR / "brent_returns.csv"
    if not path.exists():
        return []
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")
    return df[["Date", "price"]].rename(columns={"price": "value"}).to_dict("records")


def get_prices():
    """Return Brent price levels as list of {date, value} for charting."""
    path = PROCESSED_DIR / "brent_prices_cleaned.csv"
    if not path.exists():
        return []
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")
    return df[["Date", "price"]].rename(columns={"price": "value"}).to_dict("records")


def get_events(category=None):
    """
    Return events: aligned if available, else raw. Optional filter by category
    (geopolitical, economic, opec_policy).
    """
    aligned = PROCESSED_DIR / "events_aligned.csv"
    if aligned.exists():
        df = pd.read_csv(aligned)
    else:
        df = pd.read_csv(EVENTS_RAW)
        if "trading_date" not in df.columns and "date" in df.columns:
            df["trading_date"] = df["date"]
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    df["trading_date"] = pd.to_datetime(df["trading_date"], errors="coerce").dt.strftime("%Y-%m-%d")
    if category:
        df = df[df["category"].str.lower() == category.lower()]
    return df[["event_id", "date", "trading_date", "category", "short_name", "description"]].fillna("").to_dict("records")


def get_change_point_posterior():
    """Load change point posterior summary (from Task-2 notebook export)."""
    path = PROCESSED_DIR / "change_point_posterior.json"
    if not path.exists():
        return None
    with open(path, "r") as f:
        return json.load(f)
