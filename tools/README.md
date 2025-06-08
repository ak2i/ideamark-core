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

### Pattern Merge Tool (`merge_tool.py`)

A comprehensive CLI tool that merges multiple IdeaMark patterns using advanced merge strategies.

#### Setup

1. **Install dependencies**
   ```bash
   cd tools/
   pip install -r requirements.txt
   ```

2. **Configure LLM providers (optional)**

   Set the environment variables if you plan to use the `synthesis` strategy:
   ```bash
   # OpenAI
   export OPENAI_API_KEY="your-openai-api-key"

   # Anthropic
   export ANTHROPIC_API_KEY="your-anthropic-api-key"
   ```

3. **Verify installation**
   ```bash
   python merge_tool.py --help
   ```

#### Usage

**Basic syntax:**
```bash
python merge_tool.py --refs <A.ref.yaml> <B.ref.yaml> [<C.ref.yaml> ...] \
    [--intent union] [--strategy prefer] [--priority A B C] [--out <path>]
```

**Merge strategies:**
- `manual` - Leave TODO placeholders for manual resolution
- `prefer` - Resolve conflicts using a priority order
- `annotate` - Include all versions with source annotations
- `synthesis` - Use an LLM to generate a consolidated version

**Examples:**

1. **Basic merge using the `prefer` strategy:**
   ```bash
   python merge_tool.py \
     --refs ../refs/agri-mobility-platform-pivot.ref.yaml \
     --refs ../refs/fisherman-direct-ecommerce.ref.yaml \
     --strategy prefer \
     --out merged_pattern.yaml
   ```

2. **Directory output that generates three files:**
   ```bash
   python merge_tool.py \
     --refs ../refs/pattern1.ref.yaml \
     --refs ../refs/pattern2.ref.yaml \
     --strategy prefer \
     --out merged_output/
   ```
   This produces the following files:
   - `merged_output/patterns/merged-<uuid>.yaml`
   - `merged_output/refs/merged-<uuid>.ref.yaml`
   - `merged_output/summary/merged-<uuid>.md`

3. **Manual conflict resolution:**
   ```bash
   python merge_tool.py \
     --refs ../refs/pattern1.ref.yaml \
     --refs ../refs/pattern2.ref.yaml \
     --strategy manual \
     --out manual_merge.yaml
   ```

4. **Priority-based merge:**
   ```bash
   python merge_tool.py \
     --refs ../refs/pattern1.ref.yaml \
     --refs ../refs/pattern2.ref.yaml \
     --strategy prefer \
     --priority "IdeaMark-123 IdeaMark-456" \
     --out result.yaml
   ```

5. **LLM-assisted synthesis:**
   ```bash
   python merge_tool.py \
     --refs ../refs/pattern1.ref.yaml \
     --refs ../refs/pattern2.ref.yaml \
     --strategy synthesis \
     --out synthesized.yaml
   ```

6. **Annotated merge with source tracking:**
   ```bash
   python merge_tool.py \
     --refs ../refs/pattern1.ref.yaml \
     --refs ../refs/pattern2.ref.yaml \
     --strategy annotate \
     --out annotated_merge.yaml
   ```

#### Testing

**1. Verify installation:**
```bash
cd tools/
python merge_tool.py --help
```

**2. Test with sample patterns:**
```bash
# Test `prefer` strategy
python merge_tool.py \
  --refs ../refs/agri-mobility-platform-pivot.ref.yaml \
  --refs ../refs/fisherman-direct-ecommerce.ref.yaml \
  --strategy prefer \
  --out test_prefer.yaml

# Validate output against the schema
python validate_output.py test_prefer.yaml ../schema/ideamark.schema.yaml
```

**3. Test all merge strategies:**
```bash
# Manual strategy
python merge_tool.py --refs ../refs/agri-mobility-platform-pivot.ref.yaml --refs ../refs/fisherman-direct-ecommerce.ref.yaml --strategy manual --out test_manual/

# Annotate strategy
python merge_tool.py --refs ../refs/agri-mobility-platform-pivot.ref.yaml --refs ../refs/fisherman-direct-ecommerce.ref.yaml --strategy annotate --out test_annotate/

# Synthesis strategy (requires API key)
python merge_tool.py --refs ../refs/agri-mobility-platform-pivot.ref.yaml --refs ../refs/fisherman-direct-ecommerce.ref.yaml --strategy synthesis --out test_synthesis/

# Validate all outputs
python validate_output.py test_manual ../schema/ideamark.schema.yaml
python validate_output.py test_annotate ../schema/ideamark.schema.yaml  
python validate_output.py test_synthesis ../schema/ideamark.schema.yaml
```

**4. Error handling tests:**
```bash
# Test with an invalid reference file
python merge_tool.py --refs nonexistent.ref.yaml --refs ../refs/agri-mobility-platform-pivot.ref.yaml --strategy prefer --out test_error.yaml

# Test unreachable URIs (temporarily modify the ref file)
# You should see network retry behavior
```

#### Configuration

**Default settings (`config/default.yaml`):**
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
    mistral:
      model: mistral-medium
      max_tokens: 2000
      temperature: 0.3
    google:
      model: gemini-pro
      max_tokens: 2000
      temperature: 0.3
    fallback_strategy: manual
  
network:
  retries: 3
  backoff_factor: 2
  timeout: 30
```

**Custom settings:**
```bash
python merge_tool.py --config custom_config.yaml --refs pattern1.ref.yaml pattern2.ref.yaml --out result.yaml
```

#### Troubleshooting

**Common issues:**

1. **Schema validation errors:**
   - Ensure the reference files have a valid structure
   - Verify the pattern URIs are reachable
   - Check that the YAML syntax is correct

2. **Network errors:**
   - Check your internet connection
   - Ensure the GitHub URLs are reachable
   - The tool automatically retries with exponential backoff

3. **LLM integration failures:**
   - Make sure API keys are set correctly
   - The tool falls back to the `manual` strategy
   - Check API rate limits and quotas

4. **File permission errors:**
   - Confirm you have write permission to the output directory
   - Ensure there is available disk space

**Debug mode:**
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
