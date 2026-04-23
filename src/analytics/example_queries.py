from __future__ import annotations

from pathlib import Path

import pandas as pd


def read_csv_if_exists(path: str) -> pd.DataFrame:
    file_path = Path(path)
    if not file_path.exists():
        return pd.DataFrame()
    return pd.read_csv(file_path, low_memory=False)


def top_device_problems_latest_year(path: str = "data/processed/device_problem_year_summary.csv") -> pd.DataFrame:
    df = read_csv_if_exists(path)
    if df.empty or "event_count" not in df.columns:
        return pd.DataFrame()

    year_col = "report_year" if "report_year" in df.columns else "event_year" if "event_year" in df.columns else None
    if not year_col:
        return pd.DataFrame()

    latest_year = df[year_col].dropna().max()
    return (
        df[df[year_col] == latest_year]
        .sort_values("event_count", ascending=False)
        .head(10)
    )


def top_manufacturers_latest_year(path: str = "data/processed/manufacturer_year_summary.csv") -> pd.DataFrame:
    df = read_csv_if_exists(path)
    if df.empty or "event_count" not in df.columns:
        return pd.DataFrame()

    year_col = "report_year" if "report_year" in df.columns else "event_year" if "event_year" in df.columns else None
    if not year_col:
        return pd.DataFrame()

    latest_year = df[year_col].dropna().max()
    return (
        df[df[year_col] == latest_year]
        .sort_values("event_count", ascending=False)
        .head(10)
    )


if __name__ == "__main__":
    print("Top device problems for latest year:")
    print(top_device_problems_latest_year())
    print("\nTop manufacturers for latest year:")
    print(top_manufacturers_latest_year())