# SUPER CURVE TERMINAL / Finance Portal

GitHub Pagesで動く金融リサーチポータルです。

## 実装済み

- Bloomberg Terminal風トップページ
- Option Handbook 100語辞典
- JSON Knowledge Graph設計
- GEX / Oil / USDJPY / Rates / Shipping / Gold Dashboard
- Static JSONによる市場データ表示
- AI Search（RAG-ready、現状はローカルJSON横断検索）
- スマホ対応 / PWA基盤

## 更新方法

市場データは `data/market/*.json` を更新します。
用語は `data/concepts/*.json` を追加します。
検索は `api/search.json` を更新します。

## 将来拡張

`api/search.json` をEmbedding化し、Vector DB + OpenAI APIに接続すればRAG検索へ移行できます。
