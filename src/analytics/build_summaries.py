from __future__ import annotations

from pathlib import Path

import pandas as pd


EVENTS_PATH = "data/processed/device_events_clean.csv"
PROBLEMS_PATH = "data/processed/device_problems_clean.csv"

MANUFACTURER_YEAR_OUTPUT = "data/processed/manufacturer_year_summary.csv"
DEVICE_PROBLEM_YEAR_OUTPUT = "data/processed/device_problem_year_summary.csv"


def read_csv_if_exists(path: str) -> pd.DataFrame:
    file_path = Path(path)
    if not file_path.exists():
        return pd.DataFrame()
    return pd.read_csv(file_path, low_memory=False)


def build_manufacturer_year_summary() -> pd.DataFrame:
    events = read_csv_if_exists(EVENTS_PATH)
    if events.empty:
        return pd.DataFrame()

    manufacturer_col = None
    for candidate in ["manufacturer_name", "manufacturer", "mfr_name"]:
        if candidate in events.columns:
            manufacturer_col = candidate
            break

    year_col = None
    for candidate in ["report_year", "event_year"]:
        if candidate in events.columns:
            year_col = candidate
            break

    if not manufacturer_col or not year_col:
        return pd.DataFrame()

    summary = (
        events.groupby([manufacturer_col, year_col], dropna=False)
        .size()
        .reset_index(name="event_count")
    )

    return summary


def build_device_problem_year_summary() -> pd.DataFrame:
    problems = read_csv_if_exists(PROBLEMS_PATH)
    if problems.empty:
        return pd.DataFrame()

    problem_col = None
    for candidate in ["device_problem", "device_problem_code", "problem_code"]:
        if candidate in problems.columns:
            problem_col = candidate
            break

    year_col = None
    for candidate in ["report_year", "event_year"]:
        if candidate in problems.columns:
            year_col = candidate
            break

    if not problem_col or not year_col:
        return pd.DataFrame()

    summary = (
        problems.groupby([problem_col, year_col], dropna=False)
        .size()
        .reset_index(name="event_count")
    )

    return summary


def main() -> None:
    manufacturer_year = build_manufacturer_year_summary()
    problem_year = build_device_problem_year_summary()

    Path("data/processed").mkdir(parents=True, exist_ok=True)

    if not manufacturer_year.empty:
        manufacturer_year.to_csv(MANUFACTURER_YEAR_OUTPUT, index=False)
        print(f"Wrote {MANUFACTURER_YEAR_OUTPUT} with {len(manufacturer_year)} rows.")
    else:
        print("Manufacturer-year summary not created.")

    if not problem_year.empty:
        problem_year.to_csv(DEVICE_PROBLEM_YEAR_OUTPUT, index=False)
        print(f"Wrote {DEVICE_PROBLEM_YEAR_OUTPUT} with {len(problem_year)} rows.")
    else:
        print("Device-problem-year summary not created.")


if __name__ == "__main__":
    main()