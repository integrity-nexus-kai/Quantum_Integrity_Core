# QIC — Manuskriptzuordnung und Build-Ablauf

Version 1.0 · 2026-10-02 · TECHNISCHER ARBEITSSTAND / KEINE RELEASEFREIGABE

Quellenfreeze: main @ `8fb4989d43382ccf303c8c52b2c7af746fa35034`. Zugehörige Aufgaben: QIC-17, QIC-18 und QIC-22.

## Eigenständige Manuskriptobjekte

| Paket | Quelle und Build | Tatsächliche Bindung |
|---|---|---|
| Papertext | `papers/tig-paper/main.tex` | Titel „Topological Integrity Gravity: A Structural Horizon Transition“, im Text Version 1.1; repräsentativer Geometriesektor. |
| Einreichung | `submission/arxiv/main.tex` | Titel „Critical Horizon Transitions in Quadratic f(R) Gravity“, im Text Mai 2026; eigene Wirkung, Normierung und Echo-Claims. |

Die Pakete unterscheiden sich inhaltlich und sind keine nachgewiesenen Exporte derselben Quelle. Beide behalten ihr eigenes main.tex als Quelle ihres Texts; gemeinsamer Nachfolger und fachliche Harmonisierung bleiben Gegenstand der folgenden Wellen. Das strukturelle Register steht in [OBJECT_OWNERSHIP.md](../OBJECT_OWNERSHIP.md).

Das Paper verwendet ein eingebettetes `thebibliography` mit zehn Einträgen. Seine `references.bib` sowie `abstract.tex` und `photon_sphere.tex` sind im geprüften main.tex nicht eingebunden. Änderungen dort ändern dieses PDF derzeit nicht. Das Einreichungspaket verwendet `references.bib` mit `unsrt`; es zitiert im Ausgangstext vier Schlüssel. Die drei neuen Literaturquellen sind in beiden Bib-Dateien vorhanden, werden im Ausgangstext aber nicht zitiert: QIC-12 und QIC-13 bleiben offen.

## Reproduzierbarer lokaler Build

Voraussetzungen: Python 3, latexmk, pdflatex, BibTeX und die verwendeten TeX-Pakete einschließlich Latin Modern. Im ausgeführten Lauf: TeX Live 2023/Debian, latexmk 4.83.

Aus der Repositorywurzel:

```bash
python tools/build_manuscripts.py all
```

Einzelpaket und abweichender Ausgabeordner:

```bash
python tools/build_manuscripts.py paper --output-dir /tmp/qic-build
python tools/build_manuscripts.py arxiv --output-dir /tmp/qic-build
```

Standardausgabe: `.build/paper/` und `.build/arxiv/`, jeweils `main.pdf`, TeX-Hilfsdateien und `latexmk.stdout.log`. Das Skript beendet sich bei einem fehlgeschlagenen Paket mit einem Fehlercode. Bei einem Quellenwechsel vorher einen neuen Ausgabeordner wählen oder nur die betreffenden Build-Hilfsdateien bereinigen. Keine GitHub Actions werden angelegt.

## Ausgangsfehler und Korrekturen

1. Paper: pdfTeX brach in dieser Laufzeit bei Font-Erweiterung mit nicht skalierbaren Fonts ab. `lmodern` nach T1-Encoding behebt den Fehler; Text, Gleichungen und Literatur sind unverändert.
2. Einreichung: `tig_horizon_radius_prediction.png` fehlte im Paketverzeichnis. `graphicspath` bindet die vorhandene Quelle `figures/tig_horizon_radius_prediction.png`; Git-Blob `f343f7dfc7b54e404fb415ef70bf12d6fa516d15` wurde vor dem Build verifiziert. Es wird kein Ersatzbild erzeugt.

Nach den Korrekturen: beide latexmk-Läufe erfolgreich, Paper zehn Seiten, Einreichung fünf Seiten, keine offenen Zitat- oder Querverweiswarnungen. Zwei nicht fatale hyperref-PDF-String-Warnungen im Einreichungspaket bleiben sichtbar. Alle 15 Seiten wurden gerendert und gesichtet; keine abgeschnittenen oder fehlenden Inhalte festgestellt. Der vorhandene `clearpage` vor der Literatur erzeugt eine große Freifläche auf der Schlussseite der Einreichung; Endlayoutprüfung folgt in Welle 4.

## Overleaf und Einreichungspaket

Für ein neues Overleaf-Projekt kann das Repository mit der passenden Hauptdatei und den relativen Abbildungspfaden genutzt werden. Der hier ausgeführte Test war lokal. Ein bestehendes Overleaf-Projekt, dessen Compilerstand oder Synchronisation wurde in diesem Lauf nicht geprüft; in den 43 gebundenen Textquellen ist kein verifizierter Projektpointer dokumentiert. Es wird kein Live-Overleaf-PASS behauptet.

Das arXiv-Paket wird innerhalb des Repositorybaums gebaut. Es ist wegen des relativen Bildpfads noch kein eigenständig verifiziertes Upload-ZIP. Vor einem finalen Paket werden Quelle, Bib-Datei, Abbildungen und Pfade in einem abgegrenzten Export zusammengeführt und erneut gebaut. Das ist Abschlussarbeit in Welle 4 unter QIC-21/22/23, ohne automatische Veröffentlichung.

Die eingecheckten älteren PDFs werden in Welle 1 nicht ersetzt oder als Resultat dieses Builds ausgegeben. Ihre Quellenbindung gehört zu QIC-20. Build-Metadaten und Quellenfingerprints stehen in [repair_tracking.json](../registry/repair_tracking.json).
