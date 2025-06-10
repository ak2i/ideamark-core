# 🧩 Extend：ドキュメント拡張機能仕様

`ideamark extend` は、既存の IdeaMark ドキュメントに対して、議論・意見・提案・反論などを加えることで、ドキュメントの深掘りや多様な視点の追加を支援する機能です。

## 🧭 機能目的

- 任意の `.ideamark.yaml` ファイルに対して、関連する追加知識や立場を記述し、追記または派生ドキュメントを生成する。
- 課題解決策の議論や合意形成プロセスを支援する構造的拡張。

---

## 🔧 実装モード

### 1. **追記モード（in-place append）**
- 対象ファイルの `Discussion`, `Deeds`, `CounterProposal`, `Commentary` などのセクションに追記。

### 2. **派生モード（new document）**
- 元ファイルを継承した新しい `.ideamark.yaml` を生成。
- ヘッダに `extends: ./original.ideamark.yaml` を明記。

---

## 🛠️ 使用例（CLI）

```sh
# ファイルAに議論を追記
ideamark extend ideaA.ideamark.yaml --with debate.yaml --mode append

# 派生文書として新たに保存
ideamark extend ideaA.ideamark.yaml --with counter.yaml --mode derive --output ideaA.counter.ideamark.yaml
```

---

## 📄 生成される構造例（deriveモード）

```yaml
title: "Carbon Tariff Criticism"
extends: "./carbon_tariff.ideamark.yaml"

Discussion:
  - "While the original proposal focuses on EU trade fairness, this critique highlights developing countries' disadvantages..."
```

---

## 🧠 拡張対象フィールド

- `Discussion`
- `Deeds`
- `CounterProposal`
- `Commentary`
- `related_refs`（参考文献や外部出典の追加）

---

## 📎 オプション

| オプション | 内容 |
|------------|------|
| `--mode` | `append`（追記） / `derive`（派生） |
| `--with` | 拡張内容を含む補助YAMLまたはマークダウン |
| `--output` | 出力ファイル名（derive時） |
| `--tag` | 追加タグ指定（例：`--tag rebuttal`） |

---

## ✅ MCP Server連携

- エンドポイント例：
  - `POST /extend`
  - 入力：元ドキュメントID、拡張内容、モード
- サーバ側では追記or派生構造を自動生成し、バージョン管理と関連性を記録可能。

---

## 🔗 関連機能

- `ideamark compare`：拡張前後の比較
- `ideamark analyze`：拡張件数・深度の可視化
- `ideamark suggest`：拡張の候補例提示（AI支援）

---

この機能により、IdeaMark は一方向的な記述形式から、構造的かつ反復的な知識拡張の土台へと進化します。
