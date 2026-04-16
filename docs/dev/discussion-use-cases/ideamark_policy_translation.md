# IdeaMark Document: 課題変換と政策接続パターン

```yaml
ideamark_version: 1
doc_id: "ideamark.pattern.policy-translation.2026-04-17"
doc_type: "pattern"
status: "in_progress"
created_at: "2026-04-16T23:02:32.435638"
updated_at: "2026-04-16T23:02:32.435656"
lang: "ja-JP"
```

## Section 001 : 問題認識（課題変換の必要性）
```yaml
section_id: "SEC-001"
anchorage:
  view: "problem"
  phase: "confirmed"
```

### OCC-001 : 課題変換不足
```yaml
occurrence_id: "OCC-001"
entity: "IE-001"
role: "problem_core"
status:
  state: "confirmed"
```

日本は問題は多いが、課題に変換されていないため、施策や投資の効果が限定的になっている。

---

## Section 002 : 解決構造（前処理としての課題化）
```yaml
section_id: "SEC-002"
anchorage:
  view: "solution"
  phase: "confirmed"
```

### OCC-002 : 課題化プロセス
```yaml
occurrence_id: "OCC-002"
entity: "IE-002"
role: "mechanism"
status:
  state: "confirmed"
```

施策実行前に問題を課題に分解・構造化することで、投資効率を高める。

---

## Section 003 : 政策説明パターン
```yaml
section_id: "SEC-003"
anchorage:
  view: "decision"
  phase: "confirmed"
```

### OCC-003 : 前処理としての提案
```yaml
occurrence_id: "OCC-003"
entity: "IE-003"
role: "conclusion"
status:
  state: "confirmed"
```

「新しい政策」ではなく「既存施策の前処理」として説明することで、受容性が高まる。

---

## Entities Registry
```yaml
entities:
  IE-001:
    kind: "problem"
    content: "問題が課題に変換されていない構造的ボトルネック"
  IE-002:
    kind: "mechanism"
    content: "課題化プロセスによる投資効率の向上"
  IE-003:
    kind: "pattern"
    content: "政策説明における前処理化フレーム"
occurrences:
  OCC-001:
    entity: "IE-001"
    role: "problem_core"
    status: { state: "confirmed" }
  OCC-002:
    entity: "IE-002"
    role: "mechanism"
    status: { state: "confirmed" }
  OCC-003:
    entity: "IE-003"
    role: "conclusion"
    status: { state: "confirmed" }
sections:
  SEC-001:
    anchorage: { view: "problem", phase: "confirmed" }
    occurrences: ["OCC-001"]
  SEC-002:
    anchorage: { view: "solution", phase: "confirmed" }
    occurrences: ["OCC-002"]
  SEC-003:
    anchorage: { view: "decision", phase: "confirmed" }
    occurrences: ["OCC-003"]
structure:
  sections:
    - "SEC-001"
    - "SEC-002"
    - "SEC-003"
```
