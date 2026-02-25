# docs/dev/v1.0.2/anchorage.md
## Anchorage（解釈レイヤー）— v1.0.2 方針（Draft）

Generated: 2026-02-21T22:53:13.452053Z

この文書は IdeaMark YAML Spec v1.0.2 に向けた **anchorage の扱い**を定義する開発資料（差分・方針）です。
v1.0.2 では、anchorage の語彙（キー・値）を固定せず、実運用データの観測から収束を促す方針を採用します。

---

## 1. 目的と位置づけ

anchorage は、Section / Occurrence / Entity により構造化された内容に対して、
**人間およびAIが意味（解釈）を見出すための切り口（lens）**を付与するメタデータです。

- anchorage は `doc_type`（知識状態）でも `doc_profile`（文書形）でもありません。
- anchorage は **解釈の補助情報**であり、本文内容の真偽・正当性を規定しません。

---

## 2. v1.0.2 の基本方針（語彙は固定しない）

### 2.1 語彙自由（Model C）
v1.0.2 では anchorage の **キー・値の語彙を固定しません**。

- 未知のキー：許可
- 未知の値：許可
- 言語（日本語/英語/その他）：許可
- 独自語彙：許可

この方針は「LLM時代における解釈可能性」と「実運用からの語彙収束」を両立させるためのものです。

### 2.2 仕様が固定するもの（最小）
語彙は固定しませんが、**構文上の破壊**を防ぐために、次のみ strict に扱います。

- anchorage が存在する場合、anchorage は YAML mapping（object）であること

---

## 3. 構文ルール（Validation）

### 3.1 フィールドの有無
- `anchorage` は **任意（MAY）** とします。
  - ただし、解釈・再利用性の向上のため、著者は `anchorage` を付与することが望ましい（SHOULD）。

### 3.2 型（Strict）
`anchorage` が存在する場合：
- `anchorage` は **mapping/object（連想配列）でなければならない（MUST）**。
- mapping/object でない場合は Validation Error とします。

### 3.3 内容（Non-Strict）
- anchorage 配下のキー・値について、Validation は意味検査を行いません。
- 未知語彙・独自語彙・多言語語彙は Validation Error の原因になりません。
- 値の型（string/number/object/list 等）も、v1.0.2 では制限しません。

---

## 4. 推奨運用（非強制）

v1.0.2 では語彙を固定しませんが、相互運用性を高めるための推奨を置きます（SHOULD）。

### 4.1 値は短いラベルを推奨
- anchorage の値は、可能な範囲で **短い自然言語ラベル**（例：数語の文字列）を推奨します。
- ただし、説明が必要な場合は object にして補助情報を持たせてもよい。

### 4.2 言語メタの明示（任意）
語彙の言語混在による破壊を避けるため、必要に応じて言語メタを付与してよい（MAY）。

例：

```yaml
anchorage:
  lang: ja
  view: 背景
  phase: 設計
  lens: 意味機能
```

※ `lang` キー自体も固定語彙ではありません（推奨キーの一例）。

---

## 5. 例

### 5.1 最小例（自由語彙）
```yaml
anchorage:
  view: background
  phase: design
```

### 5.2 独自軸を追加する例
```yaml
anchorage:
  lens: "meaning-function"
  audience: "developer"
  time_window: "2026-Q1"
```

### 5.3 ネスト例（補助情報を含める）
```yaml
anchorage:
  lens:
    name: "meaning-function"
    note: "Roland Barthes-inspired lens; may evolve"
```

---

## 6. 互換性と将来拡張

- v1.0.2 は語彙を固定しないため、将来、推奨語彙セット（recommended vocabulary）を別成果物として追加しても後方互換になります。
- 将来の lint / describe / ls で、anchorage の観測・統計・収束支援を行う余地を残します。
  - v1.0.2 では、Validation はリモート参照や語彙辞書の解決を要求しません。

---

End of draft.
