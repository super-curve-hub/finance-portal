"""
SUPER CURVE TERMINAL
Template Loader

Version : v3.0.0-alpha-homepage
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TEMPLATE_DIR = ROOT / "templates"


# --------------------------------------------------
# Internal
# --------------------------------------------------


def _read_template(filename: str) -> str:
    """
    Read template file.
    """

    path = TEMPLATE_DIR / filename

    if not path.exists():

        raise FileNotFoundError(

            f"Template not found: {path}"

        )

    return path.read_text(

        encoding="utf-8"

    )


# --------------------------------------------------
# Generic Loader
# --------------------------------------------------


def load_template(filename: str) -> str:
    """
    Generic template loader.

    Example
    -------
    load_template("homepage.html")
    load_template("layout.html")
    """

    return _read_template(filename)


# --------------------------------------------------
# Layout
# --------------------------------------------------


def load_layout() -> str:
    """
    templates/layout.html
    """

    return _read_template(

        "layout.html"

    )


# --------------------------------------------------
# Handbook
# --------------------------------------------------


def load_handbook_template() -> str:
    """
    templates/handbook.html
    """

    return _read_template(

        "handbook.html"

    )


# --------------------------------------------------
# Homepage
# --------------------------------------------------


def load_homepage_template() -> str:
    """
    templates/homepage.html
    """

    return _read_template(

        "homepage.html"

    )


# --------------------------------------------------
# Dashboard
# --------------------------------------------------


def load_dashboard_template() -> str:
    """
    templates/dashboard.html
    """

    return _read_template(

        "dashboard.html"

    )


# --------------------------------------------------
# Validation
# --------------------------------------------------


def validate_templates() -> bool:
    """
    Validate required templates.
    """

    required = [

        "layout.html",

        "handbook.html",

        "homepage.html",

    ]

    for name in required:

        path = TEMPLATE_DIR / name

        if not path.exists():

            raise FileNotFoundError(

                f"Missing template: {path}"

            )

    return True