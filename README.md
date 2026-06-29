# SUPER CURVE FINANCE PORTAL

知識と市場データを同じJSONモデルで扱う、GitHub Pages対応の金融リサーチポータルです。

## コンセプト

- 知識：Option Handbook
- 市場データ：GEX / Oil / USDJPY / Rates / Shipping / Gold
- リサーチ：Macro Library / Notes
- 検索：AI Search / RAG拡張前提

## 公開方法

1. ZIPを解凍
2. 中身をGitHubリポジトリ直下へアップロード
3. `Settings → Pages → Branch: main / root` を選択
4. `https://super-curve-hub.github.io/finance-portal/` で公開

## 重要ディレクトリ

```text
data/concepts/      用語・概念
data/dashboards/   ダッシュボード定義
data/research/     リサーチ記事メタデータ
data/charts/       チャート定義
data/news/         Bloomberg / GS / JPM風の例文・外部リンク枠
api/search.json    将来RAG用の統合インデックス
```

## データモデル

すべての項目は以下の共通フィールドを持ちます。

```json
{
  "id": "gamma-flip",
  "type": "concept",
  "title": "Gamma Flip",
  "summary": "ディーラーのヘッジ方向が切り替わる価格帯。",
  "tags": ["options", "gex", "dealer-flow"],
  "related": ["gex", "dealer-long-gamma"],
  "dashboards": ["gex-dashboard"],
  "research": ["dealer-flow-regime-note"],
  "charts": ["gamma-flip-map"]
}
```

## 次の拡張

- Option Handbook 100語化
- 実データCSV/JSONの自動更新
- GitHub Actionsによるデータ更新
- Embedding生成
- RAG API連携
