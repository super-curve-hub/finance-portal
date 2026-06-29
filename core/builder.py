"""
SUPER CURVE TERMINAL
Builder Engine v3.0.0-alpha
"""

from pathlib import Path
import json

from core.renderer import render_page, render_handbook_content
from core.templates import load_layout, load_handbook_template


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
    # JSON読込
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
    # Handbook生成
    # --------------------------------------------------

    def build_handbook(self, concepts):

        objects = []

        for concept in concepts:

            html = render_handbook_content(
                self.handbook_template,
                concept
            )

            page = render_page(
                self.layout,
                concept["title"],
                html,
                concept.get("summary", "")
            )

            outfile = HANDBOOK_DIR / f'{concept["id"]}.html'

            outfile.write_text(page, encoding="utf-8")

            print(f"✓ handbook/{outfile.name}")

            objects.append({

                "id": concept["id"],
                "title": concept["title"],
                "summary": concept.get("summary", ""),
                "category": concept.get("category", ""),
                "tags": concept.get("tags", []),
                "type": "concept",
                "url": f"/finance-portal/handbook/{concept['id']}.html"

            })

        return objects

    # --------------------------------------------------
    # Search生成
    # --------------------------------------------------

    def build_search(self, objects):

        outfile = API_DIR / "search.json"

        outfile.write_text(

            json.dumps(
                {
                    "objects": objects
                },
                ensure_ascii=False,
                indent=2
            ),

            encoding="utf-8"

        )

        print("✓ api/search.json")

    # --------------------------------------------------
    # Handbook Index
    # --------------------------------------------------

    def build_handbook_index(self, concepts):

        cards = []

        for c in concepts:

            cards.append(f"""
<a class="terminal-module"
href="/finance-portal/handbook/{c['id']}.html">

<strong>{c['title']}</strong>

<p>{c.get("summary","")}</p>

</a>
""")

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

            "Option Knowledge Base"

        )

        (HANDBOOK_DIR / "index.html").write_text(

            page,

            encoding="utf-8"

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

        objects = self.build_handbook(concepts)

        print()

        print("Generating Search...")

        self.build_search(objects)

        print()

        print("Generating Handbook Index...")

        self.build_handbook_index(concepts)

        print()

        print("Done.")


def build_site():

    Builder().build()