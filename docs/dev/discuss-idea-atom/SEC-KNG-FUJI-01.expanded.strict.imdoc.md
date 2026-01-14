---
ideamark_version: 1
doc_id: "imdoc.breakdown.sec-kng-fuji-01"
parent_doc: "imdoc.sample.policy_compare.fhi-5cases"
section_id: "SEC-KNG-FUJI-01"
generated_by: "breakdown-sim"
created_at: "2026-01-11"
---

# Breakdown: SEC-KNG-FUJI-01

section_id: "SEC-KNG-FUJI-01"
anchorage: ["place:fuji", "problem-framing"]
entities:
  - id: "IE-KNG-FUJI-PROB-01"
    kind: "problem"
    atomic_state: true
    content: "ピーク時に人流が集中し、交通・駐車・歩行動線・安全（救護/避難）がボトルネック化しやすい。"
  - id: "IE-KNG-FUJI-PROB-02"
    kind: "problem"
    atomic_state: true
    content: "景観・自然資源の損耗（侵食/ゴミ等）が発生しうる。"
  - id: "IE-KNG-FUJI-PROB-03"
    kind: "problem"
    atomic_state: true
    content: "文化・信仰・聖性の扱いが“体験価値”と“規範/制限”の設計に影響する可能性がある。"
relations:
  - type: "supports"
    from: "IE-KNG-BG-RISK-01"
    to: "IE-KNG-FUJI-PROB-01"
  - type: "generalizes"
    from: "IE-AUS-ULU-CONF-01"
    to: "IE-KNG-FUJI-PROB-03"

## 12.2 Section: 富士山の介入候補（anchorage: place.fuji.measures）



---
# Expansion (strict): SEC-KNG-FUJI-01
mode: "strict"

## Section: 富士山の課題仮説（拡張：strict）
section_id: "SEC-KNG-FUJI-01"
anchorage: ["place:fuji", "problem-framing", "strict-expansion"]

entities:
  - id: "IE-KNG-FUJI-PROB-01"
    kind: "problem"
    atomic_state: true
    content: "ピーク時に人流が集中し、交通・駐車・歩行動線・安全（救護/避難）がボトルネック化する。"
  - id: "IE-KNG-FUJI-PROB-02"
    kind: "problem"
    atomic_state: true
    content: "景観・自然資源の損耗（侵食・ゴミ・騒音）が累積的に発生する。"
  - id: "IE-KNG-FUJI-PROB-03"
    kind: "problem"
    atomic_state: true
    content: "文化的・象徴的価値（信仰・世界遺産）が体験設計と規制の正当性に影響する。"

  - id: "IE-KNG-FUJI-STKH-01"
    kind: "stakeholder"
    atomic_state: true
    content: "登山者・観光客（国内/海外）"
  - id: "IE-KNG-FUJI-STKH-02"
    kind: "stakeholder"
    atomic_state: true
    content: "地元自治体・観光事業者"
  - id: "IE-KNG-FUJI-STKH-03"
    kind: "stakeholder"
    atomic_state: true
    content: "救護・警察・消防・山岳関係者"
  - id: "IE-KNG-FUJI-STKH-04"
    kind: "stakeholder"
    atomic_state: true
    content: "信仰・文化・環境の関係者"

  - id: "IE-KNG-FUJI-CONST-01"
    kind: "constraint"
    atomic_state: true
    content: "短期的な来訪集中（季節性・天候依存）"
  - id: "IE-KNG-FUJI-CONST-02"
    kind: "constraint"
    atomic_state: true
    content: "県境・市町村境を跨ぐ権限分散"
  - id: "IE-KNG-FUJI-CONST-03"
    kind: "constraint"
    atomic_state: true
    content: "緊急時の避難・輸送制約"

relations:
  - type: "affects"
    from: "IE-KNG-FUJI-PROB-01"
    to: "IE-KNG-FUJI-STKH-01"
  - type: "affects"
    from: "IE-KNG-FUJI-PROB-02"
    to: "IE-KNG-FUJI-STKH-04"
  - type: "constrained_by"
    from: "IE-KNG-FUJI-PROB-01"
    to: "IE-KNG-FUJI-CONST-02"
