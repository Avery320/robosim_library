#!/usr/bin/env python3
"""Generate library/index.json from per-model model.json files."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LIBRARY_ROOT = REPO_ROOT / "library"
INDEX_PATH = LIBRARY_ROOT / "index.json"
REQUIRED_FIELDS = ("id", "label", "vendor", "model", "urdf", "author")
FIELD_ORDER = ("id", "label", "vendor", "model", "urdf", "author", "source")


def load_model(path: Path) -> dict:
    data = json.loads(path.read_text())

    missing = [field for field in REQUIRED_FIELDS if not data.get(field)]
    if missing:
        raise ValueError(f"{path}: missing required fields: {', '.join(missing)}")

    urdf_path = REPO_ROOT / data["urdf"]
    if not urdf_path.exists():
        raise ValueError(f"{path}: urdf not found: {data['urdf']}")

    normalized = {}
    for field in FIELD_ORDER:
        if field in data:
            normalized[field] = data[field]

    for field, value in data.items():
        if field not in normalized:
            normalized[field] = value

    return normalized


def main() -> int:
    models = []
    for model_path in sorted(LIBRARY_ROOT.glob("*/*/model.json")):
        models.append(load_model(model_path))

    models.sort(key=lambda item: (item["vendor"].lower(), item["model"].lower(), item["id"].lower()))
    INDEX_PATH.write_text(json.dumps(models, indent=2, ensure_ascii=True) + "\n")
    print(f"Generated {INDEX_PATH} with {len(models)} entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
