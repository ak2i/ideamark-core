# IdeaMark 拡張計画：CLI & MCP Server統合

このドキュメントは、`ideamark-core` のCLIおよびMCP Serverへの拡張方針を整理した技術仕様です。目的は、IdeaMarkドキュメントをローカル操作可能な強力な知識支援ツールとすることです。

## 対象コンポーネント
- CLI (`ideamark`)
- MCP Server (`MCP API`)

## 追加予定機能

| 機能カテゴリ    | 概要                           | CLIコマンド例            | 仕様書リンク                                                                 |
|-----------------|--------------------------------|--------------------------|-------------------------------------------------------------------------------|
| Search          | ドキュメント検索               | `ideamark search`        | [ideamark_search_spec.md](./ideamark_search_spec.md)                         |
| Extend          | 特定文書の議論による拡張       | `ideamark extend`        | [ideamark_extend_spec.md](./ideamark_extend_spec.md)                         |
| Compare         | 複数文書の構造比較             | `ideamark compare`       | [ideamark_compare_spec.md](./ideamark_compare_spec.md)                       |
| Breakdown       | 抽象的IdeaMarkの分解           | `ideamark breakdown`     | [ideamark_breakdown_spec.md](./ideamark_breakdown_spec.md)                   |
| Analyze         | ローカル文書群の統計           | `ideamark analyze`       | [ideamark_analyze_spec.md](./ideamark_analyze_spec.md)                       |
| Link/Attach     | DSL/GitHub/データ等の紐付け     | `ideamark attach`        | [ideamark_attach_spec.md](./ideamark_attach_spec.md)                         |
| Index Build     | 検索インデクス構築             | `ideamark build-index`   | [ideamark_build_index_spec.md](./ideamark_build_index_spec.md)               |
| Vocab Build     | 語彙辞書の構築                 | `ideamark build-vocab`   | [ideamark_build_vocab_spec.md](./ideamark_build_vocab_spec.md)               |
| Suggest         | 類義語・関連語提示             | `ideamark suggest`       | [ideamark_suggest_spec.md](./ideamark_suggest_spec.md)                       |

各機能の詳細は、個別ファイルまたは後続ドキュメントにて記載します。

## 設計方針と要件整理

### 1. コアライブラリ中心の設計
- IdeaMarkは「課題・解決策の知識表現」に特化したコアライブラリとして設計します。
- 検索・タグ・インデックス・バージョン管理などの機能も、ライブラリとして提供し、CLIやサーバー、Agent等の応用層が利用できる形にします。
- 議論やマルチユーザーセッション、AI支援などは応用層で実装し、コアは拡張性・再利用性を重視します。

### 2. 議論・マルチユーザー対応の進め方
- まずはAgent（CLIやBot等）を実装し、IdeaMark APIや表現力の検証・PoCを行います。
- 複数Agentによる簡易的な議論やシミュレーションも可能です。
- 本格的なマルチユーザー議論やセッション管理は、MCP Server等の上位層で段階的に実装します。
- 議論そのものの記録・形式化（発言ログ、合意形成プロセス等）は、IdeaMarkとは別のフォーマットや仕組みで管理し、必要に応じてIdeaMarkエントリとリンクします。

### 3. バージョン管理・差分表示
- IdeaMark/refsを活用し、各エントリが親（前バージョン）を参照する設計とします。
- 新しいバージョンは新IDで追加し、必要なときに差分を計算・表示できるようにします。
- この仕組みにより、履歴管理やバージョン間の比較が容易になります。

### 4. 検索・タグ機能
- 検索やタグ付けは、データ形式やインデックス生成機能をライブラリとして提供します。
- 応用層（AgentやServer等）がこれらを活用し、柔軟な検索・分類・フィルタリングを実現します。

### 5. 拡張性・応用例
- コアライブラリを中心に、AgentやMCP Serverなどの応用例・実装例を外部または別リポジトリで発展させます。
- 利用者が自分のユースケースに合わせて拡張・組み合わせできる設計を目指します。

---

この方針に従い、各機能追加の要件・仕様を今後整理・記述していきます。
