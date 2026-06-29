"""
SUPER CURVE TERMINAL
Knowledge Graph Generator

Version : v3.0.0-alpha-builder
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def build_graph(concepts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Concept JSONからKnowledge Graphを構築する
    """

    graph = []

    for concept in concepts:

        node = {

            "id": concept.get("id", ""),

            "title": concept.get("title", ""),

            "type": concept.get("type", "concept"),

            "category": concept.get("category", ""),

            "url": f"/finance-portal/handbook/{concept.get('id','')}.html",

            "summary": concept.get("summary", ""),

            "tags": concept.get("tags", []),

            "related": concept.get("related", []),

            "dashboards": concept.get("dashboards", []),

            "research": concept.get("research", []),

            "charts": concept.get("charts", []),

            "news": concept.get("news", [])

        }

        graph.append(node)

    return graph


def generate_graph(
    api_dir: Path,
    concepts: list[dict[str, Any]]
) -> list[dict[str, Any]]:

    """
    api/graph.json を生成
    """

    api_dir.mkdir(parents=True, exist_ok=True)

    graph = build_graph(concepts)

    outfile = api_dir / "graph.json"

    outfile.write_text(

        json.dumps(

            {

                "version": "3.0.0-alpha-builder",

                "count": len(graph),

                "graph": graph

            },

            ensure_ascii=False,

            indent=2

        ),

        encoding="utf-8"

    )

    print("✓ api/graph.json")

    return graph


def load_graph(api_dir: Path) -> list[dict[str, Any]]:

    """
    graph.jsonを読み込む
    """

    file = api_dir / "graph.json"

    if not file.exists():

        return []

    with open(file, encoding="utf-8") as f:

        data = json.load(f)

    return data.get("graph", [])


def find_node(
    node_id: str,
    graph: list[dict[str, Any]]
) -> dict[str, Any] | None:

    """
    idでノード検索
    """

    for node in graph:

        if node["id"] == node_id:

            return node

    return None


def related_nodes(
    node_id: str,
    graph: list[dict[str, Any]]
) -> list[dict[str, Any]]:

    """
    関連ノード取得
    """

    node = find_node(node_id, graph)

    if node is None:

        return []

    related = []

    for rid in node.get("related", []):

        r = find_node(rid, graph)

        if r:

            related.append(r)

    return related