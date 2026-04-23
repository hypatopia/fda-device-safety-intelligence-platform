from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.transform.load_raw_csvs import load_and_concat_csvs
from src.transform.common import (
    add_extract_metadata,
    normalize_columns,
)


RAW_DIR = "data/raw/reporting_guidance"
OUTPUT_PATH = "data/processed/reporting_workflow_dictionary_seed.csv"


def clean_reporting_guidance() -> pd.DataFrame:
    df = load_and_concat_csvs(RAW_DIR)
    if df.empty:
        return df

    df = normalize_columns(df)
    df = add_extract_metadata(df, "medwatch_forms_and_instructions")
    return df


def main() -> None:
    output_file = Path(OUTPUT_PATH)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    df = clean_reporting_guidance()
    if df.empty:
        print("No reporting guidance CSV files found.")
        return

    df.to_csv(output_file, index=False)
    print(f"Wrote {OUTPUT_PATH} with {len(df)} rows.")


if __name__ == "__main__":
    main()