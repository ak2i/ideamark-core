---
ideamark_version: 1
template_id: "imtpl.detail.security"
template_name: "Detail Security Template"
template_version: "1.0.0"
description: "WorkCell Integration Spec / Service Flow / Decision6 を入力として、鍵管理・権限・PII・監査を定義するテンプレート。"
domain: ["software-design", "security", "workcell"]
tags: ["detail", "security", "privacy", "audit"]
lang: "ja-JP"
status: stable
created_at: "2026-01-09"
---

# Detail Security Template

本テンプレートは、WorkCellのセキュリティ仕様を **「フロー・統合仕様・意思決定」から導出**するためのもの。

---

## Slot: Provenance（参照元の明確化）【必須】

```yaml
provenance:
  security_spec_id: "<stable id, e.g. sec.relatea.v1>"
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

## Slot: Security Context（前提）【必須】

```yaml
security_context:
  actors:
    - "end-user"
    - "operator"
  threat_model:
    - "token leakage"
    - "unauthorized access"
```

---

## Slot: Secrets & Key Management（秘密情報）【必須】

```yaml
secrets:
  allowed:
    - "anon key"
  forbidden:
    - "service_role key"
  storage:
    - "secure storage for refresh_token"
```

---

## Slot: Authorization & Policies（権限）【必須】

```yaml
authorization:
  model: "RLS"
  rules:
    - "auth.uid() = owner_id"
```

---

## Slot: PII & Data Handling（PII）【必須】

```yaml
pii:
  allowed_in_logs: false
  masking:
    - "email -> hash"
```

---

## Slot: Audit & Compliance（監査）【推奨】

```yaml
audit:
  events:
    - "event.auth.session.established"
  retention: "P90D"
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
