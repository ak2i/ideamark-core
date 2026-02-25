# docs/dev/v1.0.2/evidence-annotations.md
## Evidence Annotations（統計・差分結果の埋め込み）— v1.0.2 議論ドラフト

Generated: 2026-02-22T00:08:10.484673Z

この文書は、`ideamark diff` などの Doc CLI ツールが生成する統計・差分・プロファイリング結果を、
IdeaMark 文書へ **機械可読な形で付加（annotation）**するための方針案です。

- 統計や距離指標の内容自体はプラグインで拡張できる前提
- ここでは「成果（evidence）を文書へどう格納し、CLI標準へどう影響するか」を定義する

---

## 1. 目標

1. **必要な時だけ**ツール結果を文書に付加できる（常時全量計算はしない）
2. 付加された結果は **機械処理可能**（後で検索・集計・比較ができる）
3. 結果には **生成条件・バージョン・対象範囲**などのメタが付く（再現性・信頼性）
4. 文書本文（Markdown本文）を汚さず、本文は「人間向けの解釈」を書ける

---

## 2. 基本設計：Evidence Block（Fenced YAML）

### 2.1 原則
- Evidence は本文中に “メモ的に” 追記できるが、**機械可読**であるべき
- そのため、Markdown中の **Fenced YAML** を Evidence Block として標準化する

### 2.2 最小フォーマット（案）
Evidence Block は、次の識別子で開始する：

```markdown
```yaml ideamark:evidence
...
```
```

中身は YAML mapping。未知キーは許容する（拡張前提）。

---

## 3. Evidence Block のスコープ（どこに付けられるか）

v1.0.2 では以下のスコープに付与できることを想定する（すべて任意）。

- **Document-level**：文書全体の先頭（ヘッダ直後）または末尾
- **Section-level**：各 Section の本文直下
- **Entity-level**：Entity 定義ブロックに併設（Registry/Entities 近傍）
- **Occurrence-level**：Occurrence 定義ブロックに併設

※ 「どこに付けてもよい」を優先し、厳密な位置制約は強めない。  
※ ツールは scope を明示して出力し、挿入先を選べるようにする（後述）。

---

## 4. Evidence Block の推奨スキーマ（拡張可能）

### 4.1 コア（推奨）
```yaml
kind: "diff-metric"           # 種別（例：diff-metric / profile / query-result / lint-report）
id: "ev-20260222-001"         # 文書内一意（任意だが推奨）
scope: "section"              # document|section|entity|occurrence
target:
  section_id: "SEC-012"       # 任意（scopeに応じて）
  entity_id: null
  occurrence_id: null

produced_by:
  tool: "ideamark"
  command: "diff"
  plugin: "anchorage.transition"
  tool_version: "0.9.13"      # 任意
produced_at: "2026-02-22T00:00:00Z"

inputs:
  left_ref: "git:...#v0.9.12" # 任意（比較や集計の入力）
  right_ref: "git:...#v0.9.13"
  window:
    from: "2026-02-01"
    to: "2026-02-22"

metrics:
  - name: "anchorage.transition_freq.delta"
    value:
      top_changes:
        - from: "view:background"
          to: "view:hypothesis"
          delta: +4
        - from: "view:hypothesis"
          to: "view:experiment"
          delta: -2
    units: "count"

notes:
  human: "仮説→実験の遷移が減り、背景→仮説が増えた。議論フェーズの前倒しが起きている可能性。"
limits:
  computed_on_demand: true
  completeness: "partial"     # partial|full|unknown
```

### 4.2 設計ポイント
- **produced_by / produced_at / inputs**：再現性と信頼性の足場
- **metrics**：プラグインが自由に増やせる（固定しない）
- **notes.human**：人間向け解釈はここに寄せられる（本文に散らさない）
- **limits**：オンデマンド計算であること・部分性を明示

---

## 5. “重い結果”の扱い：Evidence Ref（外部参照）

全文書や巨大な集計結果を埋め込むと肥大化する。  
そのため Evidence Block は、必要なら外部アーティファクトへ参照できる。

```yaml
kind: "query-result"
id: "ev-refs-001"
scope: "entity"
target:
  entity_id: "IE-001"
produced_by:
  tool: "ideamark"
  command: "query"
produced_at: "2026-02-22T00:00:00Z"
artifact_ref:
  uri: "artifact:ideamark/evidence/ev-refs-001.ndjson"
  digest: "sha256:..."
summary:
  statement: "このEntityは他文書 134,587 件で参照されている"
  value: 134587
  units: "docs"
limits:
  computed_on_demand: true
```

※ `artifact_ref.uri` のスキームは将来拡張（file/http/git/artifactなど）。  
v1.0.2 では **参照できる**ことだけを方針化し、解決方法はツールに委ねる。

---

## 6. Doc CLI 標準への影響（最低限）

ここは「派生手段（複数バージョン比較、和集合、共通項抽出…）」を拘束しない設計にする。  
代わりに **結果の出力と付加（attach）**の標準だけを追加する。

### 6.1 共通オプション案（diff / profile / query / lint 等に横断）
- `--emit-evidence {yaml|ndjson}`  
  - Evidence Block（yaml）または NDJSON（大量向け）で結果を stdout に出す
- `--evidence-scope {document|section|entity|occurrence}`
- `--evidence-target <id>`（例：`SEC-012`, `IE-001`）
- `--attach <file|->`  
  - 入力文書へ Evidence Block を挿入した改訂版を出力（stdoutへ）
  - 破壊的編集を避け、**入出力は常にファイルとして扱う**（publish思想と整合）
- `--artifact-out <path>`  
  - 大きい結果を外部アーティファクトとして書き出し、Evidence Block は参照だけ残す

※ capabilities で「attach対応」「artifact出力対応」などを宣言可能にする。

### 6.2 validate との関係
- Evidence Block は未知フィールドを含むため、**validate は拒否しない**。  
- ただし “Fenced YAML として壊れている” 場合は構文エラーになり得る。

---

## 7. v1.0.2 の合意として書ける最小要件（案）

- IdeaMark 文書は、Markdown 中に `yaml ideamark:evidence` の Evidence Block を含んでよい（MAY）。
- Evidence Block は拡張前提で、未知キーを許可する（MUST NOT fail）。
- Evidence Block は `produced_by` / `produced_at` / `inputs` を推奨する（SHOULD）。
- Doc CLI は Evidence を `--emit-evidence` で出力でき、`--attach` で文書に付加できることが望ましい（SHOULD）。

---

## 8. 例：Entity参照数をオンデマンド付加する

```bash
ideamark query refs --entity IE-001 --emit-evidence yaml --evidence-scope entity --evidence-target IE-001 \
  --artifact-out evidence/IE-001-refs.ndjson \
| ideamark diff --attach - in.ideamark.md > out.ideamark.md
```

（コマンド名や細部は仮。ここでは “attach/emit-evidence/artifact-out” の概念を示す。）

---

End of draft.
