# TIG3 — Quellenbindung, Build und Versionsvergleich

**Version:** 1.0 · **Datum:** 3. Oktober 2026  
**Auftrag:** TIG3-Quell-ZIP prüfen, bauen, gegen die archivierte Mai-PDF vergleichen und QIC-20 fortschreiben.  
**Eingang:** QIC `main` @ `9080eb8c4f6240eb7ffb8b76679ce7d50f0c9bb5`  
**Ergebnis:** TIG3-Quellen inhaltlich und im rekonstruierten 14-Seiten-Layout bestätigt. QIC-20 bleibt wegen des vollständigen Erzeugungspakets des separaten vierseitigen Mai-Papers teilbearbeitet.

**Nachfolgender Abschluss:** Der folgende TIG3-Vergleich dokumentiert den Zwischenstand vor dem vierseitigen Neubuild. QIC-20 ist inzwischen insgesamt ERLEDIGT; [aktueller Abschlussnachweis](QIC20_SOURCE_BINDING_CLOSEOUT_2026-10-03.md). Die ursprünglichen TIG3-Ergebnisse und ihre Grenzen bleiben unverändert.

## Alter Stand, neuer Stand, Delta

| Gegenstand | Alter Stand | Neuer Stand / Delta |
|---|---|---|
| TIG3-Quelle | Kein passendes vollständiges Paket im erreichbaren QIC-Bestand | Autor-ZIP `TIG3_Vacuum_Structure.zip`; elf zusammengehörige Dateien aus `tig3-vacuum/paper/` bytegleich [importiert](../papers/tig3-vacuum/README.md) |
| Richtige Hauptdatei | Pfad-/Titelverwechslung möglich | `tig3-vacuum/paper/main.tex` ist TIG3; das andere `paper/main.tex` im ZIP ist das separate TIG2-Paper |
| Build | Nicht ausgeführt | Unveränderte 12pt-/`\today`-Quelle erfolgreich: 16 Seiten, Datum 3. Oktober 2026 |
| Mai-Vergleich | Nur PDF-Metadaten und Inhalt bekannt | Kontrollierte Kopie mit ausschließlich 11pt und festem 17.-Mai-Datum: 14 Seiten, seitenweise gleicher Text und gleiche Inhaltsanordnung |
| Abbildungen | Erzeugungsquellen nicht gebunden | Alle fünf PNGs stimmen mit den dekodierten RGB-Pixeln der fünf Mai-PDF-Abbildungen exakt überein |
| Rest | Zwei vollständige Quellenpakete ungeklärt | TIG3-Inhalts-/Layoutbindung erfüllt; vollständiges ursprüngliches Erzeugungspaket des vierseitigen `TIG_Paper.pdf` weiter unbestätigt |

Die Originalquelle bleibt bei **12pt und `\today`**. Die 11pt-/Mai-Fassung ist ein kontrollierter Rekonstruktionsversuch, kein historisch wiedergefundenes Quellobjekt. Die Übereinstimmung ist starke Evidenz für die Quellenzuordnung, beweist aber keinen ursprünglichen Overleaf-History-Snapshot. Der beobachtete Größenunterschied erklärt die 16 gegenüber 14 Seiten; PDF-Erstellungsdatum und Druckdatum sind getrennte Metadaten.

## Eingaben und Integrität

ZIP: 12,824,141 Bytes; SHA-256 `9940b429c3be9636799ea35789d8601e3ccc77ce304ed676f1b4a3fe69ba3166`. 183 Dateien geprüft: eindeutige Namen, keine absoluten/Parent-Pfade oder Symlinks; Mitglieder erfolgreich gelesen. Importumfang ausschließlich elf Dateien: `main.tex`, `references.bib`, drei eingebundene Abschnittsdateien, fünf PNGs und die zugehörige Figuren-README. [Manifest](../registry/tig3_source_binding_2026-10-03.json) enthält Bytes, SHA-256 und Git-Blob-ID jedes importierten Mitglieds.

Alle drei `\input`- und fünf `\includegraphics`-Abhängigkeiten vorhanden. Bibliographie: 22 Schlüssel, davon 20 zitiert; keine fehlenden Zitatkeys. Ausgabe: 20 Einträge. Alle 32 nummerierten Gleichungen und die vier Hauptabschnitte einschließlich Unterabschnitten stimmen im seitenweisen Vergleich überein. Dies ist eine technische Inhaltsprüfung, keine neue Prüfung der wissenschaftlichen Beweise.

## Build und Reproduktion

Umgebung: pdfTeX 1.40.25 / TeX Live 2023/Debian, latexmk 4.83, BibTeX. Historische PDF: pdfTeX 1.40.27 / TeX Live 2025. Fehlende tcrm-Schriften wurden lokal mit existierenden separaten temporären Verzeichnissen erzeugt; kein Eingriff in die Manuskriptquelle.

Aus dem importierten Paketverzeichnis, mit einem beschreibbaren temporären Verzeichnis:

```bash
mkdir -p /tmp/qic-tig3-fonts
TMPDIR=/tmp/qic-tig3-fonts latexmk -pdf -interaction=nonstopmode -halt-on-error -no-shell-escape -outdir=build main.tex
```

Für den kontrollierten Vergleich eine separate Kopie des vollständigen Pakets anlegen und dort ausschließlich `\documentclass[12pt]{article}` auf `\documentclass[11pt]{article}` sowie `\date{\today}` auf `\date{May 17, 2026}` ändern. Dann denselben Build ausführen. Der Import selbst wird dabei nicht geändert.

| Prüfung | Unveränderter Import | Kontrollierte Vergleichsfassung |
|---|---|---|
| Ergebnis | Erfolgreich, 16 Seiten | Erfolgreich, 14 Seiten |
| Zitate / Querverweise | Vollständig aufgelöst | Vollständig aufgelöst |
| Finales Log | Zwei Overfull-hbox-Hinweise: 5,42104pt und 3,63481pt | Keine Warnungen / Overfull-Boxen |
| Bilder | Fünf identische RGB-Inhalte | Fünf identische RGB-Inhalte an den historischen Seitenpositionen 2, 3, 4, 5, 8 |
| Visuelle Prüfung | Alle 16 Seiten gerendert und gesichtet | Alle 14 Seiten gerendert und gegen alle 14 historischen Seiten gesichtet |

Keine fehlenden oder abgeschnittenen Inhalte gesehen. Die beiden kleinen Zeilenüberstände der originalen 12pt-Fassung bleiben als Befund sichtbar; ihre Behebung ist für diesen unveränderten Quellenvergleich nicht erforderlich.

## Tatsächliche Unterschiede zum Mai-PDF

Die kontrollierte Fassung hat **auf 14 von 14 Seiten exakt denselben extrahierten Text**, nach alleiniger Ersetzung des aus der lokal eingebetteten Aufzählungsschrift extrahierten U+0088 durch U+2022 (`•`). Ohne diese Ersetzung gibt es genau 66 Unterschiede, jeweils ein Aufzählungszeichen. Prosa, Gleichungstext, Zitatnummern, Bildunterschriften und Literaturausgabe benötigen keine weitere Normalisierung.

Alle fünf Bildinhalte sind RGB-pixelidentisch. Bei den vollständigen Seitenrenderings (MuPDF, Faktor 1,2) ist Seite 1 pixelgleich; die anderen Seiten zeigen kleine Renderingunterschiede, maximal **0.2880 %** abweichende Pixel. Der historische Aufzählungsfont ist `SFRM1095`; der lokale Build verwendet einen erzeugten PK-Font. Deshalb wird keine vollständige Pixel- oder PDF-Byteidentität behauptet. Unterschiedliche Compiler, Font-Einbettung, Erstellungszeitstempel und PDF-Objektstruktur bleiben sichtbar. Die 11pt-Rekonstruktion bestätigt Inhalt und Seitenaufteilung, nicht den exakten historischen Compilerzustand.

| Objekt | SHA-256 |
|---|---|
| Historische TIG3-PDF | `b14b9f7013edbb1c18a09f077fb883c3c3555ea969600eabbeba699216c58132` |
| Unveränderter 12pt-Prüfbuild | `d60befd224bf9ae42600c84bd9219593c1da195af28f7ad9effd61f047304e46` |
| Kontrollierter 11pt-/Mai-Prüfbuild | `4755e68129b7cebc20fbad3e2fa9963adcfb9808d9dc251122a4f89da477ff40` |

Prüf-PDFs sind lokale Diagnoseartefakte; der Repo-Nachweis besteht aus diesem Markdown-Bericht, dem Quellenimport und dem JSON-Manifest. Die vorhandenen historischen PDFs sowie die Welle-4-Exporte bleiben bytegleich.

## Erledigt und verbleibender Rest

**Erledigt:** TIG3-Paket identifiziert, vollständige Eingaben importiert, erfolgreich gebaut, Text/Gleichungen/Literatur/Abbildungen und alle Seiten geprüft; Versionsdelta explizit dokumentiert. Der TIG3-Teil von QIC-20 ist in diesem technischen Umfang abgeschlossen.

**QIC-20 insgesamt bleibt TEILBEARBEITET / QUELLENBLOCKIERT:** Für das separate vierseitige `TIG_Paper.pdf` vom 3. Mai existiert bereits der passende historische Hauptquellkandidat `5acbd0d12e2fd79ac3b4f8ccddbcddb0fb69f76e`; das vollständige ursprüngliche Erzeugungspaket und der genaue Eingabestand sind weiterhin unbestätigt. [Vorheriger Quellenbefund](REPAIR_CLOSEOUT_2026-10-02.md). Für TIG3 bleibt lediglich die engere historische Grenze: originale Mai-Quellbytes und ursprüngliche Compilerkonfiguration sind nicht zurückgewonnen; die Rekonstruktion ist ausdrücklich so bezeichnet.

Gesamtstand: 23 erledigt, QIC-20 teilbearbeitet, 0 unbegonnen. QIC-RQ-01–06 bleiben OFFEN und auf Nutzerauftrag zurückgestellt. Kein Release, DOI, Einreichung, SSC-Start oder wissenschaftlicher Statuswechsel. Same-run-Selbstprüfung; keine unabhängige Auditfreigabe.
