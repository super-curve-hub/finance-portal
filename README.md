# SUPER CURVE Finance Portal

GitHub Pages対応の金融ポータルです。

## 機能

- Option & Volatility Handbook
- 約100語の用語を `data/glossary.json` で管理
- 高速検索
- カテゴリ絞り込み
- ダークモード
- PWA対応
- スマホ最適化
- お気に入り保存
- 自分用メモ保存
- 関連用語リンク
- Bloomberg / Goldman Sachs / JPMorgan 風のレポート例文枠
- 将来AI検索を追加しやすいデータ構造

## GitHub Pages公開手順

1. GitHubで新規リポジトリを作成します。
   - 例: `super-curve-finance-portal`

2. このフォルダの中身をすべてアップロードします。

3. GitHubのリポジトリ画面で以下を設定します。

```text
Settings
↓
Pages
↓
Build and deployment
↓
Source: Deploy from a branch
↓
Branch: main
↓
Folder: /root
↓
Save
```

4. 数分後に以下の形式で公開されます。

```text
https://super-curve-hub.github.io/super-curve-finance-portal/
```

## ローカル確認

```bash
python3 -m http.server 8000
```

ブラウザで開く:

```text
http://localhost:8000
```

## データ更新

用語は `data/glossary.json` に追加します。
モジュール一覧は `data/modules.json` に追加します。
レポートリンクや自分の解説は `data/research-links.json` に追加します。
