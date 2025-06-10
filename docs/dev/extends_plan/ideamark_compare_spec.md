# 🧮 Compare：複数ドキュメントの構造比較機能仕様

`ideamark compare` は、複数の IdeaMark ドキュメント間の構造的類似性と差異を明示的に比較し、意思決定・統合・差分分析を支援するための機能です。

## 🧭 機能目的

- 複数の提案や視点を並列的に評価・対比しやすくする
- 同一テーマに対する多様なアプローチの整理
- 統合・派生・拡張時の判断材料を可視化する

---

## 🛠️ 使用例（CLI）

```sh
# 2つのファイルを比較
ideamark compare fileA.yaml fileB.yaml

# 複数ファイルを同時比較（並列比較）
ideamark compare file1.yaml file2.yaml file3.yaml

# 差異だけに絞って表示
ideamark compare file1.yaml file2.yaml --only-diff
```

---

## 🧠 比較対象の構造フィールド

以下の主要フィールドを対象に比較：

- `Problem`
- `Context`
- `Deeds`
- `Discussion`
- `patterns`
- `refs`
- `tags`
- `category` / `theme` などのメタ情報

---

## 📋 出力形式

### デフォルト出力（人間可読）

```text
=== Comparing: A.yaml vs B.yaml ===

[✓] Problem: 共通
[≠] Context: 内容が異なります
[+] Deeds (Aのみ): "Implement EV subsidy"
[+] Discussion (Bのみ): "Raises concern on tax burden"
...
```

### JSON形式出力（--json）

```json
{
  "Problem": "same",
  "Context": "different",
  "Deeds": {
    "only_in_A": ["..."],
    "only_in_B": ["..."]
  }
}
```

---

## 🧮 類似度スコア（オプション）

```sh
ideamark compare A.yaml B.yaml --score
```

- 各フィールドごとに `0.0〜1.0` のスコア
- 全体スコア＋重要フィールドの比較表を出力

---

## 📎 オプション一覧

| オプション | 説明 |
|------------|------|
| `--json` | JSON形式で出力 |
| `--only-diff` | 差異がある部分だけを表示 |
| `--score` | 類似度スコアを表示 |
| `--table` | MarkdownやCSVの比較表を出力 |

---

## ✅ MCP Server連携

- エンドポイント：
  - `POST /compare`
  - 入力：ファイルIDの配列、出力形式オプション
- 出力：比較結果（構造差分、スコア、要約）

---

## 🔗 関連機能

- `ideamark extend`：比較結果からどちらかを拡張
- `ideamark suggest`：類似ファイルの推薦
- `ideamark analyze`：類似テーマ群のクラスタリング

---

この機能により、IdeaMarkは単なる記述ファイルではなく、複数視点の対話・調整・統合を可能にする知識比較基盤となります。
