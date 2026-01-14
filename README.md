# ideamark-core (monorepo)

This repository hosts IdeaMark-core as a monorepo with multiple distributable artifacts:

- `@ideamark/core` — schema/validation/reference-resolution (model-agnostic)
- `ideamark` — CLI (local-first)
- `@ideamark/server` — server (Docker deploy)
- `packages/web` — Web UI (planned/optional)
- `templates/official` — official reference templates
- `infra/aws` — deployment scaffolding

See `docs/packaging.md` for the product & packaging specification.

## CLI Quickstart (Dev)

### 1. Build
```bash
pnpm -C packages/core build
pnpm -C packages/cli build
```

### 2. Create a document from a template
```bash
node packages/cli/dist/index.js new tmp/dev-sample/supabase-readme.md \
  --template templates/official/software-development/workcell-v1/Decision6-WorkCell.ideamark.template.md
```

### 3. Validate the document
```bash
node packages/cli/dist/index.js validate tmp/dev-sample/supabase-readme.md
```

### 4. Fill slots with AI (OpenAI-compatible)
```bash
export OPENAI_API_KEY="sk-..."

node packages/cli/dist/index.js assist fill tmp/dev-sample/supabase-readme.md \
  --source tmp/projects/supabase/README.md \
  --model gpt-4o-mini \
  --base-url https://api.openai.com/v1
```

### 5. Optional: JSON output for reports
```bash
node packages/cli/dist/index.js assist fill tmp/dev-sample/supabase-readme.md \
  --source tmp/projects/supabase/README.md \
  --model gpt-4o-mini \
  --base-url https://api.openai.com/v1 \
  --json
```
