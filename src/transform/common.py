from __future__ import annotations

import re
from datetime import date
from typing import Iterable

import pandas as pd


def normalize_column_name(name: str) -> str:
    value = str(name).strip().lower()
    value = re.sub(r"[^\w\s]+", "_", value)
    value = re.sub(r"\s+", "_", value)
    value = re.sub(r"_+", "_", value)
    return value.strip("_")


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [normalize_column_name(col) for col in df.columns]
    return df


def add_extract_metadata(df: pd.DataFrame, source_name: str) -> pd.DataFrame:
    df = df.copy()
    df["source_name"] = source_name
    df["extract_date"] = date.today().isoformat()
    return df


def keep_existing_columns(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
    existing = [c for c in columns if c in df.columns]
    return df.loc[:, existing].copy()


def safe_to_datetime(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    df = df.copy()
    if column_name in df.columns:
        df[column_name] = pd.to_datetime(df[column_name], errors="coerce")
    return df


def safe_to_numeric(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    df = df.copy()
    if column_name in df.columns:
        df[column_name] = pd.to_numeric(df[column_name], errors="coerce")
    return df