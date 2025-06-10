# 📊 Analyze：ローカル IdeaMark 文書群の統計分析機能仕様

`ideamark analyze` は、ローカルディレクトリ内の複数の `.ideamark.yaml` ファイルを対象として、構造的な統計分析や傾向可視化を行う機能です。プロジェクト全体の知識構造を俯瞰する上で有用です。

## 🧭 機能目的

- 全体にわたる傾向、未処理領域、頻出パターンを発見
- 分類・整理・棚卸しの補助
- MCP Serverのダッシュボード連携やナレッジベース構築への基盤提供

---

## 🛠️ 使用例（CLI）

```sh
# カレントディレクトリの統計を表示
ideamark analyze

# 統計結果をJSONで出力
ideamark analyze --json > summary.json

# 特定のフィールドに絞った分析
ideamark analyze --fields tags,patterns
```

---

## 📈 分析内容一覧

| 分析項目 | 説明 |
|----------|------|
| ドキュメント総数 | 読み込まれた `.ideamark.yaml` の数 |
| タグ頻度 | 最も多く使われている `tags` |
| patternsの共起 | 同時に現れる `patterns` の組合せ統計 |
| refsの出現元 | 各 `refs` が何件のドキュメントに登場しているか |
| 空欄フィールド | `Problem`, `Deeds` などが未記入の文書リスト |
| 未拡張のアイデア | `extends`, `Discussion`, `sub_ideas` を持たない文書の抽出 |
| カテゴリ分布 | `category`, `theme` ごとの文書数 |

---

## 📄 出力形式

### テキスト出力（デフォルト）

```text
[Stats]
- Documents: 12
- Unique Tags: 38
- Top Tags: climate(5), ev(4), policy(3)

[Missing Fields]
- 3 documents missing 'Deeds'
- 2 documents missing 'Discussion'
```

### JSON形式出力（`--json`）

```json
{
  "document_count": 12,
  "top_tags": {
    "climate": 5,
    "ev": 4
  },
  "missing_fields": {
    "Deeds": ["doc1.yaml", "doc7.yaml"]
  }
}
```

---

## 📎 オプション一覧

| オプション | 内容 |
|------------|------|
| `--json` | 結果をJSON形式で出力 |
| `--fields` | 分析対象のフィールド指定（複数可） |
| `--dir` | 対象ディレクトリ指定（デフォルト: `./`） |

---

## ✅ MCP Server連携

- エンドポイント：
  - `GET /analyze`
  - オプション：対象ディレクトリパス、出力形式（text/json）
- 出力：リアルタイム統計概要、タグクラウド、未対応アイデアの通知

---

## 🔗 関連機能

- `ideamark search`：タグや語彙頻度を用いた検索
- `ideamark breakdown`：抽象度の高い文書の抽出と分解
- `ideamark extend`：未議論ドキュメントの拡張候補提示

---

この機能により、IdeaMarkは単体ドキュメントの記述支援を超え、プロジェクト全体のナレッジマネジメントを可能にする知的基盤となります。
