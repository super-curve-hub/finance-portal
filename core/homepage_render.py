"""
SUPER CURVE TERMINAL
Homepage Renderer

Version : v3.0.0-alpha-homepage2
"""

from __future__ import annotations

from core.renderer import render_page
from core.templates import (
    load_layout,
    load_template,
)

from core.homepage_sections import (
    render_latest_objects,
    render_graph_summary,
    render_roadmap,
    render_market_panel,
)


# --------------------------------------------------
# Replace Tokens
# --------------------------------------------------


def replace_tokens(
    template: str,
    mapping: dict[str, str],
) -> str:

    html = template

    for key, value in mapping.items():

        html = html.replace(

            "{{" + key + "}}",

            value,

        )

    return html


# --------------------------------------------------
# Homepage Renderer
# --------------------------------------------------


def render_homepage(
    homepage: dict,
    search: list,
    graph: list,
) -> str:

    layout = load_layout()

    template = load_template(

        "homepage.html"

    )

    latest_html = render_latest_objects(

        search,

    )

    graph_html = render_graph_summary(

        graph,

    )

    roadmap_html = render_roadmap(

        homepage.get(

            "roadmap",

            [],

        )

    )

    market_html = render_market_panel(

        homepage.get(

            "market_panel",

            [],

        )

    )

    content = replace_tokens(

        template,

        {

            "latest_objects": latest_html,

            "graph_summary": graph_html,

            "roadmap": roadmap_html,

            "market_panel": market_html,

        },

    )

    page = render_page(

        layout,

        homepage.get(

            "title",

            "SUPER CURVE TERMINAL",

        ),

        content,

        homepage.get(

            "subtitle",

            "",

        ),

    )

    return page