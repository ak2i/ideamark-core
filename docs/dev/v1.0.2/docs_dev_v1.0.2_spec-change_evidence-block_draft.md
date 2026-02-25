# docs/dev/v1.0.2/spec-change-evidence-block.md
## v1.0.2 変更点：Evidence Block の導入（Draft）

Generated: 2026-02-22T00:12:57.249972Z

この文書は v1.0.2 における Evidence Block 導入に関する差分方針をまとめる。

---

## 1. 追加する仕様要素（IdeaMark Document/YAML Spec）

- Markdown 本文中に fenced YAML を埋め込めることは既存 Markdown の能力として当然だが、
  v1.0.2 では **`ideamark:evidence`** を識別子として、ツール生成結果の格納用途を標準化する。
- Evidence Block は拡張前提であり、キーや値の意味は固定しない。
- validate は Evidence Block の未知キーを理由に fail してはならない。

参照：`docs/dev/v1.0.2/evidence-block-normative.md`

---

## 2. Doc CLI Contract への影響（共通オプションの提案）

派生コマンド体系（複数バージョン比較、和集合、遷移プロファイル等）を拘束しないため、
**結果の出力と付加**だけを横断オプションとして標準化する案を採用する。

提案（SHOULD）：
- `--emit-evidence {yaml|ndjson}`
- `--evidence-scope {document|section|entity|occurrence}`
- `--evidence-target <id>`
- `--attach <file|->`（Evidence Block を挿入した改訂版を stdout に出す）
- `--artifact-out <path>`（大きい結果を外部化し、Evidence Block に参照を残す）

※ どのコマンドがどのオプションを実装するかは capabilities で宣言する。

---

## 3. バージョニング

Evidence Block は “追加要素” であり、既存文書を壊さない：

- v1.0.1 文書は Evidence Block を含まなくてもよい
- v1.0.2 ツールは Evidence Block の存在を許容する（パース/保持/出力）
- 後続で推奨スキーマやメトリクス語彙を追加しても、未知キー許容により後方互換を保ちやすい

---

End of draft.
