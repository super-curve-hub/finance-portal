"""
JSON validator
SUPER CURVE TERMINAL v3.0.0-alpha
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


REQUIRED_CONCEPT_FIELDS = [
    "id",
    "title",
    "summary",
    "plain_jp",
    "description",
]


def validate_required_fields(
    data: dict[str, Any],
    path: Path,
    required: list[str],
) -> None:
    """
    Validate required fields.
    """
    missing = []

    for key in required:
        value = data.get(key)

        if value is None or value == "":
            missing.append(key)

    if missing:
        raise ValueError(
            f"{path}: missing required fields: {missing}"
        )


def validate_concept(data: dict[str, Any], path: Path) -> None:
    """
    Validate concept JSON.
    """
    validate_required_fields(
        data=data,
        path=path,
        required=REQUIRED_CONCEPT_FIELDS,
    )

    if data.get("type") not in (None, "concept"):
        raise ValueError(
            f"{path}: type must be 'concept'"
        )

    concept_id = data.get("id", "")

    if "/" in concept_id or " " in concept_id:
        raise ValueError(
            f"{path}: id must be URL-safe slug"
        )


def validate_dashboard(data: dict[str, Any], path: Path) -> None:
    """
    Validate dashboard JSON.
    """
    required = [
        "id",
        "title",
        "summary",
    ]

    validate_required_fields(
        data=data,
        path=path,
        required=required,
    )

    if data.get("type") not in (None, "dashboard"):
        raise ValueError(
            f"{path}: type must be 'dashboard'"
        )