from __future__ import annotations

import pandas as pd
from pathlib import Path


DEVICE_PROBLEM_YEAR_PATH = "data/processed/device_problem_year_summary.csv"
MANUFACTURER_YEAR_PATH = "data/processed/manufacturer_year_summary.csv"


def read_csv_if_exists(path: str) -> pd.DataFrame:
    file_path = Path(path)
    if not file_path.exists():
        return pd.DataFrame()
    return pd.read_csv(file_path, low_memory=False)


def answer_device_problem_trend() -> dict:
    df = read_csv_if_exists(DEVICE_PROBLEM_YEAR_PATH)
    if df.empty or "event_count" not in df.columns:
        return {
            "answer_type": "device_problem_trend",
            "status": "no_data",
            "summary": "Device problem trend data is not available yet.",
            "data": [],
            "sources": ["data/processed/device_problem_year_summary.csv"],
        }

    year_col = "report_year" if "report_year" in df.columns else "event_year" if "event_year" in df.columns else None
    if not year_col:
        return {
            "answer_type": "device_problem_trend",
            "status": "no_data",
            "summary": "A usable year field is not available yet.",
            "data": [],
            "sources": ["data/processed/device_problem_year_summary.csv"],
        }

    latest_year = df[year_col].dropna().max()
    latest = df[df[year_col] == latest_year].sort_values("event_count", ascending=False).head(10)

    return {
        "answer_type": "device_problem_trend",
        "status": "ok",
        "summary": f"Top device problem categories in the latest available year ({latest_year}) are shown below.",
        "data": latest.to_dict(orient="records"),
        "sources": ["data/processed/device_problem_year_summary.csv"],
    }


def answer_manufacturer_summary() -> dict:
    df = read_csv_if_exists(MANUFACTURER_YEAR_PATH)
    if df.empty or "event_count" not in df.columns:
        return {
            "answer_type": "manufacturer_summary",
            "status": "no_data",
            "summary": "Manufacturer summary data is not available yet.",
            "data": [],
            "sources": ["data/processed/manufacturer_year_summary.csv"],
        }

    year_col = "report_year" if "report_year" in df.columns else "event_year" if "event_year" in df.columns else None
    if not year_col:
        return {
            "answer_type": "manufacturer_summary",
            "status": "no_data",
            "summary": "A usable year field is not available yet.",
            "data": [],
            "sources": ["data/processed/manufacturer_year_summary.csv"],
        }

    latest_year = df[year_col].dropna().max()
    latest = df[df[year_col] == latest_year].sort_values("event_count", ascending=False).head(10)

    return {
        "answer_type": "manufacturer_summary",
        "status": "ok",
        "summary": f"Top manufacturers by event count in the latest available year ({latest_year}) are shown below.",
        "data": latest.to_dict(orient="records"),
        "sources": ["data/processed/manufacturer_year_summary.csv"],
    }