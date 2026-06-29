from typing import Any
from .utils import esc, render_list

BASE_PATH = "/finance-portal"
SITE_NAME = "SUPER CURVE TERMINAL"
SITE_SUBTITLE = "Institutional Market Intelligence"


def replace_tokens(template: str, mapping: dict[str, Any]) -> str:
    out = template
    for k, v in mapping.items():
        out = out.replace("{{" + k + "}}", str(v))
    return out


def render_page(layout: str, title: str, content: str, description: str = "") -> str:
    return replace_tokens(layout, {
        "title": esc(title),
        "description": esc(description),
        "site_name": SITE_NAME,
        "site_subtitle": SITE_SUBTITLE,
        "base": BASE_PATH,
        "content": content
    })


def render_tags(items: list[str] | None) -> str:
    if not items:
        return '<p class="muted">-</p>'
    return '<div class="tag-row">' + "".join(
        f'<span class="tag">{esc(x)}</span>' for x in items
    ) + "</div>"


def render_links(items: list[str] | None) -> str:
    if not items:
        return '<p class="muted">-</p>'
    return '<div class="tag-row">' + "".join(
        f'<a class="tag" href="{BASE_PATH}/handbook/{esc(x)}.html">{esc(x)}</a>'
        for x in items
    ) + "</div>"


def render_formula(formula: Any) -> str:
    if isinstance(formula, dict):
        ascii_formula = formula.get("ascii", "")
        latex_formula = formula.get("latex", "")
    else:
        ascii_formula = formula or ""
        latex_formula = ""

    return f'''
<pre class="terminal-code"><code>{esc(ascii_formula)}</code></pre>
<p class="muted">{esc(latex_formula)}</p>
'''


def render_dealer_action(action: Any) -> str:
    if isinstance(action, str):
        return f"<p>{esc(action)}</p>"
    if not isinstance(action, dict):
        return '<p class="muted">-</p>'

    return f'''
<div class="terminal-grid two-col">
  <article class="terminal-panel">
    <div class="panel-head"><span>Long Gamma</span><strong>Mean Reversion</strong></div>
    {render_list(action.get("long_gamma", []))}
  </article>
  <article class="terminal-panel">
    <div class="panel-head"><span>Short Gamma</span><strong>Trend Amplification</strong></div>
    {render_list(action.get("short_gamma", []))}
  </article>
</div>
'''


def render_report_examples(examples: list[dict[str, Any]] | None) -> str:
    if not examples:
        return '<p class="muted">-</p>'

    blocks = []
    for ex in examples:
        source = esc(ex.get("source", "Report"))
        english = esc(ex.get("english", ex.get("text", "")))
        japanese = esc(ex.get("japanese", ex.get("jp", "")))
        blocks.append(f'''
<article class="terminal-panel">
  <div class="panel-head"><span>{source}</span><strong>Example</strong></div>
  <p class="terminal-quote">"{english}"</p>
  <p>{japanese}</p>
</article>
''')
    return "\\n".join(blocks)


def render_handbook_content(template: str, concept: dict[str, Any]) -> str:
    impact = concept.get("market_impact", concept.get("bull_bear", {}))
    bull = impact.get("bull", "") if isinstance(impact, dict) else ""
    bear = impact.get("bear", "") if isinstance(impact, dict) else ""
    impact_desc = impact.get("description", "") if isinstance(impact, dict) else ""

    return replace_tokens(template, {
        "title": esc(concept.get("title", "")),
        "english": esc(concept.get("english", concept.get("title", ""))),
        "category": esc(concept.get("category_name", concept.get("category", ""))),
        "summary": esc(concept.get("summary", "")),
        "plain_jp": esc(concept.get("plain_jp", "")),
        "description": esc(concept.get("description", "")),
        "formula": render_formula(concept.get("formula", "")),
        "bull": esc(bull),
        "bear": esc(bear),
        "market_impact_description": esc(impact_desc),
        "dealer_action": render_dealer_action(concept.get("dealer_action")),
        "trader_watch": render_list(concept.get("trader_watch", [])),
        "related": render_links(concept.get("related", [])),
        "report_examples": render_report_examples(concept.get("report_examples", [])),
        "tags": render_tags(concept.get("tags", []))
    })
