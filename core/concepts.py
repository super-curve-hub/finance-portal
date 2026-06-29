"""
SUPER CURVE TERMINAL
Concept Loader

Version : v3.0.0-alpha-builder2
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent

CONCEPT_DIR = ROOT / "data" / "concepts"


# --------------------------------------------------
# Paths
# --------------------------------------------------


def get_concept_directory() -> Path:
    """
    data/concepts ディレクトリを返す
    """

    return CONCEPT_DIR


# --------------------------------------------------
# Loader
# --------------------------------------------------


def load_concepts() -> list[dict[str, Any]]:
    """
    conceptsフォルダ内のJSONを読み込む
    """

    concepts: list[dict[str, Any]] = []

    if not CONCEPT_DIR.exists():

        raise FileNotFoundError(

            f"Concept directory not found: {CONCEPT_DIR}"

        )

    for file in sorted(CONCEPT_DIR.glob("*.json")):

        with open(file, encoding="utf-8") as f:

            concepts.append(

                json.load(f)

            )

    print(f"✓ Loaded {len(concepts)} concepts")

    return concepts


# --------------------------------------------------
# Utility
# --------------------------------------------------


def load_concept(concept_id: str) -> dict[str, Any]:
    """
    単一Conceptを取得
    """

    path = CONCEPT_DIR / f"{concept_id}.json"

    if not path.exists():

        raise FileNotFoundError(path)

    with open(path, encoding="utf-8") as f:

        return json.load(f)


def concept_exists(concept_id: str) -> bool:
    """
    Concept存在確認
    """

    return (CONCEPT_DIR / f"{concept_id}.json").exists()


def list_concept_ids() -> list[str]:
    """
    Concept ID一覧
    """

    return [

        p.stem

        for p in sorted(

            CONCEPT_DIR.glob("*.json")

        )

    ]


# --------------------------------------------------
# Validation
# --------------------------------------------------


def validate_concepts() -> bool:
    """
    全Conceptを最低限チェック
    """

    required = {

        "id",

        "title",

    }

    for concept in load_concepts():

        missing = required - set(concept.keys())

        if missing:

            raise ValueError(

                f"{concept.get('id','unknown')} missing {missing}"

            )

    return True