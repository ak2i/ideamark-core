# 💡 Suggest：類義語・関連語提示機能仕様

`ideamark suggest` は、入力された語句や検索語に対して、語彙辞書や共起データを元に**類義語・表記ゆれ・意味的に近い語**などを提示する機能です。検索支援、文書拡張、語彙標準化などの文脈で活用されます。

## 🧭 機能目的

- 語彙のばらつきを吸収して検索精度を向上
- 未知語に対する語彙候補を提示
- ドキュメント作成時の語彙選択支援

---

## 🛠️ 使用例（CLI）

```sh
# 類義語と関連語を表示
ideamark suggest --term "carbon neutrality"

# ステミング後の語幹から逆展開
ideamark suggest --term "decarbonized" --expand
```

---

## 📄 出力形式（標準）

```text
[carbon neutrality]

stem: carbon-neutral
aliases: carbon-neutral, decarbonized, climate-neutral
files: idea1.yaml, idea2.yaml

related_terms:
  - ev (3共起)
  - emission (2共起)
```

---

## 🔍 辞書・インデクス活用

- `vocab.json`：語幹、別名、登場ファイル
- `index.json`：共起語、頻度統計
- 構文ベースの展開（例："EV" → "electric vehicle", "charging station"）

---

## 📎 オプション一覧

| オプション | 内容 |
|------------|------|
| `--term` | 対象語句 |
| `--expand` | 類義語・語幹を双方向に展開 |
| `--show-files` | 登場ファイル一覧を表示 |
| `--with-context` | 実際の使用文脈例も表示 |
| `--json` | 機械可読な出力形式 |

---

## 📤 出力形式（JSON）

```json
{
  "term": "carbon neutrality",
  "stem": "carbon-neutral",
  "aliases": ["carbon-neutral", "decarbonized"],
  "related_terms": ["emission", "ev", "renewable"],
  "files": ["doc1.yaml", "doc4.yaml"]
}
```

---

## ✅ MCP Server連携

- エンドポイント：
  - `GET /suggest?term=carbon+neutrality`
  - パラメータ：`expand`, `format=json`
- GUIインターフェースでサジェスト候補をクリックして検索連携可能

---

## 🔗 関連機能

- `ideamark search --fuzzy`：サジェスト語を検索に利用
- `build-vocab`：語幹・同義語辞書を事前構築
- `build-index`：共起語・頻度データの構築基盤

---

この機能により、IdeaMarkは語彙の揺らぎや表現の多様性を内包した「語彙ネットワーク対応型知識ベース」として機能します。
