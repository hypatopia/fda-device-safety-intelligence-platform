from pathlib import Path
import csv


def write_empty_source_inventory(output_path: str) -> None:
    """
    Create an empty CSV template for FDA source tracking.
    """
    rows = [
        [
            "source_name",
            "source_type",
            "url",
            "update_frequency",
            "key_fields",
            "notes",
        ]
    ]

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


if __name__ == "__main__":
    write_empty_source_inventory("data/raw/source_inventory.csv")
    print("Created data/raw/source_inventory.csv")