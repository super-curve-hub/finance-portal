"""
SUPER CURVE TERMINAL
Search Generator

Version : v3.0.0-alpha-builder
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def build_search_objects(concepts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Concept JSON から Search Object を生成する
    """

    objects = []

    for concept in concepts:

        objects.append(
            {
                "id": concept.get("id", ""),
                "title": concept.get("title", ""),
                "summary": concept.get("summary", ""),
                "plain_jp": concept.get("plain_jp", ""),
                "category": concept.get("category", ""),
                "category_name": concept.get("category_name", ""),
                "type": concept.get("type", "concept"),
                "tags": concept.get("tags", []),
                "url": f"/finance-portal/handbook/{concept.get('id','')}.html",
            }
        )

    return objects


def generate_search(
    api_dir: Path,
    concepts: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    api/search.json を生成する

    Returns
    -------
    objects
        HomepageやKnowledge Graphから再利用する
    """

    api_dir.mkdir(parents=True, exist_ok=True)

    objects = build_search_objects(concepts)

    outfile = api_dir / "search.json"

    outfile.write_text(

        json.dumps(
            {
                "version": "3.0.0-alpha-builder",
                "count": len(objects),
                "objects": objects,
            },
            ensure_ascii=False,
            indent=2,
        ),

        encoding="utf-8",
    )

    print("✓ api/search.json")

    return objects


def load_search(api_dir: Path) -> list[dict[str, Any]]:
    """
    search.json を読み込む
    """

    file = api_dir / "search.json"

    if not file.exists():
        return []

    with open(file, encoding="utf-8") as f:

        data = json.load(f)

    return data.get("objects", [])


def search_keyword(
    keyword: str,
    objects: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    簡易全文検索
    """

    keyword = keyword.lower()

    result = []

    for obj in objects:

        text = " ".join(
            [

                obj.get("title", ""),

                obj.get("summary", ""),

                obj.get("plain_jp", ""),

                " ".join(obj.get("tags", [])),

            ]
        ).lower()

        if keyword in text:

            result.append(obj)

    return result


def search_category(
    category: str,
    objects: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Category検索
    """

    return [

        obj

        for obj in objects

        if obj.get("category") == category

    ]


def search_tag(
    tag: str,
    objects: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Tag検索
    """

    return [

        obj

        for obj in objects

        if tag in obj.get("tags", [])

    ]