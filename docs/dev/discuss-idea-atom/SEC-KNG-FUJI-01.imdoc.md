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
