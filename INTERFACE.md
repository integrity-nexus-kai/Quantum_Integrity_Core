# Repository Interface

## Purpose

This document defines the interface boundary of the Quantum Integrity Core repository.

It defines how this repository may interact with Integrity Nexus and other connected repositories without weakening local source-of-truth boundaries.

---

## Source-of-Truth Boundary

Quantum Integrity Core owns its repository-local canonical files, research files, paper files, and submission files.

External repositories may reference this material, but references do not transfer ownership.

---

## Import Boundary

Imported material must preserve:

- source repository,
- source path,
- source status,
- claim boundary,
- and limitations.

Imported material is not automatically canonical inside this repository.

---

## Export Boundary

Exports from this repository must preserve:

- candidate versus reviewed status,
- research versus paper status,
- limitations,
- open dependencies,
- and repository-local source path.

---

## Interface Rule

```text
Candidate != derived.
Working assumption != proof.
Paper draft != repository-complete status.
Repository reference != object ownership transfer.
```

---

## Audit Status

Status:

```text
STRUCTURAL INTERFACE FILE — ACTIVE
```
