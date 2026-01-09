# AI Integration Policy (v0)

This document defines how AI systems are integrated into IdeaMark-core.

It focuses on **interoperability, cost-awareness, and user experience**,  
while preserving the core principle that **judgment remains a human responsibility**.

---

## 1. Core Principles

### 1.1 AI Is Assistive, Not Authoritative

AI systems may:
- generate drafts,
- propose alternatives,
- summarize or reorganize content,
- surface relevant precedents.

AI systems must not:
- make irreversible decisions,
- overwrite human-authored content without review,
- bypass validation or reference checks.

All AI outputs are considered **proposals**, never final artifacts.

---

### 1.2 Core Is Model-Agnostic

IdeaMark-core does not depend on any specific AI model.

All AI integrations must pass through a **provider interface**  
compatible with the OpenAI API specification,  
allowing local, third-party, and OpenAI-hosted models to be used interchangeably.

---

### 1.3 Validate Everything

All AI-generated content must be:
- validated against IdeaMark schemas,
- checked for reference consistency,
- recorded with provenance metadata.

AI can write.  
The core must verify.

---

## 2. AI Provider Interface

All AI backends are accessed through a unified interface.

### Required Parameters

- `base_url` — API endpoint (OpenAI or compatible)
- `api_key` — authentication token (optional for local providers)
- `model` — model identifier
- `temperature`
- `max_tokens`

### Optional Parameters

- `top_p`
- `seed`
- `timeout`
- `cost_limit`
- `metadata` (provider-specific)

### Supported Provider Types

- OpenAI-hosted APIs
- OpenAI-compatible local servers (ollama, vLLM, llama.cpp server)
- OpenAI-compatible third-party services
- Embedded runtimes (ONNX / WASM / WebGPU), when exposed via adapter

---

## 3. Task Categories

IdeaMark defines three AI task categories.
Each category has different performance, cost, and deployment expectations.

---

### 3.1 Inline Tasks

**Purpose**
- Immediate, low-latency assistance during editing

**Examples**
- Field completion suggestions
- Formatting and structure fixes
- Short rephrasing or clarification
- Missing-field detection

**Recommended Models**
- Small models (≈1B–3B)
- ONNX / WASM / WebGPU
- Local CPU or browser execution

**Typical Integration**
- `packages/web`
- `packages/cli` (local mode)

---

### 3.2 Assist Tasks

**Purpose**
- Structured support for document creation and navigation

**Examples**
- Template slot filling
- Summary and tag extraction
- Link and reference suggestions
- Partial template instantiation

**Recommended Models**
- Small to mid-sized models
- Local or server-hosted
- Cost-aware execution

**Typical Integration**
- `packages/cli`
- `packages/server`

---

### 3.3 Reason Tasks

**Purpose**
- Deep reasoning and alternative exploration

**Examples**
- Hypothesis generation and critique
- Option comparison with trade-offs
- Long-form drafting
- Cross-document synthesis

**Recommended Models**
- Large models
- Server-hosted or external APIs

**Typical Integration**
- `packages/server`
- Explicit user-triggered operations

---

## 4. Model Escalation Policy

IdeaMark encourages **progressive escalation**:

1. Attempt task with the lowest-cost model suitable for the category.
2. If output quality is insufficient:
   - escalate to a larger model,
   - or request explicit user approval.
3. Record escalation decisions in provenance metadata.

This approach optimizes both:
- cost efficiency,
- and user experience.

---

## 5. Provenance and Attribution

All AI-assisted content must record:

- provider type
- model identifier
- task category
- timestamp
- optional prompt hash or reference
- escalation history (if any)

Provenance is metadata, not content.  
It must not interfere with human editing.

---

## 6. Package-Level Responsibilities

### 6.1 `packages/core`

- Define provenance schema
- Validate AI-generated structures
- Resolve references safely
- Reject invalid or inconsistent output

No AI logic belongs here.

---

### 6.2 `packages/cli`

- Provide AI-assisted commands
- Support local-first execution
- Allow explicit model selection and escalation
- Never auto-commit AI output

---

### 6.3 `packages/server`

- Execute shared AI jobs
- Manage provider credentials
- Run batch or asynchronous tasks
- Enforce organization-level policies

---

### 6.4 `packages/web`

- Offer inline assistance
- Support browser-based inference when available
- Provide clear UI distinction between human and AI content

---

## 7. Templates and AI

Templates define **what needs to be thought about**,  
not **how AI should think**.

Templates may:
- expose slots suitable for AI assistance,
- document expected reasoning depth.

Templates must not:
- hard-code model choices,
- embed prompts tied to specific providers.

---

## 8. Non-Goals

- Fully autonomous document generation
- AI-only workflows
- Hidden or implicit AI decision-making
- Model-specific lock-in

---

## 9. Summary

IdeaMark integrates AI as a **flexible, replaceable assistant**.

Small models provide immediacy.  
Large models provide depth.  
Humans retain judgment.

The system remains transparent, inspectable, and adaptable  
as models, costs, and deployment environments evolve.
