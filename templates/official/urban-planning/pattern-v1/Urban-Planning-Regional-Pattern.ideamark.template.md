---
ideamark_version: 1
template_id: "imtpl.pattern.urban_planning"
template_name: "Urban Planning Regional Pattern Template"
template_version: "1.0.0"
description: "都市計画・まちづくりの課題を整理し、施策や運用設計へ接続するテンプレート。"
domain: ["urban-planning", "regional-innovation"]
tags: ["pattern", "urban", "planning", "problem-solution"]
lang: "ja-JP"
status: draft
created_at: "2026-01-08"
---

# Urban Planning Regional Pattern Template

本テンプレートは、都市計画・まちづくりの課題を「文脈・課題・解決・スケール条件」で整理し、
施策・運用・協働体制の設計へつなげるための最小構造を提供する。

---

## Template Scope

### Suitable for
- 商業・居住・交通の複合課題整理
- 都市機能の再配置や運用改善
- 事業化や合意形成の前段整理

### Not responsible for
- 建築/土地区画の詳細設計
- 詳細な財政計画
- 具体的な施工計画

---

## Pattern Core (Required)
```yaml
id: "<IdeaMark-...>"
title: "<pattern title>"
type: "<pattern type>"
context:
  - "<背景/環境>"
problem:
  summary: "<解決したい課題>"
solution:
  approach: "<解決アプローチ>"
metadata:
  tags: []
  scalefactor:
    timewindow: "<導入/効果の時間軸>"
    spacemetrics: "<空間スケール>"
    regions: []
    organizations: []
access:
  uri: "<source or reference>"
  visibility: "public"
```

---

## Urban Assets & Functions
```yaml
urban_assets:
  key_functions: ["<商業/居住/福祉/交流>"]
  spatial_unit: "<街区/地区/広域>"
  underused_assets: ["<空き店舗/公共施設>"]
```
- 主要機能と資産の状況を整理する

---

## Mobility & Logistics
```yaml
mobility:
  modes: ["<公共交通/徒歩/自転車>"]
  bottlenecks: ["<混雑/アクセス課題>"]
```
- 交通や回遊性の制約を明示する

---

## Stakeholders & Governance
```yaml
stakeholders:
  - name: "<主体>"
    role: "<役割>"
policy_constraints: ["<規制/制度>"]
```
- 合意形成や制度条件を可視化する

---

## Impact & Metrics (Optional)
```yaml
impact:
  outcomes: ["<目標成果>"]
  metrics:
    - name: "<指標名>"
      definition: "<定義>"
      unit: "<単位>"
```
- 来訪/売上/居住満足などの評価軸に使う
