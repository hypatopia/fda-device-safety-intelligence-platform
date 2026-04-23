from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.transform.load_raw_csvs import load_and_concat_csvs
from src.transform.common import (
    add_extract_metadata,
    normalize_columns,
    safe_to_numeric,
)


RAW_DIR = "data/raw/device_problems"
OUTPUT_PATH = "data/processed/device_problems_clean.csv"


def clean_device_problems() -> pd.DataFrame:
    df = load_and_concat_csvs(RAW_DIR)
    if df.empty:
        return df

    df = normalize_columns(df)
    df = add_extract_metadata(df, "mdr_data_files")

    for col in ["report_year"]:
        df = safe_to_numeric(df, col)

    return df


def main() -> None:
    output_file = Path(OUTPUT_PATH)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    df = clean_device_problems()
    if df.empty:
        print("No device problem CSV files found.")
        return

    df.to_csv(output_file, index=False)
    print(f"Wrote {OUTPUT_PATH} with {len(df)} rows.")


if __name__ == "__main__":
    main()