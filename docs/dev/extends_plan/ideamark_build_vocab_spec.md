# 🧠 Vocab Build：語彙辞書構築機能仕様

`ideamark build-vocab` は、IdeaMark ドキュメント群から抽出したキーワード・パターン・参照語を分析し、**語彙空間辞書（vocabulary dictionary）**を構築するための機能です。類義語展開、ファジーマッチ、語幹変換に基づく検索や推薦の基盤を担います。

## 🧭 機能目的

- `patterns`, `refs`, `tags` を構造化語彙として整理
- 類義語・語幹・関連語のマッピング辞書を自動生成
- `search`, `suggest`, `compare` 機能の精度向上

---

## 🛠️ 使用例（CLI）

```sh
# 指定ディレクトリの語彙辞書を構築
ideamark build-vocab --dir ./ideas --output ./vocab.json
```

---

## 📄 出力形式（例：`vocab.json`）

```json
{
  "carbon-neutral": {
    "stem": "carbon-neutral",
    "aliases": ["carbon neutrality", "decarbonized"],
    "files": ["idea1.yaml", "idea3.yaml"],
    "examples": [
      "Aims to achieve carbon-neutral logistics by 2040"
    ]
  },
  "ev": {
    "stem": "ev",
    "aliases": ["electric vehicle"],
    "files": ["idea2.yaml"],
    "examples": ["Public EV charger installation incentives"]
  }
}
```

---

## 🔍 辞書構成要素

| 要素 | 説明 |
|------|------|
| `stem` | 正規化された語幹（lemmatized） |
| `aliases` | 同義語・表記ゆれ |
| `files` | 出現した `.ideamark.yaml` のファイル名リスト |
| `examples` | 出現文脈の例（抜粋） |

---

## 🧠 処理内容

- トークン分割（tokenize）
- ステミング・正規化（normalize）
- 類義語抽出（内蔵辞書 or カスタム語彙）
- 出現コンテキストのキャプチャ

---

## 📎 オプション一覧

| オプション | 内容 |
|------------|------|
| `--dir` | 対象ディレクトリ（デフォルト: `./`） |
| `--output` | 出力先ファイル（例: `vocab.json`） |
| `--fields` | 対象フィールド（例: `patterns,refs,tags`） |
| `--stemmer` | `porter`, `lemmatizer`, `none`（省略時: porter） |
| `--with-aliases` | 類義語マップの追加指定（JSONまたはTSV形式） |

---

## ✅ MCP Server連携

- エンドポイント：
  - `POST /vocab/build`
  - パラメータ：対象パス、出力パス、類義語辞書パスなど
- MCP内ではキャッシュされた語彙を用いてサジェスト・拡張・補完を実行可能

---

## 🔗 関連機能

- `ideamark search --fuzzy`：語彙辞書による拡張検索
- `ideamark suggest`：関連語・近縁語の提示
- `ideamark analyze`：語彙出現頻度や偏在の可視化
- `build-index`：辞書と連携した効率的な語→ファイル照合

---

この機能により、IdeaMarkは単なるキーワード記述の集合ではなく、**語彙空間に基づく意味構造ネットワーク**として進化します。
