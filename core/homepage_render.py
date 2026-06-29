"""
SUPER CURVE TERMINAL
Homepage Renderer

Version : v3.0.0-alpha-homepage
"""

from __future__ import annotations

from core.renderer import render_page

from core.templates import (
    load_layout,
    load_template,
)

from core.homepage_sections import (
    render_modules,
    render_latest_objects,
    render_roadmap,
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

    hero = homepage.get(
        "hero",
        {},
    )

    modules_html = render_modules(

        homepage.get(
            "modules",
            [],
        )

    )

    latest_html = render_latest_objects(

        search,

    )

    roadmap_html = render_roadmap(

        homepage.get(
            "roadmap",
            [],
        )

    )

    replacements = {

        "title": homepage.get(
            "title",
            "",
        ),

        "subtitle": homepage.get(
            "subtitle",
            "",
        ),

        "hero_headline": hero.get(
            "headline",
            "",
        ),

        "hero_description": hero.get(
            "description",
            "",
        ),

        "modules": modules_html,

        "latest": latest_html,

        "graph_count": str(
            len(graph)
        ),

        "roadmap": roadmap_html,

    }

    content = replace_tokens(

        template,

        replacements,

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