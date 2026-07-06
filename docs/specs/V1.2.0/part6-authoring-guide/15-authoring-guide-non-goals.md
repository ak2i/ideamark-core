# 15. Authoring Guide Non-goals

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 15.1 Purpose

This chapter clarifies what Part 6 does not define.

Part 6 provides authoring guidance.

It does not replace the Core Specification, Projection Specification, profiles, CLI contracts, POR design documents, or implementation-specific workflows.

## 15.2 Not a Normative Core Schema

Part 6 does not define required Core fields, required namespaces, serialization rules, or validation errors.

Those belong to Part 4.

If an authoring recommendation should become mandatory for Core conformance, it must be promoted to Part 4.

## 15.3 Not a Complete Projection Theory

Part 6 does not attempt to complete a theory of Projection quality.

Projection quality is important, but it should be informed by practical implementation experience, CLI behavior, POR experiments, sample corpora, and retrieval evaluation.

Part 6 may explain how to use or sketch a Projection during authoring.

Part 5 remains the primary place for Projection specification.

## 15.4 Not a Fixed Human-AI Workflow

Part 6 does not prescribe one fixed human-AI workflow.

It does not require humans to perform specific steps or AI systems to perform specific steps.

It describes authoring activities that may be performed by humans, AI systems, tools, or combinations of them.

Profiles, organizations, or high-risk domains may impose stricter workflow requirements separately.

## 15.5 Not a POR Specification

Progressive Occurrence Resolution is one authoring method.

Part 6 may mention POR as part of the authoring ecosystem.

It does not define POR algorithms, scheduling, UI, data structures, or implementation contracts.

POR-specific behavior should be defined in companion specifications or implementation documents.

## 15.6 Not a CLI Contract

Part 6 does not define CLI command names, exit codes, diagnostic codes, JSON output formats, or filesystem layout.

Those belong to CLI contracts or implementation documentation.

Part 6 may describe how CLI tools can support authoring, validation, correction, and samples.

## 15.7 Not a Domain Profile

Part 6 does not define domain-specific vocabularies or constraints.

For example, it does not define final role or kind vocabularies for:

- source code analysis;
- recipes;
- legal review;
- medical review;
- engineering design;
- policy planning;
- visual inspection;
- sensor analysis.

Domain-specific strictness should be defined by profiles.

## 15.8 Not a Knowledge Ontology

IdeaMark Core is not a universal ontology of knowledge.

Part 6 should not turn Entities, Sections, or Occurrences into fixed semantic categories.

They are functional authoring objects for knowledge reuse design.

## 15.9 Not a Requirement for Complete Extraction

Part 6 does not require authors to extract everything from an Original Source.

Useful omission is allowed when it supports the Projection.

Completeness requirements may be defined by profiles, organizations, or specific use cases.

## 15.10 Not a Replacement for Human Accountability

Part 6 does not remove the need for human accountability in high-risk contexts.

AI-assisted authoring can produce useful drafts, but domain, legal, ethical, safety, or compliance responsibility must be handled by appropriate processes and profiles.

Core conformance does not imply correctness for every downstream use.

## 15.11 Not a Final List of Authoring Methods

The authoring methods described in Part 6 are examples and guidance.

Future systems may introduce new authoring methods.

The specification should remain open to new human-AI collaboration patterns, authoring tools, and regeneration workflows.

## 15.12 Boundary Summary

Part 6 may answer:

- how to think about authoring;
- how to design reusable structures;
- how to review Section, Occurrence, and Entity choices;
- how to use validation and samples during authoring;
- how to treat IdeaMark Documents as working artifacts.

Part 6 should not answer:

- what exact YAML fields are mandatory in Core;
- what exact CLI commands exist;
- how POR is implemented;
- what domain vocabulary is closed;
- what all future Projection quality metrics are;
- what fixed human-AI workflow every author must follow.
