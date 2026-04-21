from pathlib import Path

from src.ingest.write_raw_manifest import build_manifest


def ensure_directories() -> None:
    required_dirs = [
        "data/raw",
        "data/interim",
        "data/processed",
        "reports",
    ]
    for directory in required_dirs:
        Path(directory).mkdir(parents=True, exist_ok=True)


def main() -> None:
    ensure_directories()
    build_manifest("data/raw", "reports/raw_manifest.csv")
    print("Week 3 setup complete.")


if __name__ == "__main__":
    main()