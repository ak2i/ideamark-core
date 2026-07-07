# Doc CLI Contract v1.0.2
## describe params (Integrated Draft)
Generated: 2026-02-25T12:15:00Z

This document defines the normative contract for:

    <tool> describe params [--format md|json]

Goals:
- Provide machine-readable parameters required to generate or validate documents.
- Provide a human-readable summary for authoring and tooling integration.
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
  "params": [
    {
      "name": "<param-name>",
      "path": "<dot-path>",
      "required": true,
      "type": "<string>",
      "pattern": "<pattern>",
      "enum": ["<value>"],
      "description": "<short text>",
      "notes": "<short text>",
      "examples": ["<example>"]
    }
  ]
}
```

### Field Requirements

- contract.name (MUST)
- contract.version (MUST)
- tool.name (MUST)
- tool.version (MUST)
- document.name (MUST)
- document.version (MUST)
- params (MUST)

### Param Fields

- name (MUST)
- path (SHOULD)
- required (MUST)
- type (MUST)
- pattern (MAY)
- enum (MAY)
- description (SHOULD)
- notes (MAY)
- examples (MAY)

Unknown fields MUST be ignored.

---------------------------------------------------------------------

## 3. Markdown Guidance (MUST)

The Markdown output MUST:

- Provide a short overview of the document format.
- List required params and optional params separately.
- Include examples when practical.

---------------------------------------------------------------------

## 4. Param Conventions (SHOULD)

To reduce ambiguity, the following conventions are RECOMMENDED:

- `path` uses dot notation (e.g., `anchorage.view`, `status.state`).
- `pattern` expresses ID format or string constraints.
- `enum` expresses vocabularies or controlled values.
- `type` is a short string (e.g., `string`, `enum`, `id`).

---------------------------------------------------------------------

## 5. Example (NON-NORMATIVE)

```json
{
  "contract": { "name": "doc-cli-contract", "version": "1.0.2" },
  "tool": { "name": "ideamark-cli", "version": "0.1.0" },
  "document": { "name": "ideamark", "version": "1.0.2" },
  "params": [
    { "name": "section_id", "path": "sections.*.section_id", "required": true, "type": "id", "pattern": "SEC-*" },
    { "name": "anchorage.view", "path": "sections.*.anchorage.view", "required": true, "type": "enum", "enum": ["background","solution"] }
  ]
}
```

---------------------------------------------------------------------

## 6. Compatibility Rules (MUST)

1. Unknown fields MUST be ignored.
2. Field types MUST remain stable across minor versions.
3. Breaking changes require a major contract version bump.

---------------------------------------------------------------------

End of describe params contract draft.
