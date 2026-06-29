# Contributing

このプロジェクトは、JSONを編集してサイトを生成する方式で運用する。

## 基本ルール

1. 手書きHTMLを増やさない。
2. 新しい用語は `data/concepts/*.json` に追加する。
3. 新しいダッシュボードは `data/dashboards/*.json` に追加する。
4. 生成物は `python3 scripts/build.py` で作る。
5. Push前にローカルでビルドする。

## Local Build

```bash
python3 scripts/build.py
```

## Commit Flow

```bash
git status
git add .
git commit -m "Update content"
git push
```

## Release Flow

```bash
git tag -a v3.0.0-alpha -m "v3.0.0-alpha Build System"
git push origin v3.0.0-alpha
```

## Concept追加手順

```text
1. data/concepts/new-concept.json を作る
2. DATA_SCHEMA.md に従って記述する
3. python3 scripts/build.py を実行する
4. handbook/new-concept.html が生成されたか確認する
5. api/search.json に入っているか確認する
6. git commit / git push
```

## 禁止事項

- 生成されたHTMLだけを直接編集しない。
- `api/search.json` を手で編集しない。
- `sitemap.xml` を手で編集しない。
- 旧 `glossary/` を新規開発に使わない。

## 例外

緊急修正の場合のみHTMLを直接編集してよい。ただし、次回ビルドで上書きされる前提で、必ずJSON側へ反映する。
