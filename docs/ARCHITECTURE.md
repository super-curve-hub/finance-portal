# Architecture

SUPER CURVE TERMINALは、ページを手書きで積み上げるのではなく、JSONを中心にした静的データベースとして設計する。

## Core Concept

```text
JSON
↓
Build System
↓
HTML / API Index / Sitemap
↓
GitHub Pages
↓
AI Search / RAG
```

## Directory Roles

```text
data/          Source of truth
templates/     HTML templates
scripts/       Build entry points and generators
assets/        CSS, JavaScript, images, icons
handbook/      Generated Handbook pages
dashboard/     Dashboard pages
library/       Research library pages
api/           Search and graph JSON
```

## Source of Truth

`data/` が唯一の正しいデータソース。

```text
data/
├── concepts/      Option Handbook concepts
├── dashboards/    Dashboard configs
├── market/        Market data snapshots
├── research/      Research objects
├── news/          External note/news references
├── charts/        Chart objects
└── modules.json   Portal module list
```

## Generated Outputs

以下は原則としてビルド生成物。

```text
handbook/*.html
handbook/index.html
api/search.json
api/graph.json
sitemap.xml
robots.txt
```

## Build Flow

```text
1. Validate JSON
2. Load templates
3. Render Handbook pages
4. Render indexes
5. Generate search index
6. Generate graph index
7. Generate sitemap
8. Publish via GitHub Pages
```

## GitHub Pages Strategy

現時点では GitHub Pages の `main / root` 公開を使う。

GitHub Actions は `scripts/build.py` を実行し、生成物が変わった場合は自動でコミットする。

これにより、GitHub Pages側の設定を変更せずに自動ビルド・自動公開が可能になる。

## Future RAG Strategy

将来は以下を追加する。

```text
api/search.json
api/graph.json
↓
Embedding
↓
Vector DB
↓
AI Search
```
