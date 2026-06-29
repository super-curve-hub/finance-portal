import json
import html
from pathlib import Path


def read_text(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def load_json(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def dump_json(path: Path, data) -> None:
    write_text(path, json.dumps(data, ensure_ascii=False, indent=2))


def esc(value) -> str:
    if value is None:
        return ''
    return html.escape(str(value), quote=True)


def render_list(items) -> str:
    if not items:
        return '<p class="muted">-</p>'
    return '<ul>' + ''.join(f'<li>{esc(x)}</li>' for x in items) + '</ul>'


def slug_url(base_path: str, section: str, slug: str) -> str:
    return f'{base_path}/{section}/{slug}.html'
