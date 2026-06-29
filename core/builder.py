"""
SUPER CURVE TERMINAL
Builder Engine

Version : v3.0.0-alpha-builder2
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from core.concepts import load_concepts
from core.handbook import generate_handbook
from core.search import generate_search
from core.graph import generate_graph
from core.homepage import build_homepage


ROOT = Path(__file__).resolve().parent.parent
API_DIR = ROOT / "api"


class Builder:
    """
    Build orchestrator.
    """

    def build(self) -> list[dict[str, Any]]:
        print()
        print("Loading Concepts...")
        concepts = load_concepts()

        print()
        print("Generating Handbook...")
        generate_handbook(concepts)

        print()
        print("Generating Search...")
        objects = generate_search(
            API_DIR,
            concepts,
        )
        print(f"✓ Search Objects : {len(objects)}")

        print()
        print("Generating Knowledge Graph...")
        graph = generate_graph(
            API_DIR,
            concepts,
        )
        print(f"✓ Graph Nodes : {len(graph)}")

        build_homepage()

        print()
        print("Done.")

        return objects


def build_site() -> list[dict[str, Any]]:
    return Builder().build()


def main() -> int:
    build_site()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())