"""Validate the released data without third-party Python packages."""
from pathlib import Path
import csv
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST_SHA256.json"


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def inspect_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = csv.reader(stream)
        columns = next(rows, [])
        count = sum(1 for _ in rows)
    return columns, count


def main():
    records = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for relative, expected in records.items():
        path = ROOT / relative
        assert path.is_file(), f"Missing file: {relative}"
        assert path.stat().st_size == expected["bytes"], f"Size mismatch: {relative}"
        assert sha256(path) == expected["sha256"], f"SHA-256 mismatch: {relative}"
        if path.suffix.lower() == ".csv":
            columns, rows = inspect_csv(path)
            assert columns == expected["columns"], f"Column mismatch: {relative}"
            assert rows == expected["rows"], f"Row-count mismatch: {relative}"

    archive = ROOT / "empirical_data/raw/kaggle_human_mobility_2021.zip"
    extracted = ROOT / "empirical_data/raw/kaggle_human_mobility_2021/IntegratedData.csv"
    with zipfile.ZipFile(archive) as bundle:
        assert bundle.testzip() is None, "Nested Kaggle archive CRC failure"
        assert bundle.namelist() == ["IntegratedData.csv"]
        nested_hash = hashlib.sha256(bundle.read("IntegratedData.csv")).hexdigest()
    assert nested_hash == sha256(extracted), "Kaggle ZIP payload differs from extracted CSV"
    print(f"DATA_VALIDATION_PASS {len(records)} files")


if __name__ == "__main__":
    main()

