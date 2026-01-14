---
ideamark_version: 1
doc_id: "imdoc.breakdown.sec-kng-fuji-02"
parent_doc: "imdoc.sample.policy_compare.fhi-5cases"
section_id: "SEC-KNG-FUJI-02"
generated_by: "breakdown-sim"
created_at: "2026-01-11"
---

# Breakdown: SEC-KNG-FUJI-02

section_id: "SEC-KNG-FUJI-02"
anchorage: ["place:fuji", "measures", "pattern-mapping"]
entities:
  - id: "IE-KNG-FUJI-MEAS-01"
    kind: "measure"
    atomic_state: true
    content: "（PAT-02）Timed Entry Pilot：特定期間・特定地点（登山口/駐車/バス結節）で時間枠予約を試行し、ピーク分散と安全確保を狙う。"
  - id: "IE-KNG-FUJI-MEAS-02"
    kind: "measure"
    atomic_state: true
    content: "（PAT-01）Normative Code + Signage：行動規範（自然/地域/安全）を短く提示し、現場の多言語サインと一体運用する。"
  - id: "IE-KNG-FUJI-MEAS-03"
    kind: "measure"
    atomic_state: true
    content: "（PAT-05）Charter + Legal Plans + Public Consultation：重点地域のビジョン/目標/取組（憲章相当）と、利用基準（ゾーン/禁止・許可）を協議プロセスつきで整備する。"
  - id: "IE-KNG-FUJI-MEAS-04"
    kind: "measure"
    atomic_state: true
    content: "（PAT-04）Maintenance Funding Loop：損耗指標→補修計画→財源→実装→再計測のループを明示し、保全の運用能力を作る。"
occurrences:
  - entity: "IE-KNG-FUJI-MEAS-01"
    role: "measure"
    note: "US事例の転写（予約枠・公平性が焦点）"
  - entity: "IE-KNG-FUJI-MEAS-03"
    role: "mechanism"
    note: "EU事例の転写（協議と規則体系）"
relations:
  - type: "derives_from"
    from: "IE-KNG-FUJI-MEAS-01"
    to: "IE-US-TE-01"
  - type: "derives_from"
    from: "IE-KNG-FUJI-MEAS-02"
    to: "IE-UK-CC-01"
  - type: "derives_from"
    from: "IE-KNG-FUJI-MEAS-03"
    to: "IE-EU-FR-CHARTER-01"
  - type: "derives_from"
    from: "IE-KNG-FUJI-MEAS-04"
    to: "IE-UK-PATH-01"

---

# 13. 地点別：箱根（交通・受け皿・住民受容）
## 13.1 Section: 箱根の課題仮説（anchorage: place.hakone.problem）
