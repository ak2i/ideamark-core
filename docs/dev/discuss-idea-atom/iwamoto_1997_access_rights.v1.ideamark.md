# 田園レクリエーションとアクセス権 —イギリスの経験

```yaml
ideamark_version: 1
doc_id: "imdoc.case.uk_countryside_access.iwamoto1997.v1"
doc_type: "derived"
status: "in_progress"
created_at: "2026-01-15"
updated_at: "2026-01-15"
lang: "ja-JP"

refs:
  sources:
    - id: "iwamoto1997"
      uri: "http://hdl.handle.net/2433/278615"
      role: "source_material"
      description: "岩本純明(1997)『田園レクリエーションとアクセス権 —イギリスの経験』農耕の技術と文化 20, 38-63"
  related:
    - uri: "ideamark://patterns/PAT-01"
      relation: "similar"
      description: "Normative Code + Signage パターンとの関連"
    - uri: "ideamark://cases/SEC-UK-01"
      relation: "follow_up"
      description: "既存のUK事例セクションを補完"
```

## Meta
```yaml
intent: |
  イギリスにおける田園アクセス権の歴史的形成過程を記録し、
  観光・レクリエーション政策における「権利」と「許可」の設計パターンを抽出する。
  日本の富士箱根伊豆交流圏等への政策転写の参照点として機能させる。

breakdown_axes:
  - axis: "time_period"
    values: ["pre_1900", "interwar", "postwar_1949", "contemporary"]
    target_sections: ["SEC-IWAMOTO-03", "SEC-IWAMOTO-04"]

  - axis: "legal_type"
    values: ["right_of_way", "access_right", "permission"]
    target_sections: ["SEC-IWAMOTO-02"]

  - axis: "stakeholder"
    values: ["landowners", "ramblers", "government", "ngo"]
    target_sections: ["SEC-IWAMOTO-04"]

convergent_targets:
  - pattern: "ideamark://patterns/PAT-01"
    relevant_entities: ["IE-PAT-UK-DEFINITIVE-MAP"]

  - pattern: "ideamark://patterns/PAT-05"
    relevant_entities: ["IE-UK-NP-STRUCTURE"]

  - case: "ideamark://cases/SEC-KNG-IMPROVE-01"
    relevant_entities: ["IE-UK-LESSON-FOR-JAPAN"]
```

この文書は学術論文を IdeaMark 形式で構造化したもの。

---

## Section 000 : 文書の読み方（Meta）
```yaml
section_id: "SEC-META"
anchorage:
  view: "background"
  phase: "exploration"
  domain: ["document_meta"]
```

- breakdown 可能な軸は Meta の `breakdown_axes` に集約
- convergent 可能な対象は Meta の `convergent_targets` に集約

---

## Section 001 : イギリス田園景観の特質（背景）
```yaml
section_id: "SEC-IWAMOTO-01"
anchorage:
  view: "background"
  phase: "confirmed"
  domain: ["uk_countryside"]
```

イギリス田園景観が「人工的自然」であるという前提を整理する。

### OCC-IWAMOTO-01-001 : 景観認識
```yaml
occurrence_id: "OCC-IWAMOTO-01-001"
entity: "IE-UK-LANDSCAPE-01"
role: "context"
status:
  state: "confirmed"
```
田園景観が「自然そのもの」ではなく、歴史的に形成された人工的景観だという前提を提示する。

#### IdeaEntity: IE-UK-LANDSCAPE-01
生け垣や牧草地などの人為的営為の蓄積が景観を形作り、それが公衆アクセスの正当化根拠になっている。

### OCC-IWAMOTO-01-002 : フットパスの歴史的起源
```yaml
occurrence_id: "OCC-IWAMOTO-01-002"
entity: "IE-UK-FOOTPATH-ORIGIN"
role: "context"
status:
  state: "confirmed"
```
public footpath と bridleway が生活道路として成立し、権利として継承された経緯を示す。

#### IdeaEntity: IE-UK-FOOTPATH-ORIGIN
共同体の生活道として生まれた通行路が、囲い込み後も権利として維持されたという歴史的起源を整理する。

---

## Section 002 : 通行権の法的構造（制度分析）
```yaml
section_id: "SEC-IWAMOTO-02"
anchorage:
  view: "discussion"
  phase: "confirmed"
  domain: ["legal_framework"]
```

通行権とアクセス権の制度類型を整理する。

### OCC-IWAMOTO-02-001 : 通行権の3類型
```yaml
occurrence_id: "OCC-IWAMOTO-02-001"
entity: "IE-UK-ROW-TYPES"
role: "mechanism"
status:
  state: "confirmed"
```
公共通行権の類型と規模感を、制度の基礎データとして押さえる。

#### IdeaEntity: IE-UK-ROW-TYPES
footpath/bridleway/byway の3類型と割合、総延長の規模を提示して制度の輪郭を示す。

### OCC-IWAMOTO-02-002 : 通行権の成立方法
```yaml
occurrence_id: "OCC-IWAMOTO-02-002"
entity: "IE-UK-ROW-ESTABLISHMENT"
role: "mechanism"
status:
  state: "confirmed"
```
通行権がどのように成立するかのルートを整理する。

#### IdeaEntity: IE-UK-ROW-ESTABLISHMENT
明示的供用、推定的供用、創設命令の3経路が並存し、制度形成の多層性を示す。

### OCC-IWAMOTO-02-003 : アクセス権の類型
```yaml
occurrence_id: "OCC-IWAMOTO-02-003"
entity: "IE-UK-ACCESS-TYPES"
role: "mechanism"
status:
  state: "confirmed"
```
アクセス権が「面的移動」を対象にしつつも、制度的には限定的であることを示す。

#### IdeaEntity: IE-UK-ACCESS-TYPES
許可・協定・命令・共有地の4類型を通じて、権利の強さと持続性の違いを整理する。

### OCC-IWAMOTO-02-004 : 通行権とアクセス権の差異
```yaml
occurrence_id: "OCC-IWAMOTO-02-004"
entity: "IE-UK-ROW-VS-ACCESS"
role: "contrasts"
status:
  state: "confirmed"
```
線的移動の通行権と面的移動のアクセス権の境界を明示する。

#### IdeaEntity: IE-UK-ROW-VS-ACCESS
通行権は線的移動で逸脱は不法侵入、アクセス権は面的移動で自由度が高いが限定的である。

---

## Section 003 : 1949年国立公園法の構造（制度史）
```yaml
section_id: "SEC-IWAMOTO-03"
anchorage:
  view: "solution"
  phase: "confirmed"
  domain: ["national_parks"]
```

「保全」と「レクリエーション」の両立を狙った制度構造を整理する。

### OCC-IWAMOTO-03-001 : 国立公園法の目的
```yaml
occurrence_id: "OCC-IWAMOTO-03-001"
entity: "IE-UK-NP-PURPOSE"
role: "context"
status:
  state: "confirmed"
```
1949年法が掲げた政策目的を確認し、制度設計の方向性を把握する。

#### IdeaEntity: IE-UK-NP-PURPOSE
保全と利用の両立、保護区設置、通行権記録が目的に明記されている点が要点。

### OCC-IWAMOTO-03-002 : 制度構造（5つの柱）
```yaml
occurrence_id: "OCC-IWAMOTO-03-002"
entity: "IE-UK-NP-STRUCTURE"
role: "mechanism"
status:
  state: "confirmed"
```
国立公園法を支える制度的な支柱を整理する。

#### IdeaEntity: IE-UK-NP-STRUCTURE
委員会設置、管理体制、自然保護区、確定地図、長距離ルートの5柱が制度構造を構成する。

### OCC-IWAMOTO-03-003 : 土地所有構造という制約
```yaml
occurrence_id: "OCC-IWAMOTO-03-003"
entity: "IE-UK-NP-OWNERSHIP"
role: "context"
status:
  state: "confirmed"
```
国立公園が私有地中心という条件のもとで制度運用される点を示す。

#### IdeaEntity: IE-UK-NP-OWNERSHIP
私有地率の高さにより、公園指定が所有権を変えず、アクセス権確保は別途設計が必要になる。

---

## Section 004 : 土地所有とアクセスの緊張（価値競合）
```yaml
section_id: "SEC-IWAMOTO-04"
anchorage:
  view: "problem"
  phase: "confirmed"
  domain: ["property_rights"]
```

私的所有権と公共的利用権の間の緊張構造を把握する。

### OCC-IWAMOTO-04-001 : 土地所有の集中構造
```yaml
occurrence_id: "OCC-IWAMOTO-04-001"
entity: "IE-UK-OWNERSHIP-CONCENTRATION"
role: "problem_core"
status:
  state: "confirmed"
```
土地所有の集中がアクセス権拡大の基底的障壁であることを示す。

#### IdeaEntity: IE-UK-OWNERSHIP-CONCENTRATION
私有地の比率や大地主の占有率など、集中構造の具体像が提示される。

### OCC-IWAMOTO-04-002 : ステークホルダー群
```yaml
occurrence_id: "OCC-IWAMOTO-04-002"
entity: "IE-UK-STAKEHOLDERS"
role: "context"
status:
  state: "confirmed"
```
対立構造を理解するために主要アクターを整理する。

#### IdeaEntity: IE-UK-STAKEHOLDERS
土地所有者、徒歩旅行者協会、オープンスペース協会、ナショナル・トラストの役割が並置される。

### OCC-IWAMOTO-04-003 : 私的所有権 vs 公共的利用権
```yaml
occurrence_id: "OCC-IWAMOTO-04-003"
entity: "IE-UK-PRIVATE-PUBLIC-TENSION"
role: "contrasts"
status:
  state: "confirmed"
```
価値対立の中心となる論理の衝突を明文化する。

#### IdeaEntity: IE-UK-PRIVATE-PUBLIC-TENSION
所有権の排他性と公共的遺産観の対立が、制度設計上の未解決課題として残る。

### OCC-IWAMOTO-04-004 : 徒歩旅行運動の歴史
```yaml
occurrence_id: "OCC-IWAMOTO-04-004"
entity: "IE-UK-RAMBLING-MOVEMENT"
role: "context"
status:
  state: "confirmed"
```
アクセス運動の社会的基盤と時間軸を捉える。

#### IdeaEntity: IE-UK-RAMBLING-MOVEMENT
成立期、戦間期、戦後以降の3段階で運動が進展したことが分かる。

---

## Section 005 : イギリス的景観認識と保全思想（文化分析）
```yaml
section_id: "SEC-IWAMOTO-05"
anchorage:
  view: "background"
  phase: "confirmed"
  domain: ["landscape_perception"]
```

文化的・思想的基盤がアクセス権の議論を支える構造を整理する。

### OCC-IWAMOTO-05-001 : 景観認識
```yaml
occurrence_id: "OCC-IWAMOTO-05-001"
entity: "IE-UK-LANDSCAPE-PERCEPTION"
role: "context"
status:
  state: "confirmed"
```
文化的に形成された景観観がアクセス権議論の前提になっていることを示す。

#### IdeaEntity: IE-UK-LANDSCAPE-PERCEPTION
絵画的美への志向や「生きた景観」への愛着が、保全とアクセスの価値観を支える。

### OCC-IWAMOTO-05-002 : stewardship 概念
```yaml
occurrence_id: "OCC-IWAMOTO-05-002"
entity: "IE-UK-STEWARDSHIP"
role: "mechanism"
status:
  state: "confirmed"
```
土地所有者側の正当化概念として stewardship を整理する。

#### IdeaEntity: IE-UK-STEWARDSHIP
管理責任が所有権の正当化と保全義務の根拠として機能し、批判的視点も併記される。

### OCC-IWAMOTO-05-003 : 国民的遺産としての景観
```yaml
occurrence_id: "OCC-IWAMOTO-05-003"
entity: "IE-UK-HERITAGE-ARGUMENT"
role: "conclusion"
status:
  state: "confirmed"
```
公衆アクセスを権利として主張する論拠を提示する。

#### IdeaEntity: IE-UK-HERITAGE-ARGUMENT
景観を国民的遺産とみなす主張が、所有権優位の法構造に挑む理屈として描かれる。

---

## Section 006 : 政策的含意の抽出（改善仮説）
```yaml
section_id: "SEC-IWAMOTO-06"
anchorage:
  view: "solution"
  phase: "hypothesis"
  domain: ["policy_design"]
```

他地域への転写を意識した制度設計上の教訓を整理する。

### OCC-IWAMOTO-06-001 : 通行権システムの教訓
```yaml
occurrence_id: "OCC-IWAMOTO-06-001"
entity: "IE-UK-LESSON-ROW-SYSTEM"
role: "conclusion"
status:
  state: "confirmed"
```
通行権システムから抽出される制度設計上の要点をまとめる。

#### IdeaEntity: IE-UK-LESSON-ROW-SYSTEM
確定地図、歴史的連続性、維持管理責任、市民参加の4要素が学びとして整理される。

### OCC-IWAMOTO-06-002 : 漸進的制度形成の教訓
```yaml
occurrence_id: "OCC-IWAMOTO-06-002"
entity: "IE-UK-LESSON-INCREMENTAL"
role: "conclusion"
status:
  state: "confirmed"
```
制度形成が長期の社会運動と法整備の積層である点を示す。

#### IdeaEntity: IE-UK-LESSON-INCREMENTAL
19世紀から2000年までの節目が列挙され、漸進性が具体的に示される。

### OCC-IWAMOTO-06-003 : 日本への転写仮説
```yaml
occurrence_id: "OCC-IWAMOTO-06-003"
entity: "IE-UK-LESSON-FOR-JAPAN"
role: "transfer_hypothesis"
status:
  state: "provisional"
  confidence: 0.7
```
日本の事例に転写する際の設計観点を仮説として提示する。

#### IdeaEntity: IE-UK-LESSON-FOR-JAPAN
権利と許可の区別、確定地図、市民参加、維持管理責任の4視点が提案される。

### OCC-IWAMOTO-06-004 : 制度設計上のトレードオフ
```yaml
occurrence_id: "OCC-IWAMOTO-06-004"
entity: "IE-UK-LESSON-TRADEOFF"
role: "contrasts"
status:
  state: "confirmed"
```
制度選択の際に避けられない対立軸を整理する。

#### IdeaEntity: IE-UK-LESSON-TRADEOFF
権利/許可、線的/面的、法定化/協定化のトレードオフが示される。

---

## Section 007 : Pattern Catalog への接続
```yaml
section_id: "SEC-IWAMOTO-07"
anchorage:
  view: "solution"
  phase: "hypothesis"
  domain: ["ideamark_patterns"]
```

抽出知見を IdeaMark パターンライブラリに接続する。

### OCC-IWAMOTO-07-001 : 確定地図パターン
```yaml
occurrence_id: "OCC-IWAMOTO-07-001"
entity: "IE-PAT-UK-DEFINITIVE-MAP"
role: "source_pattern"
status:
  state: "confirmed"
```
確定地図を制度パターンとして抽象化する。

#### IdeaEntity: IE-PAT-UK-DEFINITIVE-MAP
ルート可視化と法的証拠化を中核とし、手続きや責任の構成要素が整理される。

### OCC-IWAMOTO-07-002 : 推定的供用パターン
```yaml
occurrence_id: "OCC-IWAMOTO-07-002"
entity: "IE-PAT-UK-ROW-PRESUMPTION"
role: "source_pattern"
status:
  state: "confirmed"
```
慣行利用を権利化する推定的供用をパターン化する。

#### IdeaEntity: IE-PAT-UK-ROW-PRESUMPTION
20年要件と反証可能性を軸に、慣行尊重と所有権保護の緊張が示される。

### OCC-IWAMOTO-07-003 : 市民運動による制度形成パターン
```yaml
occurrence_id: "OCC-IWAMOTO-07-003"
entity: "IE-PAT-UK-CITIZEN-MOVEMENT"
role: "source_pattern"
status:
  state: "confirmed"
```
長期的な市民運動が制度形成に与える力学を抽出する。

#### IdeaEntity: IE-PAT-UK-CITIZEN-MOVEMENT
組織化、象徴的行動、立法への働きかけ、継続性が構成要素として整理される。

---

## Appendix A : 書誌情報
```yaml
section_id: "SEC-APP-A"
anchorage:
  view: "background"
  phase: "confirmed"
  domain: ["bibliography"]
```

- Hoskins, W.G. 1955. The Making of the English Landscape. Hodder & Stoughton.
- Countryside Commission. 1996. Second National Rights of Way Condition Survey.
- Blunden, J. and Curry, N. 1990. A People's Charter? Forty Years of the National Parks and Access to the Countryside Act 1949. HMSO.
- Macewen, A. and Macewen, M. 1982. National Parks: Conservation or Cosmetics? George Allen and Unwin.
- Norton-Taylor, R. 1982. Whose Land Is It Anyway? Turnstone Press.
- Hill, H. 1980. Freedom to Roam: the Struggle for Access to Britain's Moors and Mountains. Moorland Publishing.
- Holt, A. 1995. The Origins and Early Days of The Ramblers' Association. Ramblers' Association.
- Williams, W.H. 1965. The Commons, Open Spaces and Footpaths Preservation Society 1865-1965. The Open Spaces Society.
- Waterson, M. 1994. The National Trust, The First Hundred Years. BBC Enterprises Limited.
- Shoard, M. 1980. The Theft of the Countryside. Maurice Temple Smith.
- Lowenthal, D. and Prince, H.C. 1964. The English landscape. The Geographical Review Vol.54(July): 309-346.
- Lowenthal, D. and Prince, H.C. 1965. English landscape Tastes. The Geographical Review Vol.55(April): 186-222.
- Wiener, M. 1981. English Culture and the Decline of the Industrial Spirit. Cambridge University Press.

---

## Appendix B : Breakdown / Convergent メモ
```yaml
section_id: "SEC-APP-B"
anchorage:
  view: "background"
  phase: "confirmed"
  domain: ["notes"]
```

- Breakdown の軸と適用箇所は Meta の `breakdown_axes` を参照
- Convergent の対象は Meta の `convergent_targets` を参照

---

## Entities Registry
```yaml
entities:
  IE-UK-LANDSCAPE-01:
    kind: "context"
    content: |
      イギリスの田園景観は「ありのままの自然」ではなく、
      生け垣（hedge）や牧草地など、何世紀にもわたる人間の営為によって
      作り上げられた「人工的自然」である。
      この認識が、土地への公衆アクセスの正当化根拠となる。
    atomic_state: true
    provenance:
      type: "extracted"
      sources: ["biblio:HOSKINS1955"]

  IE-UK-FOOTPATH-ORIGIN:
    kind: "context"
    content: |
      public footpath（公共歩道）と bridleway（乗馬道）は、
      かつての農村共同体における生活道路・作業道として発生し、
      囲い込み後も権利として維持された歴史を持つ。
    atomic_state: true
    provenance:
      type: "extracted"
      sources: ["biblio:HOSKINS1955"]

  IE-UK-ROW-TYPES:
    kind: "context"
    content: |
      public rights of way（公共通行権）は3種類：
      1. footpath：徒歩のみ
      2. bridleway：徒歩＋乗馬＋自転車
      3. byway open to all traffic：すべての交通手段

      総延長約169,000km（1994年時点）。
      footpath が78%、bridleway が17%、byway が5%。
    atomic_state: true
    provenance:
      type: "extracted"
      sources: ["biblio:COUNTRYSIDE_COMMISSION1996"]

  IE-UK-ROW-ESTABLISHMENT:
    kind: "mechanism"
    content: |
      通行権の成立方法は複数存在する。
    atomic_state: false
    children: ["IE-UK-ROW-EXPRESS", "IE-UK-ROW-PRESUMED", "IE-UK-ROW-ORDER"]

  IE-UK-ROW-EXPRESS:
    kind: "mechanism"
    content: |
      express dedication（明示的供用）：
      土地所有者が明瞭な意志表示により通行権を設定。
      freehold（自由土地保有権）を持つ者のみ可能。
    atomic_state: true

  IE-UK-ROW-PRESUMED:
    kind: "mechanism"
    content: |
      presumed dedication（推定的供用）：
      長期間（20年以上）の公衆利用により通行権が推定成立。
      1932年 Rights of Way Act、1980年 Highways Act で法定化。
      「一度 highway となれば、永遠に highway」の原則。
    atomic_state: true

  IE-UK-ROW-ORDER:
    kind: "mechanism"
    content: |
      public path creation orders：
      地方自治体が公益のため通行権を創設できる（1980年 Highways Act 26条）。
      definitive map（確定地図）への登載により法的効力。
    atomic_state: true

  IE-UK-ACCESS-TYPES:
    kind: "context"
    content: |
      right of access to areas of land（土地区域へのアクセス権）は
      通行権とは異なり、特定区域内を自由に歩き回る権利。
    atomic_state: false
    children: ["IE-UK-ACCESS-PERMISSION", "IE-UK-ACCESS-AGREEMENT", "IE-UK-ACCESS-ORDER", "IE-UK-ACCESS-COMMON"]

  IE-UK-ACCESS-PERMISSION:
    kind: "mechanism"
    content: |
      permission（許可）：
      土地所有者の明示的許可による。
      National Trust、Forestry Commission 等が多くの土地を開放。
      ただし法的権利ではなく、いつでも撤回可能。
    atomic_state: true

  IE-UK-ACCESS-AGREEMENT:
    kind: "mechanism"
    content: |
      access agreements（アクセス協定）：
      地方自治体がオープン・カントリーへのアクセスのため
      土地所有者と協定を締結（1949年 National Parks Act）。
      協定期間中は公衆のアクセス権が保障される。
    atomic_state: true

  IE-UK-ACCESS-ORDER:
    kind: "mechanism"
    content: |
      access orders（アクセス命令）：
      協定が成立しない場合、地方自治体が強制的にアクセス権を設定。
      ただし補償が必要であり、実際の適用例は極めて少ない。
    atomic_state: true

  IE-UK-ACCESS-COMMON:
    kind: "mechanism"
    content: |
      common land（共有地）へのアクセス：
      1925年 Law of Property Act により、都市近郊の共有地は
      運動・レクリエーション目的で公衆に開放。
      ただし農村部の共有地は対象外という制限あり。
    atomic_state: true

  IE-UK-ROW-VS-ACCESS:
    kind: "context"
    content: |
      通行権（right of way）とアクセス権（right of access）の本質的差異：

      - 通行権：線的（passage to and fro）、逸脱は trespass
      - アクセス権：面的（right to roam）、区域内を自由に移動

      イギリスでは通行権は確立しているが、
      面的アクセス権は依然として限定的・例外的である。
    atomic_state: true

  IE-UK-NP-PURPOSE:
    kind: "decision"
    content: |
      1949年 National Parks and Access to the Countryside Act の目的：
      (a) 自然美の保存・増進
      (b) 公衆のオープンエア・レクリエーション機会の提供
      (c) 上記目的のため自然保護区を設置
      (d) 公共通行権の記録と保護

      「保全」と「利用」の両立が法律上の目的として明記された。
    atomic_state: true
    provenance:
      type: "extracted"
      sources: ["biblio:BLUNDEN_CURRY1990"]

  IE-UK-NP-STRUCTURE:
    kind: "mechanism"
    content: |
      1949年法の制度構造は5つの柱から成る。
    atomic_state: false
    children: ["IE-UK-NP-COMMISSION", "IE-UK-NP-AUTHORITY", "IE-UK-NP-RESERVE", "IE-UK-NP-MAP", "IE-UK-NP-LDR"]

  IE-UK-NP-COMMISSION:
    kind: "mechanism"
    content: |
      National Parks Commission（国立公園委員会）の設置：
      国立公園の指定、AONB（特別自然美観地域）の指定を担当。
      後に Countryside Commission へ改組。
    atomic_state: true

  IE-UK-NP-AUTHORITY:
    kind: "mechanism"
    content: |
      国立公園管理体制：
      Joint Planning Board（合同計画委員会）または
      地方計画当局（local planning authority）が管理。
      独立した管理主体ではなく、既存自治体の枠組みを活用。
    atomic_state: true

  IE-UK-NP-RESERVE:
    kind: "mechanism"
    content: |
      nature reserve（自然保護区）制度：
      (a) 国家的自然保護区 - Nature Conservancy が管理
      (b) 地方自然保護区 - 地方自治体が設定
      厳格な保全を目的とする区域。
    atomic_state: true

  IE-UK-NP-MAP:
    kind: "mechanism"
    content: |
      definitive map（確定地図）制度：
      すべての公共通行権を地図上に記録し、法的証拠とする。
      draft map → 異議申立 → 確定 の手続き。
    atomic_state: true

  IE-UK-NP-LDR:
    kind: "mechanism"
    content: |
      Long-Distance Routes（長距離ルート）制度：
      複数の通行権を接続し、連続した長距離歩道を整備。
      Pennine Way（約400km）等が代表例。
    atomic_state: true

  IE-UK-NP-OWNERSHIP:
    kind: "constraint"
    content: |
      イギリス国立公園の特徴的制約：土地の大部分が私有地である。

      例：Lake District - 農用地57%、私有地率90%以上
      例：Peak District - 農用地80%

      したがって国立公園指定は土地所有権に影響せず、
      アクセス権は別途、協定や通行権で確保する必要がある。
    atomic_state: true
    provenance:
      type: "extracted"
      sources: ["biblio:MACEWEN1982"]

  IE-UK-OWNERSHIP-CONCENTRATION:
    kind: "constraint"
    content: |
      イギリスの土地所有構造は極めて集中的である：

      - 農用地の80%以上が私有地
      - 1919年以降、自作農化が進展（1930年37%→1978年64%）
      - しかし大土地所有は依然存続
      - 5000エーカー（2000ha）以上の大地主が全農地の約20%を所有

      この所有構造が、アクセス権拡大の構造的障壁となっている。
    atomic_state: true
    provenance:
      type: "extracted"
      sources: ["biblio:NORTON-TAYLOR1982"]

  IE-UK-STAKEHOLDERS:
    kind: "stakeholder"
    content: |
      田園アクセスをめぐるステークホルダー群。
    atomic_state: false
    children: ["IE-UK-SH-LANDOWNERS", "IE-UK-SH-RAMBLERS", "IE-UK-SH-OPEN-SPACES", "IE-UK-SH-NATIONAL-TRUST"]

  IE-UK-SH-LANDOWNERS:
    kind: "stakeholder"
    content: |
      土地所有者（地主・自作農）：
      所有権に基づく排他的利用権を主張。
      trespass（不法侵入）に対する法的保護を重視。
      一部は保全や景観管理の担い手として自己認識。
    atomic_state: true

  IE-UK-SH-RAMBLERS:
    kind: "stakeholder"
    content: |
      Ramblers' Association（徒歩旅行者協会、1935年設立）：
      アクセス権の拡大を求める市民運動の中核。
      通行権の保護・創設、right to roam の法制化を主張。
      会員数は1990年代に約10万人。
    atomic_state: true
    provenance:
      type: "extracted"
      sources: ["biblio:HOLT1995"]

  IE-UK-SH-OPEN-SPACES:
    kind: "stakeholder"
    content: |
      Open Spaces Society（オープンスペース協会、1865年設立）：
      共有地・オープンスペースの保全を目的とする最古の市民団体。
      共有地登録運動、フットパス保護運動の先駆。
    atomic_state: true
    provenance:
      type: "extracted"
      sources: ["biblio:WILLIAMS1965"]

  IE-UK-SH-NATIONAL-TRUST:
    kind: "stakeholder"
    content: |
      National Trust（ナショナル・トラスト、1895年設立）：
      歴史的建造物・自然景観の保全と公開を目的。
      1995年時点で273,000haの土地を所有・管理。
      会員数約300万人（1997年時点）。
    atomic_state: true
    provenance:
      type: "extracted"
      sources: ["biblio:WATERSON1994"]

  IE-UK-PRIVATE-PUBLIC-TENSION:
    kind: "problem"
    content: |
      私的所有権と公共的利用権の間の構造的緊張：

      土地所有者側の論理：
      - 所有権は絶対的権利であり、アクセス許可は恩恵
      - 無秩序なアクセスは農業・狩猟・環境に悪影響
      - stewardship（管理責任）として景観を維持している

      アクセス推進側の論理：
      - 田園景観は国民共通の遺産（national heritage）
      - 歴史的に存在した慣行的アクセスを回復すべき
      - レクリエーションは citizen right（市民権）の一部

      この緊張は制度設計上、未解決のまま継続している。
    atomic_state: true

  IE-UK-RAMBLING-MOVEMENT:
    kind: "context"
    content: |
      徒歩旅行運動（rambling movement）の歴史的展開。
    atomic_state: false
    children: ["IE-UK-RAMBLING-ORIGIN", "IE-UK-RAMBLING-INTERWAR", "IE-UK-RAMBLING-POSTWAR"]

  IE-UK-RAMBLING-ORIGIN:
    kind: "context"
    content: |
      19世紀後半〜20世紀初頭：
      都市労働者のレクリエーションとして徒歩旅行が普及。
      「イギリス人は歩く民族である」（Lowenthal and Prince）。

      1870年代以降、フットパス保護運動が組織化。
      Peak District Federation（1894年）等の団体結成。
    atomic_state: true
    provenance:
      type: "extracted"
      sources: ["biblio:LOWENTHAL_PRINCE1964"]

  IE-UK-RAMBLING-INTERWAR:
    kind: "context"
    content: |
      戦間期（1920-30年代）：
      徒歩旅行が大衆的レジャーとして定着。
      週末には数万人がピーク地方等に押し寄せる。

      1932年 Kinder Scout mass trespass：
      約500人がピーク地方の私有地に集団侵入。
      アクセス権運動の象徴的事件となる。
    atomic_state: true
    provenance:
      type: "extracted"
      sources: ["biblio:HILL1980"]

  IE-UK-RAMBLING-POSTWAR:
    kind: "context"
    content: |
      戦後〜現代：
      1949年法による部分的成果（国立公園・通行権保護）。
      しかし right to roam は実現せず。

      運動は継続し、2000年 Countryside and Rights of Way Act で
      ようやくオープンカントリーへの面的アクセス権が法制化。
      （本論文執筆時点では未実現）
    atomic_state: true

  IE-UK-LANDSCAPE-PERCEPTION:
    kind: "context"
    content: |
      イギリスにおける景観認識の特質：

      - wilderness（原生自然）ではなく picturesque（絵画的美）を重視
      - 人間の手が入った「生きた景観」（living landscape）への愛着
      - 農村を「産業社会の対極」「本来のイギリス」として理想化

      この認識は、工業化・都市化への反発として19世紀に形成された。
      景観保全運動とアクセス権運動は同根の文化的基盤を持つ。
    atomic_state: true
    provenance:
      type: "extracted"
      sources: ["biblio:LOWENTHAL_PRINCE1965", "biblio:WIENER1981"]

  IE-UK-STEWARDSHIP:
    kind: "context"
    content: |
      stewardship（管理責任）概念：

      土地所有者は単なる所有者ではなく、
      景観の「管理人」（steward）・「保護者」（custodian）である
      という自己認識。

      この概念は：
      - 所有権の正当化根拠として機能
      - 同時に保全義務の根拠としても機能
      - アクセス許可の「恩恵」的性格を正当化

      しかし批判者（Shoard等）は、
      実際には景観破壊を行いながら stewardship を主張する矛盾を指摘。
    atomic_state: true
    provenance:
      type: "extracted"
      sources: ["biblio:SHOARD1980"]

  IE-UK-HERITAGE-ARGUMENT:
    kind: "hypothesis"
    content: |
      「国民的遺産」（national heritage）としての景観という主張：

      アクセス権推進派の論理：
      - 田園景観は特定の所有者のものではなく国民共通の遺産
      - 歴史的に形成された景観は公共財的性格を持つ
      - したがって公衆アクセスは「権利」であり「恩恵」ではない

      この主張は、所有権の絶対性を相対化する論拠となるが、
      法的には依然として所有権が優位である。
    atomic_state: true

  IE-UK-LESSON-ROW-SYSTEM:
    kind: "summary"
    content: |
      通行権（rights of way）システムからの教訓：

      1. 法的確定性：definitive map による権利の可視化・法定化
      2. 歴史的連続性：「一度 highway となれば永遠に highway」
      3. 維持管理責任：土地所有者の維持義務（stiles, gates の管理等）
      4. 市民参加：draft map への異議申立手続き

      これらは「権利」として確立したアクセスの制度設計パターン。
    atomic_state: true

  IE-UK-LESSON-INCREMENTAL:
    kind: "summary"
    content: |
      漸進的制度形成の教訓：

      イギリスのアクセス権は一挙に確立したのではなく、
      150年以上にわたる市民運動・立法・判例の積み重ねで形成された。

      - 1865年 Open Spaces Society 設立
      - 1932年 Rights of Way Act（推定的供用の法定化）
      - 1949年 National Parks Act（国立公園・通行権保護）
      - 2000年 CROW Act（面的アクセス権の法制化）

      制度は社会的合意の漸進的形成を反映する。
    atomic_state: true

  IE-UK-LESSON-FOR-JAPAN:
    kind: "transfer_hypothesis"
    content: |
      日本（富士箱根伊豆交流圏等）への転写仮説：

      1. 権利と許可の区別：
         - 現状は「許可」ベースのアクセス管理が多い
         - 「権利」として確立する場合の制度設計が参照点

      2. 確定地図の整備：
         - 利用可能ルートの法的確定と可視化
         - デジタル時代には GIS との統合が可能

      3. 市民参加の制度化：
         - ルート設定・変更への異議申立手続き
         - 長期的なステークホルダー合意形成

      4. 維持管理責任の明確化：
         - 誰が何を維持するかの明文化
         - 財源ループ（PAT-04）との接続
    atomic_state: true

  IE-UK-LESSON-TRADEOFF:
    kind: "risk"
    content: |
      制度設計上のトレードオフ：

      権利 vs 許可：
      - 権利として確立 → 安定性・予測可能性が高いが柔軟性が低い
      - 許可として運用 → 柔軟性が高いが不安定・恣意的になりうる

      線的 vs 面的：
      - 通行権（線的）→ 管理容易、資源影響限定的
      - アクセス権（面的）→ 自由度高いが管理困難、資源影響大

      法定化 vs 協定化：
      - 法定化 → 強制力あるが社会的合意が前提
      - 協定化 → 合意ベースだが実効性に限界

      これらのトレードオフは、対象地域の特性に応じて選択される。
    atomic_state: true

  IE-PAT-UK-DEFINITIVE-MAP:
    kind: "pattern"
    content: |
      パターン：Definitive Map（確定地図）

      問題：アクセス可能なルートが不明確で紛争が生じる
      解決：すべての公共通行権を地図上に記録し法的証拠とする

      構成要素：
      - 地図の作成・更新手続き
      - 異議申立・確定手続き
      - 法的効力の付与
      - 維持管理責任の明確化

      トレードオフ：
      - 作成コスト vs 紛争解決コスト
      - 硬直性 vs 法的安定性

      Note: Normative Code + Signage の法的強化版。
    atomic_state: true

  IE-PAT-UK-ROW-PRESUMPTION:
    kind: "pattern"
    content: |
      パターン：Presumed Dedication（推定的供用）

      問題：歴史的に利用されてきたルートの法的地位が不明確
      解決：長期間（20年）の公衆利用により通行権の成立を推定

      構成要素：
      - 利用期間の要件（20年）
      - 所有者の異議がないことの要件
      - 推定を覆す証拠の扱い

      トレードオフ：
      - 慣行の尊重 vs 所有権の保護
      - 証拠収集の困難さ
    atomic_state: true

  IE-PAT-UK-CITIZEN-MOVEMENT:
    kind: "pattern"
    content: |
      パターン：Citizen Movement for Access（市民運動による制度形成）

      問題：既存の所有権体制がアクセス拡大を阻む
      解決：市民運動による長期的な社会的合意形成と立法化

      構成要素：
      - 市民団体の組織化（Open Spaces Society, Ramblers' Association等）
      - 象徴的行動（mass trespass等）
      - 立法への働きかけ
      - 長期的な運動継続（150年以上）

      トレードオフ：
      - 時間コスト vs 合意の持続性
      - 対立的手法 vs 協調的手法
    atomic_state: true

occurrences:
  OCC-IWAMOTO-01-001:
    entity: "IE-UK-LANDSCAPE-01"
    role: "context"
    status: { state: "confirmed" }

  OCC-IWAMOTO-01-002:
    entity: "IE-UK-FOOTPATH-ORIGIN"
    role: "context"
    status: { state: "confirmed" }

  OCC-IWAMOTO-02-001:
    entity: "IE-UK-ROW-TYPES"
    role: "mechanism"
    status: { state: "confirmed" }

  OCC-IWAMOTO-02-002:
    entity: "IE-UK-ROW-ESTABLISHMENT"
    role: "mechanism"
    status: { state: "confirmed" }

  OCC-IWAMOTO-02-003:
    entity: "IE-UK-ACCESS-TYPES"
    role: "mechanism"
    status: { state: "confirmed" }

  OCC-IWAMOTO-02-004:
    entity: "IE-UK-ROW-VS-ACCESS"
    role: "contrasts"
    status: { state: "confirmed" }

  OCC-IWAMOTO-03-001:
    entity: "IE-UK-NP-PURPOSE"
    role: "context"
    status: { state: "confirmed" }

  OCC-IWAMOTO-03-002:
    entity: "IE-UK-NP-STRUCTURE"
    role: "mechanism"
    status: { state: "confirmed" }

  OCC-IWAMOTO-03-003:
    entity: "IE-UK-NP-OWNERSHIP"
    role: "context"
    status: { state: "confirmed" }

  OCC-IWAMOTO-04-001:
    entity: "IE-UK-OWNERSHIP-CONCENTRATION"
    role: "problem_core"
    status: { state: "confirmed" }

  OCC-IWAMOTO-04-002:
    entity: "IE-UK-STAKEHOLDERS"
    role: "context"
    status: { state: "confirmed" }

  OCC-IWAMOTO-04-003:
    entity: "IE-UK-PRIVATE-PUBLIC-TENSION"
    role: "contrasts"
    status: { state: "confirmed" }

  OCC-IWAMOTO-04-004:
    entity: "IE-UK-RAMBLING-MOVEMENT"
    role: "context"
    status: { state: "confirmed" }

  OCC-IWAMOTO-05-001:
    entity: "IE-UK-LANDSCAPE-PERCEPTION"
    role: "context"
    status: { state: "confirmed" }

  OCC-IWAMOTO-05-002:
    entity: "IE-UK-STEWARDSHIP"
    role: "mechanism"
    status: { state: "confirmed" }

  OCC-IWAMOTO-05-003:
    entity: "IE-UK-HERITAGE-ARGUMENT"
    role: "conclusion"
    status: { state: "confirmed" }

  OCC-IWAMOTO-06-001:
    entity: "IE-UK-LESSON-ROW-SYSTEM"
    role: "conclusion"
    status: { state: "confirmed" }

  OCC-IWAMOTO-06-002:
    entity: "IE-UK-LESSON-INCREMENTAL"
    role: "conclusion"
    status: { state: "confirmed" }

  OCC-IWAMOTO-06-003:
    entity: "IE-UK-LESSON-FOR-JAPAN"
    role: "transfer_hypothesis"
    status:
      state: "provisional"
      confidence: 0.7

  OCC-IWAMOTO-06-004:
    entity: "IE-UK-LESSON-TRADEOFF"
    role: "contrasts"
    status: { state: "confirmed" }

  OCC-IWAMOTO-07-001:
    entity: "IE-PAT-UK-DEFINITIVE-MAP"
    role: "source_pattern"
    status: { state: "confirmed" }

  OCC-IWAMOTO-07-002:
    entity: "IE-PAT-UK-ROW-PRESUMPTION"
    role: "source_pattern"
    status: { state: "confirmed" }

  OCC-IWAMOTO-07-003:
    entity: "IE-PAT-UK-CITIZEN-MOVEMENT"
    role: "source_pattern"
    status: { state: "confirmed" }

sections:
  SEC-META:
    anchorage: { view: "background", phase: "exploration", domain: ["document_meta"] }
    occurrences: []

  SEC-IWAMOTO-01:
    anchorage: { view: "background", phase: "confirmed", domain: ["uk_countryside"] }
    occurrences: ["OCC-IWAMOTO-01-001", "OCC-IWAMOTO-01-002"]

  SEC-IWAMOTO-02:
    anchorage: { view: "discussion", phase: "confirmed", domain: ["legal_framework"] }
    occurrences: ["OCC-IWAMOTO-02-001", "OCC-IWAMOTO-02-002", "OCC-IWAMOTO-02-003", "OCC-IWAMOTO-02-004"]

  SEC-IWAMOTO-03:
    anchorage: { view: "solution", phase: "confirmed", domain: ["national_parks"] }
    occurrences: ["OCC-IWAMOTO-03-001", "OCC-IWAMOTO-03-002", "OCC-IWAMOTO-03-003"]

  SEC-IWAMOTO-04:
    anchorage: { view: "problem", phase: "confirmed", domain: ["property_rights"] }
    occurrences: ["OCC-IWAMOTO-04-001", "OCC-IWAMOTO-04-002", "OCC-IWAMOTO-04-003", "OCC-IWAMOTO-04-004"]

  SEC-IWAMOTO-05:
    anchorage: { view: "background", phase: "confirmed", domain: ["landscape_perception"] }
    occurrences: ["OCC-IWAMOTO-05-001", "OCC-IWAMOTO-05-002", "OCC-IWAMOTO-05-003"]

  SEC-IWAMOTO-06:
    anchorage: { view: "solution", phase: "hypothesis", domain: ["policy_design"] }
    occurrences: ["OCC-IWAMOTO-06-001", "OCC-IWAMOTO-06-002", "OCC-IWAMOTO-06-003", "OCC-IWAMOTO-06-004"]

  SEC-IWAMOTO-07:
    anchorage: { view: "solution", phase: "hypothesis", domain: ["ideamark_patterns"] }
    occurrences: ["OCC-IWAMOTO-07-001", "OCC-IWAMOTO-07-002", "OCC-IWAMOTO-07-003"]

  SEC-APP-A:
    anchorage: { view: "background", phase: "confirmed", domain: ["bibliography"] }
    occurrences: []

  SEC-APP-B:
    anchorage: { view: "background", phase: "confirmed", domain: ["notes"] }
    occurrences: []

relations: []

structure:
  sections:
    - "SEC-META"
    - "SEC-IWAMOTO-01"
    - "SEC-IWAMOTO-02"
    - "SEC-IWAMOTO-03"
    - "SEC-IWAMOTO-04"
    - "SEC-IWAMOTO-05"
    - "SEC-IWAMOTO-06"
    - "SEC-IWAMOTO-07"
    - "SEC-APP-A"
    - "SEC-APP-B"
```
