# 🔗 Link / Attach：外部ソースとの紐付け機能仕様

`ideamark attach` は、IdeaMark ドキュメントとDSLコード、GitHubリポジトリ、データファイル、参考資料などの外部ソースを構造的にリンクさせるための機能です。これにより、実装・根拠・事例へのアクセス性を高め、Ideaと現実の対応関係を明示します。

## 🧭 機能目的

- IdeaMarkの各アイデアに関連する実装や参考資料を明示的に接続
- ドキュメントと外部リソースをナビゲーション可能に
- `MCP Server` や `Web Viewer` 上での双方向連携を可能に

---

## 🛠️ 使用例（CLI）

```sh
# 単一の外部ソースを紐付け
ideamark attach idea.yaml --link dsl=./logic.dsl

# 複数リンクを一括追加
ideamark attach idea.yaml \
  --link github=https://github.com/ak2i/ideamark-core \
  --link data=./data/ev_policy.csv
```

---

## 🔧 構文仕様

リンク情報は YAML ドキュメント内に `source_links` セクションとして追記：

```yaml
source_links:
  - dsl: ./dsl/ev_policy.dsl
  - github: https://github.com/ak2i/ideamark-core
  - data: ./data/policy_survey.csv
  - report: https://example.com/research2024.pdf
```

- 各リンクには任意のキー名を指定可能（`dsl`, `github`, `data`, `doc`, `api`, `ref` など）
- 相対パス・絶対URL両方対応

---

## 📎 オプション一覧

| オプション | 内容 |
|------------|------|
| `--link` | `key=value` 形式のリンク情報（複数指定可） |
| `--remove` | 特定リンクを削除（例：`--remove github`） |
| `--output` | 上書き保存せず、別ファイルとして出力 |

---

## 🌐 利用用途の例

| ソース種別 | 目的例 |
|------------|--------|
| `dsl` | 関連する意思決定ルールや定義構文 |
| `github` | 該当するコード実装やIssue |
| `data` | 実証に用いた統計データや調査結果 |
| `api` | 関連APIやサービス仕様 |
| `report` | 学術文献や白書などの参考資料 |

---

## ✅ MCP Server連携

- エンドポイント：
  - `POST /attach`
  - 入力：ドキュメントID、リンク情報のリスト
- GUI上でリンクリストをカード表示し、クリックで外部遷移可能

---

## 🔗 関連機能

- `ideamark analyze`：リンクの有無で分類・棚卸し
- `ideamark extend`：資料に基づく提案拡張
- `ideamark suggest`：類似リンク付きドキュメント推薦

---

この機能により、IdeaMarkは知識の記述を越えて、実装・証拠・資料と一体化した**構造化知識のハブ**として機能します。
