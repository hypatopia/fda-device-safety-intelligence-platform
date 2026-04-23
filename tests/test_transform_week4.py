import pandas as pd

from src.transform.common import normalize_columns, normalize_column_name


def test_normalize_column_name():
    assert normalize_column_name("Report Year") == "report_year"
    assert normalize_column_name("Device Problem") == "device_problem"


def test_normalize_columns():
    df = pd.DataFrame(columns=["Report Year", "Manufacturer Name", "Device Problem"])
    out = normalize_columns(df)
    assert list(out.columns) == ["report_year", "manufacturer_name", "device_problem"]