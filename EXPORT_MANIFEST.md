# Export Manifest

## Purpose

This manifest defines export rules for Quantum Integrity Core.

Exports may include research summaries, paper packages, LM-facing packages, or cross-repository reference packages.

This file does not validate scientific claims.

---

## Export Rule

Each export must preserve:

- source path,
- source version or commit when available,
- object ownership,
- candidate/reviewed/canonical status,
- limitations,
- and open dependencies.

---

## Required Export Fields

Each registered export should specify:

- EXPORT_ID
- EXPORT_TARGET
- SOURCE_PATHS
- SOURCE_COMMITS_OR_VERSIONS
- OBJECT_TYPES
- CLAIM_BOUNDARY
- LIMITATIONS_INCLUDED
- LM_READY
- REVIEW_STATUS

---

## Export Status Values

Allowed values:

- draft
- ready-for-review
- approved
- superseded
- blocked
- archived

---

## Boundary Rule

Exported material is not automatically proven material.
Paper export is not automatically repository-complete status.
LM-ready material is not automatically claim-complete material.

---

## Initial Registry

No exports are registered in this manifest at creation time.
