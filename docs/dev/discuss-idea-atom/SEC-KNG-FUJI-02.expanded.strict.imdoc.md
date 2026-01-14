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
# Expansion (strict): SEC-KNG-FUJI-02
mode: "strict"
policy:
  - "外部ソースから新事実を追加しない"
  - "既存のIdeaEntityを壊さず、運用・KPI・リスクを『仮説/設計案』として追加する"
  - "追加する具体値は例示に留め、確定値として断定しない"

## 12.2 Section: 富士山の介入候補（拡張：strict）
section_id: "SEC-KNG-FUJI-02"
anchorage: ["place:fuji", "measures", "pattern-mapping", "strict-expansion"]
entities:
  # 既存は保持（参照用）
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

  # 追加：運用コンポーネント（断定せず“設計案”として）
  - id: "IE-KNG-FUJI-OPS-01"
    kind: "mechanism"
    atomic_state: true
    content: "（設計案）Timed Entryの枠設計：『対象地点×期間×時間帯』で枠を定義し、総量規制ではなくピーク分散を狙う。"
  - id: "IE-KNG-FUJI-OPS-02"
    kind: "mechanism"
    atomic_state: true
    content: "（設計案）取得導線：Web/アプリ/窓口等の複線化を前提に、デジタル弱者向けの代替導線を用意する。"
  - id: "IE-KNG-FUJI-OPS-03"
    kind: "mechanism"
    atomic_state: true
    content: "（設計案）当日運用：当日枠・キャンセル再放流・現場確認（検札/照合）を組み合わせ、実効性と公平性を両立する。"
  - id: "IE-KNG-FUJI-OPS-04"
    kind: "mechanism"
    atomic_state: true
    content: "（設計案）例外ルール：救護・居住者・業務・障害者配慮などの例外区分を明文化し、濫用防止（監査可能性）を持たせる。"

  # 追加：行動規範の“最小セット”（文言は暫定案）
  - id: "IE-KNG-FUJI-CODE-01"
    kind: "mechanism"
    atomic_state: true
    content: "（暫定案）行動規範：『安全を最優先に／自然と景観を守る／地域に配慮する／指定ルートと案内に従う』の短文4本で開始する。"
  - id: "IE-KNG-FUJI-CODE-02"
    kind: "mechanism"
    atomic_state: true
    content: "（暫定案）Do/Don't例：ゴミ持ち帰り、立入制限遵守、混雑時の迂回/時間変更、救護動線確保、静穏配慮 等。"
  - id: "IE-KNG-FUJI-SIGN-01"
    kind: "mechanism"
    atomic_state: true
    content: "（設計案）サイン設置点：結節点（駅/駐車/バス乗場）、入口（登山口等）、分岐点（ルート選択）、危険箇所、救護拠点。"

  # 追加：協議・憲章（最小プロセス）
  - id: "IE-KNG-FUJI-CHAR-01"
    kind: "mechanism"
    atomic_state: true
    content: "（設計案）憲章（最小）：ビジョン→目標→行動（規範/ルール/交通）→レビュー周期、の1枚構成から始め段階的に詳細化する。"
  - id: "IE-KNG-FUJI-CONSULT-01"
    kind: "mechanism"
    atomic_state: true
    content: "（設計案）協議プロセス（最小）：関係自治体・事業者・住民・専門家が参加する公開可能な会合で論点と決定を記録する。"

  # 追加：KPI（確定ではなく“候補セット”）
  - id: "IE-KNG-FUJI-KPI-01"
    kind: "metric"
    atomic_state: true
    content: "（候補）混雑KPI：ピーク時間帯の通過人数、待ち時間、駐車満車率、公共交通の混雑率。"
  - id: "IE-KNG-FUJI-KPI-02"
    kind: "metric"
    atomic_state: true
    content: "（候補）安全KPI：事故・救護件数、熱中症/転倒等の発生、避難誘導の所要、訓練実施回数。"
  - id: "IE-KNG-FUJI-KPI-03"
    kind: "metric"
    atomic_state: true
    content: "（候補）資源影響KPI：侵食・植生損傷の観測点、ゴミ回収量、騒音/苦情件数。"
  - id: "IE-KNG-FUJI-KPI-04"
    kind: "metric"
    atomic_state: true
    content: "（候補）体験価値KPI：満足度、再訪意向、案内理解度、規範受容度。"
  - id: "IE-KNG-FUJI-KPI-05"
    kind: "metric"
    atomic_state: true
    content: "（候補）公平性KPI：予約取得の成功率（属性別）、当日枠の利用割合、情報アクセスの偏り。"
  - id: "IE-KNG-FUJI-KPI-06"
    kind: "metric"
    atomic_state: true
    content: "（候補）運用コストKPI：人員投入、現場対応時間、システム費、違反対応件数。"

  # 追加：リスク（strictでは“懸念”として）
  - id: "IE-KNG-FUJI-RISK-01"
    kind: "risk"
    atomic_state: true
    content: "（懸念）Timed Entryが『取得できた人／できない人』を分け、新たな不公平感を生む可能性。"
  - id: "IE-KNG-FUJI-RISK-02"
    kind: "risk"
    atomic_state: true
    content: "（懸念）現場確認が弱いと“抜け道”が生まれ、制度の信頼性が低下する可能性。"
  - id: "IE-KNG-FUJI-RISK-03"
    kind: "risk"
    atomic_state: true
    content: "（懸念）規範・サインが増えすぎると理解負荷が上がり、遵守率が下がる可能性。"
  - id: "IE-KNG-FUJI-RISK-04"
    kind: "risk"
    atomic_state: true
    content: "（懸念）協議が形式化すると、正当性の担保にならず対立を固定化する可能性。"

occurrences:
  - entity: "IE-KNG-FUJI-MEAS-01"
    role: "measure"
  - entity: "IE-KNG-FUJI-OPS-01"
    role: "mechanism"
    note: "Timed Entryの仕様粒度を提示"
  - entity: "IE-KNG-FUJI-KPI-01"
    role: "metric"
  - entity: "IE-KNG-FUJI-RISK-01"
    role: "risk"
  - entity: "IE-KNG-FUJI-CODE-01"
    role: "mechanism"

relations:
  - type: "derives_from"
    from: "IE-KNG-FUJI-MEAS-01"
    to: "IE-PAT-02"
    note: "PAT-02に正規化"
  - type: "derives_from"
    from: "IE-KNG-FUJI-MEAS-02"
    to: "IE-PAT-01"
  - type: "derives_from"
    from: "IE-KNG-FUJI-MEAS-03"
    to: "IE-PAT-05"
  - type: "derives_from"
    from: "IE-KNG-FUJI-MEAS-04"
    to: "IE-PAT-04"
  - type: "operationalizes"
    from: "IE-KNG-FUJI-OPS-01"
    to: "IE-KNG-FUJI-MEAS-01"
  - type: "measures"
    from: "IE-KNG-FUJI-KPI-01"
    to: "IE-KNG-FUJI-MEAS-01"
  - type: "risks"
    from: "IE-KNG-FUJI-RISK-01"
    to: "IE-KNG-FUJI-MEAS-01"
  - type: "enables"
    from: "IE-KNG-FUJI-CODE-01"
    to: "IE-KNG-FUJI-MEAS-02"
  - type: "requires"
    from: "IE-KNG-FUJI-CONSULT-01"
    to: "IE-KNG-FUJI-MEAS-03"
