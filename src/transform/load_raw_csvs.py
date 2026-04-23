from __future__ import annotations

from pathlib import Path
from typing import List

import pandas as pd


def list_csv_files(directory: str) -> List[Path]:
    folder = Path(directory)
    if not folder.exists():
        return []
    return sorted([p for p in folder.glob("*.csv") if p.is_file()])


def load_and_concat_csvs(directory: str) -> pd.DataFrame:
    files = list_csv_files(directory)
    if not files:
        return pd.DataFrame()

    frames = []
    for file_path in files:
        df = pd.read_csv(file_path, low_memory=False)
        df["source_file_name"] = file_path.name
        frames.append(df)

    return pd.concat(frames, ignore_index=True)