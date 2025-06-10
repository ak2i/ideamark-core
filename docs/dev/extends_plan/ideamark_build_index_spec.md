# 📂 Index Build：検索インデクス構築機能仕様

`ideamark build-index` は、複数の `.ideamark.yaml` ファイルを解析し、全文検索・高速検索に最適化された**逆引きインデクス構造**を構築する機能です。検索精度向上とMCP Serverでの効率的な照合を可能にします。

## 🧭 機能目的

- patterns / refs / tags を中心とした語句出現情報を整理
- 各ドキュメントがどの語句を含むか、また語句がどのドキュメントに含まれるかを双方向に保持
- `ideamark search` や `suggest` 機能の性能向上

---

## 🛠️ 使用例（CLI）

```sh
# インデクスを初期構築
ideamark build-index --dir ./ideas --output ./index.json

# 既存のインデクスに追記（マージ）
ideamark build-index --dir ./new --output ./index.json --merge
```

---

## 🧾 出力形式（JSON）

```json
{
  "terms": {
    "carbon-neutral": ["idea1.yaml", "idea3.yaml"],
    "ev": ["idea2.yaml", "idea3.yaml"]
  },
  "inverted_index": {
    "idea1.yaml": ["carbon-neutral", "policy"],
    "idea2.yaml": ["ev", "battery"]
  }
}
```

---

## 🧠 対象フィールド

インデクス対象とするフィールド（変更可能）：

- `patterns`
- `refs`
- `tags`
- `Problem`, `Discussion`（任意指定）

---

## 📎 オプション一覧

| オプション | 内容 |
|------------|------|
| `--dir` | 対象ディレクトリ（デフォルト: `./`） |
| `--output` | インデクス出力先（例: `index.json`） |
| `--fields` | 対象フィールド（例: `patterns,tags`） |
| `--merge` | 既存インデクスと統合 |
| `--purge` | 古いインデクスを削除して再構築 |

---

## 🔄 活用シナリオ

- `ideamark search` のレスポンス高速化
- MCP Serverでの即時検索・補完
- `vocab.json` 辞書と組み合わせた類義語マッチング

---

## ✅ MCP Server連携

- エンドポイント：
  - `POST /index/build`
  - 入力：対象ディレクトリ、出力ファイル名、マージ有無
- インデクスはサーバメモリまたは永続ストレージに保持され、全文検索時に参照

---

## 🔗 関連機能

- `ideamark search`：インデクスを使った高速検索
- `ideamark build-vocab`：辞書構築と組み合わせて語彙空間を最適化
- `ideamark analyze`：語の出現頻度に基づく統計分析

---

この機能により、IdeaMarkは単なるファイルの集積ではなく、「構造化検索可能な知識空間」としての基盤を獲得します。
