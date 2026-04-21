from pathlib import Path
from src.ingest.build_week2_templates import write_csv_template


def test_write_csv_template(tmp_path: Path):
    output_file = tmp_path / "template.csv"
    header = ["a", "b", "c"]

    write_csv_template(str(output_file), header)

    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8").strip()
    assert content == "a,b,c"