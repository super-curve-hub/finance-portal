"""
SUPER CURVE TERMINAL
Handbook Generator

Version : v3.0.0-alpha-builder2
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from core.renderer import (
    render_page,
    render_handbook_content,
)

from core.templates import (
    load_layout,
    load_handbook_template,
)

ROOT = Path(__file__).resolve().parent.parent

HANDBOOK_DIR = ROOT / "handbook"


# --------------------------------------------------
# Initialize
# --------------------------------------------------


def initialize() -> tuple[str, str]:

    HANDBOOK_DIR.mkdir(exist_ok=True)

    layout = load_layout()

    handbook_template = load_handbook_template()

    return layout, handbook_template


# --------------------------------------------------
# Handbook Generator
# --------------------------------------------------


def build_handbook(
    concepts: list[dict[str, Any]],
) -> None:

    layout, handbook_template = initialize()

    for concept in concepts:

        html = render_handbook_content(

            handbook_template,

            concept,

        )

        page = render_page(

            layout,

            concept["title"],

            html,

            concept.get(

                "summary",

                "",

            ),

        )

        outfile = HANDBOOK_DIR / f"{concept['id']}.html"

        outfile.write_text(

            page,

            encoding="utf-8",

        )

        print(

            f"✓ handbook/{outfile.name}"

        )


# --------------------------------------------------
# Handbook Index
# --------------------------------------------------


def build_handbook_index(
    concepts: list[dict[str, Any]],
) -> Path:

    layout, _ = initialize()

    cards = []

    for concept in concepts:

        cards.append(

            f"""
<a class="terminal-module"
href="/finance-portal/handbook/{concept['id']}.html">

<strong>{concept['title']}</strong>

<p>{concept.get("summary","")}</p>

</a>
"""

        )

    html = f"""
<h1>Option Handbook</h1>

<div class="terminal-grid">

{''.join(cards)}

</div>
"""

    page = render_page(

        layout,

        "Option Handbook",

        html,

        "Option Knowledge Base",

    )

    outfile = HANDBOOK_DIR / "index.html"

    outfile.write_text(

        page,

        encoding="utf-8",

    )

    print(

        "✓ handbook/index.html"

    )

    return outfile


# --------------------------------------------------
# Public API
# --------------------------------------------------


def generate_handbook(
    concepts: list[dict[str, Any]],
) -> None:

    build_handbook(concepts)

    build_handbook_index(concepts)