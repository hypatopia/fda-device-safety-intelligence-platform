from pathlib import Path
import csv


SOURCE_HEADER = [
    "source_name",
    "source_group",
    "source_type",
    "url_or_page_name",
    "domain_scope",
    "time_scope",
    "update_frequency",
    "key_fields",
    "planned_use",
    "priority",
    "notes",
]


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def write_csv_template(path: str, header: list[str]) -> None:
    output_path = Path(path)
    ensure_parent(output_path)

    if output_path.exists():
        print(f"Skipped existing file: {output_path}")
        return

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)

    print(f"Created template: {output_path}")


def main() -> None:
    write_csv_template("data/raw/source_inventory_template.csv", SOURCE_HEADER)


if __name__ == "__main__":
    main()