# ideamark-core parse / validate API - Minimal Implementation Proposal (v0)

This proposal is scoped to the **minimum contract** in
`docs/ideamark-core-cli-development-contract.md` and is the
**authoritative basis** for parse/validate in ideamark-core.

It intentionally avoids template-specific semantics and any AI logic.

---

## Goals

- Parse Markdown with YAML frontmatter into a machine-usable structure.
- Validate the **required** frontmatter fields only.
- Detect and extract structured blocks without interpreting them.
- Keep outputs stable and machine-friendly for CLI use.

Non-goals:
- Template-specific rules
- Semantic interpretation of blocks
- LLM or provider logic

---

## API Surface (TypeScript)

```ts
export type ParseResult =
  | { ok: true; document: IdeaMarkDocument; warnings: ParseWarning[] }
  | { ok: false; errors: ParseError[] };

export type ValidateResult =
  | { ok: true; warnings: ValidationWarning[] }
  | { ok: false; errors: ValidationError[] };

export type IdeaMarkDocument = {
  frontmatter: Record<string, unknown>;
  body: string;
  structuredBlocks: StructuredBlock[];
  // raw keeps fidelity for tooling
  raw: {
    markdown: string;
    frontmatterText: string | null;
  };
};

export type StructuredBlock = {
  lang: 'yaml' | 'json' | 'unknown';
  content: string; // raw block text
  // parsed data is optional; only if syntactically valid
  data?: unknown;
  // a light, non-semantic metadata channel
  meta: {
    startLine: number; // 1-based
    endLine: number;   // 1-based
  };
};

export function parse(markdown: string): ParseResult;
export function validate(doc: IdeaMarkDocument): ValidateResult;
```

Notes:
- `structuredBlocks` extraction is syntactic only.
- `data` is populated only when the block is valid YAML/JSON.
- `meta` provides location info for CLI diagnostics.

---

## Minimal Frontmatter Contract (Validation)

Required fields (exactly as contract):

```yaml
ideamark_version: 1
template_id: "<template identifier>"
doc_id: "<unique document identifier>"
created_at: "<ISO 8601 timestamp>"
lang: "<language tag>"
```

Validation rules (minimum):
- All required keys must exist.
- `ideamark_version` must be number and equal to 1.
- `template_id`, `doc_id`, `created_at`, `lang` must be non-empty strings.
- `created_at` must be ISO 8601 (basic validation: Date.parse ok).
- `lang` must match BCP-47 basic pattern `^[A-Za-z]{2,3}(-[A-Za-z0-9]{2,8})*$`.

Nothing else is required by core.

---

## Parsing Behavior

1. Detect YAML frontmatter at the top of the file:
   - `---` on first line
   - `---` closing delimiter
2. Parse frontmatter as YAML into an object.
3. Keep the remainder as raw Markdown body.
4. Extract structured blocks from body:
   - Fenced code blocks with info string `yaml` or `json`.
   - For each block, attempt to parse (YAML or JSON) and store `data` on success.

If frontmatter is missing or invalid YAML:
- `parse` returns `ok: false` with a parse error.

If a fenced block is invalid YAML/JSON:
- `parse` still returns `ok: true`, but adds a warning.
- The block is included with `data` omitted.

---

## Validation Behavior

`validate` does **only** the minimal contract checks described above.

It must not:
- enforce template-specific structure
- interpret YAML block contents
- apply external schemas unless explicitly requested by caller

---

## Error / Warning Shape

```ts
export type ParseError = {
  code:
    | 'frontmatter_missing'
    | 'frontmatter_invalid_yaml'
    | 'frontmatter_not_object';
  message: string;
  line?: number;
};

export type ParseWarning = {
  code: 'structured_block_invalid';
  message: string;
  line: number;
};

export type ValidationError = {
  code:
    | 'required_field_missing'
    | 'invalid_ideamark_version'
    | 'invalid_field_type'
    | 'invalid_created_at'
    | 'invalid_lang';
  message: string;
  field?: string;
};

export type ValidationWarning = {
  code: 'recommended_field_missing';
  message: string;
  field?: string;
};
```

Recommended field warnings (optional):
- `created_by`
- `provenance`

---

## Minimal Implementation Notes

- Parser libraries: `gray-matter` for frontmatter + `js-yaml` for YAML.
- JSON blocks use `JSON.parse`.
- Keep implementation deterministic and side-effect free.
- No file I/O in core; CLI handles reading/writing.

---

## CLI Integration Contract

- `ideamark validate <file>`
  - reads file
  - calls `parse`
  - calls `validate` if parse ok
  - returns machine-readable errors on failure

---

## Example Flow

Input file:

```md
---
ideamark_version: 1
template_id: "imtpl.decision6.workcell"
doc_id: "doc.sample.001"
created_at: "2026-01-07T12:00:00Z"
lang: "ja-JP"
---

# Title

```yaml
intent:
  summary: "..."
```
```

Output:
- `parse` returns document with `structuredBlocks[0].lang = 'yaml'` and parsed `data`.
- `validate` returns ok.

---

## Open Questions (Optional)

- Should structured block extraction include non-fenced YAML markers?
- Should `created_at` accept date-only strings?

These are explicitly **out of scope** for the minimal contract and
should be decided by future revisions.
