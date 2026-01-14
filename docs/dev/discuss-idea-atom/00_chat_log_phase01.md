---
ideamark_version: 1
title: "ロラン・バルトの写真論"
doc_id: "ideamark.concept-design.2026-01-11.akki-sample"
date: 2026-01-11
created_at: "2026-01-11"
tags: [ideamark-doc]
---

# Chat Archive: ロラン・バルトの写真論

## Meta

```yaml
started_at: 2026-01-11
participants:
    user: Akki
    assistant: ChatGPT5.2
intent: IdeaMarkの詳細な構造を決める過程の写真論の観点の付加による解決とサンプル生成の観測
domain: [ideamark, concept-design]
statu: exploratory
```

## Section 001 : ロラン・バルトの写真論を思い出す

```yaml
section_id: "sec-001"
anchorage:
  - view:background
  - phase:recall
  - phase:ignition
  - mode:observation
intent: |
    IdeaEntityのAtomic性を考えるにあたり、
    「意味がどこで発生するのか」という既存理論への参照点として、
    ロラン・バルトの写真論が想起された過程を観測する
```

> 最初のセクションは
>「ロラン・バルトの写真論を思い出す」的な内容

これは IdeaMark 的には：
* まだ「問題定義」ではない
* まだ「解決」でもない
* 思考が起動した瞬間の観測ログ

なので、Section の view は background / observation が最適です。

ポイント：
* タイトルは内容要約でOK
* intent は「このSectionを読む意味」を書く
* まだ IdeaMark 用語を無理に入れなくていい

### Occurrence 001 : 問いの発生

```yaml
- id: occ-001-001
  role: observation
  source: chatlog#turn-user-001
  note: |
    メディア論・意味論の文脈で、
    「写真にキャプションを与えることで意味が発生する」
    という理論を思い出そうとしたが、
    著者名が曖昧な状態で想起されている。
```

ポイント：
* タイトルは内容要約でOK
* intent は「このSectionを読む意味」を書く
* まだ IdeaMark 用語を無理に入れなくていい


## Section 002 : ロラン・バルトへの同定
```yaml
section_id: "sec-002"
anchorage:
  - view:background
  - phase:identification
  - phase:conceptualization
  - mode:explanation
intent: |
    IdeaEntityのAtomic性を考えるにあたり、
    「意味がどこで発生するのか」という既存理論への参照点として、
    ロラン・バルトの写真論が想起された過程を観測する
```

### IdeaEntitys : このセクションのIdeaEntity

写真論の使いたい部分の抽出

```yaml
idea_entities:
  - id: idea.image_text_anchorage
    payload: |
      画像は本来的に多義的であり、
      キャプションや説明文といった言語が付与されることで、
      その意味が特定の方向に固定・誘導されるという考え方。

      ロラン・バルトはこれを
      **アンカラージュ（anchorage）** と呼び、
      言語と画像が相補的に意味を生成する関係を
      **リレー（relay）** として区別した。

      この理論は、意味が「対象そのもの」に内在するのではなく、
      付与・配置・関係によって発生することを示している。
```

### Occurence 001 : ロラン・バルトへの同定

```yaml
- id: occ-002-001
  role: observation
  source: chatlog#turn-assistant-001
  instantiates: idea.image_text_anchorage
  note: |
    写真と言語の関係をめぐる理論として、
    ロラン・バルトの「アンカラージュ／リレー」が提示され、
    想起されていた関心対象が特定された。
```

ここで初めて instantiates が出てきます。

理由：ここで出てきたのは

* 単なる固有名詞ではなく
* 再利用可能な概念の核

だからです。

## Section 003 : バルト理論を IdeaMark 設計に引き寄せる
```yaml
section_id: "sec-003"
anchorage:
  - view:design
  - view:meta
  - phase:exploration
  - phase:conceptualization
  - mode:questioning
  - mode:reinterpretation
intent: |
  ロラン・バルトの写真論（anchorage / relay）を、
  IdeaMark における IdeaEntity / IdeaAtom の設計問題として再解釈し、
  既存理論が「答え」ではなく「設計素材」として
  どのように機能しうるかを探索する。
```

> このセクションでは、
> バルト理論を「正しく理解する」ことよりも、
> **IdeaMark の内部概念を設計するためにどう使えるか**
> という観点で再読・再配置を行う。

---

### Occurrence 001 : Akki による設計上の問いの提示

```yaml
- id: occ-003-001
  role: questioning
  source: chatlog#turn-user-003
  note: |
    ロラン・バルトの anchorage / relay の考え方をヒントに、
    IdeaMark における IdeaEntity / IdeaAtom の構成を検討しているが、
    現在の設計案では「意味がどこで発生し、どこで固定されるのか」
    がうまく着地していないという問題意識が提示された。

    IdeaMark 文書は Problem / Solution / 仮説 / 計画といった
    文脈的意味を持つ記録を扱うが、
    それらをデータベース的に蓄積・再利用する際に、
    意味を固定しすぎず、しかし操作可能に保つ必要がある、
    という設計上の緊張が明確化された。
```

**この Occurrence の性格**

* まだ仮説ではない
* まだ設計案でもない
* **設計探索を開始させる問い**

👉 Section 全体の **駆動力** になっている。

---

### Occurrence 002 : ChatGPT5.2 による理論的再構成の提示

```yaml
- id: occ-003-002
  role: explanation
  source: chatlog#turn-assistant-003
  instantiates:
    - idea.text_work_distinction
    - idea.enonce_like_unit
    - idea.non_central_core
  note: |
    ロラン・バルトの anchorage / relay を
    そのまま IdeaMark に適用するのではなく、
    「意味を一時的に固定する操作」と
    「意味を横断的に流通させる操作」
    として再定義する視点が提示された。

    あわせて、
    - バルト後期の Text / Work の区別
    - フーコーの「言表（énoncé）」
    - ドゥルーズの非中心化・生成的中心
    といった周辺理論を組み合わせることで、

    IdeaAtom を
    「意味を持たないが、文脈内で役割を果たす最小単位」
    として捉え、
    IdeaEntity を
    「視点とフェーズによって生成される収束体」
    として再定義できる可能性が示された。

    ここで提示されたのは最終解ではなく、
    IdeaMark の設計を進めるための
    概念的フレームの候補群である。
```

---

### IdeaEntities : このセクションで立ち上がった概念核（暫定）

```yaml
idea_entities:
  - id: idea.text_work_distinction
    payload: |
      バルト後期における Work / Text の区別。
      意味が固定された成果物ではなく、
      読まれるたびに生成される関係のネットワークとして
      文書を捉える視点。

  - id: idea.enonce_like_unit
    payload: |
      フーコーの「言表（énoncé）」に近い単位。
      真偽や完結性ではなく、
      文脈内で果たす役割によって規定される最小構成要素。

  - id: idea.non_central_core
    payload: |
      IdeaEntity における Core は
      固定された意味の中心ではなく、
      使用や視点によって一時的に生成される収束点である、
      という非中心化された捉え方。
```

## Section 004 : IdeaAtom を「薄いコア」として再定義する

```yaml
section_id: "sec-004"
anchorage:
  - view:design
  - view:meta
  - phase:structuring
  - phase:integration
  - mode:agreement
  - mode:proposal
intent: |
  IdeaMark における IdeaAtom / IdeaEntity の役割分担について、
  「意味は読む側で発生する」という前提に立ち、
  IdeaAtom を最小限かつ安定した構造として定義し直す。
  あわせて、roles / relations / anchors の配置レイヤを整理し、
  実装に耐える着地点を探索する。
```

> このセクションでは、
> バルト理論や周辺思想の参照を前提としつつ、
> **IdeaMark-core の内部構造として何を持ち、何を持たないか**
> を具体的に決めにいく。

---

### Occurrence 001 : Akki による設計方針の明確化

```yaml
- id: occ-004-001
  role: proposal
  source: chatlog#turn-user-004
  note: |
    IdeaEntity に無意識に意味を持たせる設計を避け、
    意味は IdeaMark 文書を人間や AI が読んだときに発生するもの、
    という立場を明確にする提案がなされた。

    IdeaMark 文書は、
    Section ごとに「意味の与え方」を記述し、
    Section 間の関係（順序・範囲・対立など）によって
    上位の意味構造を形成する。

    その中で IdeaAtom は、
    文脈が与えられれば意味を見出せる最小粒度として、
    単純なメタ構造・配列（ベクトル）として設計されるべき、
    という方針が提示された。

    Atom は機械的操作に必要な最小情報を持ちうるが、
    potential_roles や relations は
    具体機能に依存するため、
    今後の検討対象として切り分けることが示唆された。

    payload は当面テキストを想定しつつ、
    将来的には任意バイト列や構造化ベクトルを許容する。
```

**この Occurrence の性格**

* Section 003 の問いを受けた **立場表明**
* まだ仕様ではないが、**設計原則が明確化された瞬間**

---

### Occurrence 002 : ChatGPT5.2 による着地点案の提示

```yaml
- id: occ-004-002
  role: explanation
  source: chatlog#turn-assistant-004
  instantiates:
    - idea.atom_thin_core
    - idea.section_as_semantic_engine
    - idea.projection_layer
  note: |
    IdeaAtom を「薄い・安定・汎用」な単位として設計することに賛同し、
    Atom の責務を以下に限定する案が提示された。

    - 同一性（参照可能な id）
    - 内容（任意バイト列になり得る payload）
    - 最小メタ情報（media_type, hash など）
    - 軽量な anchor（意味固定の痕跡としての参照）

    roles / relations は Atom 自体に固定せず、
    解釈・推論・分類の結果として
    Projection（外部成果物）に逃がす構成が提案された。

    また、意味の主戦場は Atom ではなく Section / View にあり、
    Section は「意味を与える灌漑装置」として機能する、
    という整理が与えられた。

    この提案は最終仕様ではなく、
    IdeaMark-core の実装に向けた
    合理的な初期着地点として提示されている。
```

---

### IdeaEntities : このセクションで立ち上がった設計概念（暫定）

```yaml
idea_entities:
  - id: idea.atom_thin_core
    payload: |
      IdeaAtom は意味を持たないが、
      文脈が与えられれば意味が立ち上がる
      「薄く・安定した」最小単位であるという設計原則。

  - id: idea.section_as_semantic_engine
    payload: |
      意味の生成・固定・流動は
      Atom ではなく Section / View / Phase 側で行われる、
      という責務分離の考え方。

  - id: idea.projection_layer
    payload: |
      roles / relations / embeddings など、
      解釈や推論に依存する情報を
      Atom / Entity から分離し、
      Projection として外部管理する設計レイヤ。
```

---

Section 004 を分けたことの意味（重要）

* **Section 003**

  * 探索
  * 再解釈
  * 理論をどう使えるか
* **Section 004**

  * 合意形成
  * 設計原則の確定
  * 実装に向けた責務分離

👉 同じ「IdeaAtom」の話でも、
**Section を分けないと phase が混ざる**。

これはあなたが最初に言っていた
「Section ごとに意味の与え方を記述する」
という思想そのものです。

---


## Section 005 : 「IdeaAtom」という名称が孕む違和感
```yaml
section_id: "sec-005"
anchorage:
  - view:meta
  - view:design
  - phase:reflection
  - phase:integration
  - mode:questioning
  - mode:critique
intent: |
  IdeaAtom という名称が英語圏の学術的・設計的文脈で
  どのような含意を持つかを検討し、
  IdeaMark における「atomic」という概念が
  本質的不可分性ではなく運用上の状態であることを
  どのように表現すべきかを整理する。
```

> このセクションでは、
> 構造や機能の話ではなく、
> **「どう名付けるかが、どう誤解されるか」**
> というレイヤの問題を扱う。

---

### Occurrence 001 : Akki による命名への違和感の提示

```yaml
- id: occ-005-001
  role: questioning
  source: chatlog#turn-user-005
  note: |
    「IdeaAtom」という名称が、
    英語圏の学者や設計者の感覚において
    不可分性や本質的最小単位を強く含意してしまうのではないか、
    という違和感が提示された。

    IdeaAtom は IdeaEntity に内包される要素であり、
    特別に atomic であるとみなしているだけで、
    実際にそれ以上分解不可能であることは保証されない。

    また、IdeaEntity 自体も
    再帰的に IdeaEntity を内包できる論理構造であり、
    「実体」として固定的に存在するものではない。

    Content が本当に atomic かどうかは
    観測・運用・文脈に依存して不定であり、
    atomic であることは状態であって本質ではない、
    という前提が明確にされた。
```

**この Occurrence の性格**

* 実装上の問題ではない
* しかし **設計思想を誤解させうる危険点の指摘**
* 「言葉が構造を裏切る瞬間」の検出

---

### Occurrence 002 : ChatGPT5.2 による含意分析と代替整理

```yaml
- id: occ-005-002
  role: explanation
  source: chatlog#turn-assistant-005
  instantiates:
    - idea.epistemic_atomicity
    - idea.atomic_as_state
    - idea.naming_as_design_constraint
  note: |
    英語圏における atomic / atom という語が、
    不可分性・存在論的最小単位を強く含意する点が整理された。

    一方で、IdeaAtom が指しているのは
    ontological atom（存在論的原子）ではなく、
    epistemic atom（認識上・運用上の原子）であり、
    このズレが違和感の正体であると説明された。

    その上で、
    atomic を名詞ではなく状態・扱いとして表現する、
    あるいは IdeaEntity を唯一の存在論的単位とし、
    「atomic であるかどうか」は
    分解されていない状態として扱う方が、
    思想的・言語的に整合的であるという整理が提示された。

    命名は単なるラベルではなく、
    設計思想そのものを外部に伝達する制約条件であり、
    IdeaMark-core の理解可能性に直結する要素であることが強調された。
```

---

### IdeaEntities : このセクションで明確化された設計上の論点

```yaml
idea_entities:
  - id: idea.epistemic_atomicity
    payload: |
      atomic であることは本質的性質ではなく、
      認識・運用・文脈に依存して
      「そう扱われている」状態であるという考え方。

  - id: idea.atomic_as_state
    payload: |
      atomic は名詞（Atom）ではなく、
      分解されていないという状態・フラグとして
      表現されるべきだとする設計方針。

  - id: idea.naming_as_design_constraint
    payload: |
      命名は実装上の便宜ではなく、
      設計思想や存在論的前提を
      暗黙に規定してしまう制約条件であるという認識。
```

---

Section 005 を分けた意味（確認）

* **Section 004**

  * 構造設計
  * 責務分離
  * 実装の着地点
* **Section 005**

  * 命名
  * 存在論的含意
  * 誤解されないための調整

👉 これは **「細かい話」ではなく設計の最上流**です。

---

## Section 006 : Atomicity を「状態」として扱い、IdeaEntity を唯一の単位にする
```yaml
section_id: "sec-006"
anchorage:
  - view:design
  - view:meta
  - phase:convergence
  - phase:formalization
  - mode:agreement
  - mode:specification
intent: |
  「IdeaAtom」という名詞を前面に出さず、
  IdeaEntity を唯一の参照単位（存在論的単位）として採用する。
  その上で atomicity を本質的性質ではなく、
  Section / View / 操作によって成立する「状態（扱い）」として定義し、
  スキーマ・運用・説明（英語圏含む）に耐える形へ収束させる。
```

> このセクションでは、命名の議論を「用語整理」で終わらせず、
> **IdeaMark の存在論とスキーマ方針を確定**する。

---

### Occurrence 001 : Akki による最終方針（IdeaAtom を前面に出さない）

```yaml
- id: occ-006-001
  role: agreement
  source: chatlog#turn-user-006
  note: |
    IdeaAtom は実体というより概念上の便宜的表現であり、
    実務上は「ある IdeaEntity を atomic とみなす」という
    説明のときに呼ぶ程度でよい、という整理が提示された。

    したがって「IdeaAtom」という語の使用頻度を下げ、
    「atomic な IdeaEntity」あるいは
    「atomic として扱われる IdeaEntity」
    のような形容表現へ寄せることが提案された。

    atomic かどうかは内容の本質ではなく、
    運用・観測・文脈に依存して不定であるため、
    名詞化（Atom）より状態化（atomicity）が適切である。
```

---

### Occurrence 002 : ChatGPT5.2 による存在論・スキーマの確定案

```yaml
- id: occ-006-002
  role: specification
  source: chatlog#turn-assistant-006
  instantiates:
    - idea.entity_only_ontology
    - idea.atomicity_as_assumption
    - idea.atomicity_in_section_view
  note: |
    IdeaMark の存在論として「IdeaEntity しか存在しない」
    という方針が最も整合的であると整理された。

    atomicity は IdeaEntity の内在的性質ではなく、
    観測者やツールが文脈上置く仮定であり、
    「型」ではなく「扱い（状態）」である。

    実装上は、
    - children が空なら atomic とみなす
    - breakdown 操作により children が生成される
    といった方法で、
    atomicity を明示フラグにせず導出することも可能である。

    さらに、
    atomicity は Section / View に属する読み方の指定として説明でき、
    Entity 自体は中立であるという責務分離が示された。
```

---

### IdeaEntities : このセクションで確定した設計概念（暫定）

```yaml
idea_entities:
  - id: idea.entity_only_ontology
    payload: |
      IdeaMark における唯一の参照単位・概念単位として
      IdeaEntity を採用し、再帰的包含で表現する設計方針。

  - id: idea.atomicity_as_assumption
    payload: |
      atomic であることは本質的不可分性ではなく、
      観測者・ツール・文脈が置く仮定（扱い）であるという定義。
      したがって IdeaAtom という名詞は必須ではない。

  - id: idea.atomicity_in_section_view
    payload: |
      atomicity は Entity に内在させず、
      Section / View が「この範囲では atomic として読む」
      あるいは「ここで breakdown する」という読み方の指定として
      表現できる、という責務分離の考え方。
```

---

Section 006 のポイント（確認）

* Section 005 までの「違和感」は **設計方針へ収束した**
* 「Atom」ではなく「atomicity（状態）」へ
* Entity が中立、読み方（atomic / decomposable）は Section / View 側
* breakdown は **状態遷移（children が生える）**として自然に表現できる

---

## Section 007 : Section と IdeaEntity の間に解釈レイヤを差し込む
```yaml
section_id: "sec-007"
anchorage:
  - view:design
  - view:meta
  - phase:structuring
  - phase:exploration
  - mode:questioning
  - mode:proposal
intent: |
  ref なし・単一ドキュメントで閉じた最小構造として、
  Document > Section > (Occurrence) > IdeaEntity という骨格を採用し、
  Decision / View / Projection といった「解釈レイヤ」を
  Section と IdeaEntity のどこに置くべきか（スコープ設計）を整理する。
  目的は Entity を中立に保ちつつ、Section と出現（Occurrence）で
  読み方・役割・投影を扱える拡張余地を確保すること。
```

> このセクションでは、
> YAML/JSON といった表記形式は保留しつつ、
> **属性の置き場所（Section-level / Occurrence-level / Entity-level）**
> を原則として確定させる。

---

### Occurrence 001 : Akki による「原始的構造」からの設計方針提案

```yaml
- id: occ-007-001
  role: proposal
  source: chatlog#turn-user-007
  note: |
    コアの記述形式（YAML/JSON）を一旦保留し、
    ref 記述を持たない単一ドキュメントで閉じた形から始める方針が提示された。

    最小構造としては、
    - 1つの Document に複数の Section
    - Section 内に複数の IdeaEntity（IdeaEntity は再帰的に内包可能）
    を想定する。

    ただし Decision / View や IdeaEntity の Projection は、
    Section と IdeaEntity の間（あるいは Section 内で列挙される Entity の各要素）
    に対応する属性として表現される必要があり、
    この「属性の置き場所」をどう設計すべきかが次の論点として提示された。
```

---

### Occurrence 002 : ChatGPT5.2 によるスコープ原則と Occurrence 中間ノード案

```yaml
- id: occ-007-002
  role: explanation
  source: chatlog#turn-assistant-007
  instantiates:
    - idea.entity_neutral_principle
    - idea.section_vs_occurrence_scope
    - idea.occurrence_as_interpretation_node
    - idea.projection_placement_options
  note: |
    「解釈レイヤ」を誤って Entity に入れると Entity が重くなるか、
    Section に寄せすぎると Section が肥大化するため、
    最初に “属性の置き場所” を原則として決めるべきだと整理された。

    原則A：IdeaEntity は中立（意味論を持たない）
      - Entity は payload と入れ子（children）を担うのみ
      - 解釈（Decision / View / Projection）は Entity の外側へ

    原則B：解釈はスコープ分割する
      - Section-level：セクション全体の読み方（defaults）
      - Occurrence-level：この出現での読み（role/override/注釈/リンク）

    これを素直に表す構造として、
    Section が Entity を直接列挙するのではなく、
    中間ノードとして Occurrence を置き、
    Occurrence が entity を指して読み方・役割・投影を付与する案が提示された。

    さらに、View/Decision/Projection の置き場所について
    3案（Section-default + override / Occurrence全明示 / Projectionを外部化）
    が提示され、初期段階では
    「Section-default + override（Occurrence）」が最も実用的だと提案された。
```

---

### IdeaEntities : このセクションで整理された設計原則（暫定）

```yaml
idea_entities:
  - id: idea.entity_neutral_principle
    payload: |
      IdeaEntity は「素材」であり意味論を内包しない。
      解釈（View/Decision/Projection）は Entity の外に置く。

  - id: idea.section_vs_occurrence_scope
    payload: |
      解釈のスコープは2段で管理する：
      Section-level（defaults）と Occurrence-level（この出現での扱い）。

  - id: idea.occurrence_as_interpretation_node
    payload: |
      Section と Entity の間に Occurrence を置き、
      文書内の出現ごとに role / override / links / projection を付与できるようにする。
      同じ Entity が複数回出現する設計に強い。

  - id: idea.projection_placement_options
    payload: |
      Projection の格納は3段階の選択肢がある：
      1) Section-default + Occurrence override（初期おすすめ）
      2) Occurrence で完全明示（冗長になりやすい）
      3) sidecar に外部化（将来の正攻法）
```

## Section 008 : AIによる構造拡張の試行（機能的テスト）
```yaml
section_id: "sec-008"
anchorage:
  - view:design
  - view:meta
  - phase:exploration
  - phase:simulation
  - mode:experiment
  - mode:generation
intent: |
  Section 007 までに整理された設計原則を前提として、
  AI が自律的に Section / Occurrence / IdeaEntity を拡張生成することで、
  IdeaMark 文書がどの程度「書けて・読めて・増やせる」かを
  機能的にテストする。
  本セクション自体がその実験ログである。
```

> このセクションは、人間が最小セットを確定する前に、
> AI が **既存の設計原則だけを手がかりに**
> どこまで構造的に自然な拡張を行えるかを確認する試行である。

---

### Occurrence 001 : 既存セクション構造の再解釈
```yaml
- id: occ-008-001
  role: analysis
  source: ai.self_expansion
  note: |
    Section 001〜007 を再走査した結果、
    IdeaMark 文書はすでに以下の機能を満たしていると判断された。

    - Section ごとに phase / view / mode が一貫している
    - 同一トピックでも phase 遷移に応じて Section が分割されている
    - IdeaEntity は「概念核」としてのみ立ち上げられ、
      意味の確定は Section / Occurrence 側に寄せられている

    これは、最小スキーマを明示的に確定していないにもかかわらず、
    設計原則だけで文書が自己増殖可能であることを示唆している。
```

---

### Occurrence 002 : AIによる暗黙スキーマの抽出
```yaml
- id: occ-008-002
  role: hypothesis
  source: ai.self_expansion
  instantiates:
    - idea.implicit_minimal_schema
    - idea.section_driven_semantics
  note: |
    明示的な「最小セット定義」が存在しなくても、
    以下の暗黙的スキーマがすでに共有されていると推定される。

    - Section は意味付与の主単位である
    - Occurrence は「この文書内での出現」を表す中間ノードである
    - IdeaEntity は再利用可能な概念核であり中立である
    - anchorage は Section の読み方を規定する軽量タグ集合である

    この暗黙スキーマは、人間と AI のチャットを通じて
    漸進的に形成されたものであり、
    IdeaMark の「学習可能な構造」を示す事例となっている。
```

---

### IdeaEntities : 本セクションで生成されたメタ概念

```yaml
idea_entities:
  - id: idea.implicit_minimal_schema
    payload: |
      明示的に定義されていなくても、
      文書の生成・拡張を通じて共有される最小構造理解。
      IdeaMark における「暗黙のスキーマ」。

  - id: idea.section_driven_semantics
    payload: |
      意味の生成・解釈・固定は
      Section 単位で駆動されるという設計特性。
      AI が自律拡張を行う際の主要な手がかりとなる。
```

---

### 補足 : 本セクションの位置づけ

* Section 008 自体が **IdeaMark の機能テスト**
* 「最小セットを決める前に使ってみる」という判断が、
  設計の妥当性を検証する有効な方法であることを示している
* 今後、本セクションは以下の用途に再利用可能：
  - LLM に IdeaMark を教える教材
  - 拡張生成の品質評価用ログ
  - 最小スキーマ抽出の元データ