# QIC — Artefakt- und Abbildungszuordnung

Version 1.3 · 2026-10-03 · abgeleitete strukturelle Sicht. Eingang main @ `9f6cdf096716c6d070685b0d88555f403f6db8fa`. Alle 255 Eingangsblobs lokal gegen Git verifiziert: 241 Textdateien und 14 als PDF/PNG benannte Objekte. Eine PNG-Endung beweist keinen Bildinhalt.

## PDF-Objekte und Quellenlücke — QIC-20

| Objekt | Verifizierte Identität und Versionsmerkmale | Quellen-/Verwendungsergebnis |
|---|---|---|
| papers/tig-paper/TIG3_Vacuum_Structure.pdf | Git-Blob 8c223ea0f80d1b32f9b3494d4cf9fc01550f126c; 14 Seiten; Titel „Topological Integrity Gravity III: Conditional Vacuum Admissibility and Bounded Curvature Structure“; Druck-/PDF-Datum 17.05.2026; Uploadcommit 379a07df7ba38fa1531c9a0963c60a83d4d5603b | Exakt im historischen Zenodo-Repositoryarchiv enthalten. Autorenimport vom 3. Oktober: elf vollständige Eingabedateien, erfolgreicher Originalbuild und textgleiche 14-Seiten-Rekonstruktion; fünf RGB-identische Abbildungen. Exakte Mai-Quellbytes nicht zurückgewonnen; damaliges benachbartes Paper-main.tex hat einen anderen Titel. |
| papers/tig-paper/TIG_Paper.pdf | Git-Blob 33cecf3454fdf2ab8ff93372f9f3d1c4f9e5ef69; vier Seiten; Titel „Topological Integrity Gravity (TIG): A Quadratic f(R) Model with a Critical Horizon Transition“; Druck-/PDF-Datum 03.05.2026; Uploadcommit 1b3bf81b5a79d3a542cca8ad4fa140b34ca98888 vom 04.05.2026 | Exakt im historischen Repositoryarchiv enthalten; fehlende Zitate/Abbildungsplatzhalter in dieser Alt-PDF. Historische Hauptquelle Blob 5acbd0d12e2fd79ac3b4f8ccddbcddb0fb69f76e bytegleich gebunden; Fehlereingabe-Rekonstruktion stimmt auf allen vier Seiten überein. PDF-Altdefekte erhalten; keine fehlerfreie Kompilierung behauptet. |
| submission/exports/wave4_2026-10-02/paper.pdf | Paper v1.4, zwölf Seiten; aktuelle source main.tex mit 18 eingebetteten Literaturangaben | Eindeutiger neuer lokaler Build, SHA-256 in Nachweissicht. Keine Überschreibung der Mai-PDFs. |
| submission/exports/wave4_2026-10-02/arxiv.pdf | Draft Welle 4, sechs Seiten; source submission/arxiv/main.tex und references.bib | PDF aus isoliertem Quell-ZIP; vollständig pixelgleich zum Repository-Build. Kein neues Release/DOI. |

Metadaten-/Druckdatum, Uploaddatum und Veröffentlichungsdatum sind verschiedene Ereignisse. **QIC-20 ERLEDIGT:** Beide historischen PDFs sind durch vollständige Inhalts-/Layoutvergleiche ihren belegten Quellenversionen zugeordnet. Exakte ursprüngliche Compilerzustände und vollständige Eingabeablagen bleiben ausdrücklich unbestätigt; kein fehlendes Originalasset wurde erfunden. PDFs selbst bleiben unverändert. [Historische DOI-/Archivkette](PUBLICATION_CHAIN.md).

## Figuren: Identität, Verwendung und Evidenzgrenze — QIC-21

Neue aktive Grafik: [figures/tig_horizon_branches.png](../figures/tig_horizon_branches.png), erzeugt durch [tools/generate_horizon_figure.py](../tools/generate_horizon_figure.py). 601 Stichproben je Ast, Residuum kleiner 2·10⁻¹⁵; kritischer Doppelpunkt und β=0-Randfall explizit. [Metadaten](../figures/tig_horizon_branches.json). Statische Hayward-Repräsentantin, kein Evolutionsbeweis. Einzige aktive includegraphics-Abhängigkeit im Einreichungsmanuskript; Papertext ohne eingebundene Bilder.

| Aktueller Pfad des vorhandenen Objekts | Unveränderte Eingangsidentität (Git-Blob) | Rolle / aktuelle Verwendung |
|---|---|---|
| `figures/tig_expansion_history_prediction.png` | `61334d3036a95863069265fa1e553687581b9c4f` | frühere illustrative Grafik; passende Generator-/Datenfassung nicht rekonstruiert, nicht aktuell eingebunden |
| `figures/tig_horizon_radius_prediction.png` | `f343f7dfc7b54e404fb415ef70bf12d6fa516d15` | frühere äußere Horizontgrafik, bytegleich mit Paperkopie; aktuelle Einreichung verwendet den neuen Generator |
| `papers/tig-paper/tig_bifurcation_robustness.png` | `3764bd04372009733b406b01ecd2992c9ce4fed4` | frühere illustrative Grafik; passende Generator-/Datenfassung nicht rekonstruiert, nicht aktuell eingebunden |
| `papers/tig-paper/tig_echo_delay_prediction_legacy.png` | `29afc26e433346dcea666784fa5af2da78596cca` | frühere Echoillustration; keine gebundene Generator-/Randvorschrift, kein aktueller Echo-Nachweis |
| `papers/tig-paper/tig_horizon_radius_prediction.png` | `f343f7dfc7b54e404fb415ef70bf12d6fa516d15` | bytegleiche Kopie; erhalten, nicht aktuell eingebunden |
| `papers/tig-paper/tig_horizon_transition_publication.png` | `733b93d29f8c4b75ee1401e14e106eabfafbf68f` | frühere illustrative Grafik; passende Generator-/Datenfassung nicht rekonstruiert, nicht aktuell eingebunden |
| `papers/tig-paper/tig_photon_sphere_deviation_legacy.png` | `0833bf6fc9a3bd71ec6679c905d5f9653bccbb97` | echtes PNG mit anderer Identität; Generator/Parameterdomäne ungebunden, keine aktuelle Evidenz |
| `papers/tig-paper/photon_sphere_generation_notes.md` | `2d719f735246498a0f4a1239c759da02d22dbecb` | UTF-8-Chat-/Generierungsnotiz, kein PNG; vollständige Bytes als Markdown erhalten |
| `papers/tig_schwarzschild_horizon_comparison.png` | `b6347b60bb6ea2619f5ba9aafd6d702dbc2a0e15` | frühere illustrative Grafik; passende Generator-/Datenfassung nicht rekonstruiert, nicht aktuell eingebunden |
| `submission/arxiv/tig_echo_delay_prediction_legacy.png` | `29afc26e433346dcea666784fa5af2da78596cca` | bytegleich mit Paper-Echoillustration; früheres Exportobjekt |
| `submission/arxiv/tig_horizon_branches_critical_transition.png` | `99788c21fb868b9f0d4ddac98269adee3ec4670e` | frühere illustrative Grafik; passende Generator-/Datenfassung nicht rekonstruiert, nicht aktuell eingebunden |
| `submission/arxiv/tig_qnm_frequency_prediction.png` | `48f29ccc226a0efa27202bb18e422d19080ae56c` | frühere illustrative Grafik; passende Generator-/Datenfassung nicht rekonstruiert, nicht aktuell eingebunden |

Alle elf echten Eingangs-PNGs visuell verglichen und Format/Dimensionen geprüft. Zwei Byte-Dublettengruppen: äußere Horizontgrafik sowie Echoillustration. Unterschiedliche Bildinhalte bleiben getrennt; keine stillschweigende Bildersetzung. Fehlende Generator-/Datenbindungen werden nicht durch visuelle Ähnlichkeit ersetzt. Altgrafiken sind aus dem aktuellen Export ausgeschlossen, nicht wissenschaftlich validiert.

## Kontrollierte Dateinamen — QIC-24

| Eingangsname | Aktueller Name | Ergebnis |
|---|---|---|
| `topology/admissibility_conditions,md` | `topology/admissibility_conditions.md` | identische vollständige Bytes / Blob-ID |
| `papers/derivations/integrity_functional.mdderi` | `papers/derivations/integrity_functional.md` | identische vollständige Bytes / Blob-ID |
| `papers/derivations/concrete_scalar_mode:prediction.md` | `papers/derivations/concrete_scalar_mode_prediction.md` | identische vollständige Bytes / Blob-ID |
| `strategy/tig_emergence_progra` | `strategy/tig_emergence_program.md` | identische vollständige Bytes / Blob-ID |
| `project/submission/reviwer_.md` | `project/submission/reviewer_notes.md` | identische vollständige Bytes / Blob-ID |
| `papers/tig-paper/arvix_upload` | `papers/tig-paper/arxiv_upload_placeholder.txt` | identische vollständige Bytes / Blob-ID |
| `papers/tig-paper/tig_photon_sphere_deviation.png` | `papers/tig-paper/photon_sphere_generation_notes.md` | identische vollständige Bytes / Blob-ID |
| `papers/tig-paper/tig_photon_sphere_deviation (1).png` | `papers/tig-paper/tig_photon_sphere_deviation_legacy.png` | identische vollständige Bytes / Blob-ID |
| `submission/arxiv/tig_echo_delay_prediction .png` | `submission/arxiv/tig_echo_delay_prediction_legacy.png` | identische vollständige Bytes / Blob-ID |
| `papers/tig-paper/tig_echo_delay_prediction.png` | `papers/tig-paper/tig_echo_delay_prediction_legacy.png` | identische vollständige Bytes / Blob-ID |

Kein Zielpfad war belegt; keine Objektbytes verloren. Die skalare Notiz hat denselben Inhalt wie tig_positioning.md; beide Quellenidentitäten bleiben getrennt dokumentiert, keine wissenschaftliche Konsolidierung durch Dateinamenspflege. Der Upload-Platzhalter bleibt leer und begründet keine Einreichung. Dateinamen innerhalb expliziter Archive/DOI-Fassungen bleiben historische Identitäten. Aktuelle lokale Verweise geprüft; historische Register-/Nachweispfade bleiben als Snapshots erhalten und über wave4.path_migrations auflösbar.

## Ergänzung v1.1 — vollständige erreichbare Historie geprüft

Auf Nutzerauftrag wurde QIC-20 nach Welle 4 zusätzlich über die gesamte erreichbare QIC-Historie untersucht: 634 Commits, 536 unterschiedliche Blobs aus main und v1.0.0, 2.684 Git-Objekte mit erneut geprüfter Identität. Die oben dokumentierten Welle-4-Snapshots bleiben historische Prüfstände.

Für das vierseitige TIG_Paper.pdf ist nun ein inhaltlich passender Hauptquellkandidat gebunden: submission/arxiv/main.tex, Blob `5acbd0d12e2fd79ac3b4f8ccddbcddb0fb69f76e`, frühester gefundener Snapshot [d15eea1](https://github.com/integrity-nexus-kai/Quantum_Integrity_Core/blob/d15eea1003efbc6632f847255221dee0231271e6/submission/arxiv/main.tex). Titel, Datum, Prosa, Abschnittsstruktur und Platzhalter stimmen in den dokumentierten Merkmalen überein. Vollständiges Original-Erzeugungspaket und genauer Compiler-/Eingabestand bleiben unbestätigt; kein historischer PDF-Neubuild oder Pixelvergleich durchgeführt. Für TIG3 kein passendes vollständiges Paket im untersuchten erreichbaren Bestand identifiziert.

**QIC-20 bleibt TEILBEARBEITET / QUELLENBLOCKIERT.** [Abschlussnachweis](REPAIR_CLOSEOUT_2026-10-02.md), [vollständiges Quellensuchmanifest](../registry/repair_source_search_2026-10-02.json). Kein bestehendes historisches PDF oder Quellenblob überschrieben.

## Fortschreibung — TIG3-Quellenbindung, 3. Oktober 2026

Die vorstehenden Wellen-/Historienbefunde behalten ihre geprüften Bezugsstände. Neu: [TIG3-Quellstand](../papers/tig3-vacuum/README.md) aus dem Autoren-ZIP vom 3. Oktober bytegleich importiert; erfolgreiche Builds mit 16 Seiten (Originaleinstellung) und 14 Seiten (kontrollierte 11pt-/Mai-Rekonstruktion). Auf allen 14 Vergleichsseiten gleicher Text nach alleiniger Aufzählungszeichen-Normalisierung, fünf RGB-identische Abbildungen, gleiche 32 nummerierte Gleichungen und 20 Literaturangaben. [Vollständiger Vergleich](TIG3_SOURCE_COMPARISON_2026-10-03.md), [Manifest](../registry/tig3_source_binding_2026-10-03.json).

TIG3-Teil von QIC-20 erledigt; Gesamtaufgabe bleibt teilbearbeitet wegen des vollständigen ursprünglichen Erzeugungspakets des vierseitigen `TIG_Paper.pdf`. Die exakten Mai-TIG3-Quellbytes und der damalige Compilerstand sind nicht zurückgewonnen; die Rekonstruktion ist entsprechend bezeichnet. Quellenimport ersetzt weder wissenschaftliche Owner noch reparierte Manuskripte, historische PDF-/DOI-Objekte oder Forschungsstatus.

## Aktueller Abschluss — QIC-20, 3. Oktober 2026

**QIC-20 ERLEDIGT; alle 24 Reparaturaufgaben erledigt.** [Abschlussnachweis](QIC20_SOURCE_BINDING_CLOSEOUT_2026-10-03.md), [Manifest](../registry/qic20_source_binding_closeout_2026-10-03.json). Die unveränderte historische Hauptquelle des vierseitigen Mai-Papers reproduziert alle vier Seiten einschließlich der sieben ungelösten Zitatkeys, zweier Bildplatzhalter und doppelter leerer References-Überschrift. Zwei unabhängige Arbeitsordnerläufe bestätigen den Vergleich; Compiler-Exitcodes bleiben 1/2/1/1. Die Quelle wird als Archivobjekt registriert; keine fehlenden Originaldateien erfunden. Quelle/PDF-Zuordnung ist erfüllt, exakter historischer Compiler-/Eingabestand bleibt qualifiziert. Die vorher dokumentierten Teilbearbeitungsstände sind historische Zwischenstände und werden durch diesen Abschluss abgelöst. Aktuelle reparierte Manuskripte/Exporte, historische PDF-/DOI-Objekte und Forschungsstatus bleiben unverändert.
