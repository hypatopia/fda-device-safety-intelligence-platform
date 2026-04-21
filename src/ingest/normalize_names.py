import re


def normalize_name(name: str) -> str:
    value = name.strip().lower()
    value = re.sub(r"[^\w\s]+", "_", value)
    value = re.sub(r"\s+", "_", value)
    value = re.sub(r"_+", "_", value)
    return value.strip("_")