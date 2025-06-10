# IdeaMark 拡張計画：CLI & MCP Server統合

このドキュメントは、`ideamark-core` のCLIおよびMCP Serverへの拡張方針を整理した技術仕様です。目的は、IdeaMarkドキュメントをローカル操作可能な強力な知識支援ツールとすることです。

## 対象コンポーネント
- CLI (`ideamark`)
- MCP Server (`MCP API`)

## 追加予定機能

| 機能カテゴリ | 概要 | CLIコマンド例 |
|--------------|------|----------------|
| Search | ドキュメント検索 | `ideamark search` |
| Extend | 特定文書の議論による拡張 | `ideamark extend` |
| Compare | 複数文書の構造比較 | `ideamark compare` |
| Breakdown | 抽象的IdeaMarkの分解 | `ideamark breakdown` |
| Analyze | ローカル文書群の統計 | `ideamark analyze` |
| Link/Attach | DSL/GitHub/データ等の紐付け | `ideamark attach` |
| Index Build | 検索インデクス構築 | `ideamark build-index` |
| Vocab Build | 語彙辞書の構築 | `ideamark build-vocab` |
| Suggest | 類義語・関連語提示 | `ideamark suggest` |

各機能の詳細は、個別ファイルまたは後続ドキュメントにて記載します。
