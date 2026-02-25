# docs/dev/v1.0.2/evidence-block-normative.md
## Evidence Block — v1.0.2 最小要件（Normative Draft）

Generated: 2026-02-22T00:12:57.249972Z

この文書は、`docs/dev/v1.0.2/evidence-annotations.md`（議論ドラフト）を前提に、
**v1.0.2 の正式仕様（specs側）へ取り込む最小要件**を切り出したものです。

狙い：
- spec 本体を重くしない（指標やスキーマは拡張前提）
- ただし「文書に機械可読な evidence を埋め込める」ことは標準として保証する

---

## 1. 定義

**Evidence Block** とは、IdeaMark 文書の Markdown 本文に埋め込まれる、機械可読な注釈ブロックである。  
Evidence Block は主に Doc CLI（例：`ideamark diff`）が生成する統計・差分・プロファイリング等の結果を、
必要に応じてオンデマンドに付加する用途で用いる。

---

## 2. 形式（MUST / MUST NOT）

### 2.1 ブロック識別子
Evidence Block は次の fenced code block 形式で表現される：

```markdown
```yaml ideamark:evidence
<YAML mapping>
```
```

- フェンス言語は `yaml` を用いる。
- info string に `ideamark:evidence` を含めること（MUST）。

### 2.2 内容の型
- ブロック内容は YAML の **mapping/object** でなければならない（MUST）。
- mapping/object でない場合、文書は validation error となり得る（MAY）。
  - ただし、v1.0.2 では “どのコマンドがどこまで検証するか” はツール実装に委ねる。

### 2.3 拡張性
- Evidence Block のキーは拡張前提であり、未知キーを理由に validation failure してはならない（MUST NOT）。
- Evidence Block の目的は “結果の記録” であり、文書の主本文（meaning content）の真偽を拘束しない。

---

## 3. 配置（Placement）

Evidence Block は文書中の任意位置に置いてよい（MAY）。  
ただし、ツールが挿入しやすいよう、次のスコープ位置が推奨される（SHOULD）：

- Document-level：ヘッダ直後、または文末
- Section-level：該当 Section 本文直下
- Entity-level：Entity 定義（Registry内）直下または近傍
- Occurrence-level：Occurrence 定義（Registry内）直下または近傍

※ v1.0.2 では厳密な位置制約は設けない（再利用性・互換性優先）。

---

## 4. 推奨メタ（SHOULD）

Evidence Block は次のメタ情報を含むことが望ましい（SHOULD）：

- `kind`（例：diff-metric / profile / query-result / lint-report）
- `scope` と `target`（document/section/entity/occurrence + 対象ID）
- `produced_by`（tool / command / plugin / tool_version）
- `produced_at`（生成時刻）
- `inputs`（比較対象・クエリ条件・対象期間など）
- `limits`（オンデマンド計算、部分性、近似など）

※ 推奨スキーマの詳細は `docs/dev/v1.0.2/evidence-annotations.md` を参照。

---

## 5. 仕様への取り込み方針

v1.0.2 の正式仕様（specs）には、次のみを含める：

- Evidence Block を許容すること（MAY）
- 識別子（`yaml ideamark:evidence`）
- 内容が mapping/object であること
- 未知キーで落とさないこと（拡張性）
- 配置は任意（位置制約なし）

指標の種類、メトリクス名、統計モデル、外部アーティファクト参照などは、
拡張仕様（docs/dev）として管理し、後続バージョンで必要に応じて固める。

---

End of draft.
