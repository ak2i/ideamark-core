# 🔍 Search：ドキュメント検索機能仕様

`ideamark search` は、ローカルに存在する IdeaMark ドキュメント群（YAML形式）に対して、構造的かつ語彙的に検索を行うためのコマンドです。

## 🧭 機能目的

- patterns / refs / tags などに記載された語句を用いて、関連ドキュメントを素早く特定する。
- MCP ServerやGUIインターフェースでの再利用も前提とした検索用メタ構造の整備。

---

## 🔍 対象構造フィールド

検索対象は以下のYAML構造フィールドです（オプションで指定可能）：

- `Problem`
- `Context`
- `Deeds`
- `Discussion`
- `patterns`
- `refs`
- `tags`

---

## 🛠️ 使用例（CLI）

```sh
# シンプルな検索
ideamark search --query "carbon-neutral"

# 特定フィールドに限定した検索
ideamark search --query "EV" --fields patterns,tags

# 類義語・語幹マッチも含めた検索
ideamark search --query "decarbonization" --fuzzy
```

---

## 🧠 検索モード

| モード | 説明 |
|-------|------|
| 通常 | 単語またはフレーズで一致するファイルを返す |
| 部分一致 | タグやrefs中に部分一致する文字列を含むファイルを返す |
| 類義語展開 (`--fuzzy`) | 語彙辞書（`vocab.json`）を用いた類義語・語幹展開 |

---

## 📦 出力形式（CLI）

- 標準出力に一致ファイルと一致箇所の要約を返す
- `--json` オプション指定で、機械処理可能な構造を返す：

```json
[
  {
    "file": "policy1.ideamark.yaml",
    "matched": ["patterns:carbon-neutral", "tags:climate"]
  },
  ...
]
```

---

## 🔗 関連機能

- `ideamark build-index`: 高速検索のためのインデクス作成
- `ideamark build-vocab`: 語彙辞書を使った類義語・語幹展開支援
- `ideamark suggest`: 検索語に関連する候補語を提案

---

## ✅ MCP Server連携

- HTTPエンドポイント：`GET /search?q=carbon+neutral`
- パラメータ：`fields=patterns,tags`、`mode=fuzzy`
- 検索インデクスを利用することでリアルタイム検索に対応可能

---

この機能は、構造化知識資源としてのIdeaMarkを横断的に活用する中核機能となります。
