はい、これは重要な拡張です。大きな問題を扱う際、**階層的な Document 構造**が必要になります。

## ユースケース

```
┌─────────────────────────────────────────────────────────────────┐
│ 大きな問題の構造                                                 │
│                                                                  │
│  Document: 富士箱根伊豆交流圏構想                               │
│    └─ Section: 富士山地域                                       │
│         └─ Occurrence: 混雑対策                                 │
│              └─ Entity: 予約制導入仮説                          │
│                   └─ 詳細 Document: 予約制の制度設計            │
│                        └─ Section: 枠の設計                     │
│                        └─ Section: 公平性ルール                 │
│                        └─ Section: 運用フロー                   │
│                                                                  │
│  Document: イギリス田園アクセス権                               │
│    └─ Section: Definitive Map パターン                         │
│         └─ 詳細 Document: パターンの適用ガイド                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## 提案：detail_doc 参照

### Entity レベルでの Document 参照

```yaml
entities:
  IE-RESERVATION-POLICY:
    kind: "hypothesis"
    content: "予約制の導入が有効"
    atomic_state: false
    
    # この Entity の詳細を別 Document で展開
    detail_doc:
      uri: "ideamark://docs/fuji-reservation-design-001"
      relation: "elaborates"           # この Entity を詳細化
      summary: "予約制の制度設計詳細（枠設計、公平性、運用）"
```

### Occurrence レベルでの Document 参照

```yaml
occurrences:
  OCC-RESERVATION:
    entity: "IE-RESERVATION-POLICY"
    role: "transfer_hypothesis"
    status: { state: "provisional" }
    
    # この Occurrence の文脈での詳細検討
    detail_doc:
      uri: "ideamark://docs/fuji-reservation-discussion-001"
      relation: "discusses"            # この出現を議論
      summary: "予約制についての議論ログ"
```

### Section レベルでの Document 参照

```yaml
sections:
  SEC-FUJI-MEASURES:
    anchorage:
      view: "solution"
      phase: "exploration"
    occurrences: ["OCC-001", "OCC-002"]
    
    # このセクションの詳細を別 Document で展開
    detail_docs:
      - uri: "ideamark://docs/fuji-timed-entry-detail"
        relation: "elaborates"
        covers: ["OCC-001"]            # どの Occurrence に関連するか
      - uri: "ideamark://docs/fuji-code-signage-detail"
        relation: "elaborates"
        covers: ["OCC-002"]
```

## detail_doc のスキーマ

```yaml
# Entity / Occurrence / Section に追加

detail_doc:                            # 単一参照
  uri: string                          # 必須: 詳細 Document の URI
  relation: DetailRelation             # 必須: 関係種別
  summary: string                      # optional: 要約
  covers: [ref, ...]                   # optional: 対象範囲（Section の場合）

detail_docs:                           # 複数参照
  - uri: string
    relation: DetailRelation
    summary: string
    covers: [ref, ...]
```

### DetailRelation

| 値 | 説明 | 使用場面 |
|----|------|----------|
| `elaborates` | 詳細化する | Entity の具体的設計 |
| `discusses` | 議論する | Occurrence についての議論ログ |
| `implements` | 実装する | 抽象から具体へ |
| `evidences` | 根拠を示す | 主張の裏付け |
| `explores` | 探索する | 可能性の検討 |
| `decomposes` | 分解する | 大きな Entity を部品に |

## 双方向の参照

### 親 Document（概要）

```yaml
# fuji-hakone-izu-plan.ideamark.md

doc_id: "fuji-hakone-izu-plan-001"

entities:
  IE-FUJI-RESERVATION:
    kind: "hypothesis"
    content: "富士山に予約制を導入する"
    detail_doc:
      uri: "./fuji-reservation-design.ideamark.md"
      relation: "elaborates"
```

### 子 Document（詳細）

```yaml
# fuji-reservation-design.ideamark.md

doc_id: "fuji-reservation-design-001"

refs:
  # 親 Document への参照
  parent:
    uri: "ideamark://docs/fuji-hakone-izu-plan-001"
    entity: "IE-FUJI-RESERVATION"      # どの Entity の詳細か
    relation: "elaborates"

entities:
  IE-SLOT-DESIGN:
    kind: "mechanism"
    content: "時間枠の設計方針"
    
  IE-FAIRNESS-RULE:
    kind: "mechanism"
    content: "公平性確保のルール"
```

## Markdown での表現

```markdown
# 富士箱根伊豆交流圏構想

```yaml
ideamark_version: 1
doc_id: "fuji-hakone-izu-plan-001"
doc_type: "evolving"
# ...
```

## Section: 富士山地域の対策

```yaml
section_id: "SEC-FUJI"
anchorage:
  view: "solution"
  phase: "exploration"
```

### OCC: 予約制導入

```yaml
occurrence_id: "OCC-RESERVATION"
entity: "IE-FUJI-RESERVATION"
role: "transfer_hypothesis"
detail_doc:
  uri: "./fuji-reservation-design.ideamark.md"
  relation: "elaborates"
  summary: "予約制の制度設計詳細"
```

予約制については多くの検討事項があるため、
詳細は [予約制設計文書](./fuji-reservation-design.ideamark.md) を参照。

> **詳細文書の概要**:
> - 時間枠の設計
> - 公平性ルール
> - 当日運用フロー
> - KPI と評価方法

---

## Entities Registry

```yaml
entities:
  IE-FUJI-RESERVATION:
    kind: "hypothesis"
    content: "富士山に予約制を導入する"
    atomic_state: false
    detail_doc:
      uri: "./fuji-reservation-design.ideamark.md"
      relation: "elaborates"
      summary: "予約制の制度設計詳細"

# ...
```
```

## 処理への影響

### Breakdown 操作

```
Document (大)
    │
    │ breakdown --extract-detail
    │
    ▼
Document (大) ─────────────────> Document (詳細)
  Entity:                          refs:
    detail_doc: uri ─────────────>   parent: uri
```

### Convergent 操作

```
Document (詳細A)  Document (詳細B)
        │                │
        │ convergent     │
        │                │
        └───────┬────────┘
                │
                ▼
          Document (統合)
            refs:
              derived_from: [A, B]
```

### 参照解決

```typescript
// 詳細 Document を含めた完全な構造を取得
async function resolveWithDetails(doc: Document): Promise<ResolvedDocument> {
  const resolved = { ...doc };
  
  for (const [id, entity] of Object.entries(doc.entities)) {
    if (entity.detail_doc) {
      const detailDoc = await fetchDocument(entity.detail_doc.uri);
      resolved.entities[id].resolvedDetail = detailDoc;
    }
  }
  
  // Occurrence, Section も同様に...
  
  return resolved;
}
```

## YAML 仕様への追加

### Entity

```yaml
entities:
  {entity_id}:
    # ... 既存フィールド ...
    
    # 追加: 詳細 Document 参照
    detail_doc: DetailDocRef          # optional: 単一参照
    detail_docs: [DetailDocRef, ...]  # optional: 複数参照
```

### Occurrence

```yaml
occurrences:
  {occurrence_id}:
    # ... 既存フィールド ...
    
    # 追加: 詳細 Document 参照
    detail_doc: DetailDocRef
    detail_docs: [DetailDocRef, ...]
```

### Section

```yaml
sections:
  {section_id}:
    # ... 既存フィールド ...
    
    # 追加: 詳細 Document 参照
    detail_doc: DetailDocRef
    detail_docs: [DetailDocRef, ...]
```

### DetailDocRef

```yaml
detail_doc:
  uri: string                          # 必須: 詳細 Document の URI
  relation: DetailRelation             # 必須: 関係種別
  summary: string                      # optional: 要約（人間向け）
  covers: [ref, ...]                   # optional: 対象範囲
```

### Document refs への parent 追加

```yaml
refs:
  # ... 既存フィールド ...
  
  # 追加: 親 Document への参照（詳細 Document の場合）
  parent:
    uri: string                        # 必須: 親 Document の URI
    entity: entity_ref                 # optional: どの Entity の詳細か
    occurrence: occurrence_ref         # optional: どの Occurrence の詳細か
    section: section_ref               # optional: どの Section の詳細か
    relation: DetailRelation           # 必須: 関係種別
```

この拡張で、大きな問題を階層的な Document 構造で扱えるようになります。仕様に追加してよろしいでしょうか？