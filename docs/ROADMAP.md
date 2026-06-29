# SUPER CURVE TERMINAL Roadmap

このプロジェクトは、静的HTMLサイトではなく、JSONを中心にした金融リサーチ・プラットフォームとして運用する。

## v3.0.0-alpha: Build System

目的: JSONからサイトを自動生成する基盤を完成させる。

対象:

- `data/concepts/*.json`
- `data/dashboards/*.json`
- `data/research/**`
- `templates/*.html`
- `scripts/build.py`
- `api/search.json`
- `sitemap.xml`

完了条件:

- `python3 scripts/build.py` でHandbookが生成される
- `api/search.json` が自動生成される
- `sitemap.xml` が自動生成される
- GitHub Actionsでビルドが走る
- GitHub Pagesに自動反映される

## v3.1.0-beta: Option Handbook

目的: Option & Volatility Handbookを約100語まで拡張する。

対象カテゴリ:

- Dealer Flow
- Greeks
- Volatility
- Strategy
- Market Structure
- Flow
- Macro / Event
- Indices

各用語ページの構成:

- English
- 一言でいうと
- 詳細説明
- Formula
- Market Impact
- Dealer Action
- Trader Watch
- Report Examples
- Related Concepts

## v3.2.0: Dashboards

目的: 主要マーケット・ダッシュボードをJSON駆動で生成する。

対象:

- GEX Dashboard
- Oil Regime Dashboard
- USDJPY Intervention Dashboard
- Rates Dashboard
- Shipping Dashboard
- Gold / Silver Dashboard

## v3.3.0: Knowledge Graph

目的: 用語、ダッシュボード、リサーチ、ニュース、チャートの関連性を統合する。

生成物:

- `api/graph.json`
- 関連用語リンク
- 関連ダッシュボードリンク
- 関連リサーチリンク

## v3.4.0: Macro Library

目的: Markdown / JSONベースのリサーチライブラリを生成する。

対象:

- Oil
- Rates
- FX
- Shipping
- Metals
- Macro
- Japan

## v3.5.0: Search Engine

目的: `api/search.json` を用いた高速検索を完成させる。

対象:

- Handbook
- Dashboard
- Macro Library
- Charts
- News

## v4.0.0: AI Search / RAG

目的: JSONデータベースとKnowledge GraphをRAGへ拡張する。

流れ:

```text
JSON
↓
Search Index
↓
Embedding
↓
Vector Store
↓
RAG
↓
AI Search
```

## v5.0.0: Personal Bloomberg Terminal

目的: 個人版Bloomberg Terminalとして、知識・市場データ・リサーチ・AI検索を統合する。
