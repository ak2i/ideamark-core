# Doc CLI Contract v1.0.2
## Capabilities JSON Schema
Generated: 2026-02-25T09:50:35.688972Z

This section defines the JSON schema for:

    <tool> describe capabilities --format json

The goal is:
- Allow caller tools (e.g., Responder-Bridge) to programmatically inspect supported commands and options.
- Provide short English descriptions to reduce misuse by LLMs or automation scripts.
- Preserve forward compatibility (unknown fields MUST be ignored).

---------------------------------------------------------------------

## 1. Top-Level Structure (MUST)

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
  "features": {
    "...": { }
  },
  "commands": {
    "...": { }
  }
}
```

### Field Requirements

- contract.name (MUST)
- contract.version (MUST)
- tool.name (MUST)
- tool.version (MUST, SemVer recommended)
- features (MAY)
- commands (MUST)

Unknown top-level fields MUST NOT cause failure.

---------------------------------------------------------------------

## 2. Command Definition (MUST / SHOULD)

Each command MUST be declared under "commands".

Minimal example:

```json
{
  "commands": {
    "describe": {
      "formats": ["md", "json"],
      "topics": ["ai-authoring", "params", "capabilities"],
      "description": "Print tool and document guidance. Use topics to retrieve authoring rules and supported features."
    },
    "validate": {
      "formats": ["ndjson"],
      "stdin": true,
      "description": "Check whether a document conforms to the tool rules. Outputs diagnostics and does not modify input."
    }
  }
}
```

---------------------------------------------------------------------

## 3. Command Fields

### MUST

For describe:

- formats (array)
- topics (array)

For validate:

- formats (array)
- stdin (boolean)

### SHOULD

- description (short English sentence or two)

Design rule:
- Keep descriptions concise.
- Explain what the command does.
- Optionally clarify what it does NOT do.

Example style:
    "Does not modify input."
    "Does not resolve external references."

---------------------------------------------------------------------

## 4. Option Definition (SHOULD)

Commands MAY define supported options.

```json
{
  "commands": {
    "validate": {
      "options": {
        "--strict": {
          "description": "Enable stricter validation checks."
        },
        "--fail-on": {
          "values": ["error", "warning", "info"],
          "description": "Fail the command if diagnostics at or above this severity exist."
        }
      }
    }
  }
}
```

### Option Fields

- description (SHOULD, short English text)
- values (MAY, enumeration of accepted values)

Unknown options MUST NOT break consumers.

---------------------------------------------------------------------

## 5. Evidence Feature Declaration (MAY)

If the tool supports evidence emission:

```json
{
  "features": {
    "evidence": {
      "emit": ["yaml", "ndjson"],
      "attach": true,
      "artifact_out": true
    }
  }
}
```

This section is OPTIONAL.

---------------------------------------------------------------------

## 6. Compatibility Rules

1. Unknown fields MUST be ignored.
2. Field types MUST remain stable across minor versions.
3. Breaking schema changes require major contract version bump.

---------------------------------------------------------------------

End of schema.
