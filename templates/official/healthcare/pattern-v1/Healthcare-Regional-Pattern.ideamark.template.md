---
ideamark_version: 1
template_id: "imtpl.pattern.healthcare"
template_name: "Healthcare Regional Pattern Template"
template_version: "1.0.0"
description: "医療アクセスや地域医療の課題を整理し、実装・運用設計へ接続するテンプレート。"
domain: ["healthcare", "regional-innovation"]
tags: ["pattern", "healthcare", "access", "problem-solution"]
lang: "ja-JP"
status: draft
created_at: "2026-01-08"
---

# Healthcare Regional Pattern Template

本テンプレートは、医療アクセスや地域医療の課題を「文脈・課題・解決・スケール条件」で整理し、
運用・制度・実装へ接続するための最小構造を提供する。

---

## Template Scope

### Suitable for
- 医療アクセス改善（遠隔医療・移動診療等）の整理
- 医療機関/自治体/住民の連携整理
- 実装フェーズの前段設計

### Not responsible for
- 臨床プロトコルの詳細設計
- 医療機器の詳細設計
- 法規制の詳細解釈

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

## Range & Granularity
```yaml
range:
  spatial: "<地域/圏域>"
  temporal: "<短期/中期/長期>"
  social_scope: "<対象コミュニティ>"
granularity:
  level: "<policy/implementation/operation>"
  description: "<粒度の説明>"
```
- 介入範囲と粒度の合意に使う

---

## References & Evidence
```yaml
reference:
  - label: "<参照名>"
    url: "<URL>"
    type: "standard"
evidence:
  - type: "case-study"
    description: "<根拠の説明>"
    url: "<URL>"
```
- ガイドラインや先行事例を明示する

---

## Timeline & Dependencies
```yaml
timeline:
  - entity: "task:<id>"
    year: 2024
    milestone: "<節目>"
    status: "planned"
dependencies:
  - from: "task:<id>"
    to: "task:<id>"
    type: "sequential"
    risk: "medium"
```
- 導入計画や依存関係の整理に使う

---

## Observed Metrics
```yaml
observed_metrics:
  - entity: "metric:<id>"
    metric: "<単位>"
    average: "<平均>"
    stdev: "<標準偏差>"
```
- 現状の観測値やベースラインを置く

---

## Patterns & Hypotheses
```yaml
patterns:
  - type: "<pattern-type>"
    occurred_in: ["task:<id>"]
    severity: "medium"
hypotheses:
  - text: "<仮説>"
    confidence: 0.5
```
- 繰り返し起きる問題と仮説を記録する
