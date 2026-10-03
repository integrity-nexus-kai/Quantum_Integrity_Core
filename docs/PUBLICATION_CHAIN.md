# QIC — Veröffentlichungskette und DOI-Zuordnung

Version 1.2 · 2026-10-03 · QIC-23 · Zuordnung, keine neue Veröffentlichung.

## Aktuelle Arbeitsartefakte

| Quelle | Abgeleitetes Artefakt | Technischer Nachweis / Publikationsstatus |
|---|---|---|
| papers/tig-paper/main.tex, Paper v1.4, eingebettete Bibliografie | submission/exports/wave4_2026-10-02/paper.pdf | aktueller lokaler PDF-Build, zwölf Seiten; kein neuer DOI oder Upload |
| submission/arxiv/main.tex, references.bib, unsrtnat.bst, generierte Horizontgrafik, aktuelles LICENSE | submission/exports/wave4_2026-10-02/arxiv_source.zip und arxiv.pdf | Quellenbytes gebunden, ZIP isoliert gebaut, sechs PDF-Seiten pixelgleich zum Repo-Build; nicht eingereicht |

SHA-256-Fingerprints jedes Quell-ZIP-Mitglieds: [source_manifest.json](../submission/exports/wave4_2026-10-02/source_manifest.json). PDF-/Quellen-/Logfingerprints und Abbildungs-/Pfadmigrationen: wave4 in [repair_tracking.json](../registry/repair_tracking.json). Exportobjekte sind kein Scientific Owner; lokale Arbeitsfassung ist nicht durch einen früheren DOI publiziert. PDF-Zeitstempel sind keine wissenschaftlichen Versionsnachweise. Ein Compilerwechsel kann neue PDF-Bytes erzeugen, ohne denselben Quellenhash zu ändern.

## Verifizierter historischer Repository-Release

- GitHub-Release [v1.0.0](https://github.com/integrity-nexus-kai/Quantum_Integrity_Core/releases/tag/v1.0.0), veröffentlicht 19.05.2026, 17:58:28 UTC; Tagcommit b099c24b09c26a0aa5258c17ebb051f65f65f951. Keine separat hochgeladenen GitHub-Releaseassets.
- [Zenodo-Record 20292983](https://zenodo.org/records/20292983), Titel „integrity-nexus-kai/Quantum_Integrity_Core: Topological Integrity Gravity (TIG) v1.0.0“; Ressourcentyp Software. **Versions-DOI 10.5281/zenodo.20292983**, **Konzept-DOI 10.5281/zenodo.20292982**. Datensatz verweist auf den GitHub-Tag; IsVersionOf/HasVersion-Beziehung zusätzlich im DataCite-Datensatz geprüft.
- Primärdaten: https://zenodo.org/api/records/20292983 und https://api.datacite.org/dois?query=%22Quantum_Integrity_Core%22 . Katalogabfrage identifiziert den historischen Datensatz; Web-Landingpage über Suchdienst nicht abrufbar, offizielle API und Download direkt erfolgreich.
- Das 8.185.014-Byte-Archiv ist gegen das bereitgestellte MD5 e6aa822ab4b152d300a84a679d0ef42a geprüft; SHA-256 9a8b38894c6982b11dc8c169050a07aee1f131e526587afe7078bfc6e57526a6. **Alle 156 enthaltenen Dateien entsprechen exakt den Git-Blob-Identitäten des Tags**, einschließlich beider Mai-PDFs.

Damit sind die Mai-PDFs als Bestandteile dieses Repositoryarchivs belegt; daraus folgt keine nachgewiesene passende LaTeX-Erzeugungsquelle und kein eigener Artikel-DOI für TIG3. QIC-20 ist inzwischen durch den gesonderten Quellen-/Versionsvergleich abgeschlossen; siehe den aktuellen Abschluss unten. Der zusätzliche Zenodo-Artikelrecord 20293344/Versions-DOI 10.5281/zenodo.20293344 betrifft das separate TIG-II-PDF, nicht automatisch das Repository, die Mai-TIG3-PDF oder eine jetzige Manuskriptfassung. Er wird nicht als deren DOI übernommen.

## Versions- und Lizenzgrenzen

Historisches Archiv/Tag/DOI bleiben unverändert. Der Zenodo-Repositoryrecord beschreibt die historische Lizenz als MIT; aktuelles main besitzt die eigene Lizenz v2.0. Die historische Lizenznotiz und der aktuelle LICENSE-Inhalt werden in diesem Lauf nicht geändert. [Bestehende Übergangsnotiz](../LICENSE_DOI_TRANSITION_NOTICE.md), [kanonische Versionsgrenze](../CANONICAL_STATUS.md). Der mitgelieferte unsrtnat-Stil bewahrt seinen eigenen Drittanbieter-Lizenzhinweis.

QIC-23 ist als Versions-/Artefaktzuordnung erledigt. Keine arXiv-Einreichung, neue Release-/DOI-Veröffentlichung oder unabhängige wissenschaftliche Freigabe ausgeführt. Ein künftiges Publikationspaket muss seinen konkreten Quellenstand, PDF, Lizenz und Versions-/Konzept-DOI separat binden; die unrekonstruierten Mai-Quellen werden nicht stillschweigend ergänzt.

## Fortschreibung — TIG3-Quellenbindung, 3. Oktober 2026

Die vorstehenden Wellen-/Historienbefunde behalten ihre geprüften Bezugsstände. Neu: [TIG3-Quellstand](../papers/tig3-vacuum/README.md) aus dem Autoren-ZIP vom 3. Oktober bytegleich importiert; erfolgreiche Builds mit 16 Seiten (Originaleinstellung) und 14 Seiten (kontrollierte 11pt-/Mai-Rekonstruktion). Auf allen 14 Vergleichsseiten gleicher Text nach alleiniger Aufzählungszeichen-Normalisierung, fünf RGB-identische Abbildungen, gleiche 32 nummerierte Gleichungen und 20 Literaturangaben. [Vollständiger Vergleich](TIG3_SOURCE_COMPARISON_2026-10-03.md), [Manifest](../registry/tig3_source_binding_2026-10-03.json).

TIG3-Teil von QIC-20 erledigt; Gesamtaufgabe bleibt teilbearbeitet wegen des vollständigen ursprünglichen Erzeugungspakets des vierseitigen `TIG_Paper.pdf`. Die exakten Mai-TIG3-Quellbytes und der damalige Compilerstand sind nicht zurückgewonnen; die Rekonstruktion ist entsprechend bezeichnet. Quellenimport ersetzt weder wissenschaftliche Owner noch reparierte Manuskripte, historische PDF-/DOI-Objekte oder Forschungsstatus.

## Aktueller Abschluss — QIC-20, 3. Oktober 2026

**QIC-20 ERLEDIGT; alle 24 Reparaturaufgaben erledigt.** [Abschlussnachweis](QIC20_SOURCE_BINDING_CLOSEOUT_2026-10-03.md), [Manifest](../registry/qic20_source_binding_closeout_2026-10-03.json). Die unveränderte historische Hauptquelle des vierseitigen Mai-Papers reproduziert alle vier Seiten einschließlich der sieben ungelösten Zitatkeys, zweier Bildplatzhalter und doppelter leerer References-Überschrift. Zwei unabhängige Arbeitsordnerläufe bestätigen den Vergleich; Compiler-Exitcodes bleiben 1/2/1/1. Die Quelle wird als Archivobjekt registriert; keine fehlenden Originaldateien erfunden. Quelle/PDF-Zuordnung ist erfüllt, exakter historischer Compiler-/Eingabestand bleibt qualifiziert. Die vorher dokumentierten Teilbearbeitungsstände sind historische Zwischenstände und werden durch diesen Abschluss abgelöst. Aktuelle reparierte Manuskripte/Exporte, historische PDF-/DOI-Objekte und Forschungsstatus bleiben unverändert.
