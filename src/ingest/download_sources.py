from __future__ import annotations

from pathlib import Path
from typing import Iterable
from urllib.request import urlretrieve
import csv
import json


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def download_file(url: str, output_path: Path) -> None:
    ensure_dir(output_path.parent)
    urlretrieve(url, output_path)


def read_download_plan(csv_path: str) -> list[dict]:
    rows: list[dict] = []
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def write_download_log(records: Iterable[dict], output_path: str) -> None:
    output_file = Path(output_path)
    ensure_dir(output_file.parent)
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(list(records), f, indent=2)


if __name__ == "__main__":
    print("Downloader scaffold ready. Add concrete source URLs in Week 4+ as needed.")