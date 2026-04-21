from __future__ import annotations

from pathlib import Path
import csv


def build_manifest(raw_dir: str, output_csv: str) -> None:
    raw_path = Path(raw_dir)
    output_path = Path(output_csv)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    for file_path in sorted(raw_path.rglob("*")):
        if file_path.is_file():
            rows.append(
                {
                    "file_name": file_path.name,
                    "relative_path": str(file_path.relative_to(raw_path)),
                    "suffix": file_path.suffix.lower(),
                    "size_bytes": file_path.stat().st_size,
                }
            )

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["file_name", "relative_path", "suffix", "size_bytes"],
        )
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    build_manifest("data/raw", "reports/raw_manifest.csv")
    print("Wrote reports/raw_manifest.csv")