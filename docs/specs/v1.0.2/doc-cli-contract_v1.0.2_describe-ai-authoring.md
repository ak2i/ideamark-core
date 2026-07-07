# Doc CLI Contract v1.0.2
## describe ai-authoring (Integrated Draft)
Generated: 2026-02-25T12:15:00Z

This document defines the normative contract for:

    <tool> describe ai-authoring [--format md|json]

Goals:
- Provide authoring guidance for humans and LLMs.
- Keep guidance aligned with the document format and validation rules.
- Preserve forward compatibility (unknown fields MUST be ignored).

---------------------------------------------------------------------

## 1. Output Rules (MUST)

- `--format md` MUST produce a human-readable document.
- `--format json` MUST produce a machine-readable document.
- If a tool does not support one of the formats, it MUST omit it from `describe capabilities`.

---------------------------------------------------------------------

## 2. JSON Structure (MUST)

Top-level object:

```json
{
  "contract": {
    "name": "doc-cli-contract",
    "version": "1.0.2"
  },
  "tool": {
    "name": "<tool-name>",
    "version": "<semver>"
  },
  "document": {
    "name": "<document-format-name>",
    "version": "<document-format-version>"
  },
  "guidance": {
    "overview": "<short text>",
    "principles": ["<rule>"],
    "do": ["<rule>"],
    "dont": ["<rule>"],
    "checklist": ["<item>"],
    "examples": ["<example>"]
  }
}
```

### Field Requirements

- contract.name (MUST)
- contract.version (MUST)
- tool.name (MUST)
- tool.version (MUST)
- document.name (MUST)
- document.version (MUST)
- guidance (MUST)
- guidance.overview (MUST)
- guidance.principles (MAY)
- guidance.do (SHOULD)
- guidance.dont (SHOULD)
- guidance.checklist (MAY)
- guidance.examples (MAY)

Unknown fields MUST be ignored.

---------------------------------------------------------------------

## 3. Markdown Guidance (MUST)

The Markdown output MUST:

- Provide an overview of the authoring intent.
- Include explicit “do / do not” rules.
- Include at least one example when practical.

If available, include Principles and Checklist sections.

---------------------------------------------------------------------

## 4. Example (NON-NORMATIVE)

```json
{
  "contract": { "name": "doc-cli-contract", "version": "1.0.2" },
  "tool": { "name": "ideamark-cli", "version": "0.1.0" },
  "document": { "name": "ideamark", "version": "1.0.2" },
  "guidance": {
    "overview": "Generate valid IdeaMark documents for human review and tooling.",
    "principles": ["Use stable IDs", "Prefer explicit structure"],
    "do": ["Include required header fields"],
    "dont": ["Invent values not in vocab"],
    "checklist": ["Header has ideamark_version/doc_id/doc_type/status/created_at/updated_at/lang"],
    "examples": ["..."]
  }
}
```

---------------------------------------------------------------------

## 5. Compatibility Rules (MUST)

1. Unknown fields MUST be ignored.
2. Field types MUST remain stable across minor versions.
3. Breaking changes require a major contract version bump.

---------------------------------------------------------------------

End of describe ai-authoring contract draft.
