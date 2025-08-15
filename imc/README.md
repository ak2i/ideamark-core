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
