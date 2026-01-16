# 聖地ウルルをめぐる場所のポリティクスとアウトバックツーリズム

```yaml
ideamark_version: 1
doc_id: "imdoc.case.uluru_sacred_politics.matsui2015"
doc_type: "derived"
status: "in_progress"
created_at: "2026-01-16"
updated_at: "2026-01-16"
lang: "ja-JP"

refs:
  sources:
    - id: "matsui2015"
      uri: "tmp/dev-sample/2015-8-1.9.pdf"
      role: "source_material"
      description: "松井圭介・堤純・吉田道代・葉倩瑋・筒井由起乃 (2015)『聖地ウルルをめぐる場所のポリティクスとアウトバックツーリズム』地理空間 8-1, 131-142"
```

## Meta
```yaml
intent: |
  聖地ウルルにおける観光動態と場所のポリティクスを、
  先住民文化としての聖地の管理・保全と資源化の視点から整理する。
```

---

## Section 001 : 研究背景と問題設定
```yaml
section_id: "SEC-MATSUI-01"
anchorage:
  view: "background"
  phase: "confirmed"
  domain: ["uluru", "sacred_site", "tourism"]
```

現代のウルルをめぐる観光と聖地管理の緊張を研究課題として提示する。

### OCC-MATSUI-01-001 : 研究目的
```yaml
occurrence_id: "OCC-MATSUI-01-001"
entity: "IE-MATSUI-RESEARCH-AIM"
role: "context"
status:
  state: "confirmed"
```
観光動態と場所のポリティクスを、管理・保全と資源化の視点から検討する。

#### IdeaEntity: IE-MATSUI-RESEARCH-AIM
ウルルのツーリズム、管理、宗教的世界観を段階的に整理し、場所の政治性を考察する。

### OCC-MATSUI-01-002 : 聖地と観光資源の二重性
```yaml
occurrence_id: "OCC-MATSUI-01-002"
entity: "IE-ULURU-DUAL-VALUE"
role: "problem_core"
status:
  state: "confirmed"
```
神話的中心であると同時に高い観光価値を持つため、登山をめぐる緊張が生じる。

#### IdeaEntity: IE-ULURU-DUAL-VALUE
聖地性と資源化の両立が構造的な摩擦を生み、ステークホルダー内外で相克が起きる。

### OCC-MATSUI-01-003 : 場所のポリティクス視点
```yaml
occurrence_id: "OCC-MATSUI-01-003"
entity: "IE-PLACE-POLITICS-FRAME"
role: "topic_focus"
status:
  state: "confirmed"
```
「登山制限」を巡る政治性を分析の軸に据える。

#### IdeaEntity: IE-PLACE-POLITICS-FRAME
先住民文化の真正性、政府の努力、ツーリスト満足の交差点として場所を読む。

---

## Section 002 : ウルルにおけるツーリズムの動態
```yaml
section_id: "SEC-MATSUI-02"
anchorage:
  view: "observation_series"
  phase: "confirmed"
  domain: ["tourism_dynamics"]
```

観光客数の推移、移動手段、観光インフラを整理する。

### OCC-MATSUI-02-001 : 観光客数の減少傾向
```yaml
occurrence_id: "OCC-MATSUI-02-001"
entity: "IE-TOURISM-DECLINE"
role: "observation_at_t"
status:
  state: "confirmed"
```
2005年から2013年にかけて観光客数が大きく減少した。

#### IdeaEntity: IE-TOURISM-DECLINE
国際ツーリストの減少が顕著で、約40万人規模から約25万人規模へ低下している。

### OCC-MATSUI-02-002 : 国際ツーリストの志向
```yaml
occurrence_id: "OCC-MATSUI-02-002"
entity: "IE-TOURISM-MARKET-SKEW"
role: "context"
status:
  state: "confirmed"
```
国内と国際で訪問地の志向が異なり、国際ツーリストは自然資源型に集中する。

#### IdeaEntity: IE-TOURISM-MARKET-SKEW
国内は都市近郊志向、国際はウルルやカカドゥなど国立公園志向で差が明確。

### OCC-MATSUI-02-003 : 移動手段とゲートウェイ
```yaml
occurrence_id: "OCC-MATSUI-02-003"
entity: "IE-ACCESS-ROUTES"
role: "observation_at_t"
status:
  state: "confirmed"
```
遠隔地ゆえ航空機利用が過半を占め、シドニー経由が中心となる。

#### IdeaEntity: IE-ACCESS-ROUTES
航空機単独利用が最多で、シドニーが主要ゲートウェイとして卓越する。

### OCC-MATSUI-02-004 : 観光インフラと訪問管理
```yaml
occurrence_id: "OCC-MATSUI-02-004"
entity: "IE-RESORT-MANAGEMENT"
role: "mechanism"
status:
  state: "confirmed"
```
リゾート集約と入園料、ツアー運用によって環境負荷を制御する。

#### IdeaEntity: IE-RESORT-MANAGEMENT
エアーズロック・リゾートに宿泊機能を集約し、入園料とツアーで動線管理を行う。

---

## Section 003 : 聖地管理とツーリストの相克
```yaml
section_id: "SEC-MATSUI-03"
anchorage:
  view: "problem"
  phase: "confirmed"
  domain: ["sacred_management", "stakeholders"]
```

聖域保全と観光体験の衝突を、登山問題を軸に整理する。

### OCC-MATSUI-03-001 : 共同管理と土地返還契約
```yaml
occurrence_id: "OCC-MATSUI-03-001"
entity: "IE-JOINT-MANAGEMENT-LEASE"
role: "mechanism"
status:
  state: "confirmed"
```
土地返還と99年借地契約により、先住民と政府の共同管理が成立した。

#### IdeaEntity: IE-JOINT-MANAGEMENT-LEASE
入園料の一部を先住民へ配分する仕組みが、保全と生活資源の両面を支える。

### OCC-MATSUI-03-002 : 聖域保全の具体的管理
```yaml
occurrence_id: "OCC-MATSUI-03-002"
entity: "IE-SACRED-RESTRICTIONS"
role: "mechanism"
status:
  state: "confirmed"
```
撮影禁止区域や立入禁止区域など、儀礼空間を保護する管理が行われる。

#### IdeaEntity: IE-SACRED-RESTRICTIONS
聖域に対する物理的制限が示され、観光資源化の中で文化保全が制度化される。

### OCC-MATSUI-03-003 : 登山を巡るコンフリクト
```yaml
occurrence_id: "OCC-MATSUI-03-003"
entity: "IE-CLIMB-CONFLICT"
role: "problem_core"
status:
  state: "confirmed"
```
登山は観光体験の核である一方、聖地への冒涜として忌避される。

#### IdeaEntity: IE-CLIMB-CONFLICT
登山の可否は安全性・文化性・観光需要が交差する最大の争点となる。

### OCC-MATSUI-03-004 : 登山制限の運用
```yaml
occurrence_id: "OCC-MATSUI-03-004"
entity: "IE-CLIMB-REGULATION"
role: "mechanism"
status:
  state: "confirmed"
```
登山禁止は恒久化されず、気象条件や文化的要請で一時的に運用される。

#### IdeaEntity: IE-CLIMB-REGULATION
6条件による入山判断や多言語掲示で、禁止ではなく抑制の枠組みが作られている。

### OCC-MATSUI-03-005 : ツーリスト行動の実態
```yaml
occurrence_id: "OCC-MATSUI-03-005"
entity: "IE-TOURIST-BEHAVIOR-DATA"
role: "evidence"
status:
  state: "confirmed"
```
登山者割合は国籍で差が大きく、日本人比率が高い。

#### IdeaEntity: IE-TOURIST-BEHAVIOR-DATA
調査では登山者が全体の約38％で、日本人登山率が突出していると報告される。

### OCC-MATSUI-03-006 : 文化的要請の掲示
```yaml
occurrence_id: "OCC-MATSUI-03-006"
entity: "IE-KEEP-TJUKURPA-STRONG"
role: "context"
status:
  state: "confirmed"
```
「登らないでほしい」という要請が政府・先住民双方のメッセージとして示される。

#### IdeaEntity: IE-KEEP-TJUKURPA-STRONG
伝統法を守る要請が、理解を促すソフトな統治装置として機能する。

---

## Section 004 : 先住民の宗教的世界と土地所有
```yaml
section_id: "SEC-MATSUI-04"
anchorage:
  view: "background"
  phase: "confirmed"
  domain: ["indigenous_worldview", "land_ownership"]
```

ジュクルパ概念と土地の意味を、宗教的世界観から整理する。

### OCC-MATSUI-04-001 : ジュクルパの基礎概念
```yaml
occurrence_id: "OCC-MATSUI-04-001"
entity: "IE-TJUKURPA-CONCEPT"
role: "context"
status:
  state: "confirmed"
```
ジュクルパは天地創造神話であり、生きた法として世界の原理を示す。

#### IdeaEntity: IE-TJUKURPA-CONCEPT
時間と空間を超えた秩序の説明原理として、儀礼や規範の根拠となる。

### OCC-MATSUI-04-002 : 場所と人間の結びつき
```yaml
occurrence_id: "OCC-MATSUI-04-002"
entity: "IE-PLACE-IDENTITY"
role: "context"
status:
  state: "confirmed"
```
出生地や儀礼に結びつく場所が、個人のアイデンティティを形成する。

#### IdeaEntity: IE-PLACE-IDENTITY
特定の場所との関係は「守るべきもの」として生涯継続する関係とされる。

### OCC-MATSUI-04-003 : 土地所有概念の差異
```yaml
occurrence_id: "OCC-MATSUI-04-003"
entity: "IE-OWNERSHIP-DIFFERENCE"
role: "contrasts"
status:
  state: "confirmed"
```
契約による所有と、ジュクルパ理解に基づく所有の間に大きな差がある。

#### IdeaEntity: IE-OWNERSHIP-DIFFERENCE
土地所有は儀礼知識と祖先との交流を継続する責任であり、西洋的所有と異なる。

---

## Section 005 : 場所のポリティクスとしての登山制限
```yaml
section_id: "SEC-MATSUI-05"
anchorage:
  view: "discussion"
  phase: "confirmed"
  domain: ["place_politics", "tourism_governance"]
```

登山制限を巡る政治性がどのように機能しているかを考察する。

### OCC-MATSUI-05-001 : ステークホルダーのジレンマ
```yaml
occurrence_id: "OCC-MATSUI-05-001"
entity: "IE-STAKEHOLDER-DILEMMA"
role: "problem_core"
status:
  state: "confirmed"
```
観光収入と聖地保全の両立が、先住民側にもジレンマを生む。

#### IdeaEntity: IE-STAKEHOLDER-DILEMMA
登山禁止の完全実施が経済損失を生む一方、保全要求も強いという二重拘束がある。

### OCC-MATSUI-05-002 : 登山制限の政治装置性
```yaml
occurrence_id: "OCC-MATSUI-05-002"
entity: "IE-POLITICS-DEVICE"
role: "mechanism"
status:
  state: "confirmed"
```
禁止ではなく「要請」を続けることで、複数の利害を同時に担保する。

#### IdeaEntity: IE-POLITICS-DEVICE
先住民文化の真正性、政府の努力、ツーリスト満足を同時に成立させる装置として作用する。

### OCC-MATSUI-05-003 : 観光体験の再構成
```yaml
occurrence_id: "OCC-MATSUI-05-003"
entity: "IE-TOURISM-ETHIC"
role: "conclusion"
status:
  state: "confirmed"
```
登らないという行為が、文化的配慮と観光満足の両方を意味づける。

#### IdeaEntity: IE-TOURISM-ETHIC
「登らない態度」が真正性の担保として価値づけられ、ツーリズムの倫理を形成する。

---

## Appendix A : 文献情報
```yaml
section_id: "SEC-APP-A"
anchorage:
  view: "background"
  phase: "confirmed"
  domain: ["bibliography"]
```

- 松井圭介・堤純・吉田道代・葉倩瑋・筒井由起乃 (2015). 聖地ウルルをめぐる場所のポリティクスとアウトバックツーリズム. 地理空間 8-1, 131-142.

---

## Entities Registry
```yaml
entities:
  IE-MATSUI-RESEARCH-AIM:
    kind: "summary"
    content: |
      現代ウルルの観光動態と場所のポリティクスを、
      先住民文化としての管理・保全と資源化の視点から検討する。
    atomic_state: true

  IE-ULURU-DUAL-VALUE:
    kind: "problem"
    content: |
      ウルルはアナング族にとって神話的意味世界の中心であり、
      同時に高い観光価値を有するため、登山を巡る緊張が生じる。
    atomic_state: true

  IE-PLACE-POLITICS-FRAME:
    kind: "structural_hypothesis"
    content: |
      登山制限を巡る場所のポリティクスを、
      先住民文化の真正性、政府の努力、ツーリスト満足の交点として読む。
    atomic_state: true

  IE-TOURISM-DECLINE:
    kind: "observation"
    content: |
      2005年頃に約40万人だった観光客数は、2013年には約25万人へ減少した。
      国際ツーリストの減少が特に顕著である。
    atomic_state: true

  IE-TOURISM-MARKET-SKEW:
    kind: "context"
    content: |
      国内ツーリストは都市近郊の観光地志向が強い一方、
      国際ツーリストはウルルなど自然資源型の国立公園に集中する。
    atomic_state: true

  IE-ACCESS-ROUTES:
    kind: "observation"
    content: |
      ウルルは遠隔地に位置し航空機利用が最多で、
      シドニー経由が主要ゲートウェイとなる。
    atomic_state: true

  IE-RESORT-MANAGEMENT:
    kind: "mechanism"
    content: |
      エアーズロック・リゾートに宿泊施設を集約し、
      入園料とパックツアーで訪問動線と環境負荷を管理する。
    atomic_state: true

  IE-JOINT-MANAGEMENT-LEASE:
    kind: "mechanism"
    content: |
      1985年の土地返還後、国立公園として99年借地契約が結ばれ、
      入園料収入の一部が先住民へ還元される共同管理体制が成立した。
    atomic_state: true

  IE-SACRED-RESTRICTIONS:
    kind: "mechanism"
    content: |
      儀礼空間の撮影禁止や立入禁止区域の設定により、
      聖域としてのウルルを保護する管理が行われている。
    atomic_state: true

  IE-CLIMB-CONFLICT:
    kind: "problem"
    content: |
      登山は観光体験として求められる一方、
      先住民にとっては聖地への冒涜として忌避される。
    atomic_state: true

  IE-CLIMB-REGULATION:
    kind: "mechanism"
    content: |
      登山は禁止ではなく、気象条件や文化的要請により一時的に制限される。
      多言語掲示と条件設定で登山抑制を図る。
    atomic_state: true

  IE-TOURIST-BEHAVIOR-DATA:
    kind: "evidence"
    content: |
      2006年調査では登山者が全体の約38％で、
      国籍別では日本人の登山率が突出して高かった。
    atomic_state: true

  IE-KEEP-TJUKURPA-STRONG:
    kind: "context"
    content: |
      「登らないでほしい」という要請が掲示や広報で示され、
      伝統法を守るという姿勢が強調される。
    atomic_state: true

  IE-TJUKURPA-CONCEPT:
    kind: "context"
    content: |
      ジュクルパは天地創造神話であり、
      時空を超えた秩序として儀礼や規範の基盤となる。
    atomic_state: true

  IE-PLACE-IDENTITY:
    kind: "context"
    content: |
      出生や儀礼に関わる場所との関係が個人のアイデンティティを形成し、
      その場所を守る責任として継続される。
    atomic_state: true

  IE-OWNERSHIP-DIFFERENCE:
    kind: "context"
    content: |
      土地所有は契約ではなく、ジュクルパ理解と儀礼の継続を伴う責任であり、
      西洋的所有概念とは根本的に異なる。
    atomic_state: true

  IE-STAKEHOLDER-DILEMMA:
    kind: "problem"
    content: |
      聖地保全と観光収入の確保は先住民にとってもジレンマであり、
      完全禁止は経済損失を伴う。
    atomic_state: true

  IE-POLITICS-DEVICE:
    kind: "mechanism"
    content: |
      登山禁止ではなく要請に留めることで、
      先住民文化の真正性、政府の努力、ツーリスト満足を同時に担保する。
    atomic_state: true

  IE-TOURISM-ETHIC:
    kind: "summary"
    content: |
      「登らない態度」を文化的に正しい行為として位置づけ、
      観光体験の意味を再構成する。
    atomic_state: true

occurrences:
  OCC-MATSUI-01-001:
    entity: "IE-MATSUI-RESEARCH-AIM"
    role: "context"
    status: { state: "confirmed" }

  OCC-MATSUI-01-002:
    entity: "IE-ULURU-DUAL-VALUE"
    role: "problem_core"
    status: { state: "confirmed" }

  OCC-MATSUI-01-003:
    entity: "IE-PLACE-POLITICS-FRAME"
    role: "topic_focus"
    status: { state: "confirmed" }

  OCC-MATSUI-02-001:
    entity: "IE-TOURISM-DECLINE"
    role: "observation_at_t"
    status: { state: "confirmed" }

  OCC-MATSUI-02-002:
    entity: "IE-TOURISM-MARKET-SKEW"
    role: "context"
    status: { state: "confirmed" }

  OCC-MATSUI-02-003:
    entity: "IE-ACCESS-ROUTES"
    role: "observation_at_t"
    status: { state: "confirmed" }

  OCC-MATSUI-02-004:
    entity: "IE-RESORT-MANAGEMENT"
    role: "mechanism"
    status: { state: "confirmed" }

  OCC-MATSUI-03-001:
    entity: "IE-JOINT-MANAGEMENT-LEASE"
    role: "mechanism"
    status: { state: "confirmed" }

  OCC-MATSUI-03-002:
    entity: "IE-SACRED-RESTRICTIONS"
    role: "mechanism"
    status: { state: "confirmed" }

  OCC-MATSUI-03-003:
    entity: "IE-CLIMB-CONFLICT"
    role: "problem_core"
    status: { state: "confirmed" }

  OCC-MATSUI-03-004:
    entity: "IE-CLIMB-REGULATION"
    role: "mechanism"
    status: { state: "confirmed" }

  OCC-MATSUI-03-005:
    entity: "IE-TOURIST-BEHAVIOR-DATA"
    role: "evidence"
    status: { state: "confirmed" }

  OCC-MATSUI-03-006:
    entity: "IE-KEEP-TJUKURPA-STRONG"
    role: "context"
    status: { state: "confirmed" }

  OCC-MATSUI-04-001:
    entity: "IE-TJUKURPA-CONCEPT"
    role: "context"
    status: { state: "confirmed" }

  OCC-MATSUI-04-002:
    entity: "IE-PLACE-IDENTITY"
    role: "context"
    status: { state: "confirmed" }

  OCC-MATSUI-04-003:
    entity: "IE-OWNERSHIP-DIFFERENCE"
    role: "contrasts"
    status: { state: "confirmed" }

  OCC-MATSUI-05-001:
    entity: "IE-STAKEHOLDER-DILEMMA"
    role: "problem_core"
    status: { state: "confirmed" }

  OCC-MATSUI-05-002:
    entity: "IE-POLITICS-DEVICE"
    role: "mechanism"
    status: { state: "confirmed" }

  OCC-MATSUI-05-003:
    entity: "IE-TOURISM-ETHIC"
    role: "conclusion"
    status: { state: "confirmed" }

sections:
  SEC-MATSUI-01:
    anchorage: { view: "background", phase: "confirmed", domain: ["uluru", "sacred_site", "tourism"] }
    occurrences: ["OCC-MATSUI-01-001", "OCC-MATSUI-01-002", "OCC-MATSUI-01-003"]

  SEC-MATSUI-02:
    anchorage: { view: "observation_series", phase: "confirmed", domain: ["tourism_dynamics"] }
    occurrences: ["OCC-MATSUI-02-001", "OCC-MATSUI-02-002", "OCC-MATSUI-02-003", "OCC-MATSUI-02-004"]

  SEC-MATSUI-03:
    anchorage: { view: "problem", phase: "confirmed", domain: ["sacred_management", "stakeholders"] }
    occurrences: ["OCC-MATSUI-03-001", "OCC-MATSUI-03-002", "OCC-MATSUI-03-003", "OCC-MATSUI-03-004", "OCC-MATSUI-03-005", "OCC-MATSUI-03-006"]

  SEC-MATSUI-04:
    anchorage: { view: "background", phase: "confirmed", domain: ["indigenous_worldview", "land_ownership"] }
    occurrences: ["OCC-MATSUI-04-001", "OCC-MATSUI-04-002", "OCC-MATSUI-04-003"]

  SEC-MATSUI-05:
    anchorage: { view: "discussion", phase: "confirmed", domain: ["place_politics", "tourism_governance"] }
    occurrences: ["OCC-MATSUI-05-001", "OCC-MATSUI-05-002", "OCC-MATSUI-05-003"]

  SEC-APP-A:
    anchorage: { view: "background", phase: "confirmed", domain: ["bibliography"] }
    occurrences: []

relations: []

structure:
  sections:
    - "SEC-MATSUI-01"
    - "SEC-MATSUI-02"
    - "SEC-MATSUI-03"
    - "SEC-MATSUI-04"
    - "SEC-MATSUI-05"
    - "SEC-APP-A"
```
