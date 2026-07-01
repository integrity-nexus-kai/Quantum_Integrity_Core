# LM Export Manifest

## Purpose

This manifest defines language-model export readiness rules for Quantum Integrity Core.

It is a structural readiness file.
It does not create theory, validate derivations, or promote claims.

---

## LM Export Readiness Criteria

An LM export is ready only if it preserves:

- repository identity,
- source paths,
- candidate versus reviewed status,
- research versus paper status,
- limitations,
- unresolved dependencies,
- and claim-boundary rules.

---

## Required LM Export Fields

Each LM export should specify:

- LM_EXPORT_ID
- EXPORT_SCOPE
- SOURCE_PATHS
- SOURCE_COMMITS_OR_VERSIONS
- INCLUDED_LIMITATIONS
- INCLUDED_OPEN_DEPENDENCIES
- CLAIM_BOUNDARY_LEVEL
- REVIEW_STATUS

---

## Disallowed LM Export Behavior

LM exports must not:

- remove limitations,
- present candidates as completed derivations,
- present working assumptions as proofs,
- merge paper status with repository status,
- or treat summaries as source-of-truth files.

---

## Initial Registry

No LM exports are registered in this manifest at creation time.
