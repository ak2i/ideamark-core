# imc — IdeaMark Compiler (Node/TypeScript)

CLI that turns a project brief + IdeaMark schema into:
- `<project>.designdoc.yaml` (DesignDoc v0.1)
- `<project>.ADR-XXXX.md` (fixed 4-digit index)
- `<project>.schema.json`
- `<project>.types.ts`

## Quick start

```bash
cd imc
npm i
npm run build
npm link   # or: pnpm link --global
imc --help
```

The CLI reads `/schema/ideamark.schema.yaml` and `/schema/AboutSchema.md` from the repo root by default.
If you run `imc init --root .` in an empty folder, packaged templates are used to scaffold.

to anlink imc command, do this.

```bash
npm unlink -g imc
```

if you would prefered to use pmpm, do bellows:

# Using **pnpm**: Build & Link the `imc` CLI

## A) Install globally (use `imc` anywhere)

```bash
cd imc
pnpm install
pnpm build
pnpm link --global    # registers `imc` as a global command

imc --help            # sanity check
```

Unregister later:

```bash
pnpm unlink --global imc
```

## B) Monorepo usage (workspaces)

Create `pnpm-workspace.yaml` at the repo root (if you don’t have one):

```yaml
packages:
  - 'imc'
```

Then:

```bash
pnpm -w install
pnpm -w --filter imc run build
pnpm -w exec imc -- --help
```

(Optionally) also make it global from the workspace:

```bash
pnpm -w --filter imc link --global
```

## C) Run in dev mode (no build)

```bash
cd imc
pnpm run dev -- --help   # uses tsx to run src/index.ts directly
```

## D) Typical workflow with pnpm

```bash
# 1) Setup
cd imc
pnpm install
pnpm build
pnpm link --global

# 2) Use the CLI from your repo root (with /schema present)
cd /path/to/IdeaMark-Core
imc init     --root . --project sample
imc synth    --root . --project sample --brief ./projects/sample/briefs/sample.brief.md --fix
imc validate --root . --project sample
imc generate --root . --project sample
```

## Tips

* Check where the global binary lives:

  ```bash
  pnpm bin -g
  which imc
  ```
* LLM features (optional):

  ```bash
  export OPENAI_API_KEY=sk-...
  export IMC_OPENAI_MODEL=gpt-4o-mini   # optional override
  ```
* By default the CLI reads the repo’s **`/schema/ideamark.schema.yaml`** and **`/schema/AboutSchema.md`**.
  If you run `imc init --root .` in an empty directory, bundled templates are used to scaffold.

