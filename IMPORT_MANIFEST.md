# Import Manifest

## Purpose

This manifest defines import rules for Quantum Integrity Core.

It is a structural governance file only.
It does not validate derivations or promote scientific claims.

---

## Import Rule

Imported material must retain:

- source repository identity,
- source path,
- source version or commit when available,
- object type,
- import status,
- and claim boundary.

---

## Required Import Fields

Each registered import should specify:

- IMPORT_ID
- SOURCE_REPOSITORY
- SOURCE_PATH
- SOURCE_COMMIT_OR_VERSION
- OBJECT_TYPE
- LOCAL_TARGET_PATH
- IMPORT_STATUS
- CLAIM_BOUNDARY
- REVIEW_STATUS

---

## Import Status Values

Allowed values:

- referenced
- candidate
- reviewed
- superseded
- archived
- blocked

---

## Boundary Rule

Imported material is not automatically canonical.
Referenced material is not automatically derived.
Reviewed material is not automatically proven.

---

## Initial Registry

No imports are registered in this manifest at creation time.
