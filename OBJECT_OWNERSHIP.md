# Object Ownership Manifest

## Purpose

This manifest defines object ownership boundaries for Quantum Integrity Core.

Object ownership is structural ownership only.
It does not imply proof status, derivation completion, or physical validation.

---

## Ownership Rule

Each object should have one primary source-of-truth location.

Paper artifacts, research artifacts, figures, status files, and export packages must not silently replace one another.

---

## Ownership Categories

Allowed categories:

- local-canonical-object
- local-research-object
- local-paper-object
- local-submission-object
- imported-reference-object
- exported-package-object
- cross-repository-interface-object

---

## Required Ownership Fields

Each registered object should specify:

- OBJECT_ID
- OBJECT_NAME
- OBJECT_TYPE
- PRIMARY_OWNER_REPOSITORY
- PRIMARY_OWNER_PATH
- LOCAL_REFERENCE_PATH
- OWNERSHIP_CATEGORY
- CLAIM_BOUNDARY
- REVIEW_STATUS

---

## Boundary Rule

Paper object is not automatically canonical research object.
Research object is not automatically completed derivation.
Export package is not primary source of truth.

---

## Initial Registry

No object entries are registered in this manifest at creation time.
