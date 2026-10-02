# QIC — Manuskriptzuordnung und Build-Ablauf

Version 1.2 · 2026-10-02 · TECHNISCHER ARBEITSSTAND / KEINE RELEASEFREIGABE

Aktueller Reparatureingang Welle 3: main @ `da326a4041054c01f2574d02312826870616670c`. Historischer Welle-2-Eingang: `88fef45371dbefe89ee35dce4e8accc5e8eb6baa`. Historischer Welle-1-Quellenfreeze: `8fb4989d43382ccf303c8c52b2c7af746fa35034`. Zugehörige Aufgaben: QIC-17, QIC-18 und QIC-22; Kernkorrekturen QIC-01–03; Quellen-/Echo-Korrekturen QIC-15/16/10/05/11/14/12/04.

## Eigenständige Manuskriptobjekte

| Paket | Quelle und Build | Tatsächliche Bindung |
|---|---|---|
| Papertext | `papers/tig-paper/main.tex` | Titel „Topological Integrity Gravity: A Structural Horizon Transition“, im Text Version 1.3 vom 2. Oktober 2026; repräsentativer Geometriesektor mit negativem Vakuum-f(R)-Test. |
| Einreichung | `submission/arxiv/main.tex` | Titel „A Structural Horizon Transition in a Representative TIG Geometry: A Test Against Quadratic f(R) Gravity“, überarbeiteter Draft vom 2. Oktober 2026; Normierung korrigiert, negativer Vakuumtest, bedingte Laufzeit hergeleitet, physische Echo-Vorhersage offen. |

Die Pakete unterscheiden sich inhaltlich und sind keine nachgewiesenen Exporte derselben Quelle. Beide behalten ihr eigenes main.tex als Quelle ihres Texts; gemeinsamer Nachfolger und fachliche Harmonisierung bleiben Gegenstand der folgenden Wellen. Das strukturelle Register steht in [OBJECT_OWNERSHIP.md](../OBJECT_OWNERSHIP.md).

Das Paper verwendet ein eingebettetes thebibliography mit **18 Einträgen**. Seine references.bib sowie abstract.tex und photon_sphere.tex sind nicht eingebunden; die ersten beiden wurden als Begleitobjekte nachgeführt. Das Einreichungspaket verwendet references.bib mit unsrt und zitiert **elf Schlüssel**. Ghosh/Sarkar, Bessa und Garay werden jetzt in beiden Texten an ihren begrenzten Aussagepositionen zitiert; QIC-12 ist erledigt. Die erforderliche arXiv-/DOI-/Linkausgabe im unsrt-Build bleibt QIC-13/Welle 4 offen.

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

Historischer Build Welle 1 nach den technischen Korrekturen: beide latexmk-Läufe erfolgreich, Paper zehn Seiten, Einreichung fünf Seiten, keine offenen Zitat- oder Querverweiswarnungen. Zwei nicht fatale hyperref-PDF-String-Warnungen im Einreichungspaket bleiben sichtbar. Alle 15 Seiten wurden gerendert und gesichtet; keine abgeschnittenen oder fehlenden Inhalte festgestellt. Der vorhandene `clearpage` vor der Literatur erzeugt eine große Freifläche auf der Schlussseite der Einreichung; Endlayoutprüfung folgt in Welle 4.

## Overleaf und Einreichungspaket

Für ein neues Overleaf-Projekt kann das Repository mit der passenden Hauptdatei und den relativen Abbildungspfaden genutzt werden. Der hier ausgeführte Test war lokal. Ein bestehendes Overleaf-Projekt, dessen Compilerstand oder Synchronisation wurde in diesem Lauf nicht geprüft; in den 43 gebundenen Textquellen ist kein verifizierter Projektpointer dokumentiert. Es wird kein Live-Overleaf-PASS behauptet.

Das arXiv-Paket wird innerhalb des Repositorybaums gebaut. Es ist wegen des relativen Bildpfads noch kein eigenständig verifiziertes Upload-ZIP. Vor einem finalen Paket werden Quelle, Bib-Datei, Abbildungen und Pfade in einem abgegrenzten Export zusammengeführt und erneut gebaut. Das ist Abschlussarbeit in Welle 4 unter QIC-21/22/23, ohne automatische Veröffentlichung.

Die eingecheckten älteren PDFs werden in Welle 1 nicht ersetzt oder als Resultat dieses Builds ausgegeben. Ihre Quellenbindung gehört zu QIC-20. Build-Metadaten und Quellenfingerprints stehen in [repair_tracking.json](../registry/repair_tracking.json).

## Historische Prüfung nach Welle 2

Beide fachlich korrigierten Manuskripte bauen mit dem bestehenden Skript erfolgreich. Paper: zehn Seiten; Einreichung: sechs Seiten. Alle 16 Seiten der letzten Fassung gerendert und gesichtet, keine abgeschnittenen oder fehlenden Inhalte gesehen. Die finalen LaTeX-Logs enthalten keine Warnungen, offenen Zitate/Querverweise oder Overfull-Boxen. Die bisherige mathematische Abschnittsüberschrift der Einreichung wurde im Zuge der Kernkorrektur ersetzt; die beiden früheren Bookmarkwarnungen treten dadurch nicht mehr auf.

Der vorhandene clearpage vor dem Einreichungs-Literaturverzeichnis und unsrt bleiben erhalten. Die bibliografische Linkausgabe und das Endlayout gehören weiter QIC-13/22 in Welle 4. Die alten eingecheckten PDFs werden durch diese lokale Prüfung nicht automatisch ersetzt. Live-Overleaf, eigenständiges Upload-ZIP und Veröffentlichung wurden nicht geprüft oder ausgeführt.

Mathematische Selbstprüfung mit SymPy (geprüft 1.14.0): `python tools/verify_wave2.py`. Dieser Lauf rekonstruiert die Krümmung aus der Metrik und prüft 27 Bedingungen. Ein PASS der Rechnung steht neben dem **negativen** Vakuumlösungsresultat; es ist keine wissenschaftliche Promotion. Quellen, Rechnungen und Build-Fingerprints: [Welle-2-Arbeitsnachweis](REPAIR_WAVE2_2026-10-02.md), [Kernrechnung](../papers/derivations/quadratic_fr_and_horizon_checks.md), [Nachweissicht](../registry/repair_tracking.json).

## Aktuelle Prüfung nach Welle 3

Beide Manuskripte mit tools/build_manuscripts.py in frischen Ausgabeordnern gebaut; danach je zwei explizite finale pdflatex-Pässe im jeweiligen Paket-Ausgabeordner. Erst danach vollständige PDFs und Logs gebunden und ihre SHA-256-Fingerprints erneut gelesen. Paper: **zwölf Seiten**, Einreichung: **sieben Seiten**; alle 19 finalen Seiten gerendert und visuell geprüft, keine abgeschnittenen oder fehlenden Inhalte festgestellt. Extrahierte Zitate aufgelöst, finale LaTeX-Logs ohne Warnungen, fehlende Referenzen oder Overfull-Boxen. Fingerprints in registry/repair_tracking.json unter wave3.builds.

Die bestehenden unsrt-Linkgrenzen und die Freifläche durch clearpage bleiben Abschlussarbeit in Welle 4. Dieser Arbeitsbuild ersetzt keine eingecheckten älteren PDFs, kein eigenständiges Upload-ZIP und keinen Live-Overleaf-Test. Kein Release erzeugt.

Mathematische Prüfung (SymPy 1.14.0, mpmath 1.3.0): python tools/verify_wave3.py. 18 exakte und fünf numerische Bedingungen mit 60 Dezimalstellen geprüft: Hayward-Identität, lokale Faltenentwicklung, Laufzeitvorfaktoren, Oberflächengravitation, Testskalaroperator sowie horizontlose, mitlaufende und feste äußere Grenzen. Physische Reflexion, gravitative Störungen und eine beobachtbare Echo-Wellenform werden dadurch nicht nachgewiesen. [Laufzeitableitung](../papers/derivations/echo_delay_with_boundaries.md) · [Arbeitsnachweis](REPAIR_WAVE3_2026-10-02.md).
