# 8. Original Source Open-hand Principle

**Part:** 2 — Architecture of Human-AI Co-evolution  
**Status:** Draft Rev001  
**Type:** Informative / Reference Architecture

Original Source is defined by architectural role, not by medium, format, origin, ownership, or current interpretation.

Any artifact that may later serve as an authoritative basis for intellectual activity may function as an Original Source.

## 8.1 Purpose

The purpose of the Original Source concept is to preserve access to the material basis from which future intellectual activity may be reconstructed.

Original Source does not mean only written documents.

It does not mean only materials that already have an explicit explanation, caption, metadata schema, or intended use.

It refers to anything that may become authoritative for a future reconstruction activity.

## 8.2 Open-hand Definition

IdeaMark Core intentionally leaves both media and context open.

A radiograph, tourist photograph, artwork, conversation, sensor stream, dataset, design document, planning framework, reasoning model, video, log, transcript, future knowledge representation, or another yet-to-be-invented artifact may all become Original Sources.

The Core should not attempt to enumerate all possible source forms.

It should define the architectural relationship between sources, Projections, IdeaMark documents, and reconstruction.

This allows future intellectual activities to be supported without redesigning the Core each time a new source medium or practice emerges.

## 8.3 Medium Does Not Determine Meaning

The medium of a source does not determine its future intellectual role.

For example, an image may function as:

- a medical radiograph for clinical reasoning;
- a field observation for disaster response;
- a casual snapshot for personal memory;
- an artwork for aesthetic interpretation;
- historical evidence for future social research;
- training material for an educational activity.

The same media type may therefore participate in very different reconstruction activities.

IdeaMark Core should not bind a source to one meaning merely because of its medium.

## 8.4 Context Is Also Open

The current context of a source does not exhaust its future potential.

A photograph taken casually today may become evidence for future historical, cultural, environmental, architectural, or personal reconstruction.

A planning framework created for one project may later become an Original Source for another field.

A Projection created during one reconstruction activity may later become an Original Source for improving Projection libraries.

The Core should therefore avoid fixing a source's future interpretation through current labels, captions, categories, or intended use.

## 8.5 Caption and Fixation of Meaning

A caption, label, metadata field, explanation, or category may help humans and AI systems use a source.

However, such contextual material may also narrow or fix interpretation.

IdeaMark Core does not prohibit captions or metadata.

It treats them as additional source context rather than as final meaning.

A future Projection may reinterpret the same source differently, use the caption as evidence, ignore it, question it, or treat it as a historically situated interpretation.

This preserves the possibility that future intellectual activity may discover value not visible in the original context.

## 8.6 Original Source and Projection

Projection determines how an Original Source becomes relevant for a particular reconstruction activity.

The same source may participate in multiple Projections.

```text
Original Source
        x
Projection A
        ↓
IdeaMark Document A

Original Source
        x
Projection B
        ↓
IdeaMark Document B
```

This does not mean the source itself changed.

It means the reconstruction strategy changed.

The Core should allow multiple projections of the same source to coexist.

## 8.7 Original Source and Future Knowledge Forms

IdeaMark Core should remain compatible with knowledge forms that already exist and forms that may emerge later.

Frameworks such as TPCG, OKF, IdeaMark documents, specifications, workflows, model outputs, collaborative records, and future intellectual artifacts may all become Original Sources when later reconstruction activities treat them as authoritative material.

The Core does not need to absorb these forms into itself.

It only needs to allow them to participate as sources.

This is why Original Source should remain an architectural role rather than a prescribed format.

## 8.8 Original Source and Authority

Calling something an Original Source does not mean that it is true, complete, unbiased, lawful to use, or ethically sufficient.

It means that, within a reconstruction activity, it is treated as material that should be returned to, inspected, cited, questioned, or interpreted.

Authority may come from provenance, domain practice, legal status, institutional trust, authorship, evidence quality, preservation, or other context.

IdeaMark Core does not define a universal theory of authority.

It preserves the architectural ability to return to the source and make such authority reviewable.

## 8.9 Non-goals

This section does not define:

- a universal source media taxonomy;
- a required metadata schema;
- a source ownership model;
- a copyright or licensing policy;
- a legal theory of evidence;
- a universal authority ranking;
- a preservation protocol;
- a required storage format;
- a required relationship between source and caption.

These concerns may be defined by implementations, domains, institutions, law, or future specifications.

## 8.10 Design Rationale

IdeaMark Core should not close the future of intellectual activity by predicting all possible source forms or contexts.

If the Core fixed Original Source to a narrow class of documents, it would fail to support images, sensor streams, collaborative artifacts, future knowledge representations, and new forms of human-AI work.

If the Core fixed a source's meaning through its current caption or context, it would prevent future reconstruction under different Projections.

The open-hand principle preserves potential.

It allows IdeaMark to treat sources as authoritative material for reconstruction without claiming that their present interpretation is final.

## 8.11 Summary

Original Source is an architectural role.

It is not limited by medium, format, origin, ownership, current caption, or current context.

A source becomes relevant through Projection and reconstruction.

By leaving both media and context open, IdeaMark Core remains capable of supporting future intellectual activities, future knowledge forms, and future human-AI collaboration without redesigning the Core around each new source type.
