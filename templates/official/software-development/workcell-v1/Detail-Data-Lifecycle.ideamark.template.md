---
ideamark_version: 1
template_id: "imtpl.detail.data_lifecycle"
template_name: "Detail Data Lifecycle Template"
template_version: "1.0.0"
description: "WorkCell Integration Spec / Service Flow / Decision6 を入力として、保持期間・削除・アーカイブを定義するテンプレート。"
domain: ["software-design", "data", "workcell"]
tags: ["detail", "data-lifecycle", "retention", "deletion"]
lang: "ja-JP"
status: stable
created_at: "2026-01-09"
---

# Detail Data Lifecycle Template

本テンプレートは、WorkCellのデータ保持/削除/アーカイブを **「フロー・統合仕様・意思決定」から導出**するためのもの。

---

## 0. Provenance（参照元の明確化）【必須】

```yaml
provenance:
  lifecycle_spec_id: "<stable id, e.g. lifecycle.relatea.v1>"
  created_by: "<human or tool>"
  created_at: "<ISO-8601 datetime>"
  method: "manual|engine|hybrid"
  based_on:
    integration_spec:
      - doc_id: "<integ doc_id>"
        template_ref: "<template ref>"
        locator: "<path/uri>"
        content_hash: "<optional sha256>"
    decision6:
      - doc_id: "<decision6 doc_id>"
        template_ref: "<template ref>"
        locator: "<path/uri>"
        content_hash: "<optional sha256>"
  notes: []
```

---

## 1. Lifecycle Policy（ポリシー）【必須】

```yaml
lifecycle_policy:
  - entity: "event_log"
    retention: "P90D"
    action: "archive"
  - entity: "storage.private"
    retention: "P365D"
    action: "delete"
```

---

## 2. Deletion & Export（削除/エクスポート）【推奨】

```yaml
deletion:
  - trigger: "user.request"
    scope: ["user_data", "storage_objects"]
export:
  - trigger: "user.request"
    format: ["json", "csv"]
```

---

## 3. References（参照）【必須】

```yaml
refs:
  - id: "ref.integration"
    kind: "ideamark_doc"
    title: "WorkCell Integration Spec"
    locator: "<integ-doc-uri>"
```
