# QIC — Manuskriptzuordnung und Build-Ablauf

Version 1.5 · 2026-10-03 · TECHNISCHER ARBEITSSTAND / KEINE RELEASEFREIGABE

Aktueller Reparatureingang Welle 4: main @ `9f6cdf096716c6d070685b0d88555f403f6db8fa`. Historischer Welle-3-Eingang: `da326a4041054c01f2574d02312826870616670c`. Historischer Welle-2-Eingang: `88fef45371dbefe89ee35dce4e8accc5e8eb6baa`. Historischer Welle-1-Quellenfreeze: `8fb4989d43382ccf303c8c52b2c7af746fa35034`. Zugehörige Aufgaben: QIC-17, QIC-18 und QIC-22; Kernkorrekturen QIC-01–03; Quellen-/Echo-Korrekturen QIC-15/16/10/05/11/14/12/04.

## Eigenständige Manuskriptobjekte

| Paket | Quelle und Build | Tatsächliche Bindung |
|---|---|---|
| Papertext | `papers/tig-paper/main.tex` | Titel „Topological Integrity Gravity: A Structural Horizon Transition“, im Text Version 1.4 vom 2. Oktober 2026; repräsentativer Geometriesektor mit negativem Vakuum-f(R)-Test. |
| Einreichung | `submission/arxiv/main.tex` | Titel „A Structural Horizon Transition in a Representative TIG Geometry: A Test Against Quadratic f(R) Gravity“, überarbeiteter Draft vom 2. Oktober 2026; Normierung korrigiert, negativer Vakuumtest, bedingte Laufzeit hergeleitet, physische Echo-Vorhersage offen. |

Die Pakete unterscheiden sich inhaltlich und sind keine nachgewiesenen Exporte derselben Quelle. Beide behalten ihr eigenes main.tex als Quelle ihres Texts. Ein gemeinsamer wissenschaftlicher Nachfolger ist durch diesen Reparaturlauf nicht begründet. Das strukturelle Register steht in [OBJECT_OWNERSHIP.md](../OBJECT_OWNERSHIP.md).

Das Paper verwendet ein eingebettetes thebibliography mit **18 Einträgen**. Seine references.bib sowie abstract.tex und photon_sphere.tex sind nicht eingebunden; die ersten beiden wurden als Begleitobjekte nachgeführt. Das Einreichungspaket verwendet references.bib mit dem gebundenen unsrtnat-Stil und natbib (numerisch) und zitiert **elf Schlüssel**. Ghosh/Sarkar, Bessa und Garay werden jetzt in beiden Texten an ihren begrenzten Aussagepositionen zitiert; QIC-12 ist erledigt. QIC-13 ist abgeschlossen: vorhandene geprüfte DOI, versionierte arXiv-Kennungen und Links erscheinen in den beiden finalen PDF-Bibliografien; PDF-Linkannotationen geprüft.

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

Bis Welle 3 war nur der Build innerhalb des Repositorybaums geprüft. Welle 4 bindet nun Quelle, Bib-Datei, Stil, aktuelle Abbildung und LICENSE in einem abgegrenzten Quell-ZIP und baut es isoliert. Der Export ist technisch geprüft; eine Einreichung oder Veröffentlichung wurde nicht ausgeführt. Einzelheiten im aktuellen Abschlussnachweis unten.

Die eingecheckten älteren PDFs werden in Welle 1 nicht ersetzt oder als Resultat dieses Builds ausgegeben. Ihre Quellenbindung gehört zu QIC-20. Build-Metadaten und Quellenfingerprints stehen in [repair_tracking.json](../registry/repair_tracking.json).

## Historische Prüfung nach Welle 2

Beide fachlich korrigierten Manuskripte bauen mit dem bestehenden Skript erfolgreich. Paper: zehn Seiten; Einreichung: sechs Seiten. Alle 16 Seiten der letzten Fassung gerendert und gesichtet, keine abgeschnittenen oder fehlenden Inhalte gesehen. Die finalen LaTeX-Logs enthalten keine Warnungen, offenen Zitate/Querverweise oder Overfull-Boxen. Die bisherige mathematische Abschnittsüberschrift der Einreichung wurde im Zuge der Kernkorrektur ersetzt; die beiden früheren Bookmarkwarnungen treten dadurch nicht mehr auf.

Der vorhandene clearpage vor dem Einreichungs-Literaturverzeichnis und unsrt bleiben erhalten. Die bibliografische Linkausgabe und das Endlayout gehören weiter QIC-13/22 in Welle 4. Die alten eingecheckten PDFs werden durch diese lokale Prüfung nicht automatisch ersetzt. Live-Overleaf, eigenständiges Upload-ZIP und Veröffentlichung wurden nicht geprüft oder ausgeführt.

Mathematische Selbstprüfung mit SymPy (geprüft 1.14.0): `python tools/verify_wave2.py`. Dieser Lauf rekonstruiert die Krümmung aus der Metrik und prüft 27 Bedingungen. Ein PASS der Rechnung steht neben dem **negativen** Vakuumlösungsresultat; es ist keine wissenschaftliche Promotion. Quellen, Rechnungen und Build-Fingerprints: [Welle-2-Arbeitsnachweis](REPAIR_WAVE2_2026-10-02.md), [Kernrechnung](../papers/derivations/quadratic_fr_and_horizon_checks.md), [Nachweissicht](../registry/repair_tracking.json).

## Historische Prüfung nach Welle 3

Beide Manuskripte mit tools/build_manuscripts.py in frischen Ausgabeordnern gebaut; danach je zwei explizite finale pdflatex-Pässe im jeweiligen Paket-Ausgabeordner. Erst danach vollständige PDFs und Logs gebunden und ihre SHA-256-Fingerprints erneut gelesen. Paper: **zwölf Seiten**, Einreichung: **sieben Seiten**; alle 19 finalen Seiten gerendert und visuell geprüft, keine abgeschnittenen oder fehlenden Inhalte festgestellt. Extrahierte Zitate aufgelöst, finale LaTeX-Logs ohne Warnungen, fehlende Referenzen oder Overfull-Boxen. Fingerprints in registry/repair_tracking.json unter wave3.builds.

Die bestehenden unsrt-Linkgrenzen und die Freifläche durch clearpage bleiben Abschlussarbeit in Welle 4. Dieser Arbeitsbuild ersetzt keine eingecheckten älteren PDFs, kein eigenständiges Upload-ZIP und keinen Live-Overleaf-Test. Kein Release erzeugt.

Mathematische Prüfung (SymPy 1.14.0, mpmath 1.3.0): python tools/verify_wave3.py. 18 exakte und fünf numerische Bedingungen mit 60 Dezimalstellen geprüft: Hayward-Identität, lokale Faltenentwicklung, Laufzeitvorfaktoren, Oberflächengravitation, Testskalaroperator sowie horizontlose, mitlaufende und feste äußere Grenzen. Physische Reflexion, gravitative Störungen und eine beobachtbare Echo-Wellenform werden dadurch nicht nachgewiesen. [Laufzeitableitung](../papers/derivations/echo_delay_with_boundaries.md) · [Arbeitsnachweis](REPAIR_WAVE3_2026-10-02.md).

## Aktueller Abschlussbuild Welle 4

Paper zwölf, Einreichung sechs Seiten. Beide Builds in frischen Ordnern erfolgreich; danach je zwei explizite finale pdflatex-Pässe, vollständige PDFs/Logs gebunden und Fingerprints erneut gelesen. Alle **18 finalen Seiten** gerendert und visuell geprüft; kein fehlender Inhalt, keine offenen Zitate/Referenzen, keine finalen LaTeX-Warnungen oder Overfull-Boxen. Die unabhängige Exportkompilierung liefert sechs pixelgleiche Einreichungsseiten. Die Freifläche durch clearpage ist beseitigt; eine kompakte, lesbare Literaturausgabe verhindert den isolierten letzten Eintrag.

Aktuelle PDFs: [Exportübersicht](../submission/exports/wave4_2026-10-02/README.md). Das Paper verwendet 18 eingebettete Einträge; beide Begleit-Bibdateien haben identische geprüfte Identifier-Ergänzungen. Originaltexte der Quellen werden damit nicht als neue TIG-Beweise übernommen. Die zuvor unbelegte Aussage über bereits vorliegende numerische Photonensphärenkurven ist auf die gegebene Gleichung und noch zu liefernde quantitative Vorhersage begrenzt.

Die einzige aktive Abbildung der Einreichung stammt aus tools/generate_horizon_figure.py; alle früheren Figuren sind separat gebunden und nicht Teil des aktuellen Builds. python tools/generate_horizon_figure.py erzeugt PNG und JSON aus der konkreten Kubik; NumPy/Matplotlib erforderlich. Nicht benötigte Altbilder werden beim Export ausgeschlossen.

Eigenständiges Quellpaket erzeugen und prüfen:

```bash
python tools/export_arxiv.py --output-dir /tmp/qic-export
```

Das Skript erzeugt ein deterministisches ZIP mit main.tex, references.bib, unsrtnat.bst, der einen Abbildung und dem unveränderten aktuellen LICENSE. ZIP wird in einen unabhängigen temporären Ordner entpackt und dort gebaut; keine Repository-Abbildungspfade im tatsächlich verwendeten INPUT-Set. Quellenbytes, ZIP-Integrität, finale Logs und PDF-Fingerprints geprüft. Kein Upload. Die komprimierte ZIP-Identität ist reproduzierbar; PDF-Zeitstempel/Compiler können bei Wiederholung andere PDF-Bytes ergeben.

Bestehendes Live-Overleaf-Projekt weiterhin nicht verifiziert; der lokale beziehungsweise isolierte Compiler-Test wird davon unterschieden. TeX Live 2023/Debian, latexmk 4.83; Drittanbieter-Stil mit eigenem Lizenzhinweis. [Veröffentlichungskette](PUBLICATION_CHAIN.md) und wave4 im [Nachweisregister](../registry/repair_tracking.json) enthalten Quellen-/Exportfingerprints und den verbleibenden QIC-20-Restpunkt.

## Fortschreibung — TIG3-Quellenbindung, 3. Oktober 2026

Die vorstehenden Wellen-/Historienbefunde behalten ihre geprüften Bezugsstände. Neu: [TIG3-Quellstand](../papers/tig3-vacuum/README.md) aus dem Autoren-ZIP vom 3. Oktober bytegleich importiert; erfolgreiche Builds mit 16 Seiten (Originaleinstellung) und 14 Seiten (kontrollierte 11pt-/Mai-Rekonstruktion). Auf allen 14 Vergleichsseiten gleicher Text nach alleiniger Aufzählungszeichen-Normalisierung, fünf RGB-identische Abbildungen, gleiche 32 nummerierte Gleichungen und 20 Literaturangaben. [Vollständiger Vergleich](TIG3_SOURCE_COMPARISON_2026-10-03.md), [Manifest](../registry/tig3_source_binding_2026-10-03.json).

TIG3-Teil von QIC-20 erledigt; Gesamtaufgabe bleibt teilbearbeitet wegen des vollständigen ursprünglichen Erzeugungspakets des vierseitigen `TIG_Paper.pdf`. Die exakten Mai-TIG3-Quellbytes und der damalige Compilerstand sind nicht zurückgewonnen; die Rekonstruktion ist entsprechend bezeichnet. Quellenimport ersetzt weder wissenschaftliche Owner noch reparierte Manuskripte, historische PDF-/DOI-Objekte oder Forschungsstatus.

## Aktueller Abschluss — QIC-20, 3. Oktober 2026

**QIC-20 ERLEDIGT; alle 24 Reparaturaufgaben erledigt.** [Abschlussnachweis](QIC20_SOURCE_BINDING_CLOSEOUT_2026-10-03.md), [Manifest](../registry/qic20_source_binding_closeout_2026-10-03.json). Die unveränderte historische Hauptquelle des vierseitigen Mai-Papers reproduziert alle vier Seiten einschließlich der sieben ungelösten Zitatkeys, zweier Bildplatzhalter und doppelter leerer References-Überschrift. Zwei unabhängige Arbeitsordnerläufe bestätigen den Vergleich; Compiler-Exitcodes bleiben 1/2/1/1. Die Quelle wird als Archivobjekt registriert; keine fehlenden Originaldateien erfunden. Quelle/PDF-Zuordnung ist erfüllt, exakter historischer Compiler-/Eingabestand bleibt qualifiziert. Die vorher dokumentierten Teilbearbeitungsstände sind historische Zwischenstände und werden durch diesen Abschluss abgelöst. Aktuelle reparierte Manuskripte/Exporte, historische PDF-/DOI-Objekte und Forschungsstatus bleiben unverändert.

Forensischer Vergleich: `python tools/reproduce_historical_tig.py --output-dir /tmp/qic-may3-reproduction` aus der Repo-Wurzel. Werkzeug-Exitcode 0 bedeutet Inhaltsvergleich bestanden; einzelne Compiler-/BibTeX-Fehler werden ausdrücklich erhalten. Archivquelle nicht in den aktiven Export aufnehmen.
