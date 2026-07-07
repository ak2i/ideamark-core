# Doc CLI Contract v1.0.2
## validate Contract (Integrated Draft)
Generated: 2026-02-25T12:00:00Z

This document defines the normative contract for:

    <tool> validate [options] <input|->

Goals:
- Allow caller tools to interpret validation results in a uniform way.
- Preserve forward compatibility (unknown fields MUST be ignored).
- Keep tool-specific rules out of this contract (they belong to the document spec).

---------------------------------------------------------------------

## 1. Command Signature (MUST)

```bash
<tool> validate [--format ndjson|json|md] [common options...] <input|->
```

- `<input>` accepts a file path.
- `-` means stdin.
- Output is stdout by default.

Notes:
- Supported formats MUST be declared in `describe capabilities`.
- If a tool does not support `--format`, it MAY omit the flag entirely and always emit its default format (typically `ndjson`).
- Callers MUST NOT pass `--format` unless the format is declared in `describe capabilities`.

---------------------------------------------------------------------

## 2. Exit Codes (MUST)

- `0` = validation OK (no failing diagnostics at the selected fail threshold)
- `1` = validation failed (diagnostics at or above fail threshold exist)
- `2` = usage error / invalid CLI arguments
- `3` = runtime error (I/O, parse error before diagnostics emission, unexpected exception) (MAY)

Tools MAY use additional non-zero codes for tool-specific errors, but MUST document them.

---------------------------------------------------------------------

## 3. Diagnostics Model (MUST)

Diagnostics are emitted as records. The contract defines three record types:

- `meta` (exactly once, first)
- `diagnostic` (zero or more)
- `summary` (exactly once, last)

Unknown fields MUST be ignored by consumers.

### 3.1 NDJSON (MUST when --format ndjson or when ndjson is the default)

Each record is a single JSON object per line.

#### Record: meta (MUST)

```json
{
  "type": "meta",
  "tool": "<tool-name>",
  "version": "<semver>",
  "mode": "<string>",
  "command": "validate"
}
```

`command` is OPTIONAL.

#### Record: diagnostic (MUST)

```json
{
  "type": "diagnostic",
  "severity": "error|warning|info",
  "code": "<short_code>",
  "message": "<human-readable message>",
  "location": {
    "scope": "<string>",
    "path": "<string>",
    "id": "<string>",
    "line": 0,
    "column": 0
  },
  "mode": "<string>"
}
```

All `location` fields are OPTIONAL. If a field is not applicable, omit it.

#### Record: summary (MUST)

```json
{
  "type": "summary",
  "ok": true,
  "error_count": 0,
  "warning_count": 0,
  "info_count": 0
}
```

### 3.2 JSON (MAY when --format json)

If `--format json` is supported, emit a single JSON object:

```json
{
  "meta": { ... },
  "diagnostics": [ ... ],
  "summary": { ... }
}
```

The object fields reuse the NDJSON record schemas.

### 3.3 Markdown (MAY when --format md)

If `--format md` is supported, output is human-oriented and non-normative.

---------------------------------------------------------------------

## 4. Severity and Failure Threshold (MUST)

Severity levels are:

- `error`
- `warning`
- `info`

The command fails when diagnostics exist at or above the selected threshold.

### 4.1 Default threshold (MUST)

Default fail threshold is `error`.

### 4.2 Strict mode (SHOULD)

If `--strict` is supported, it MUST be declared in `describe capabilities`.
Strict mode MAY increase the set of checks or promote certain diagnostics.

### 4.3 Fail-on / Level options (SHOULD)

If the tool supports `--fail-on <severity>` or `--level <severity>`,
the selected severity MUST define the fail threshold.

---------------------------------------------------------------------

## 5. Input Handling (MUST)

- If `<input>` is omitted, treat as stdin.
- If both file and `-` are specified, the tool MUST return exit code `2`.

---------------------------------------------------------------------

## 6. Compatibility Rules (MUST)

1. Unknown fields MUST be ignored.
2. Field types MUST remain stable across minor versions.
3. Breaking changes require a major contract version bump.

---------------------------------------------------------------------

End of validate contract draft.
