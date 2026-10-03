# QIC-20 — Abschluss der historischen PDF-Quellenzuordnung

**Version:** 1.0 · **Datum:** 3. Oktober 2026  
**Eingang:** QIC `main` @ `574a24d072f0b0eb446601349683d1bf682fe12a`  
**Auftrag:** „dann führe aus was zum schliessen der aufgabe führt bitte“  
**Ergebnis:** **QIC-20 ERLEDIGT; alle 24 beauftragten Reparaturen erledigt.**

## Alter Stand, neuer Stand und Delta

| Gegenstand | Alter Stand | Neuer Stand |
|---|---|---|
| Vierseitiges Mai-Paper | Hauptquellkandidat gefunden; noch kein historischer Neubuild/Vergleich | Unveränderte historische Quelle gesichert; Fehlereingabe-Build reproduziert alle vier Seiten des alten PDFs |
| Quellenversion | Inhaltlich passende Einzelmerkmale | Exakter Git-Blob `5acbd0d12e2fd79ac3b4f8ccddbcddb0fb69f76e`, zehn erreichbare Snapshots; frühester Snapshot vor dem PDF-Erstellungsdatum |
| Literatur-/Bildlücke | Als Blocker der Quellenzuordnung geführt | Die leere Literatur und fehlenden Bilder sind im historischen PDF selbst sichtbar und werden durch denselben fehlenden Eingabesatz reproduziert |
| QIC-20 | TEILBEARBEITET / QUELLENBLOCKIERT | ERLEDIGT als Quellen-/Versionszuordnung, mit expliziten historischen Rekonstruktionsgrenzen |
| Gesamtliste | 23 erledigt, 1 teilbearbeitet | 24 erledigt, 0 teilbearbeitet, 0 unbegonnen |

Der Originalauftrag lautet: **„PDFs ihren Quellen zuordnen. Insbesondere für TIG3_Vacuum_Structure.pdf die zugehörige Manuskriptquelle und Version ermitteln und dokumentieren.“** Die zusätzlich geforderte Wiedergewinnung sämtlicher ursprünglicher Eingabedateien war im Zwischenstand eine strengere Abschlussbedingung. Der neue Vergleich belegt die Quellenzuordnung auch für das bereits fehlerhafte vierseitige Alt-PDF. Diese strengere Bedingung wird nicht als erfüllt ausgegeben: Original-Bib/Bilder und die ursprüngliche Compilerkonfiguration sind weiterhin nicht zurückgewonnen. Ihre fehlende Wiedergewinnung wird als **historische Provenienzgrenze** dokumentiert, ohne den erledigten Zuordnungsauftrag mit einem neuen Restaurierungsauftrag gleichzusetzen.

## Historische Quelle und PDF

Quelle: [papers/archive/source_bindings/tig_2026-05-03/main.tex](../papers/archive/source_bindings/tig_2026-05-03/main.tex), bytegleich aus der Git-Historie übernommen. Ursprünglicher Pfad `submission/arxiv/main.tex`; frühester gefundener Snapshot [d15eea1](https://github.com/integrity-nexus-kai/Quantum_Integrity_Core/blob/d15eea1003efbc6632f847255221dee0231271e6/submission/arxiv/main.tex), 3. Mai 2026, 15:40:05 MESZ / 13:40:05 UTC. Zehn erreichbare Snapshots haben denselben Blob. Quellen-SHA-256 `9d6d183b159cec956058efbff0bb270760cab94af738c537a76ede6283e742b5`.

Historisches PDF: [TIG_Paper.pdf](../papers/tig-paper/TIG_Paper.pdf), vier Seiten, Druckdatum 3. Mai 2026; Git-Blob `33cecf3454fdf2ab8ff93372f9f3d1c4f9e5ef69`; SHA-256 `40eb555066bd1609a7d6e32154a88c56356773aef704d08b72076f8e2d0a8a87`. PDF-Erstellung 3. Mai 2026, 13:41:26 UTC. Der zeitliche Zusammenhang ist unterstützende Evidenz; entscheidend ist der vollständige Inhalts-/Layoutvergleich. Originaler Generator laut PDF-Metadaten pdfTeX 1.40.27; lokaler Vergleich pdfTeX 1.40.25 / TeX Live 2023/Debian.

## Forensische Erzeugung — Fehler ausdrücklich erhalten

In einen isolierten Arbeitsordner wurde ausschließlich die unveränderte `main.tex` kopiert. Keine Literaturdatei und keine Bilder angelegt. Dann:

```text
pdflatex -interaction=nonstopmode -no-shell-escape -recorder -output-directory=build main.tex
cd build; bibtex main.aux
cd ..; pdflatex -interaction=nonstopmode -no-shell-escape -recorder -output-directory=build main.tex
pdflatex -interaction=nonstopmode -no-shell-escape -recorder -output-directory=build main.tex
```

Die vier Prozesse liefern Exitcodes **1, 2, 1, 1**. pdfLaTeX erzeugt im Nonstop-Modus trotz der Grafikfehler eine vierseitige PDF. BibTeX meldet die fehlende `references.bib` und erzeugt selbst ein leeres `thebibliography`; dieses erklärt die zweite leere References-Überschrift. Kein Bibliografieinhalt wurde erfunden oder manuell eingefügt. Die beiden fehlenden Grafiken werden durch Dateinamenkästen dargestellt. Sie stimmen mit den historischen Platzhaltern überein.

Der Lauf ist **keine fehlerfreie Kompilierung**. Er ist eine kontrollierte Nachbildung des sichtbar fehlerhaften historischen Ausgabezustands. Die ursprüngliche Overleaf-Fehlerhistorie ist damit nicht bewiesen; ein hinreichender Erzeugungsweg aus der belegten historischen Hauptquelle ist nachgewiesen. [LaTeX-Log](evidence/qic20_2026-10-03/main.log), [BibTeX-Log](evidence/qic20_2026-10-03/main.blg), [generierte leere BBL](evidence/qic20_2026-10-03/main.bbl), [Prozesscodes](evidence/qic20_2026-10-03/runs.json).

## Vergleich und Prüfung

| Merkmal | Ergebnis |
|---|---|
| Seiten | 4 von 4 stimmen in Inhalt und Aufteilung überein |
| Extrahierter Text | Seiten 1/2 exakt gleich; Seiten 3/4 nach alleiniger Aufzählungszeichen-Kodierungsnormalisierung gleich |
| Rohtext-Unterschiede | Genau drei Aufzählungszeichen: historisch U+2022, lokal U+0088 |
| Gleichungen | Alle 23 nummerierten Gleichungen im identischen seitenweisen Text enthalten |
| Abschnitte | Alle 13 nummerierten Hauptabschnitte und drei Unterabschnitte enthalten |
| Historische Defekte | Sieben ungelöste Zitatkeys, zwei passende Bilddateinamen-/Rahmenplatzhalter, zwei leere References-Überschriften |
| Bilder | Null eingebettete Rasterbilder in beiden PDFs |
| Visuelle Prüfung | Alle acht historischen/reproduzierten Seiten gerendert und gesichtet; kein neuer Layout- oder Inhaltsverlust gesehen |
| Rendering | Kleine Font-/Renderingunterschiede; maximal 0.1023 % abweichende Pixel bei MuPDF, Faktor 1,5 |
| PDF-Bytes | Verschieden; keine Byte- oder vollständige Pixelidentität behauptet |

Prüfbuild-SHA-256 `50e3de7f8936ca7f2abe1c37b5f7cfe1a0d19cccd0623305029ef9fd97a25c76`. Die einzige Textnormalisierung ist U+0088 → U+2022; keine Prosa, Mathematik, Referenz, Leerzeichen oder Zeile wurde entfernt. [Vollständiger maschinenlesbarer Nachweis](../registry/qic20_source_binding_closeout_2026-10-03.json).

Für eine erneute kontrollierte Prüfung, mit `pdflatex`, BibTeX und PyMuPDF installiert:

```bash
python tools/reproduce_historical_tig.py --output-dir /tmp/qic-may3-reproduction
```

Das Werkzeug kopiert die Quelle isoliert, erhält alle Prozess-Exitcodes und prüft vier Seiten gegen das Original. Werkzeug-Exitcode 0 bedeutet **Quelleninhaltsvergleich bestanden**, nicht fehlerfreier Compilerlauf. Ein zweiter unabhängiger Arbeitsordnerlauf wurde ausgeführt und liefert erneut vier übereinstimmende Seiten mit denselben Prozesscodes.

## Abschluss und verbleibende Grenzen

Auch TIG3 ist bereits durch den [Autorenimport und 14-Seiten-Vergleich](TIG3_SOURCE_COMPARISON_2026-10-03.md) gebunden: elf Paketdateien, 32 Gleichungen, 20 Literaturangaben und fünf RGB-identische Abbildungen. Damit sind beide historischen PDFs ihren jeweils belegten Quellenversionen zugeordnet; QIC-20 ist im ursprünglichen Reparaturumfang abgeschlossen.

Die Mai-PDFs bleiben unverändert. Ihre technischen Defekte und die historischen fachlichen Aussagen werden durch die Quellenzuordnung nicht validiert. Aktuelle reparierte Manuskripte und Exporte behalten ihre eigenen Quellen und erfolgreichen Builds. Wissenschaftliche Fragen QIC-RQ-01–06 bleiben OFFEN und auf Nutzerauftrag zurückgestellt; bestehende Audit-/OQ-Status unverändert. Keine neue Veröffentlichung, DOI, Einreichung oder SSC-Bearbeitung. Exakte historische Compilerzustände und vollständige ursprüngliche Eingabepakete bleiben als benannte Provenienzgrenzen bestehen.

**Reparaturliste: 24/24 ERLEDIGT. Nächster Schritt: Rücksprache mit Human Authority.** Selbstprüfung derselben Instanz; kein unabhängiger wissenschaftlicher Audit. Git-Ablage, vollständiges Datei-Readback und Schutz der historischen Objekte werden am tatsächlichen Ablagecommit geprüft.
