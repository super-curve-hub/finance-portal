"""
Template Loader
SUPER CURVE TERMINAL v3.0.0-alpha
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = ROOT / "templates"


def _read_template(filename: str) -> str:
    """
    テンプレートファイルを読み込む
    """
    path = TEMPLATE_DIR / filename

    if not path.exists():
        raise FileNotFoundError(
            f"Template not found: {path}"
        )

    return path.read_text(
        encoding="utf-8"
    )


def load_layout() -> str:
    """
    layout.html
    """
    return _read_template("layout.html")


def load_handbook_template() -> str:
    """
    handbook.html
    """
    return _read_template("handbook.html")


def load_dashboard_template() -> str:
    """
    dashboard.html
    """
    return _read_template("dashboard.html")