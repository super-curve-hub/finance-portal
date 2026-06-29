"""
SUPER CURVE TERMINAL
Homepage Generator

Version : v3.0.0-alpha-homepage2
"""

from __future__ import annotations

from pathlib import Path

from core.homepage_data import (
    load_homepage,
    load_search,
    load_graph,
)

from core.homepage_render import (
    render_homepage,
)

ROOT = Path(__file__).resolve().parent.parent

OUTPUT_FILE = ROOT / "index.html"


# --------------------------------------------------
# Homepage Generator
# --------------------------------------------------


def generate_homepage() -> Path:
    """
    Generate index.html.
    """

    homepage = load_homepage()

    search = load_search()

    graph = load_graph()

    html = render_homepage(

        homepage,

        search,

        graph,

    )

    OUTPUT_FILE.write_text(

        html,

        encoding="utf-8",

    )

    print("✓ index.html")

    return OUTPUT_FILE


# --------------------------------------------------
# Public API
# --------------------------------------------------


def build_homepage() -> Path:
    """
    Builder entry point.
    """

    print()

    print("Generating Homepage...")

    return generate_homepage()


# --------------------------------------------------
# CLI
# --------------------------------------------------


def main() -> int:

    try:

        build_homepage()

        print()

        print("Homepage generation complete.")

        return 0

    except Exception as exc:

        print()

        print("Homepage generation failed.")

        print(exc)

        return 1


# --------------------------------------------------
# Main
# --------------------------------------------------


if __name__ == "__main__":

    raise SystemExit(main())