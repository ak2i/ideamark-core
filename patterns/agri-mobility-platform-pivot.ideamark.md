---
ideamark_version: 1
doc_id: "pattern.agri-mobility-platform-pivot.v2"
title: "農機具メンテナンス事業から汎用モビリティプラットフォームへのピボット"
template_ref: "imtpl.business_model_pivot@1.0.0"
domain: ["agriculture", "mobility", "rural"]
tags: ["pivot", "agri", "maintenance", "mobility", "rural-transport"]
lang: "ja-JP"
status: active
created_at: "2026-01-06"
source: "https://github.com/ak2i/ideamark-core/blob/main/patterns/agri-mobility-platform-pivot.yaml"
data_policy:
  contains_sensitive: false
  pii: none
  handling: public
---

# Pattern Overview

本パターンは、**地域農機メンテナンス事業の縮小**を前提条件として、
既存の資産・整備ネットワークを活かしながら、
**地域の人・物の移動を支える汎用モビリティプラットフォームへと
事業をピボットするための意思決定構造**を記述する。

---

## Intent: I-AGRI-001
```yaml
type: intent
summary: "持続可能な地域ビジネスの再設計"
lang: "ja-JP"
stakeholders:
  - 農機具メンテナンス事業者
  - JA協同組合
  - 地域住民
constraints:
  - 人口減少
  - 農機需要低下
  - 地方交通インフラ不足
```
既存の収益源が先細る中で、地域に残るための事業構造そのものを問い直す。

---

## Hypothesis: H-AGRI-001
```yaml
type: hypothesis
claim: "農機具整備サービスを地域モビリティに転用することで、農作業以外の移動ニーズを捉えられる"
tags: ["shared-mobility", "rural", "repurpose"]
falsifiable_by: ["M-AGRI-001", "M-AGRI-002"]
links:
  - {to: "O-AGRI-001", rel: "evaluates_option"}
```
農機具・整備網という既存の仕組みを、地域交通の基盤として再定義できるという仮説。

---

## DecisionOption: O-AGRI-001
```yaml
type: decision_option
option: "地域農機を共有モビリティ基盤として再活用し、地域交通サービスと統合する"
pros:
  - 既存資産を最大限活用できる
  - 整備ネットワークを基盤サービス化できる
cons:
  - 新需要の立ち上がりが不透明
  - 他の交通施策との調整が必要
prerequisites:
  - 地域移動ニーズ調査
  - プラットフォーム運用体制
links:
  - {to: "E-AGRI-001", rel: "implemented_as"}
```
事業の重心を「農業専用」から「地域汎用」へ移す選択肢。

---

## Experiment: E-AGRI-001
```yaml
type: experiment
purpose: "地域内移動・物流ニーズを実証し、プラットフォーム化の妥当性を検証する"
scope:
  - 農機改装車両の実証運用
  - 地域住民ヒアリング
out_of_scope:
  - 全国展開
  - 高度自動運転
artifact:
  - 実証運用レポート
  - 利用ログ
links:
  - {to: "M-AGRI-001", rel: "measured_by"}
  - {to: "M-AGRI-002", rel: "measured_by"}
  - {to: "D-AGRI-001", rel: "leads_to"}
```
実際に「使われるか」を見るための最小実験。

---

## Metric: M-AGRI-001
```yaml
type: metric
name: "利用需要スコア"
definition: "一定期間内に確認された移動・物流サービス利用希望数"
unit: "count/week"
time_window: "P7D"
collection:
  method: "アンケート + 実証予約ログ"
refs:
  - id: "ref.agri.mobility.survey.wk01"
    kind: "sheet"
    title: "地域移動ニーズアンケート"
    locator: "internal://sheets/agri_mobility_survey_wk01"
    access: "internal"
```
---

## Metric: M-AGRI-002
```yaml
type: metric
name: "サービス維持コスト比"
definition: "実運用コスト ÷ 想定受領料金"
unit: "ratio"
time_window: "P30D"
collection:
  method: "実証運用収支集計"
refs:
  - id: "ref.agri.mobility.costs.wk04"
    kind: "report"
    title: "実証運用コストレポート"
    locator: "internal://reports/agri_mobility_costs_wk04"
    access: "internal"
```
---

## DecisionLog: D-AGRI-001
```yaml
type: decision_log
decision: "需要スコアが一定水準を超え、コスト比が1.0未満であれば次フェーズへ進む"
why_now: "既存農機メンテナンス事業の市場縮小が進行しているため"
stop_rule_ref: ["M-AGRI-001", "M-AGRI-002"]
evidence_refs:
  - "ref.agri.mobility.survey.wk01"
  - "ref.agri.mobility.costs.wk04"
next_candidates:
  - "地域物流特化モデルへの転換"
  - "高齢者移動支援サービスへの派生"
```
意思決定は成功・失敗ではなく、**仮説の支持／否定**として記録される。
