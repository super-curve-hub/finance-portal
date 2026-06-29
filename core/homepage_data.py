"""
SUPER CURVE TERMINAL
Homepage Data Loader

Version : v3.0.0-alpha-homepage2
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data"
API_DIR = ROOT / "api"


# --------------------------------------------------
# Internal
# --------------------------------------------------


def _load_json(path: Path) -> dict[str, Any]:

    if not path.exists():

        return {}

    with open(path, encoding="utf-8") as f:

        return json.load(f)


# --------------------------------------------------
# Homepage
# --------------------------------------------------


def load_homepage() -> dict[str, Any]:

    return _load_json(

        DATA_DIR / "homepage.json"

    )


# --------------------------------------------------
# Search
# --------------------------------------------------


def load_search() -> list[dict[str, Any]]:

    data = _load_json(

        API_DIR / "search.json"

    )

    return data.get(

        "objects",

        [],

    )


# --------------------------------------------------
# Graph
# --------------------------------------------------


def load_graph() -> list[dict[str, Any]]:

    data = _load_json(

        API_DIR / "graph.json"

    )

    return data.get(

        "graph",

        [],

    )


# --------------------------------------------------
# Validation
# --------------------------------------------------


def validate_homepage_data() -> bool:

    load_homepage()

    load_search()

    load_graph()

    return True