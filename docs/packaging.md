# IdeaMark-core — Product & Packaging Specification v0

This document defines the **official monorepo skeleton**, **deliverables**, and **responsibility boundaries** for IdeaMark-core.

It exists to keep the project coherent as it grows (CLI / Server / Web / Templates / Infra), and to prevent the “core” from becoming an opinionated methodology.

---

## 1. Purpose

IdeaMark-core is a **tooling framework** that operationalizes the IdeaMark philosophy.

It provides:

- a stable expressive core (schemas, validation, reference resolution),
- official reference templates (non-mandatory),
- tools for creating, storing, retrieving, and collaborating on IdeaMark documents,
- optional AI-assisted workflows that remain transparent and reviewable.

IdeaMark-core aims to support problem solving across a wide range of scales and domains by enabling:
- structured recording of problem/solution/decision artifacts,
- reuse via retrieval and composition,
- learning via both successes and failures.

---

## 2. Monorepo Structure

IdeaMark-core is managed as a **single Git repository** (monorepo) with multiple distributable artifacts.

```
ideamark-core/
├── docs/
│   ├── philosophy.md
│   ├── philosophy.ja-JP.md
│   ├── packaging.md
│   └── ai-integration-policy.md
│
├── packages/
│   ├── core/        # schema/validation/reference-resolution/provenance (model-agnostic)
│   ├── cli/         # ideamark CLI (local-first)
│   ├── server/      # ideamark-server (Docker deploy; shared infra)
│   └── web/         # Web UI (collaborative editing; optional)
│
├── templates/
│   └── official/    # official but non-mandatory templates (data, not code)
│
├── infra/
│   └── aws/         # deployment scaffolding (ECS/S3/etc.)
│
└── README.md
```

**Rationale**
- Cross-cutting changes (schema → templates → tooling) are common early on.
- Monorepo enables atomic PRs and avoids version-skew across packages.
- Packages remain independently buildable and releasable.

---

## 3. Distributable Artifacts

IdeaMark-core ships multiple artifacts. The repository is the source of truth; distribution formats are secondary.

| Artifact | Location | Distribution | Primary Users |
|---|---|---|---|
| Core library | `packages/core` | npm package (ESM) | CLI/Server/Web, integrators |
| CLI | `packages/cli` | npm global install | local users, authors |
| Server | `packages/server` | Docker image | self-host, ECS, SaaS |
| Web UI | `packages/web` | bundled web app | authors, reviewers |
| Official templates | `templates/official` | git / release archive | authors, teams |
| Infra scaffolding | `infra/aws` | git / templates | deployers |

---

## 4. Responsibility Boundaries

This section is normative: it defines **what belongs where**.

### 4.1 `packages/core` — Expressive Core

**Role**
- Define *what can be expressed* in IdeaMark.
- Provide safety rails for tools (validation, reference checks).

**Must include**
- schemas/specs (e.g., JSON Schema)
- validation rules
- reference/link resolution primitives
- provenance metadata schema (AI/human attribution)
- minimal structural diff/merge semantics (optional, but core-friendly)

**Must NOT include**
- storage concerns (DB, S3, filesystem persistence)
- UI concerns
- workflow opinions (e.g., “you should use Decision6”)
- model/provider-specific AI logic or prompts

**Design target**
- small, stable, slow to change

---

### 4.2 `templates/official` — Reference Templates

**Role**
- Define *how to use IdeaMark* in specific ways (methodologies, workflows).
- Provide official templates without forcing adoption.

**Rules**
- Templates are **data** (YAML/Markdown), not code.
- Templates may evolve faster than core.
- Templates may conflict or offer competing approaches.

**Must include**
- template intent, scope, non-goals
- required nodes/fields
- linking conventions relevant to the template

**Must NOT include**
- hard-coded model choices or provider-specific prompts
- assumptions that should be core constraints

---

### 4.3 `packages/cli` — Local-first Interface

**Role**
- Authoring and maintenance tooling for IdeaMark repositories.

**Typical capabilities**
- init repository, manage template pins
- create documents from templates
- validate documents (via core)
- resolve and inspect links/references
- local search and listing
- optional AI assist (via policy and provider interface)

**Key constraints**
- file-based source of truth by default
- works offline (AI optional)
- never auto-commits AI output

---

### 4.4 `packages/server` — Shared Infrastructure

**Role**
- Collaborative, multi-user capabilities and shared storage/search.

**Typical capabilities**
- document storage (object store like S3; local FS for dev)
- metadata DB (Postgres recommended)
- search/index management (simple to start; extensible later)
- authentication/authorization
- AI job execution for shared workflows
- serve Web UI (optional)

**Distribution**
- Docker image is the primary deployment unit.
- The same image should run locally (Docker Compose) and on ECS.

---

### 4.5 `packages/web` — Collaborative UI

**Role**
- Human-friendly authoring and navigation, including collaboration.

**Typical capabilities**
- template-driven document creation and editing
- linked navigation (graph-like browsing)
- review & diff visualization
- AI suggestions preview + selective adoption

**Constraints**
- UI must not embed core rules; it must call core/validator interfaces.
- Real-time collaborative editing is optional in v0.

---

### 4.6 `infra/aws` — Deployment Scaffolding

**Role**
- Make self-hosting easy and repeatable.

**Targets**
- ECS/Fargate (server)
- S3 (documents)
- optional Postgres/OpenSearch/Cognito

**Rules**
- Infra should track server releases.
- Keep configuration documented and reproducible.

---

## 5. AI Integration (Policy Hook)

AI integration is governed by `docs/ai-integration-policy.md`.

High-level constraints:
- AI is assistive, not authoritative.
- Provider interface is OpenAI-compatible.
- Small models support low-latency “Inline/Assist” tasks.
- Large models are reserved for “Reason” tasks and explicit user intent.
- All AI outputs must be validated by `packages/core`.

**Important boundary**
> If it can be expressed as a template, it does not belong in the core.  
> If a decision can be deferred to the user, the system must not make it.

---

## 6. Development Order (Recommended)

1. **Core**
   - schema + validator + reference resolution + provenance schema
2. **Official templates**
   - stabilize Decision6 / WorkCell as reference methodologies
3. **CLI (local-first MVP)**
   - init / new / validate / resolve / search (AI optional)
4. **Server (single-tenant first)**
   - storage + metadata + search + Docker deploy
5. **Web UI**
   - editor + navigator + review/diff
6. **Infra templates**
   - ECS + S3 deployment scaffolding

---

## 7. Versioning & Compatibility

- `packages/core` changes should be conservative.
- Templates may require a minimum core version.
- CLI and Server should declare compatible core ranges.
- Prefer additive schema evolution:
  - add fields before changing meaning
  - deprecate before removing
  - keep migration notes (CHANGELOG)

---

## 8. Definition of Done for v0 Skeleton

The monorepo “v0 skeleton” is considered complete when:

- each `packages/*` is independently buildable,
- core validation works end-to-end from the CLI,
- server exposes a health endpoint and can be containerized,
- official templates exist as data and can be instantiated by tools (even if minimally),
- docs anchor the philosophy and policies.

---

## 9. Appendix: Naming Conventions (Optional)

- npm scope: `@ideamark/*` for libraries/services
- cli binary: `ideamark`
- server image: `ghcr.io/<org>/ideamark-server`

---