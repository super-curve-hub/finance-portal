from pathlib import Path
import json
import html
from datetime import date

ROOT = Path(__file__).resolve().parents[1]

DATA_CONCEPTS = ROOT / "data" / "concepts"
TEMPLATES = ROOT / "templates"

HANDBOOK_DIR = ROOT / "handbook"
API_DIR = ROOT / "api"

LAYOUT_TEMPLATE = TEMPLATES / "layout.html"
HANDBOOK_TEMPLATE = TEMPLATES / "handbook.html"

SITE_URL = "https://super-curve-hub.github.io/finance-portal"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def esc(value) -> str:
    if value is None:
        return ""
    return html.escape(str(value))


def render_list(items) -> str:
    if not items:
        return "<p>-</p>"
    return "<ul>" + "".join(f"<li>{esc(x)}</li>" for x in items) + "</ul>"


def render_related(items) -> str:
    if not items:
        return "<p>-</p>"
    links = []
    for item in items:
        links.append(f'<a class="tag" href="/handbook/{esc(item)}.html">{esc(item)}</a>')
    return '<div class="tag-row">' + "".join(links) + "</div>"


def render_dealer_action(action) -> str:
    if not isinstance(action, dict):
        return f"<p>{esc(action)}</p>"

    long_gamma = render_list(action.get("long_gamma", []))
    short_gamma = render_list(action.get("short_gamma", []))

    return f"""
    <div class="grid two">
      <section class="card">
        <h3>Long Gamma</h3>
        {long_gamma}
      </section>
      <section class="card">
        <h3>Short Gamma</h3>
        {short_gamma}
      </section>
    </div>
    """


def render_report_examples(examples) -> str:
    if not examples:
        return "<p>-</p>"

    html_blocks = []
    for ex in examples:
        source = esc(ex.get("source", "Report"))
        english = esc(ex.get("english", ex.get("text", "")))
        japanese = esc(ex.get("japanese", ex.get("jp", "")))

        html_blocks.append(f"""
        <section class="card">
          <h3>{source}</h3>
          <p class="quote">"{english}"</p>
          <p>{japanese}</p>
        </section>
        """)

    return "\n".join(html_blocks)


def replace_many(template: str, mapping: dict) -> str:
    out = template
    for key, value in mapping.items():
        out = out.replace("{{" + key + "}}", str(value))
    return out


def validate_concept(data: dict, path: Path) -> None:
    required = ["id", "title", "summary", "plain_jp", "description"]
    missing = [k for k in required if not data.get(k)]
    if missing:
        raise ValueError(f"{path} missing required fields: {missing}")


def load_concepts() -> list[dict]:
    concepts = []

    for path in sorted(DATA_CONCEPTS.glob("*.json")):
        data = load_json(path)
        validate_concept(data, path)
        data["_source_path"] = str(path.relative_to(ROOT))
        concepts.append(data)

    return concepts


def render_concept_page(concept: dict, layout: str, page_tpl: str) -> str:
    formula = concept.get("formula", {})
    if isinstance(formula, dict):
        formula_ascii = formula.get("ascii", "")
    else:
        formula_ascii = formula

    market_impact = concept.get("market_impact", concept.get("bull_bear", {}))
    if isinstance(market_impact, dict):
        bull = market_impact.get("bull", "")
        bear = market_impact.get("bear", "")
        impact_desc = market_impact.get("description", "")
    else:
        bull = ""
        bear = ""
        impact_desc = esc(market_impact)

    content = replace_many(page_tpl, {
        "title": esc(concept.get("title", "")),
        "english": esc(concept.get("english", concept.get("title", ""))),
        "summary": esc(concept.get("summary", "")),
        "plain_jp": esc(concept.get("plain_jp", "")),
        "description": esc(concept.get("description", "")),
        "formula_ascii": esc(formula_ascii),
        "market_impact_description": esc(impact_desc),
        "bull": esc(bull),
        "bear": esc(bear),
        "dealer_action": render_dealer_action(concept.get("dealer_action", "")),
        "trader_watch": render_list(concept.get("trader_watch", [])),
        "related": render_related(concept.get("related", [])),
        "report_examples": render_report_examples(concept.get("report_examples", [])),
    })

    return replace_many(layout, {
        "title": esc(concept.get("title", "")) + " | SUPER CURVE TERMINAL",
        "content": content
    })


def build_handbook_index(concepts: list[dict], layout: str) -> None:
    cards = []

    for c in concepts:
        cid = esc(c["id"])
        title = esc(c["title"])
        summary = esc(c.get("summary", ""))
        category = esc(c.get("category_name", c.get("category", "")))

        cards.append(f"""
        <a class="card link-card" href="/handbook/{cid}.html">
          <div class="muted">{category}</div>
          <h2>{title}</h2>
          <p>{summary}</p>
        </a>
        """)

    content = f"""
    <section class="hero">
      <p class="eyebrow">OPTION & VOLATILITY HANDBOOK</p>
      <h1>Option Handbook</h1>
      <p>オプション・ボラティリティ・ディーラーフローの実務辞典。</p>
    </section>

    <section class="grid cards">
      {''.join(cards)}
    </section>
    """

    html_out = replace_many(layout, {
        "title": "Option Handbook | SUPER CURVE TERMINAL",
        "content": content
    })

    write_text(HANDBOOK_DIR / "index.html", html_out)


def build_search_index(concepts: list[dict]) -> None:
    rows = []

    for c in concepts:
        rows.append({
            "id": c.get("id"),
            "type": c.get("type", "concept"),
            "title": c.get("title"),
            "category": c.get("category"),
            "summary": c.get("summary"),
            "plain_jp": c.get("plain_jp"),
            "tags": c.get("tags", []),
            "url": f"/handbook/{c.get('id')}.html",
            "source_path": c.get("_source_path")
        })

    write_text(API_DIR / "search.json", json.dumps(rows, ensure_ascii=False, indent=2))


def build_sitemap(concepts: list[dict]) -> None:
    urls = [
        f"{SITE_URL}/",
        f"{SITE_URL}/handbook/",
        f"{SITE_URL}/search/",
    ]

    for c in concepts:
        urls.append(f"{SITE_URL}/handbook/{c.get('id')}.html")

    today = date.today().isoformat()

    body = "\n".join(
        f"""  <url>
    <loc>{html.escape(u)}</loc>
    <lastmod>{today}</lastmod>
  </url>"""
        for u in urls
    )

    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
"""
    write_text(ROOT / "sitemap.xml", sitemap)


def main() -> None:
    print("=" * 48)
    print("SUPER CURVE TERMINAL BUILD")
    print("=" * 48)

    layout = read_text(LAYOUT_TEMPLATE)
    page_tpl = read_text(HANDBOOK_TEMPLATE)

    concepts = load_concepts()
    print(f"Loaded concepts: {len(concepts)}")

    HANDBOOK_DIR.mkdir(parents=True, exist_ok=True)

    for concept in concepts:
        html_out = render_concept_page(concept, layout, page_tpl)
        out_path = HANDBOOK_DIR / f"{concept['id']}.html"
        write_text(out_path, html_out)
        print(f"Generated: {out_path.relative_to(ROOT)}")

    build_handbook_index(concepts, layout)
    print("Generated: handbook/index.html")

    build_search_index(concepts)
    print("Generated: api/search.json")

    build_sitemap(concepts)
    print("Generated: sitemap.xml")

    print("Build completed.")


if __name__ == "__main__":
    main()