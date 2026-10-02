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

## Konkrete strukturelle Zuordnung — Welle 1

Stand: 2026-10-02; Quellenfreeze main @ `8fb4989d43382ccf303c8c52b2c7af746fa35034`. Die historischen Angaben zum anfänglich leeren Register bleiben erhalten. Die folgenden Einträge registrieren vorhandene Pfadobjekte, keine neuen wissenschaftlichen Claims.

PRIMARY_OWNER_REPOSITORY für alle Zeilen: `integrity-nexus-kai/Quantum_Integrity_Core`. OBJECT_ID ist jeweils die bestehende repositoryrelative Pfadidentität. LOCAL_REFERENCE_PATH entspricht dem PRIMARY_OWNER_PATH; es wird kein Alias erzeugt.

| OBJECT_ID / OBJECT_NAME / PRIMARY_OWNER_PATH | OBJECT_TYPE | OWNERSHIP_CATEGORY | CLAIM_BOUNDARY | REVIEW_STATUS |
|---|---|---|---|---|
| `papers/tig-paper/main.tex` | Papertext | local-paper-object | Repräsentatives statisch-sphärisches Modell; Umfang laut Papertext | strukturell registriert; QIC-01–04 repariert, Echo-Physik offen |
| `submission/arxiv/main.tex` | Einreichungsmanuskript | local-submission-object | Eigener begrenzter Modelltext, negativer Vakuum-f(R)-Test, bedingte Laufzeit, keine Exportgleichheit | QIC-01–04 repariert; eigenständige Dynamik/Materie und physische Echo-Vorhersage offen |
| `field_equations/field_equation_1_0.md` | Feldgleichungsarchitektur | local-canonical-object | Research Candidate mit statisch-sphärischem Scope laut Quelle; keine vollständige kovariante Theorie | Quellstatus unverändert; parallele Tensorstatus nicht harmonisiert |
| `topology/theory/` | Grundlagen- und Strukturprogramm | local-research-object | Exploratory Mathematical Research laut eigenen Controls | Strukturzuordnung, keine wissenschaftliche Promotion |
| `theory/integrity_tensor/` | Tensorforschung und Kandidaten | local-research-object | Kandidatenslots, Evaluationen und Auditobjekte bleiben getrennt | Statusunterschiede in repair_tracking dokumentiert |
| `papers/derivations/` | Ableitungs- und Arbeitsnotizen | local-research-object | Scope jeder Notiz separat; keine automatische Gleichsetzung mit Paper oder kanonischem Ergebnis | Aussagenprüfung task-spezifisch offen |

Die strukturelle Zuordnung bestimmt, welche Datei für ihren eigenen Text bearbeitet wird. Sie erklärt keines der beiden Manuskripte zum globalen Scientific Owner aller TIG-Aussagen. Ein gemeinsamer wissenschaftlicher Nachfolger oder eine Exportgleichheit wird erst aus dem Quellenabgleich begründet. Stand und Nachweise: [Welle-1-Arbeitsnachweis](docs/REPAIR_WAVE1_2026-10-02.md).

Fortschreibung Welle 2: Quellenfreeze `88fef45371dbefe89ee35dce4e8accc5e8eb6baa`; [Kernrechnung](papers/derivations/quadratic_fr_and_horizon_checks.md) und [Arbeitsnachweis](docs/REPAIR_WAVE2_2026-10-02.md). Der negative quadratische Vakuumtest wird nicht auf die separate effektive TIG-Tensorarchitektur übertragen.

Fortschreibung Welle 3: Quellenfreeze `da326a4041054c01f2574d02312826870616670c`; [Arbeitsnachweis](docs/REPAIR_WAVE3_2026-10-02.md). Beide Manuskripte führen ihre geprüften Quellen und Laufzeitgrenzen selbst. Primäre Pfade der neuen Reparaturnachweise, mit unveränderter Repositoryzuständigkeit und LOCAL_REFERENCE_PATH jeweils gleich PRIMARY_OWNER_PATH:

| OBJECT_ID / OBJECT_NAME / PRIMARY_OWNER_PATH | OBJECT_TYPE | OWNERSHIP_CATEGORY | CLAIM_BOUNDARY | REVIEW_STATUS |
|---|---|---|---|---|
| `research/wave3_source_review.md` | Quellenprüfnotiz | local-research-object | versionierte fremde Quellen und lokale Übertragungsprüfung; kein TIG-Theorem | benannte Passagen geprüft, same-run |
| `papers/derivations/echo_delay_with_boundaries.md` | Bedingte Laufzeitableitung | local-research-object | statische Geometrie, vorgeschriebene Reflexion und Grenzen; keine physische TIG-Echo-Vorhersage | 18 exakte / fünf numerische Bedingungen PASS, same-run |
| `tools/verify_wave3.py` | Rechenprüfung | local-research-object | lokale Identitäts-/Konvergenzprüfung, keine unabhängige wissenschaftliche Validierung | ausgeführt mit SymPy 1.14.0 / mpmath 1.3.0 |

## Fortschreibung Welle 4

Die Quellenkarte und historischen Owner-/Statusbindungen bleiben erhalten. Die zehn kontrollierten Pfadmigrationen bewahren die Objektbytes und bisherige Quellenidentitäten; aktuelle Auflösung über registry/repair_tracking.json, wave4.path_migrations. Keine wissenschaftliche Statuspromotion durch Umbenennung. [Artefaktzuordnung](docs/ARTIFACT_BINDINGS.md) bindet historische PDFs und frühere Abbildungen; passende Mai-LaTeX-Quellen bleiben unbestimmt.

| OBJECT_ID / PRIMARY_OWNER_PATH | OBJECT_TYPE | OWNERSHIP_CATEGORY | CLAIM_BOUNDARY | REVIEW_STATUS |
|---|---|---|---|---|
| `tools/generate_horizon_figure.py` | Grafikgenerator | local-research-object | überprüfte statische Kubik; kein dynamischer Entstehungsnachweis | ausgeführt, Gleichungsresiduen geprüft |
| `figures/tig_horizon_branches.png` | Abgeleitete aktuelle Grafik | local-paper-object | Export des angegebenen Generators, keine eigene Theorieautorität | PNG/Metadaten/aktive Einbindung geprüft |
| `tools/export_arxiv.py` | Quellpaketexport | local-submission-object | transportiert exakt gebundene Quellen; veröffentlicht nicht | isolierter ZIP-Build PASS |
| `submission/exports/wave4_2026-10-02/` | PDFs und Quell-ZIP | exported-package-object | abgeleitete Arbeitsfassungen; kein neuer DOI, keine Einreichung | Inhalte/Fingerprints, Build, PDF und ZIP geprüft |

PRIMARY_OWNER_REPOSITORY jeweils Quantum_Integrity_Core; LOCAL_REFERENCE_PATH jeweils derselbe Pfad. Primäre Manuskriptquellen bleiben papers/tig-paper/main.tex beziehungsweise submission/arxiv/main.tex. Der mitgelieferte unsrtnat-Stil bewahrt seinen eigenen Drittanbieter-Lizenzhinweis.
