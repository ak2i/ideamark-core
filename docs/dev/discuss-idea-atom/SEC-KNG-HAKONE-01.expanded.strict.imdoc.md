---
ideamark_version: 1
doc_id: "imdoc.breakdown.sec-kng-hakone-01"
parent_doc: "imdoc.sample.policy_compare.fhi-5cases"
section_id: "SEC-KNG-HAKONE-01"
generated_by: "breakdown-sim"
created_at: "2026-01-11"
---

# Breakdown: SEC-KNG-HAKONE-01

section_id: "SEC-KNG-HAKONE-01"
anchorage: ["place:hakone", "problem-framing"]
entities:
  - id: "IE-KNG-HAKONE-PROB-01"
    kind: "problem"
    atomic_state: true
    content: "交通混雑（道路・駐車・公共交通のピーク集中）が体験価値と生活圧を同時に悪化させる。"
  - id: "IE-KNG-HAKONE-PROB-02"
    kind: "problem"
    atomic_state: true
    content: "受け皿（シャトル/駐車/動線）の運用が“局所最適”になりやすく、全体の分散設計が必要。"
relations:
  - type: "generalizes"
    from: "IE-UK-LD-OVR-01"
    to: "IE-KNG-HAKONE-PROB-01"

## 13.2 Section: 箱根の介入候補（anchorage: place.hakone.measures）



---
# Expansion (strict): SEC-KNG-HAKONE-01
mode: "strict"

## Section: 箱根の課題仮説（拡張：strict）
section_id: "SEC-KNG-HAKONE-01"
anchorage: ["place:hakone", "problem-framing", "strict-expansion"]

entities:
  - id: "IE-KNG-HAKONE-PROB-01"
    kind: "problem"
    atomic_state: true
    content: "道路・駐車・公共交通にピーク集中が発生し、来訪体験と住民生活の双方を圧迫する。"
  - id: "IE-KNG-HAKONE-PROB-02"
    kind: "problem"
    atomic_state: true
    content: "交通・受け皿施策が局所最適化し、地域全体としての分散設計が弱い。"

  - id: "IE-KNG-HAKONE-STKH-01"
    kind: "stakeholder"
    atomic_state: true
    content: "観光客（国内・インバウンド）"
  - id: "IE-KNG-HAKONE-STKH-02"
    kind: "stakeholder"
    atomic_state: true
    content: "地元住民・通勤通学者"
  - id: "IE-KNG-HAKONE-STKH-03"
    kind: "stakeholder"
    atomic_state: true
    content: "交通事業者（鉄道・バス・道路管理）"
  - id: "IE-KNG-HAKONE-STKH-04"
    kind: "stakeholder"
    atomic_state: true
    content: "自治体・観光事業者"

  - id: "IE-KNG-HAKONE-CONST-01"
    kind: "constraint"
    atomic_state: true
    content: "地形制約（道路拡幅・新規駐車場が困難）"
  - id: "IE-KNG-HAKONE-CONST-02"
    kind: "constraint"
    atomic_state: true
    content: "複数交通事業者間の調整コスト"
