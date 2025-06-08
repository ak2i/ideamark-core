# Tools for IdeaMark Core

This directory contains helper scripts and utilities for managing, validating, and visualizing IdeaMark patterns.

---

## Tool Categories

### ✅ Validation
- Schema validation for `.yaml` files against `/schema/ideamark.schema.yaml`.

### 🔄 Conversion
- Format conversion: YAML ↔ JSON ↔ Markdown.

### 🔗 Composition / Merge
- **Pattern Merge Tool (`merge_tool.py`)** - Comprehensive CLI tool for merging multiple IdeaMark patterns using sophisticated merge strategies.

### 📊 Visualization
- Scripts to output pattern graphs using DOT, Mermaid, or GraphQL-like structures.

---

## Available Tools

### パターンマージツール (`merge_tool.py`)

複数のIdeaMarkパターンを高度なマージ戦略を使用して結合する包括的なCLIツールです。

#### セットアップ

1. **依存関係のインストール**
   ```bash
   cd tools/
   pip install -r requirements.txt
   ```

2. **LLMプロバイダーの設定（オプション）**
   
   synthesis戦略を使用する場合は、環境変数を設定してください：
   ```bash
   # OpenAI
   export OPENAI_API_KEY="your-openai-api-key"
   
   # Anthropic
   export ANTHROPIC_API_KEY="your-anthropic-api-key"
   ```

3. **インストールの確認**
   ```bash
   python merge_tool.py --help
   ```

#### 使用方法

**基本構文:**
```bash
python merge_tool.py --refs <A.ref.yaml> <B.ref.yaml> [<C.ref.yaml> ...] \
    [--intent union] [--strategy prefer] [--priority A B C] [--out <path>]
```

**マージ戦略:**
- `manual` - 手動解決用のTODOプレースホルダーを残す
- `prefer` - 優先順位を使用して競合を解決
- `annotate` - ソース注釈付きですべてのバージョンを含める
- `synthesis` - LLMを使用して統合されたコンテンツを生成

**使用例:**

1. **prefer戦略を使用した基本的なマージ:**
   ```bash
   python merge_tool.py \
     --refs ../refs/agri-mobility-platform-pivot.ref.yaml \
     --refs ../refs/fisherman-direct-ecommerce.ref.yaml \
     --strategy prefer \
     --out merged_pattern.yaml
   ```

2. **3つのファイルを生成するディレクトリ出力:**
   ```bash
   python merge_tool.py \
     --refs ../refs/pattern1.ref.yaml \
     --refs ../refs/pattern2.ref.yaml \
     --strategy prefer \
     --out merged_output/
   ```
   以下のファイルが作成されます:
   - `merged_output/patterns/merged-<uuid>.yaml`
   - `merged_output/refs/merged-<uuid>.ref.yaml`
   - `merged_output/summary/merged-<uuid>.md`

3. **手動競合解決:**
   ```bash
   python merge_tool.py \
     --refs ../refs/pattern1.ref.yaml \
     --refs ../refs/pattern2.ref.yaml \
     --strategy manual \
     --out manual_merge.yaml
   ```

4. **優先順位ベースのマージ:**
   ```bash
   python merge_tool.py \
     --refs ../refs/pattern1.ref.yaml \
     --refs ../refs/pattern2.ref.yaml \
     --strategy prefer \
     --priority "IdeaMark-123 IdeaMark-456" \
     --out result.yaml
   ```

5. **LLM支援による統合:**
   ```bash
   python merge_tool.py \
     --refs ../refs/pattern1.ref.yaml \
     --refs ../refs/pattern2.ref.yaml \
     --strategy synthesis \
     --out synthesized.yaml
   ```

6. **ソース追跡付きの注釈マージ:**
   ```bash
   python merge_tool.py \
     --refs ../refs/pattern1.ref.yaml \
     --refs ../refs/pattern2.ref.yaml \
     --strategy annotate \
     --out annotated_merge.yaml
   ```

#### テスト方法

**1. ツールのインストール確認:**
```bash
cd tools/
python merge_tool.py --help
```

**2. サンプルパターンでのテスト:**
```bash
# prefer戦略のテスト
python merge_tool.py \
  --refs ../refs/agri-mobility-platform-pivot.ref.yaml \
  --refs ../refs/fisherman-direct-ecommerce.ref.yaml \
  --strategy prefer \
  --out test_prefer.yaml

# スキーマに対する出力の検証
python validate_output.py test_prefer.yaml ../schema/ideamark.schema.yaml
```

**3. すべてのマージ戦略のテスト:**
```bash
# Manual戦略
python merge_tool.py --refs ../refs/agri-mobility-platform-pivot.ref.yaml --refs ../refs/fisherman-direct-ecommerce.ref.yaml --strategy manual --out test_manual/

# Annotate戦略  
python merge_tool.py --refs ../refs/agri-mobility-platform-pivot.ref.yaml --refs ../refs/fisherman-direct-ecommerce.ref.yaml --strategy annotate --out test_annotate/

# Synthesis戦略（APIキーが必要）
python merge_tool.py --refs ../refs/agri-mobility-platform-pivot.ref.yaml --refs ../refs/fisherman-direct-ecommerce.ref.yaml --strategy synthesis --out test_synthesis/

# すべての出力を検証
python validate_output.py test_manual ../schema/ideamark.schema.yaml
python validate_output.py test_annotate ../schema/ideamark.schema.yaml  
python validate_output.py test_synthesis ../schema/ideamark.schema.yaml
```

**4. エラーハンドリングのテスト:**
```bash
# 無効な参照ファイルでのテスト
python merge_tool.py --refs nonexistent.ref.yaml --refs ../refs/agri-mobility-platform-pivot.ref.yaml --strategy prefer --out test_error.yaml

# 到達不可能なURIでのテスト（一時的にrefファイルを変更）
# ネットワークリトライ動作が表示されるはずです
```

#### 設定

**デフォルト設定 (`config/default.yaml`):**
```yaml
merge:
  default_intent: union
  default_strategy: prefer
  
llm:
  providers:
    openai:
      model: gpt-4
      max_tokens: 2000
      temperature: 0.3
    anthropic:
      model: claude-3-sonnet-20240229
      max_tokens: 2000
      temperature: 0.3
  fallback_strategy: manual
  
network:
  retries: 3
  backoff_factor: 2
  timeout: 30
```

**カスタム設定:**
```bash
python merge_tool.py --config custom_config.yaml --refs pattern1.ref.yaml pattern2.ref.yaml --out result.yaml
```

#### トラブルシューティング

**よくある問題:**

1. **スキーマ検証エラー:**
   - 参照ファイルが有効な構造を持っていることを確認
   - パターンURIがアクセス可能であることを確認
   - YAML構文が正しいことを確認

2. **ネットワークエラー:**
   - インターネット接続を確認
   - GitHub URLがアクセス可能であることを確認
   - ツールは指数バックオフで自動的にリトライします

3. **LLM統合の失敗:**
   - APIキーが正しく設定されていることを確認
   - ツールは自動的にmanual戦略にフォールバックします
   - APIレート制限とクォータを確認

4. **ファイル権限エラー:**
   - 出力ディレクトリの書き込み権限を確認
   - ディスク容量が利用可能であることを確認

**デバッグモード:**
```bash
python merge_tool.py --log-level DEBUG --refs pattern1.ref.yaml pattern2.ref.yaml --out debug_output.yaml
```

---

## How to Use

Each tool should:
- Be placed in a subfolder under `/tools/`
- Include a README or help message
- Avoid modifying files unless explicitly instructed

---

If you add a new tool, please update this file and include usage instructions.
