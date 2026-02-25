# Doc CLI Contract v1.0.2
## describe capabilities --format md (Human-facing Template)
Generated: 2026-02-25T09:52:47.242003Z

This document defines a **stable Markdown template** for:

    <tool> describe capabilities --format md

Purpose:
- Provide a human- and LLM-friendly overview of what the tool supports.
- Reduce repeated misuse caused by misleading command/option names.
- Keep it easy to copy-paste into prompts.

This template is **normative for headings and required fields**.
Tool-specific content fills the placeholders.

---------------------------------------------------------------------

## 1. Output Rules (MUST)

- Use Markdown headings exactly as defined below (MUST).
- Keep each description concise (1–2 sentences) (SHOULD).
- Prefer explicit “does / does not” statements to prevent confusion (SHOULD).
- If something is not supported, say “Not supported” explicitly (SHOULD).

---------------------------------------------------------------------

# {"<TOOL NAME>"}
**Tool Version:** {"<SEMVER>"}
**Doc CLI Contract:** 1.0.2

## Summary
{"<One-paragraph summary of the tool and what documents it operates on.>"}

## Commands
List supported commands. For each command, include:
- **What it does**
- **What it does not do**
- **Formats**
- **Inputs** (file/stdin)
- **Key options** (only the important ones)

### describe
**Description:** { "<Short English description.>" }
**Does:** { "<Bullet list of key things it does.>" }
**Does not:** { "<Bullet list of key things it does NOT do.>" }
**Formats:** `md`, `json`
**Topics:** `ai-authoring`, `params`, `capabilities`
**Input:** file path, `-` (stdin) { "(if supported)" }

**Key options**
- `--format <md|json>` — { "<Explain intended use of md vs json.>" }
- `--quiet` — { "<If supported>" } / Not supported

### validate
**Description:** { "<Short English description.>" }
**Does:**
- { "<e.g., checks required fields, references, structural constraints>" }
**Does not:**
- { "<e.g., does not modify input; does not resolve external refs>" }
**Formats:** `ndjson`{ ", `json` (optional)" }
**Input:** file path, `-` (stdin) { "(if supported)" }

**Diagnostics / severity**
- **Levels:** { "`error`, `warning`, `info`" or "Not supported" }
- **Default fail-on:** { "`error`" or "Not supported" }
- **Strict mode:** { "Supported / Not supported" }

**Key options**
- `--strict` — { "<Supported/Not supported and meaning>" }
- `--fail-on <level>` — { "<Supported/Not supported and meaning>" }
- `--level <level>` — { "<Supported/Not supported and meaning>" }
- `--quiet` — { "<Supported/Not supported>" }

## Evidence (Cross-cutting)
Describe whether the tool can emit/attach evidence annotations.

- **Emit evidence:** { "Not supported / Supported (yaml, ndjson)" }
- **Attach evidence to a document:** { "Not supported / Supported" }
- **Artifact out:** { "Not supported / Supported" }

## Compatibility Notes
{ "<Short notes about compatibility, known limitations, and forward/backward behavior.>" }

## Machine-readable capabilities
This Markdown output corresponds to:
- `<tool> describe capabilities --format json`

---------------------------------------------------------------------

## 2. Example (NON-NORMATIVE)

Below is an example snippet (tools should not copy this verbatim):

- **describe**: “Print tool and document guidance. Use topics to retrieve authoring rules and supported features.”
- **validate**: “Check whether a document conforms to the tool rules. Outputs diagnostics and does not modify input.”

