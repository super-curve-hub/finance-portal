"""
Utility functions
SUPER CURVE TERMINAL v3.0.0-alpha
"""

from __future__ import annotations

import json
import html
from pathlib import Path
from typing import Any


def read_text(path: Path) -> str:
    """
    Read UTF-8 text file.
    """
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    """
    Write UTF-8 text file, creating parent directories if needed.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    """
    Load JSON object from file.
    """
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError(f"JSON root must be object: {path}")

    return data


def dump_json(path: Path, data: Any) -> None:
    """
    Write JSON with Japanese text preserved.
    """
    text = json.dumps(data, ensure_ascii=False, indent=2)
    write_text(path, text)


def esc(value: Any) -> str:
    """
    HTML escape.
    """
    if value is None:
        return ""

    return html.escape(str(value), quote=True)


def as_list(value: Any) -> list[Any]:
    """
    Normalize value to list.
    """
    if value is None:
        return []

    if isinstance(value, list):
        return value

    return [value]


def render_list(items: Any) -> str:
    """
    Render HTML unordered list.
    """
    rows = as_list(items)

    if not rows:
        return '<p class="muted">-</p>'

    return "<ul>" + "".join(
        f"<li>{esc(item)}</li>" for item in rows
    ) + "</ul>"


def ensure_dir(path: Path) -> None:
    """
    Ensure directory exists.
    """
    path.mkdir(parents=True, exist_ok=True)


def safe_get(data: dict[str, Any], key: str, default: Any = "") -> Any:
    """
    Safe dictionary getter.
    """
    value = data.get(key, default)

    if value is None:
        return default

    return value