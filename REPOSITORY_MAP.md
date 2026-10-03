# Repository Map

## Purpose

This document maps the internal structure of the Quantum Integrity Core repository.

It is a structural map only.
It does not create, validate, or promote scientific claims.

---

## Repository Role

Repository role:

```text
Quantum Integrity Core research and paper-development repository
```

Primary function:

- maintain repository-local research artifacts,
- maintain paper and submission artifacts,
- preserve canonical status boundaries,
- distinguish candidate material from reviewed material,
- and expose controlled interfaces to the wider Integrity Nexus architecture.

---

## Major Document Groups

Observed major groups:

- root canonical and status files,
- topology material,
- theory material,
- field-equation material,
- paper and submission material,
- application-oriented material,
- figures and supporting artifacts.

---

## Source-of-Truth Boundary

The repository-local canonical status file controls canonical repository status.

Paper artifacts are not automatically equivalent to repository-level canonical status.
Research artifacts are not automatically equivalent to completed derivations.

---

## Cross-Repository Boundary

This repository may be referenced by Integrity Nexus or other connected repositories.

References must preserve:

- source path,
- source status,
- claim boundary,
- and limitations.

---

## Audit Status

Status:

```text
STRUCTURAL MAP — ACTIVE
```

## Tatsächliche Ablagen und Quellenrollen — 2026-10-02

Geprüfter Tree: main @ `8fb4989d43382ccf303c8c52b2c7af746fa35034`; 244 Dateiobjekte, vollständiger nicht abgeschnittener Tree. Die Rollen sind aus vorhandenen Controls abgeleitet; einzelne Forschungsnotizen behalten ihren eigenen Status.

| Tatsächlicher Pfad | Dateiobjekte | Rolle und maßgeblicher Einstieg |
|---|---:|---|
| `field_equations/` | 4 | Aktuelle begrenzte Architektur; field_equation_1_0.md, validation_status.md und open_questions.md gemeinsam lesen. |
| `topology/` | 87 | Grundlagen, Struktur, Interpretationen und Exploration; topology/theory/README.md und die Controls unter structure/. |
| `theory/` | 37 | Tensor- und Sektorforschung; Kandidaten-/Audit-/Statusobjekte nicht gleichsetzen. |
| `papers/derivations/` | 36 | Ableitungs-/Arbeitsnotizen; jeweiliger Scope gilt. |
| `papers/tig-paper/` | 13 | Papertext main.tex; eingebettetes Literaturverzeichnis. abstract.tex/photon_sphere.tex sind im aktuellen main.tex nicht eingebunden. |
| `submission/arxiv/` | 5 | Eigenständiges Einreichungsmanuskript und BibTeX; Abbildungsabhängigkeit auf figures/. |
| `papers/archive/` | 9 | Ausdrücklich archivierte Materialgruppen; keine Current-Autorität aus Pfadnähe. |
| `papers/topological-foundations-program/` | 1 | Programmpaper/-übersicht; erklärt die kubische Herleitung ausdrücklich als nicht abgeschlossen. |

`papers/TIG2/` und `papers/TIG3/` existieren im geprüften Tree nicht. TIG1/TIG2/TIG3 bleiben wissenschaftliche Ebenenbezeichnungen; daraus werden keine neuen Ordner oder Owner erzeugt. Die tatsächliche Evolutionsablage ist `topology/evolution/`; `topology/theory/evolution/` ist in diesem Tree nicht vorhanden.

Weitere Arbeitsbindung: [Build und Manuskriptzuordnung](docs/BUILD_WORKFLOW.md), [Welle-1-Arbeitsnachweis](docs/REPAIR_WAVE1_2026-10-02.md), [abgeleitete Nachweissicht](registry/repair_tracking.json).

## Reparatur-Endstand Welle 4 — 2026-10-02

Aktueller Eingang main @ `9f6cdf096716c6d070685b0d88555f403f6db8fa`; 255 Blobs, 241 Textdateien und 14 als PDF/PNG benannte Objekte gegen Git geprüft. Eine vermeintliche PNG ist tatsächlich UTF-8-Chattext; ihr korrigierter Pfad und die übrigen Migrationen stehen in [Artefaktzuordnung](docs/ARTIFACT_BINDINGS.md). Der vorstehende Welle-1-Tree bleibt historisch.

[Literaturmatrix](research/tig_literature_matrix.md) · [Quellenprüfung](research/wave3_source_review.md) · [Manuskript-/PDF-/Abbildungsrollen](docs/ARTIFACT_BINDINGS.md) · [Veröffentlichungskette](docs/PUBLICATION_CHAIN.md) · [Build/Export](docs/BUILD_WORKFLOW.md). Aktuelle Exportobjekte unter submission/exports/wave4_2026-10-02/ ersetzen keine Paper- oder Scientific Owner. Historische PDF-Quellenrekonstruktion bleibt QIC-20 teilbearbeitet.

## Fortschreibung — TIG3-Quellenbindung, 3. Oktober 2026

Die vorstehenden Wellen-/Historienbefunde behalten ihre geprüften Bezugsstände. Neu: [TIG3-Quellstand](papers/tig3-vacuum/README.md) aus dem Autoren-ZIP vom 3. Oktober bytegleich importiert; erfolgreiche Builds mit 16 Seiten (Originaleinstellung) und 14 Seiten (kontrollierte 11pt-/Mai-Rekonstruktion). Auf allen 14 Vergleichsseiten gleicher Text nach alleiniger Aufzählungszeichen-Normalisierung, fünf RGB-identische Abbildungen, gleiche 32 nummerierte Gleichungen und 20 Literaturangaben. [Vollständiger Vergleich](docs/TIG3_SOURCE_COMPARISON_2026-10-03.md), [Manifest](registry/tig3_source_binding_2026-10-03.json).

TIG3-Teil von QIC-20 erledigt; Gesamtaufgabe bleibt teilbearbeitet wegen des vollständigen ursprünglichen Erzeugungspakets des vierseitigen `TIG_Paper.pdf`. Die exakten Mai-TIG3-Quellbytes und der damalige Compilerstand sind nicht zurückgewonnen; die Rekonstruktion ist entsprechend bezeichnet. Quellenimport ersetzt weder wissenschaftliche Owner noch reparierte Manuskripte, historische PDF-/DOI-Objekte oder Forschungsstatus.

## Aktueller Abschluss — QIC-20, 3. Oktober 2026

**QIC-20 ERLEDIGT; alle 24 Reparaturaufgaben erledigt.** [Abschlussnachweis](docs/QIC20_SOURCE_BINDING_CLOSEOUT_2026-10-03.md), [Manifest](registry/qic20_source_binding_closeout_2026-10-03.json). Die unveränderte historische Hauptquelle des vierseitigen Mai-Papers reproduziert alle vier Seiten einschließlich der sieben ungelösten Zitatkeys, zweier Bildplatzhalter und doppelter leerer References-Überschrift. Zwei unabhängige Arbeitsordnerläufe bestätigen den Vergleich; Compiler-Exitcodes bleiben 1/2/1/1. Die Quelle wird als Archivobjekt registriert; keine fehlenden Originaldateien erfunden. Quelle/PDF-Zuordnung ist erfüllt, exakter historischer Compiler-/Eingabestand bleibt qualifiziert. Die vorher dokumentierten Teilbearbeitungsstände sind historische Zwischenstände und werden durch diesen Abschluss abgelöst. Aktuelle reparierte Manuskripte/Exporte, historische PDF-/DOI-Objekte und Forschungsstatus bleiben unverändert.
