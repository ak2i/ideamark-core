# IdeaMark YAML Specification v1.0.2

IdeaMark 文書に埋め込む YAML ブロックの仕様。

-----

## 1. 概要

### 1.1 目的

IdeaMark は Markdown 文書に構造化メタデータを埋め込むことで、以下を実現する：

- 機械的に処理可能な知識の構造化
- 人間が読める自然言語文書としての可読性
- AI による構造化・非構造化両方の情報活用

### 1.2 設計原則

1. **実体と参照の分離**: Entity / Occurrence / Section は実体として定義し、参照で構成する
1. **意味は読み方で発生**: Entity 自体は中立、anchorage と role で意味が付与される
1. **3層構造**: Entity（内容）→ Occurrence（出現）→ Section（文脈）
1. **ストリーム処理対応**: provisional / confirmed による状態管理

### 1.3 YAML ブロックの配置

YAML は Markdown の fenced code block として埋め込む：

```markdown
# 文書タイトル

```yaml
ideamark_version: 1
doc_id: "..."
# ... 以下仕様に従う
```

本文のテキスト...
```



### 1.4 v1.0.2 の変更点（要約）

- **テンプレート参照**を明確化：Header に `template`（optional）を追加し、`refs.sources[].role` に `template` を追加。
- **検証ルール**を追加：`header_singleton` / `yaml_parseable` / `id_unique_within_doc` を必須検証に追加。
- DocType は抽象語彙のまま維持し、具体的な作成プロセスや文書形（例：WorkCell）は **template で表現**することを推奨。

-----

## 2. Document（文書）

### 2.1 Header（必須）

```yaml
ideamark_version: 1                    # 必須: 固定値
doc_id: string                         # 必須: 文書の一意識別子
doc_type: DocType                      # 必須: 文書種別
status: DocStatus                      # 必須: 文書状態
created_at: timestamp                  # 必須: 作成日時 (ISO 8601)
updated_at: timestamp                  # 必須: 更新日時 (ISO 8601)
lang: string                           # 必須: 言語コード (BCP 47)
template: TemplateRef                 # optional: 生成に利用したテンプレート参照（doc_typeは抽象語彙のまま）
```

#### DocType

|値         |説明                  |
|----------|--------------------|
|`source`  |元文書（論文、報告書、外部資料の構造化）|
|`derived` |派生文書（操作により生成）       |
|`evolving`|進行中文書（議論、作業中）       |
|`pattern` |パターン文書（再利用可能な抽象構造）  |

#### DocStatus

|値            |説明 |
|-------------|---|
|`in_progress`|作業中|
|`paused`     |中断 |
|`completed`  |完了 |

### 2.2 Refs（文書間参照、optional）

```yaml
refs:
  sources:                             # 素材・入力として参照
    - id: string                       # 必須: この文書内での短縮ID
      uri: string                      # 必須: 参照先 URI
      role: SourceRole                 # 必須: 参照の役割
      description: string              # optional: 説明
      accessed_at: timestamp           # optional: 参照時点

  derived_from:                        # この文書の生成元
    - uri: string                      # 必須: 参照先 URI
      operation: DerivationOp          # 必須: 操作種別
      at: timestamp                    # optional: 操作実行時点
      description: string              # optional: 説明

  continues:                           # 継続元（単一）
    uri: string                        # 必須: 参照先 URI
    at_section: string                 # optional: 継続開始 Section
    at_entity: string                  # optional: 継続開始 Entity
    description: string                # optional: 説明

  supersedes:                          # 置換した文書
    - uri: string                      # 必須: 参照先 URI
      reason: string                   # optional: 置換理由

  related:                             # 関連文書
    - uri: string                      # 必須: 参照先 URI
      relation: RelationType           # 必須: 関連種別
      description: string              # optional: 説明

  parent:                              # 親文書（詳細文書の場合、単一）
    uri: string                        # 必須: 親 Document の URI
    entity: entity_ref                 # optional: どの Entity の詳細か
    occurrence: occurrence_ref         # optional: どの Occurrence の詳細か
    section: section_ref               # optional: どの Section の詳細か
    relation: DetailRelation           # 必須: 関係種別
```

#### SourceRole

|値                  |説明       |
|-------------------|---------|
|`source_material`  |素材として参照  |
|`background`       |背景情報として参照|
|`template`         |テンプレートとして参照|
|`comparison_target`|比較対象として参照|
|`evidence`         |根拠として参照  |



#### TemplateRef（テンプレート参照）

テンプレートから生成・編集された文書は、Header の `template`（optional）でテンプレート情報を保持できる。
パスが不明な場合でも、`file` に **テンプレートファイル名のみ**を記録して追跡できる。

```yaml
template:
  id: string                           # optional: template_id（分かる場合）
  name: string                         # optional: テンプレート名
  version: string                      # optional: テンプレートバージョン
  uri: string                          # optional: 参照URI（相対/ideamark://docs/外部URL）
  file: string                         # optional: パス不明時のファイル名（例: Decision6-WorkCell.ideamark.template.md）
  description: string                  # optional: 何をテンプレートとして使ったか
```

推奨：テンプレート文書そのものは `refs.sources` にも `role: template` として記録し、監査・来歴の追跡性を担保する。

#### DerivationOp

|値           |説明           |
|------------|-------------|
|`extraction`|抽出（別ドメインへの転用）|
|`breakdown` |分割           |
|`convergent`|統合           |
|`synthesis` |合成（チャット等から生成）|
|`refinement`|精緻化          |

#### RelationType

|値             |説明  |
|--------------|----|
|`similar`     |類似  |
|`contrast`    |対照  |
|`prerequisite`|前提知識|
|`follow_up`   |発展  |

### 2.3 Detail Document References

Entity / Occurrence / Section から詳細文書を参照できる。

```yaml
detail_doc: DetailDocRef               # optional: 単一参照
detail_docs: [DetailDocRef, ...]       # optional: 複数参照
```

#### DetailDocRef

```yaml
detail_doc:
  uri: string                          # 必須: 詳細 Document の URI
  relation: DetailRelation             # 必須: 関係種別
  summary: string                      # optional: 要約（人間向け）
  covers: [cover_ref, ...]             # optional: 対象範囲
```

#### DetailRelation

|値           |説明       |
|------------|----------|
|`elaborates`|詳細化する   |
|`discusses` |議論する    |
|`implements`|実装する    |
|`evidences` |根拠を示す   |
|`explores`  |探索する    |
|`decomposes`|分解する    |

### 2.4 URI スキーム

```
ideamark://docs/{doc_id}                       # Document
ideamark://docs/{doc_id}#/entities/{id}        # Entity
ideamark://docs/{doc_id}#/occurrences/{id}     # Occurrence
ideamark://docs/{doc_id}#/sections/{id}        # Section

# 相対参照
./other-doc.ideamark.md
./other-doc.ideamark.md#/entities/IE-001

# 外部参照
https://example.com/ideamark/docs/xxx.yaml
```

-----

## 3. Entity（実体）

### 3.1 Entities Registry

```yaml
entities:
  {entity_id}:                         # ID は IE- プレフィックス推奨
    # 実体定義
    kind: EntityKind                   # 必須: 種別
    content: string                    # 必須: 内容
    atomic_state: boolean              # optional: 分割停止フラグ (default: false)
    content_lang: string               # optional: content の言語 (default: doc の lang)
    children: [entity_ref, ...]        # optional: 子 Entity への参照
    measure_type: MeasureType          # optional: 測度タイプ（観測系で使用）
    provenance: Provenance             # optional: 出自情報
    transfer_context: TransferContext  # optional: 転用文脈（transfer 系 kind で使用）
    supersedes: entity_ref             # optional: 置換した Entity
    superseded_by: entity_ref          # optional: 置換された Entity
    detail_doc: DetailDocRef           # optional: 詳細 Document 参照（単一）
    detail_docs: [DetailDocRef, ...]   # optional: 詳細 Document 参照（複数）
    
  {entity_id}:
    # 外部参照
    ref: uri                           # 外部 Entity への参照
    cache:                             # optional: オフライン用キャッシュ
      kind: EntityKind
      content: string
```

### 3.2 EntityKind

#### 基本種別

|値            |説明       |
|-------------|---------|
|`problem`    |課題・問題点   |
|`hypothesis` |仮説・推測    |
|`measure`    |施策・対策    |
|`mechanism`  |仕組み・メカニズム|
|`evidence`   |根拠・事実    |
|`observation`|観測データ    |
|`risk`       |リスク・懸念   |
|`constraint` |制約条件     |
|`context`    |文脈・背景    |
|`stakeholder`|関係者      |
|`metric`     |評価指標     |
|`decision`   |決定事項     |
|`outcome`    |結果・成果    |

#### パターン・転用系

|値                    |説明                            |
|---------------------|------------------------------|
|`pattern`            |再利用可能な抽象パターン                  |
|`transfer_hypothesis`|異ドメイン転用の仮説                    |
|`transfer_risk`      |転用時のリスク **（extraction 操作で必須）**|

#### 構造系

|値                      |説明                   |
|-----------------------|---------------------|
|`structural_hypothesis`|構造についての仮説（トピック、フェーズ等）|
|`decision_package`     |意思決定のまとまり            |
|`summary`              |要約                   |

### 3.3 MeasureType（観測・指標系で使用）

|値        |説明      |例          |
|---------|--------|-----------|
|`count`  |離散カウント  |件数、人数      |
|`flow`   |期間合計    |売上/月、入場者数/日|
|`stock`  |時点残高    |在庫、会員数     |
|`share`  |比率 (0-1)|満足度、認知率    |
|`state`  |離散状態    |施行前/後、フェーズ |
|`quality`|定性的状態   |良/悪、高/低    |

### 3.4 Provenance（出自情報）

```yaml
provenance:
  type: ProvenanceType                 # 必須: 出自種別
  sources: [uri, ...]                  # optional: 元となった参照
  model: string                        # optional: AI モデル名
  prompt_hash: string                  # optional: プロンプトハッシュ
  created_by: string                   # optional: 作成者ID
```

#### ProvenanceType

|値            |説明       |
|-------------|---------|
|`extracted`  |既存文書から抽出 |
|`authored`   |人間が直接記述  |
|`generated`  |AI が生成   |
|`synthesized`|複数ソースから統合|

### 3.5 TransferContext（転用文脈）

```yaml
transfer_context:
  source_domain: string                # 必須: 転用元ドメイン
  target_domain: string                # 必須: 転用先ドメイン
  mapping_type: MappingType            # 必須: マッピング種別
```

#### MappingType

|値           |説明      |
|------------|--------|
|`analogical`|類推的マッピング|
|`structural`|構造的マッピング|
|`direct`    |直接適用    |

-----

## 4. Occurrence（出現）

### 4.1 Occurrences Registry

```yaml
occurrences:
  {occurrence_id}:                     # ID は OCC- プレフィックス推奨
    entity: entity_ref                 # 必須: Entity への参照
    role: OccurrenceRole               # 必須: この出現での役割
    status: OccurrenceStatus           # 必須: 状態
    target: entity_ref                 # optional: role の対象 Entity
    attribution: Attribution           # optional: 帰属情報
    derived_from: DerivedFrom          # optional: 派生元情報
    supporting_evidence: [entity_ref]  # optional: 根拠となる Entity
    timestamp: timestamp               # optional: 出現時刻
    detail_doc: DetailDocRef           # optional: 詳細 Document 参照（単一）
    detail_docs: [DetailDocRef, ...]   # optional: 詳細 Document 参照（複数）
```

### 4.2 OccurrenceRole

#### 基本役割

|値                 |説明       |
|------------------|---------|
|`problem_core`    |中心的な問題   |
|`context`         |文脈・背景    |
|`mechanism`       |仕組み・手段   |
|`evidence`        |根拠       |
|`conclusion`      |結論       |
|`observation_at_t`|時点 t での観測|

#### 関係的役割

|値          |説明     |
|-----------|-------|
|`addresses`|～に対処する |
|`supports` |～を支持する |
|`contrasts`|～と対立する |
|`refines`  |～を精緻化する|
|`risks`    |～のリスク  |
|`enables`  |～を可能にする|
|`requires` |～を必要とする|

#### 転用関連

|値                    |説明     |
|---------------------|-------|
|`source_pattern`     |転用元パターン|
|`transfer_hypothesis`|転用仮説   |
|`transfer_risk`      |転用リスク  |
|`target_application` |転用先での適用|

#### 構造仮説関連

|値                 |説明         |
|------------------|-----------|
|`topic_focus`     |トピックの焦点    |
|`phase_hypothesis`|フェーズについての仮説|
|`stance`          |立場・スタンス    |

#### 因果・時系列関連

|値              |説明       |
|---------------|---------|
|`cause`        |原因       |
|`effect`       |結果       |
|`trigger`      |状態遷移のきっかけ|
|`precondition` |前提条件     |
|`postcondition`|事後条件     |

### 4.3 OccurrenceStatus

```yaml
status:
  state: StatusState                   # 必須: 状態
  confidence: number                   # optional: 確信度 (0.0-1.0)
  confirmed_at: timestamp              # optional: 確定時刻
  confirmed_by: ConfirmationMethod     # optional: 確定方法
  awaiting: string                     # optional: 待機中の条件（provisional 時）
```

#### StatusState

|値            |説明         |
|-------------|-----------|
|`provisional`|暫定（未確定）    |
|`confirmed`  |確定済み       |
|`superseded` |置換された      |
|`rejected`   |棄却された      |
|`active`     |有効（構造仮説で使用）|

#### ConfirmationMethod

|値                     |説明            |
|----------------------|--------------|
|`user_explicit`       |ユーザーが明示的に承認   |
|`time_elapsed`        |時間経過による自動確定   |
|`subsequent_reference`|後続入力が参照したことで確定|
|`batch_review`        |バッチ処理での確定     |

### 4.4 Attribution（帰属情報）

```yaml
attribution:
  contributor: string                  # 必須: 貢献者ID
  source_utterance: string             # optional: 元発言ID（チャットの場合）
  generated_by: GeneratedBy            # optional: 生成方法
  reviewed_by: string                  # optional: レビュー者ID
  reviewed_at: timestamp               # optional: レビュー時刻
```

#### GeneratedBy

|値          |説明           |
|-----------|-------------|
|`human`    |人間が作成        |
|`small_llm`|Small LLM が生成|
|`large_llm`|Large LLM が生成|

### 4.5 DerivedFrom（派生元情報）

```yaml
derived_from:
  entity: entity_ref                   # 必須: 派生元 Entity
  operation: DerivationOp              # 必須: 操作種別
```

-----

## 5. Section（セクション）

### 5.1 Sections Registry

```yaml
sections:
  {section_id}:                        # ID は SEC- プレフィックス推奨
    anchorage: Anchorage               # 必須: 読み方の指定
    occurrences: [occurrence_ref]      # 必須: Occurrence への参照リスト
    source_session: string             # optional: 元セッションID
    timestamp_range: TimestampRange    # optional: 時間範囲
    detail_doc: DetailDocRef           # optional: 詳細 Document 参照（単一）
    detail_docs: [DetailDocRef, ...]   # optional: 詳細 Document 参照（複数）
```

### 5.2 Anchorage（読み方の指定）

```yaml
anchorage:
  view: ViewType                       # 必須: 観点
  phase: PhaseType                     # 必須: フェーズ
  domain: [string, ...]                # optional: ドメインタグ
  temporality: TemporalityType         # optional: 時間的性質
  snapshot_at: timestamp               # optional: スナップショット時点
```

#### ViewType

|値                      |説明           |
|-----------------------|-------------|
|`problem`              |問題として読む      |
|`solution`             |解決策として読む     |
|`comparison`           |比較として読む      |
|`discussion`           |議論として読む      |
|`decision`             |意思決定として読む    |
|`background`           |背景情報として読む    |
|`structural_hypothesis`|構造仮説として読む    |
|`observation_series`   |観測時系列として読む   |
|`causal_network`       |因果ネットワークとして読む|
|`state_transition`     |状態遷移として読む    |
|`event_sequence`       |イベント列として読む   |

#### PhaseType

|値            |説明  |
|-------------|----|
|`hypothesis` |仮説段階|
|`exploration`|探索段階|
|`plan`       |計画段階|
|`outcome`    |結果段階|
|`confirmed`  |確定段階|
|`evolving`   |進行中 |

#### TemporalityType

|値         |説明        |
|----------|----------|
|`snapshot`|この時点での確定状態|
|`evolving`|変化しうる状態   |

### 5.3 TimestampRange

```yaml
timestamp_range:
  from: timestamp                      # 必須: 開始時刻
  to: timestamp                        # 必須: 終了時刻
```

-----

## 6. Relations（Entity 間の関係）

### 6.1 Relations List

```yaml
relations:
  - type: RelationTypeValue            # 必須: 関係種別
    from: entity_ref                   # 必須: 起点 Entity
    to: entity_ref                     # 必須: 終点 Entity
    temporal_kernel: TemporalKernel    # optional: 時間カーネル
    note: string                       # optional: 説明
```

### 6.2 RelationTypeValue

#### 論理的関係

|値              |説明    |
|---------------|------|
|`supports`     |支持する  |
|`contrasts`    |対立する  |
|`refines`      |精緻化する |
|`generalizes`  |一般化する |
|`derives_from` |～から派生 |
|`is_example_of`|～の例である|

#### 操作的関係

|値                |説明    |
|-----------------|------|
|`operationalizes`|具体化する |
|`requires`       |必要とする |
|`enables`        |可能にする |
|`risks`          |リスクとなる|
|`mitigates`      |軽減する  |
|`measures`       |測定する  |

#### 因果・時系列関係

|値             |説明     |
|--------------|-------|
|`causes`      |原因となる  |
|`influences`  |影響する   |
|`follows`     |時系列的に続く|
|`triggers`    |誘発する   |
|`evolves_from`|進化する   |
|`supersedes`  |置換する   |

### 6.3 TemporalKernel（時間カーネル）

```yaml
temporal_kernel:
  delay: DelaySpec                     # optional: 遅延
  duration: DurationSpec               # optional: 持続
  strength: StrengthSpec               # optional: 強度
  nonlinearity: NonlinearityType       # optional: 非線形性
```

#### DelaySpec

```yaml
delay:
  estimate: DelayEstimate              # 必須: 粗い推定
  distribution: DistributionType       # optional: 分布種別
  p10: number                          # optional: 10パーセンタイル
  p50: number                          # optional: 50パーセンタイル
  p90: number                          # optional: 90パーセンタイル
  unit: TimeUnit                       # optional: 時間単位
```

#### DelayEstimate

|値          |説明 |
|-----------|---|
|`immediate`|即時 |
|`days`     |数日 |
|`weeks`    |数週間|
|`months`   |数ヶ月|
|`years`    |数年 |
|`decades`  |数十年|

#### DurationSpec

```yaml
duration:
  estimate: DurationEstimate           # 必須: 粗い推定
  decay: DecayType                     # optional: 減衰種別
```

#### DurationEstimate

|値          |説明 |
|-----------|---|
|`transient`|一時的|
|`sustained`|持続的|
|`permanent`|恒久的|

#### DecayType

|値        |説明    |
|---------|------|
|`sharp`  |急激に減衰 |
|`gradual`|緩やかに減衰|
|`none`   |減衰なし  |

#### StrengthSpec

```yaml
strength:
  estimate: StrengthEstimate           # 必須: 粗い推定
  elasticity: number                   # optional: 弾性値
  confidence: number                   # optional: 確信度 (0.0-1.0)
```

#### StrengthEstimate

|値         |説明 |
|----------|---|
|`weak`    |弱い |
|`moderate`|中程度|
|`strong`  |強い |

#### NonlinearityType

|値           |説明   |
|------------|-----|
|`linear`    |線形   |
|`threshold` |閾値効果 |
|`saturation`|飽和効果 |
|`s_curve`   |S字カーブ|

#### DistributionType

|値          |説明    |
|-----------|------|
|`lognormal`|対数正規分布|
|`gamma`    |ガンマ分布 |
|`weibull`  |ワイブル分布|
|`fixed`    |固定値   |

#### TimeUnit

|値       |説明|
|--------|--|
|`days`  |日 |
|`weeks` |週 |
|`months`|月 |
|`years` |年 |

-----

## 7. Structure（文書構成）

### 7.1 Structure Block

```yaml
structure:
  sections:                            # 必須: Section の順序付きリスト
    - section_ref                      # Section ID への参照
    - section_ref
```

-----

## 8. Continuation（継続処理用、optional）

`doc_type: evolving` の場合に使用。

```yaml
continuation:
  last_processed_at: timestamp         # 必須: 最終処理時刻
  open_threads:                        # optional: 未解決の議論スレッド
    - string
  suggested_next:                      # optional: 次に検討すべき事項
    - string
  pending_decisions:                   # optional: 保留中の判断
    - question: string                 # 必須: 問い
      options: [string, ...]           # optional: 選択肢
      discussed_in: [entity_ref]       # optional: 関連 Entity
```

-----

## 9. インライン記述

冗長さを避けるため、以下のインライン記述を許可する。

### 9.1 Occurrence 内での Entity インライン

```yaml
occurrences:
  OCC-001:
    entity: "IE-001"                   # 参照形式
    role: "problem_core"
    
  OCC-002:
    inline:                            # インライン形式
      kind: "observation"
      content: "2025年の入場者数は過去最高"
    role: "evidence"
    status:
      state: "confirmed"
```

### 9.2 Section 内での Occurrence インライン

```yaml
sections:
  SEC-001:
    anchorage:
      view: "problem"
      phase: "confirmed"
    occurrences:
      - ref: "OCC-001"                 # 参照形式
      - entity: "IE-002"               # 簡易インライン（Entity 参照 + 最小属性）
        role: "context"
        status:
          state: "confirmed"
```

-----

## 10. 検証ルール

### 10.1 必須検証

|ルール                       |説明                              |
|--------------------------|--------------------------------|
|`header_required`         |Header の必須フィールドが存在すること          |
|`header_singleton`        |Document Header の YAML ブロックが 1 つであること（複数は error）|
|`yaml_parseable`          |すべての fenced `yaml` が YAML としてパース可能であること|
|`id_unique_within_doc`    |entity_id / occurrence_id / section_id が文書内で一意であること|
|`entity_ref_valid`        |Entity 参照が解決可能であること             |
|`occurrence_ref_valid`    |Occurrence 参照が解決可能であること         |
|`section_ref_valid`       |Section 参照が解決可能であること            |
|`structure_sections_exist`|structure.sections の参照がすべて存在すること|
|`detail_doc_ref_valid`    |detail_doc/detail_docs の必須項目が存在すること|
|`detail_doc_cover_ref_valid`|detail_doc.covers の参照が解決可能であること|
|`parent_ref_valid`        |refs.parent の必須項目が存在すること         |

### 10.2 Extraction 検証（–strict モード）

|ルール                     |説明                                                                             |
|------------------------|-------------------------------------------------------------------------------|
|`transfer_risk_required`|`derived_from.operation: extraction` の場合、`kind: transfer_risk` の Entity が最低1つ必要|

-----

## 11. 型定義サマリ

```
timestamp     = ISO 8601 形式の日時文字列
entity_ref    = string (Entity ID または URI)
occurrence_ref = string (Occurrence ID)
section_ref   = string (Section ID)
cover_ref     = entity_ref | occurrence_ref | section_ref
uri           = string (IdeaMark URI または URL)
number        = 数値 (整数または浮動小数点)
boolean       = true | false
```

-----

## 12. バージョン履歴

|バージョン|日付        |変更内容|
|-----|----------|----|
|1    |2026-01-16|初版  |

-----

*IdeaMark Project | 2026年1月*


-----

## 13. Evidence YAML Handling（v1.0.2）


### 13.0 ノート（哲学）

Evidence Block は文書の意味内容を拘束しない注釈であり、
refs/sources 等の来歴宣言と独立である（矛盾を許容する）。
実装は既定で Evidence Block を diff 対象から除外することが望ましい。


### 13.1 識別

`yaml ideamark:evidence` と識別される fenced YAML ブロックは Evidence Block として扱う。

### 13.2 Validation

- 内容が YAML mapping/object であることを検証してよい（MAY）
- 未知キーを理由に validation failure してはならない（MUST NOT）

### 13.3 Diff Interaction

- diff 実装は既定で Evidence Block を比較対象から除外することが望ましい（SHOULD）
- `--include-evidence` 等のオプションで比較対象に含めることを許可してよい（MAY）



-----

## 付記: v1.0.2 変更点（2026-02-22）

- Evidence Block 対応
- validation における未知キー許容の明示
- diff との相互運用方針追加
