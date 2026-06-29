"""
SUPER CURVE TERMINAL
Homepage Sections

Version : v3.0.0-alpha-homepage2
"""

from __future__ import annotations

from typing import Any


# --------------------------------------------------
# Latest Objects
# --------------------------------------------------


def render_latest_objects(
    objects: list[dict[str, Any]],
    limit: int = 6,
) -> str:

    if not objects:

        return "<p>No objects.</p>"

    cards = []

    for obj in objects[:limit]:

        cards.append(f"""
<a class="terminal-module"
href="{obj.get('url','#')}">

<strong>{obj.get('title','')}</strong>

<p>{obj.get('summary','')}</p>

</a>
""")

    return f"""
<div class="terminal-grid">

{''.join(cards)}

</div>
"""


# --------------------------------------------------
# Knowledge Graph Summary
# --------------------------------------------------


def render_graph_summary(
    graph: list[dict[str, Any]],
) -> str:

    if not graph:

        return "<p>No graph.</p>"

    categories = sorted({

        node.get("category", "")

        for node in graph

        if node.get("category")

    })

    html = f"""
<ul>

<li><strong>Nodes</strong> : {len(graph)}</li>

<li><strong>Categories</strong> : {len(categories)}</li>

</ul>
"""

    return html


# --------------------------------------------------
# Roadmap
# --------------------------------------------------

def render_roadmap(
    roadmap: list[str],
) -> str:

    if not roadmap:

        return "<p>No roadmap.</p>"

    rows = []

    for i, item in enumerate(roadmap, start=1):

        rows.append(f"""
<div class="terminal-module">

<strong>Phase {i}</strong>

<p>{item}</p>

</div>
""")

    return f"""
<div class="terminal-grid">

{''.join(rows)}

</div>
"""


# --------------------------------------------------
# Market Panel
# --------------------------------------------------


def render_market_panel(
    panel: list[dict[str, Any]] | None,
) -> str:

    if not panel:

        return """
<div class="terminal-panel">

<h3>Market Panel</h3>

<p>Coming Soon</p>

</div>
"""

    rows = []

    for item in panel:

        rows.append(f"""
<div class="market-row">

<strong>{item.get("title","")}</strong>

<span>{item.get("value","")}</span>

</div>
""")

    return f"""
<div class="terminal-panel">

<h3>Market Panel</h3>

{''.join(rows)}

</div>
"""
# --------------------------------------------------
# Modules
# --------------------------------------------------

def render_modules(modules):

    if not modules:
        return "<p>No modules.</p>"

    cards = []

    for module in modules:

        cards.append(f"""
<a class="terminal-module"
href="{module.get('url', '#')}">

<strong>{module.get('title', '')}</strong>

<p>{module.get('description', '')}</p>

</a>
""")

    return "\n".join(cards)