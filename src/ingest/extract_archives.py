from __future__ import annotations

from pathlib import Path
import zipfile


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def extract_zip_file(zip_path: str, output_dir: str) -> list[str]:
    zip_file = Path(zip_path)
    destination = Path(output_dir)
    ensure_dir(destination)

    extracted_files: list[str] = []

    with zipfile.ZipFile(zip_file, "r") as zf:
        zf.extractall(destination)
        extracted_files = [str(destination / member) for member in zf.namelist()]

    return extracted_files


if __name__ == "__main__":
    print("Archive extractor ready.")