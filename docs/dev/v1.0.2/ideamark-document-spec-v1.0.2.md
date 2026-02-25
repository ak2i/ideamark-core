# Chat Archive: ロラン・バルトの写真論

<!--- 
  Document メタ情報
  機械処理はこの YAML ブロックから開始
--->
```yaml
ideamark_version: 1
doc_id: "ideamark.concept-design.2026-01-11"
doc_type: "evolving"
status: "in_progress"
created_at: "2026-01-11"
updated_at: "2026-01-11"
lang: "ja-JP"

refs:
  sources: []
```

## Meta
```yaml
# 人間向けの補足メタ情報（任意）
started_at: 2026-01-11
participants:
  user: Akki
  assistant: ChatGPT5.2
intent: IdeaMarkの詳細な構造を決める過程
domain: [ideamark, concept-design]
```

ここに文書全体の説明を自然言語で書ける。
機械処理には影響しないが、人間や高度な AI が読む際の文脈となる。

---

## Section 001 : ロラン・バルトの写真論を思い出す
```yaml
section_id: "SEC-001"
anchorage:
  view: "background"
  phase: "exploration"
```

> **Intent**: IdeaEntity の Atomic 性を考えるにあたり、
> 「意味がどこで発生するのか」という既存理論への参照点として、
> ロラン・バルトの写真論が想起された過程を観測する。

このセクションは IdeaMark 的には：
- まだ「問題定義」ではない
- まだ「解決」でもない
- 思考が起動した瞬間の観測ログ

### OCC-001 : 問いの発生
```yaml
occurrence_id: "OCC-001"
entity: "IE-001"
role: "observation"
status:
  state: "confirmed"
  confidence: 0.9
attribution:
  contributor: "user"
  source_utterance: "turn-user-001"
```

メディア論・意味論の文脈で、「写真にキャプションを与えることで意味が発生する」
という理論を思い出そうとしたが、著者名が曖昧な状態で想起されている。

---

## Section 002 : ロラン・バルトへの同定
```yaml
section_id: "SEC-002"
anchorage:
  view: "background"
  phase: "confirmed"
```

### OCC-002 : 理論の同定
```yaml
occurrence_id: "OCC-002"
entity: "IE-002"
role: "explanation"
status:
  state: "confirmed"
```

写真と言語の関係をめぐる理論として、ロラン・バルトの「アンカラージュ／リレー」が
提示され、想起されていた関心対象が特定された。

ここで初めて `instantiates` が出てくる。理由：ここで出てきたのは
- 単なる固有名詞ではなく
- 再利用可能な概念の核

だから。
```mermaid
graph LR
  A[曖昧な記憶] --> B[バルトの同定]
  B --> C[アンカラージュ/リレー概念]
```

---

## Entities Registry
```yaml
entities:
  IE-001:
    kind: "observation"
    content: |
      メディア論・意味論の文脈で、
      「写真にキャプションを与えることで意味が発生する」
      という理論への関心が想起された。
    atomic_state: true
    provenance:
      type: "authored"
      created_by: "user"

  IE-002:
    kind: "concept"
    content: |
      画像は本来的に多義的であり、
      キャプションや説明文といった言語が付与されることで、
      その意味が特定の方向に固定・誘導される。
      
      ロラン・バルトはこれを **アンカラージュ（anchorage）** と呼び、
      言語と画像が相補的に意味を生成する関係を
      **リレー（relay）** として区別した。
    atomic_state: true
    provenance:
      type: "extracted"
      sources: ["バルト写真論"]

  IE-HYPO-001:
    kind: "structural_hypothesis"
    content: |
      この議論はIdeaMarkの設計における「意味の発生場所」を
      探索するフェーズにある。
    atomic_state: true

occurrences:
  OCC-001:
    entity: "IE-001"
    role: "observation"
    status: { state: "confirmed" }
    
  OCC-002:
    entity: "IE-002"
    role: "explanation"
    status: { state: "confirmed" }

  OCC-HYPO-001:
    entity: "IE-HYPO-001"
    role: "phase_hypothesis"
    status: { state: "active", confidence: 0.8 }

sections:
  SEC-001:
    anchorage: { view: "background", phase: "exploration" }
    occurrences: ["OCC-001"]
  SEC-002:
    anchorage: { view: "background", phase: "confirmed" }
    occurrences: ["OCC-002"]
  SEC-META:
    anchorage: { view: "structural_hypothesis", phase: "evolving" }
    occurrences: ["OCC-HYPO-001"]

relations:
  - type: "evolves_from"
    from: "IE-002"
    to: "IE-001"
    note: "曖昧な記憶から具体的概念へ"

structure:
  sections:
    - "SEC-META"
    - "SEC-001"
    - "SEC-002"
```

---

## 補足: この文書の読み方

この文書は IdeaMark の機能テストを兼ねている。
各セクションの `anchorage` を参照することで、読む観点が指定される。
```

## 設計方針の提案

### 原則

1. **YAML は機械処理の対象、Markdown 本文は人間/AI 向け**
2. **同じ情報の二重記述を避ける**: content は YAML に、説明は Markdown に
3. **Registry は文書末尾にまとめる**: 実体定義を一箇所に集約
4. **Section/Occurrence の YAML は分散配置**: 読みながら構造がわかる

### Markdown 見出しレベル

| レベル | 用途 |
|--------|------|
| `#` | Document タイトル |
| `##` | Section |
| `###` | Occurrence / Entities Registry / Relations |
| `####` | IdeaEntity 概要などのサブ構造（必要に応じて） |

### Markdown 配置パターン（推奨）

````markdown
## Section 001 : セクション名
```yaml
section_id: "SEC-001"
anchorage:
  view: "background"
  phase: "confirmed"
```

セクション全体の概要を自然言語で記述する。

### OCC-001 : 出現タイトル
```yaml
occurrence_id: "OCC-001"
entity: "IE-001"
role: "context"
status:
  state: "confirmed"
detail_doc:
  uri: "./detail-doc.ideamark.md"
  relation: "elaborates"
```
Occurrence の概要を自然言語で記述する。

#### IdeaEntity: IE-001
IdeaEntity の概要を自然言語で記述する。
````

### YAML ブロックの種類

| 位置 | 内容 | 必須/任意 |
|------|------|----------|
| 文書冒頭 | Document Header (ideamark_version, doc_id, ...) | **必須** |
| 各 Section 冒頭 | section_id, anchorage | **必須** |
| 各 Occurrence | occurrence_id, entity, role, status | **必須** |
| 文書末尾 | Entities Registry (entities, occurrences, sections, relations, structure) | **必須** |
| その他 | 補足メタ情報、人間向け構造化データ | 任意 |
| YAML 直後の Markdown | Occurrence/IdeaEntity の概要テキスト | 任意 |

### 詳細 Document 参照（optional）

Entity / Occurrence / Section に `detail_doc` または `detail_docs` を付与できる。
詳細文書側は `refs.parent` で親文書への参照を持つ。

```yaml
entities:
  IE-001:
    kind: "hypothesis"
    content: "予約制の導入が有効"
    detail_doc:
      uri: "./reservation-design.ideamark.md"
      relation: "elaborates"

refs:
  parent:
    uri: "ideamark://docs/main-plan-001"
    entity: "IE-001"
    relation: "elaborates"
```

### 機械処理の方針
```
1. 文書冒頭の YAML ブロック（ideamark_version: 1 を含む）を検出
2. 文書末尾の Entities Registry を検出（entities: キーを含む）
3. 各 ## セクション内の section_id を持つ YAML を検出
4. 各 ### 内の occurrence_id を持つ YAML を検出
5. fenced `yaml` 以外の Markdown は補足情報として無視（または LLM 用コンテキスト）
6. YAML ブロック直後の Markdown は人間向けの概要として扱い、機械処理対象外とする


-----

## 13. Evidence Block（v1.0.2）

### 13.1 概要

### 13.1.1 位置づけ（哲学）

Evidence Block は、文書の主張（meaning content）を規定・拘束するものではなく、
観測・解析・検証・クエリ等の結果を補助的に記録するための注釈である。
Evidence Block は本文構造（Section / Entity / Occurrence）と独立であり、
削除されても文書の意味内容は変化しないことを前提とする。
また、Evidence は refs/sources 等の来歴宣言と矛盾していてもよい。

IdeaMark 文書は、Doc CLI ツール（例：`ideamark diff`）が生成する統計・差分・解析結果を
**機械可読な形で埋め込むための Evidence Block** を含んでよい（MAY）。

Evidence Block は本文の意味内容を変更しない付加情報である。

### 13.2 形式

````markdown
```yaml ideamark:evidence
<YAML mapping>
```
````

- fenced 言語は `yaml` を用いる（MUST）
- info string に `ideamark:evidence` を含めること（MUST）
- 内容は YAML mapping/object であること（MUST）

### 13.3 拡張性

- 未知キーを理由に validation failure してはならない（MUST NOT）
- 同一 target に複数 Evidence Block を付与してよい（MAY）
- `id` フィールドは任意（MAY）

### 13.4 Diff における扱い

- `ideamark diff` は既定動作として Evidence Block を
  差分計算対象から除外することが望ましい（SHOULD）
- オプションで Evidence を含めた diff を許可してよい（MAY）



-----

## 付記: v1.0.2 変更点

- Evidence Block を正式導入
- diff における Evidence 除外ポリシー追加
- Evidence は拡張前提で未知キー許容
