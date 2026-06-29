"""
Path and site configuration
SUPER CURVE TERMINAL v3.0.0-alpha
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

SITE_NAME = "SUPER CURVE TERMINAL"
SITE_SUBTITLE = "Institutional Market Intelligence"

SITE_URL = "https://super-curve-hub.github.io/finance-portal"
BASE_PATH = "/finance-portal"

DATA_DIR = ROOT / "data"
CONCEPTS_DIR = DATA_DIR / "concepts"
DASHBOARDS_DIR = DATA_DIR / "dashboards"
MARKET_DIR = DATA_DIR / "market"
RESEARCH_DIR = DATA_DIR / "research"
NEWS_DIR = DATA_DIR / "news"
CHARTS_DIR = DATA_DIR / "charts"

TEMPLATES_DIR = ROOT / "templates"

HANDBOOK_DIR = ROOT / "handbook"
DASHBOARD_DIR = ROOT / "dashboard"
LIBRARY_DIR = ROOT / "library"
SEARCH_DIR = ROOT / "search"
API_DIR = ROOT / "api"

ASSETS_DIR = ROOT / "assets"

SITEMAP_PATH = ROOT / "sitemap.xml"
ROBOTS_PATH = ROOT / "robots.txt"