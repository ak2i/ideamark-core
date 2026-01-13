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



---
# Expansion (conservative): SEC-KNG-FUJI-02
mode: "conservative"
policy:
  - "外部ソースは使わない（このシミュレーションでは未添付のため）"
  - "ただし、運用仕様は『確定値』ではなく『仕様項目（スロット）』として具体化する"
  - "仕様項目は後で外部根拠を追加して埋められるよう、スロット化してentity化する"

## 12.2 Section: 富士山の介入候補（拡張：conservative / slot-based）
section_id: "SEC-KNG-FUJI-02"
anchorage: ["place:fuji", "measures", "pattern-mapping", "conservative-expansion", "slots"]
entities:
  # 既存保持（参照）
  - id: "IE-KNG-FUJI-MEAS-01"
    kind: "measure"
    atomic_state: true
    content: "（PAT-02）Timed Entry Pilot：特定期間・特定地点（登山口/駐車/バス結節）で時間枠予約を試行し、ピーク分散と安全確保を狙う。"

  # Timed Entry 仕様スロット（埋める対象をentity化）
  - id: "IE-KNG-FUJI-TE-SLOT-01"
    kind: "projection"
    atomic_state: true
    content: "Timed Entry: 対象範囲スロット（地点/期間/対象者/対象行為）"
  - id: "IE-KNG-FUJI-TE-SLOT-02"
    kind: "projection"
    atomic_state: true
    content: "Timed Entry: 枠モデルスロット（枠数、時間単位、混雑閾値、調整ロジック）"
  - id: "IE-KNG-FUJI-TE-SLOT-03"
    kind: "projection"
    atomic_state: true
    content: "Timed Entry: 取得導線スロット（Web/窓口/旅行商品、本人確認、転売対策）"
  - id: "IE-KNG-FUJI-TE-SLOT-04"
    kind: "projection"
    atomic_state: true
    content: "Timed Entry: 当日運用スロット（当日枠、キャンセル再放流、現地確認、例外処理）"
  - id: "IE-KNG-FUJI-TE-SLOT-05"
    kind: "projection"
    atomic_state: true
    content: "Timed Entry: 公平性スロット（抽選、優先枠、アクセシビリティ配慮、属性別影響評価）"
  - id: "IE-KNG-FUJI-TE-SLOT-06"
    kind: "projection"
    atomic_state: true
    content: "Timed Entry: 料金/財源スロット（予約手数料、保全基金、返金/変更ルール）"
  - id: "IE-KNG-FUJI-TE-SLOT-07"
    kind: "projection"
    atomic_state: true
    content: "Timed Entry: KPIスロット（混雑/安全/資源影響/満足/公平性/運用コスト）"

  # Shuttle-first（箱根等でも再利用できるのでパターン化寄り）
  - id: "IE-KNG-FUJI-SHUT-SLOT-01"
    kind: "projection"
    atomic_state: true
    content: "Shuttle-first: 導入条件スロット（駐車容量、道路渋滞、結節点、代替輸送能力）"
  - id: "IE-KNG-FUJI-SHUT-SLOT-02"
    kind: "projection"
    atomic_state: true
    content: "Shuttle-first: 運用スロット（運行頻度、優先レーン、情報提供、混雑期ダイヤ）"

  # Code + Signage（文言・配置を“スロット”として固定）
  - id: "IE-KNG-FUJI-CODE-SLOT-01"
    kind: "projection"
    atomic_state: true
    content: "Code: 原則スロット（短文3〜7本）"
  - id: "IE-KNG-FUJI-CODE-SLOT-02"
    kind: "projection"
    atomic_state: true
    content: "Code: Do/Don't例スロット（具体例、ローカル例外、罰則の有無）"
  - id: "IE-KNG-FUJI-SIGN-SLOT-01"
    kind: "projection"
    atomic_state: true
    content: "Signage: 設置点スロット（結節点/入口/分岐/危険箇所/救護/出口）"
  - id: "IE-KNG-FUJI-SIGN-SLOT-02"
    kind: "projection"
    atomic_state: true
    content: "Signage: 表現スロット（多言語、ピクト、ユニバーサルデザイン、理解度テスト）"

  # Charter + Consultation（最小プロセスの“項目”を定義）
  - id: "IE-KNG-FUJI-CHAR-SLOT-01"
    kind: "projection"
    atomic_state: true
    content: "Charter: 構成スロット（ビジョン/目標/取組/改定周期/責任主体）"
  - id: "IE-KNG-FUJI-CONSULT-SLOT-01"
    kind: "projection"
    atomic_state: true
    content: "Consultation: 参加者スロット（自治体/事業者/住民/専門家/救護/環境）"
  - id: "IE-KNG-FUJI-CONSULT-SLOT-02"
    kind: "projection"
    atomic_state: true
    content: "Consultation: 公開性スロット（議事録公開、意見募集、反映ルール）"

  # Maintenance Funding Loop（資源インベントリ等をスロット化）
  - id: "IE-KNG-FUJI-MNT-SLOT-01"
    kind: "projection"
    atomic_state: true
    content: "Maintenance: 資源インベントリスロット（歩道/植生/案内/トイレ等）"
  - id: "IE-KNG-FUJI-MNT-SLOT-02"
    kind: "projection"
    atomic_state: true
    content: "Maintenance: 影響指標スロット（侵食/ゴミ/混雑/苦情）"
  - id: "IE-KNG-FUJI-MNT-SLOT-03"
    kind: "projection"
    atomic_state: true
    content: "Maintenance: 財源スロット（基金/協賛/利用料/予約手数料）"
  - id: "IE-KNG-FUJI-MNT-SLOT-04"
    kind: "projection"
    atomic_state: true
    content: "Maintenance: 公開報告スロット（年次レポート、ダッシュボード、透明性）"

occurrences:
  - entity: "IE-KNG-FUJI-MEAS-01"
    role: "measure"
  - entity: "IE-KNG-FUJI-TE-SLOT-01"
    role: "projection"
    note: "後で外部根拠を付与して埋める"
  - entity: "IE-KNG-FUJI-CONSULT-SLOT-02"
    role: "projection"

relations:
  - type: "derives_from"
    from: "IE-KNG-FUJI-TE-SLOT-01"
    to: "IE-PROJ-01"
    note: "予約/配分の運用投影と整合"
  - type: "derives_from"
    from: "IE-KNG-FUJI-CODE-SLOT-01"
    to: "IE-PROJ-02"
  - type: "derives_from"
    from: "IE-KNG-FUJI-TE-SLOT-07"
    to: "IE-PROJ-03"
  - type: "derives_from"
    from: "IE-KNG-FUJI-CONSULT-SLOT-02"
    to: "IE-PROJ-04"
  - type: "operationalizes"
    from: "IE-KNG-FUJI-TE-SLOT-02"
    to: "IE-KNG-FUJI-MEAS-01"
  - type: "requires"
    from: "IE-KNG-FUJI-CONSULT-SLOT-01"
    to: "IE-KNG-FUJI-CHAR-SLOT-01"
