"""
SUPER CURVE TERMINAL
Builder Engine

Version : v3.0.0-alpha-builder
"""

from __future__ import annotations

import json
from pathlib import Path

from core.renderer import (
    render_page,
    render_handbook_content,
)

from core.templates import (
    load_layout,
    load_handbook_template,
)

from core.search import generate_search
from core.graph import generate_graph


ROOT = Path(__file__).resolve().parent.parent

CONCEPT_DIR = ROOT / "data" / "concepts"

HANDBOOK_DIR = ROOT / "handbook"

API_DIR = ROOT / "api"


class Builder:

    def __init__(self):

        self.layout = load_layout()

        self.handbook_template = load_handbook_template()

        HANDBOOK_DIR.mkdir(exist_ok=True)

        API_DIR.mkdir(exist_ok=True)

    # --------------------------------------------------
    # Load Concepts
    # --------------------------------------------------

    def load_concepts(self):

        concepts = []

        for file in sorted(CONCEPT_DIR.glob("*.json")):

            with open(file, encoding="utf-8") as f:

                obj = json.load(f)

            concepts.append(obj)

        print(f"✓ Loaded {len(concepts)} concepts")

        return concepts

    # --------------------------------------------------
    # Handbook Generator
    # --------------------------------------------------

    def build_handbook(self, concepts):

        for concept in concepts:

            html = render_handbook_content(

                self.handbook_template,

                concept,

            )

            page = render_page(

                self.layout,

                concept["title"],

                html,

                concept.get("summary", ""),

            )

            outfile = HANDBOOK_DIR / f'{concept["id"]}.html'

            outfile.write_text(

                page,

                encoding="utf-8",

            )

            print(f"✓ handbook/{outfile.name}")

    # --------------------------------------------------
    # Search Generator
    # --------------------------------------------------

    def build_search(self, concepts):

        return generate_search(

            API_DIR,

            concepts,

        )

    # --------------------------------------------------
    # Knowledge Graph
    # --------------------------------------------------

    def build_graph(self, concepts):

        return generate_graph(

            API_DIR,

            concepts,

        )

    # --------------------------------------------------
    # Handbook Index
    # --------------------------------------------------

    def build_handbook_index(self, concepts):

        cards = []

        for c in concepts:

            cards.append(

                f"""
<a class="terminal-module"
href="/finance-portal/handbook/{c['id']}.html">

<strong>{c['title']}</strong>

<p>{c.get("summary","")}</p>

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

            self.layout,

            "Option Handbook",

            html,

            "Option Knowledge Base",

        )

        (HANDBOOK_DIR / "index.html").write_text(

            page,

            encoding="utf-8",

        )

        print("✓ handbook/index.html")

    # --------------------------------------------------
    # Build
    # --------------------------------------------------

    def build(self):

        print()

        print("Loading Concepts...")

        concepts = self.load_concepts()

        print()

        print("Generating Handbook...")

        self.build_handbook(concepts)

        print()

        print("Generating Search...")

        objects = self.build_search(concepts)

        print(f"✓ Search Objects : {len(objects)}")

        print()

        print("Generating Knowledge Graph...")

        graph = self.build_graph(concepts)

        print(f"✓ Graph Nodes : {len(graph)}")

        print()

        print("Generating Handbook Index...")

        self.build_handbook_index(concepts)

        print()

        print("Done.")

        return objects


def build_site():

    Builder().build()