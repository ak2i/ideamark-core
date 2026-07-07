# Doc CLI Contract v1.0.2
Generated: 2026-02-25T12:20:00Z

この文書は、IdeaMark / FlowMark / Responder-Bridge / TPCG など **複数ツールに共通適用**するための
Doc CLI Contract（操作IFの標準）を定義する。

- Doc CLI Contract は **文書形式そのものを規定しない**
- 代わりに、ツールが対象文書を操作するための **自己記述（describe）** と **検証（validate）** を中心に、
  呼び出し側（例：Responder-Bridge）が同一手順で利用できることを保証する

---

## 0. 用語

- **Tool Interface Contract（Layer A）**: ツール共通のCLI操作IF
- **Document Profile（Layer B）**: ツールが扱う文書形式・運用の自己記述（`describe <topic>` の中身）

---

## 1. Layer A: Tool Interface Contract（v1.0.2）

### 1.1 MUST コマンド

#### describe
```bash
<tool> describe <topic> [--format md|json] [common options...]
```

- `--format` 既定値は `md`（MUST）
- `--format json` は機械可読な構造化出力（MUST）
- 追加フォーマットは許容されるが、対応状況は `describe capabilities` で宣言する（MUST）

#### validate
```bash
<tool> validate [--format ndjson|json|md] [common options...] <input|->
```

- validate は “正しいかどうかを確認できる” ことを保証する（MUST）
- 具体的な診断レコード（NDJSONスキーマ等）は Layer B / tool 実装で拡張可能
- `--format` は任意。対応状況は `describe capabilities` で宣言し、未対応の場合は既定フォーマットで出力する（MUST）

### 1.2 MUST トピック（describe topics）

- `describe ai-authoring`
- `describe params`
- `describe capabilities`

#### describe capabilities 仕様の参照（MUST）

- `describe capabilities --format json` は次を満たすこと（MUST）
  - `docs/specs/v1.0.2/doc-cli-contract_v1.0.2_capabilities-schema.md`
- `describe capabilities --format md` は次のテンプレートに従うこと（MUST）
  - `docs/specs/v1.0.2/doc-cli-contract_v1.0.2_capabilities-md-template.md`

### 1.3 MUST フラグ

#### --help
- すべてのツールは `--help` を実装する（MUST）
- 出力内容は人間向けでよく、厳密な機械可読性は要求しない（MAY）

#### --version
- すべてのツールは `--version` を実装する（MUST）
- 推奨：`--version --format json`（SHOULD）
  - tool の SemVer
  - 対応する Doc CLI Contract バージョン
  - 対象文書仕様（document/yaml spec）のバージョン（該当する場合）

---

## 2. Layer A: 共通オプション（提案：SHOULD）

Responder-Bridge 等の呼び出し側が統一して扱えるよう、次のオプションを標準化する。

### 2.1 入出力
- `<input>` はファイルパスを受け取れる（SHOULD）
- `-` は stdin を意味する（SHOULD）
- 出力は既定で stdout（SHOULD）

### 2.2 フォーマット
- `--format <fmt>` を共通化する（SHOULD）
  - `describe`: `md|json`
  - `validate`: `ndjson|json|md`（ツールにより差異があってよいが、宣言は capabilities で行う）

### 2.3 ログ抑制
- `--quiet` : 最小出力（SHOULD）

### 2.4 厳格度（validate向け）
- `--strict` : 厳格モード（SHOULD）
- `--level <severity>` または `--fail-on <severity>` : 失敗とみなす最低レベル（SHOULD）
  - 例：`error|warning|info`
  - 実装の詳細は capabilities で宣言可能

---

## 3. Layer B: Document Profile（describe の責務）

Doc CLI Contract が固定するのは「topic名と目的」であり、内容はツールごとに異なる。

- `describe params`: 対象文書の生成/入力に必要な属性・IDルール・参照形式等
- `describe ai-authoring`: 人間/AI（LLM）が正しい文書を生成するためのガイド
- `describe capabilities`: ツールが実装するコマンド/オプション/フォーマットを宣言

### describe params / ai-authoring 仕様の参照（MUST）

- `describe params --format md|json` は次を満たすこと（MUST）
  - `docs/specs/v1.0.2/doc-cli-contract_v1.0.2_describe-params.md`
- `describe ai-authoring --format md|json` は次を満たすこと（MUST）
  - `docs/specs/v1.0.2/doc-cli-contract_v1.0.2_describe-ai-authoring.md`

---

## 4. validate 仕様の参照（MUST）

`validate` の共通仕様は別紙で定義する。

- `docs/specs/v1.0.2/doc-cli-contract_v1.0.2_validate-schema.md`

---

## 5. Evidence（注釈）は横断機構（別枠）

Evidence の表現は文書形式に依存し得るため、Layer A の必須コマンドには含めない。  
ただし横断オプションとして標準化する余地がある（例：`--emit-evidence` / `--attach`）。

---

## 6. Non-goals（v1.0.2）

- lint / normalize は本バージョンでは必須にしない（後続で検討）
- 派生コマンド（diff/profile/query/集合演算など）の追加を拘束しない

---

## Notes

- このリポジトリ内の `docs/specs/v1.0.2/` を参照すること。
- 将来的に `ideamark-core` への参照に移行する可能性がある。

---

End of contract.
