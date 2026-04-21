from pathlib import Path
import zipfile

from src.ingest.extract_archives import extract_zip_file
from src.ingest.normalize_names import normalize_name
from src.ingest.write_raw_manifest import build_manifest


def test_normalize_name():
    assert normalize_name("Device Problem") == "device_problem"
    assert normalize_name("Event/Type") == "event_type"
    assert normalize_name("  Report Year  ") == "report_year"


def test_extract_zip_file(tmp_path: Path):
    zip_path = tmp_path / "sample.zip"
    output_dir = tmp_path / "out"

    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.writestr("example.txt", "hello")

    extracted = extract_zip_file(str(zip_path), str(output_dir))

    assert len(extracted) == 1
    assert (output_dir / "example.txt").exists()


def test_build_manifest(tmp_path: Path):
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    (raw_dir / "file1.txt").write_text("abc", encoding="utf-8")

    output_csv = tmp_path / "manifest.csv"
    build_manifest(str(raw_dir), str(output_csv))

    assert output_csv.exists()
    content = output_csv.read_text(encoding="utf-8")
    assert "file1.txt" in content