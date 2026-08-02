# TIG Research Governance Standard — QIC Local Profile

## Candidate Status

```text
Repository: Quantum_Integrity_Core
Base snapshot: 080190b331d0713776bbc1bdf832ca79e2cd2c5b
Local scientific authority: Quantum_Integrity_Core
Cross-repository governance authority: Integrity_Nexus
Meta-standard reference: Integrity_Nexus pull request 1
State: CANDIDATE MAPPING; INDEPENDENT AUDIT PENDING
Scientific effect: NONE
```

This profile applies the draft TIG Research Governance Standard to QIC without replacing QIC's authority over its scientific content. Integrity Nexus controls cross-repository governance and shared status axes; QIC controls its own claims, evidence, derivations, limitations, and publication artifacts.

## Status and Claim Mapping

The local classes in `governance/claim_boundary_standard.md` are artifact/workflow descriptors, not replacements for the Integrity Nexus Claim Status axis. The local required-file list in `governance/repository_standard.md` is a QIC extension, not an ecosystem-wide standard. No local label may promote a claim, close an Open Question, or change global synchronization.

## Literature and Citation Inventory

| Artifact | Governing source | Release boundary |
|---|---|---|
| `papers/tig-paper/main.tex` | its embedded `thebibliography` block | Citation keys resolve internally; `papers/tig-paper/references.bib` is supplemental unless the build is changed to use it |
| `submission/arxiv/main.tex` | `submission/arxiv/references.bib` | Canonical bibliography for that submission tree |
| Repository citation identity | root `CITATION.cff` | The lowercase `citation.cff` is non-authoritative and must be removed |

Different publication artifacts may have different bibliographies. Versions represented as the same publication must share one source bibliography or record and justify their divergence. Bibliographic metadata requires source-level verification before release. Repository citation metadata and scientific bibliographies remain separate objects.

## Responsibility and Disclosures

```text
Sole accountable human author: Kai Stefan Dietrich
External funding: none
Known competing interests: none declared by the author
AI role: research infrastructure and assistance; not author, evidence, approval authority, or scientific authority
Data/code/ethics/privacy/security/IP: determine and record per publication artifact; NOT APPLICABLE requires a reason
Independent scientific review: not established by this profile
```

## Fourteen-Control Candidate Mapping

| Control | QIC evidence or rule | Candidate state |
|---|---|---|
| Integrity principles | Integrity Nexus standard plus QIC non-escalation rules | PRESENT IN CANDIDATE |
| Authority and scope | This profile; QIC repository authority boundary | PRESENT IN CANDIDATE |
| Claims, evidence, uncertainty, status | Local classes explicitly separated from Nexus status axes | PRESENT IN CANDIDATE |
| Literature and citation | Artifact-specific inventory above | PRESENT IN CANDIDATE |
| Records and provenance | Git snapshot, manifests, source paths, and correction history | PRESENT IN CANDIDATE |
| Data/code/reproducibility | Artifact-level applicability record required before release | PRESENT IN CANDIDATE |
| Authorship/contribution | Root author and citation records plus disclosure above | PRESENT IN CANDIDATE |
| Funding/interests/ethics/privacy/security/IP | Disclosure rule above | PRESENT IN CANDIDATE |
| Independent review | Fixed-snapshot read-only audit required | PRESENT IN CANDIDATE |
| Integrity concerns | Integrity Nexus concern protocol governs escalation | PRESENT IN CANDIDATE |
| Corrections/withdrawal | Versioned Git correction plus public action record required | PRESENT IN CANDIDATE |
| Responsible AI | Human responsibility and AI non-authorship recorded | PRESENT IN CANDIDATE |
| Conformance without status inflation | Candidate-only state; no scientific or sync effect | PRESENT IN CANDIDATE |
| Competence/risk/collaboration | Qualified physics/mathematics review and artifact risk assessment required; feedback is not endorsement | PRESENT IN CANDIDATE |

## Audit Handoff

An independent audit must verify this mapping, both manuscript bibliography paths, source metadata, all release disclosures, and the absence of a competing lowercase citation file. Until then the repository is not certified, accredited, independently validated, or publication-ready by virtue of this profile.
