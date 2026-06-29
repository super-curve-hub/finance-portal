# Data Schema

このプロジェクトでは、JSONをサイト全体のマスターデータとして扱う。

## Concept Schema

`data/concepts/*.json` はOption Handbookの各用語を表す。

```json
{
  "metadata": {
    "version": "1.0",
    "updated": "2026-06-29",
    "author": "SUPER CURVE"
  },
  "display": {
    "icon": "📊",
    "color": "blue"
  },
  "id": "gamma-flip",
  "type": "concept",
  "category": "dealer-flow",
  "category_name": "Dealer Flow",
  "title": "Gamma Flip",
  "english": "Gamma Flip",
  "summary": "市場全体のGamma Exposureが切り替わる価格帯。",
  "plain_jp": "ディーラーのヘッジ行動が変わる価格。",
  "description": "詳細説明。",
  "formula": {
    "ascii": "Net GEX = Σ(Gamma × OI × Multiplier)",
    "latex": "Net\\ GEX = \\sum_i \\Gamma_i \\times OI_i \\times Multiplier_i"
  },
  "market_impact": {
    "bull": 5,
    "bear": 2,
    "description": "相場への影響。"
  },
  "dealer_action": {
    "long_gamma": ["価格上昇 → 売る", "価格下落 → 買う"],
    "short_gamma": ["価格上昇 → 買う", "価格下落 → 売る"]
  },
  "trader_watch": ["Spot価格", "Net GEX"],
  "report_examples": [
    {
      "source": "Bloomberg",
      "english": "Example sentence.",
      "japanese": "日本語訳。"
    }
  ],
  "related": ["gex", "vanna"],
  "dashboards": ["gex-dashboard"],
  "research": ["dealer-flow-regime-note"],
  "charts": ["gamma-flip-map"],
  "news": ["bloomberg-gamma-flip"],
  "tags": ["options", "gex"],
  "page": "gamma-flip.html"
}
```

## Required Fields

Conceptでは最低限以下を必須にする。

```text
id
type
title
summary
plain_jp
description
```

## Dashboard Schema

`data/dashboards/*.json` は各ダッシュボードを表す。

```json
{
  "id": "gex-dashboard",
  "type": "dashboard",
  "title": "GEX Dashboard",
  "summary": "Dealer Gamma regime monitor.",
  "metrics": ["spot", "net-gex", "gamma-flip"],
  "related": ["gamma-flip", "gex", "vanna"],
  "page": "gex.html"
}
```

## Search Index Schema

`api/search.json` はビルド時に自動生成する。

```json
{
  "id": "gamma-flip",
  "type": "concept",
  "title": "Gamma Flip",
  "category": "dealer-flow",
  "summary": "...",
  "url": "/handbook/gamma-flip.html",
  "tags": ["options", "gex"]
}
```

## Knowledge Graph Schema

`api/graph.json` は将来生成する。

```json
{
  "nodes": [],
  "edges": []
}
```
