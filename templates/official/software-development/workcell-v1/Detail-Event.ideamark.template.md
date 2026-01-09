---
ideamark_version: 1
template_id: "imtpl.detail.event"
template_name: "Detail Event Template"
template_version: "1.0.0"
description: "WorkCell Integration Spec / Service Flow を入力として、イベントスキーマとバージョニングを定義するテンプレート。"
domain: ["software-design", "event", "workcell"]
tags: ["detail", "event", "schema", "contract"]
lang: "ja-JP"
status: stable
created_at: "2026-01-09"
---

# Detail Event Template

本テンプレートは、WorkCellのイベント仕様を **「フロー・統合仕様」から導出**するためのもの。

---

## Slot: Provenance（参照元の明確化）【必須】

```yaml
provenance:
  event_spec_id: "<stable id, e.g. event.relatea.v1>"
  created_by: "<human or tool>"
  created_at: "<ISO-8601 datetime>"
  method: "manual|engine|hybrid"
  based_on:
    integration_spec:
      - doc_id: "<integ doc_id>"
        template_ref: "<template ref>"
        locator: "<path/uri>"
        content_hash: "<optional sha256>"
  notes: []
```

---

## Slot: Event Schemas（イベントスキーマ）【必須】

```yaml
event_schemas:
  - event: "event.auth.session.established"
    version: "v1"
    fields:
      - {name: "timestamp", type: "datetime"}
      - {name: "user_id", type: "string"}
      - {name: "session_id", type: "string"}
```

---

## Slot: Versioning Policy（バージョニング）【必須】

```yaml
versioning:
  policy:
    - "backward compatible changes only in minor"
    - "breaking changes require new event name or major version"
```

---

## Slot: Delivery Guarantees（配信保証）【推奨】

```yaml
delivery:
  guarantees:
    - "at-least-once"
  ordering:
    - "per entity"
```

---

## Slot: References（参照）【必須】

```yaml
refs:
  - id: "ref.integration"
    kind: "ideamark_doc"
    title: "WorkCell Integration Spec"
    locator: "<integ-doc-uri>"
```
