# 🧱 Breakdown：抽象的 IdeaMark の分解機能仕様

`ideamark breakdown` は、抽象的・包括的に記述された IdeaMark ドキュメントを、より細分化された具体的な IdeaMark 群に分解するための機能です。これにより、複雑な課題を複数の扱いやすい単位へと整理・変換できます。

## 🧭 機能目的

- 大きな社会課題や構造問題を、個別の論点・ステークホルダー・要素技術などに分割
- 複数の視点から構造的に課題を捉えるための出発点を構築
- `sub_ideas` や `category` を活用したドキュメント再構成

---

## 🛠️ 使用例（CLI）

```sh
# general.ideamark.yaml を複数のサブIdeaMarkに分解
ideamark breakdown general.ideamark.yaml

# 出力ディレクトリ指定
ideamark breakdown general.ideamark.yaml --out-dir ./sub_ideas
```

---

## ⚙️ 分解戦略（ルール）

- 元ファイル内の以下のフィールドを分割基準とする：
  - `patterns`: 各パターンが1つのサブIdeaMarkに
  - `refs`: 論点ごとに分割（出典・出発点に着目）
  - `Deeds`: 行動項目別に展開
  - `Discussion`: 意見・視点を単位に分岐
- 自動命名：`originalID.pattern001.ideamark.yaml` のように生成

---

## 🧱 出力形式

### 派生ドキュメント例

```yaml
title: "EV Infrastructure Development"
extends: "./general.ideamark.yaml"

Problem: "Insufficient EV charging networks in rural areas"
patterns:
  - "build-ev-infra"
...
```

### メタリンク付き親ファイル更新（任意）

```yaml
sub_ideas:
  - ./sub_ideas/ev_infra.ideamark.yaml
  - ./sub_ideas/battery_policy.ideamark.yaml
```

---

## 📎 オプション一覧

| オプション | 内容 |
|------------|------|
| `--out-dir` | 出力先ディレクトリ（デフォルト: `./`） |
| `--mode` | `split`（個別ファイル） / `embed`（親ファイルに埋め込み） |
| `--strategy` | `patterns`, `refs`, `deeds`, `discussion` など分割基準 |

---

## ✅ MCP Server連携

- エンドポイント：
  - `POST /breakdown`
  - 入力：ファイルID、分解戦略、出力モード
- 出力：サブファイル群、親子リンク付き構造

---

## 🔗 関連機能

- `ideamark analyze`：抽象度の高いIdeaの検出
- `ideamark extend`：各サブIdeaへの議論追加
- `ideamark compare`：分解前後の差分確認

---

この機能により、IdeaMarkは単なる知識の記述媒体から、「構造的アイディエーション」および「戦略的課題解体」のツールへと進化します。
