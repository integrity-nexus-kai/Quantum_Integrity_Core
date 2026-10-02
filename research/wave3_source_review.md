# QIC — Quellenprüfung Welle 3

Version 1.0 · 2026-10-02 · deutschsprachiger Repair-Nachweis / keine zweite Arbeitsliste.

Eingang main @ da326a4041054c01f2574d02312826870616670c; Tree 4308f46358899bd5fecba9fd65b73c744336a448. 251 Blobs inventarisiert, 231 Textdateien gegen Git-Blob-SHAs verifiziert; unveränderte materialisierte Quellen wiederverwendet, zwölf zentrale Dateien frisch über den Connector gelesen. Keine vollständige wissenschaftliche Prüfung aller Dateien oder aller 14 Repositories.

## Suchrahmen und Priorisierung — QIC-15/16

Die vorhandene Matrix trägt den Stichtag **2. Oktober 2026**. Ein früherer tatsächlicher Suchlauf mit Endzeit/reproduzierbarem Protokoll ist im Eingang nicht gebunden. Das jüngste Ersteinreichungsdatum, 25. September, beweist keinen früheren Berichtsstichtag.

Gewähltes Aktualitätsfenster: **1. September 2026 bis zum Abruf am 2. Oktober 2026**, ergänzt durch zeitlich unbeschränkte Originalquellensuche zu Beweispflichten. Kein rekonstruierter historischer Zeitraum; der verbleibende Teil des 2. Oktober ist nicht erfasst. Tagesdaten Europe/Berlin, arXiv-Zeitstempel ausdrücklich UTC.

Vor Textintegration gelten getrennte Kriterien: direkter Prüfwert oder Analogie; neuer Titel, neue Version, bekannter Titel neu geprüft oder ältere Hintergrundquelle; Originalquelle, Publikationsstatus, Voraussetzungen/Geltungsbereich. Direkte Beweispflicht schlägt Aktualität. Einzelbewertungen: [Literaturmatrix](tig_literature_matrix.md).

Abfragen über zwei Suchdienste, ergänzt durch direkte arXiv-/Verlagsprüfung:

- site:arxiv.org "black hole formation" "2026" "f(R)" sowie "black hole" "formation" "regular" "September 2026"; Frischefilter 30 Tage.
- "black hole formation" "f(R)"; f(R) gravitational collapse black hole formation numerical scalar 2015 2016; Hayward Formation evaporation regular black holes gr-qc 0506126.
- site:arxiv.org "horizon formation" "September 2026" und "f(R)" "collapse" "September 2026".
- site:arxiv.org "Topological Integrity Gravity" quantum mechanics mit Frischefilter; "Topological Integrity Gravity" "quantum mechanics" und "Schrodinger" ohne Frischefilter.
- reconstruction quantum theory continuous reversible dynamics Hardy Chiribella purification; site:arxiv.org "quantum reconstruction" "September 2026".

Enge Aktualitätsabfragen: leere oder überwiegend sachfremde Treffer. Das Fenster ist **nicht vollständig abgedeckt**; kein Anspruch „keine neue Literatur vorhanden“. Zweiter Suchdienst und Originalprüfung ergänzten die Treffer. Die Septembertitel sind bekannte Einträge mit v1 zuletzt angezeigt. Hayward/Cardoso waren bibliografisch vorhanden; Hardy/Chiribella sind ältere jetzt ergänzte Prüfmaßstäbe. Die Hayward-Identität ist eine neue Quellenzuordnung, keine neue Veröffentlichung.

Weiterer Treffer: [Nashed/Eid, 2601.02416v2](https://arxiv.org/abs/2601.02416v2), §§IV–V; Ersteinreichung 03.01.2026, v2 04.06.2026. Datensatz „In press Eur. Phys. J. C“; Verlagspublikation nicht verifiziert. v2 begrenzt die PBH-Schwelle auf qualitativen Trend und ein zu integrierendes ODE-System. Außerhalb des Fensters, kein TIG-Test; nicht als geprüfter quantitativer Beweis übernommen. Ein weiterer MDPI-Kollapsvergleich war wegen HTTP 429 nicht als Volltext verfügbar.

## Horizontbildung und Vorläufer — QIC-10

[Hayward, gr-qc/0506126v2](https://arxiv.org/html/gr-qc/0506126v2), PRL 96, 031103 (2006), [DOI](https://doi.org/10.1103/PhysRevLett.96.031103): Eq. (5) statische Metrik; Eqs. (10)–(19) fortgeschrittene Zeit, variable Masse, zusätzlicher Energiefluss, trapping horizons. Dynamischer Vergleich mit gewählten Quellen, kein TIG-Evolutionsnachweis oder allgemeiner Ereignishorizontsatz.

**Eigene Umrechnung:** \(m=M,\ \ell^2=r_c^3/(2M)\) ergibt exakt die TIG-Repräsentantin. Statische Metrik und doppelte Horizontwurzel sind bekannte Eigenschaften dieser Familie, stärker als Ähnlichkeit. Kein \(\mu\leftrightarrow r_c\)-Zusammenhang eingeführt.

Bei festem \(\ell\) würde \(r_c^3=2M(v)\ell^2\) mitlaufen; Variation bei festem \(r_c\) ist nicht dieselbe Evolution. Nullstellenwechsel ersetzt keine Anfangsdaten/Materiedynamik. Trapping-, Killing- und globale Ereignishorizonte sind nicht allgemein austauschbar. Beide Manuskripte ergänzen diese Herkunfts-/Aussagegrenze.

## Ghosh/Sarkar — QIC-05

Geprüft: [2609.24648v1](https://arxiv.org/html/2609.24648v1), §§II–III, Eqs. (2)–(3), Appendix A; Preprint.

Voraussetzungen: glatter stationärer Killing-Horizont, gültige Feldgleichung, \(T_{\xi\xi}=0\); im Ricci-Quadrat-Sektor konstante nichtverschwindende Kopplung \(b_R\), kompakter zusammenhängender räumlicher Querschnitt ohne Rand und im dargestellten Beweis Nicht-Extremalität. \(E_{\xi\xi}=-b_R D^2(\kappa^2)=0\). \(b_R\) ist **nicht** TIGs \(\beta\).

Reines \(f(R)\): Ausnahme \(b_R=0\), Division unzulässig; gemischte Projektion, geeignete Materiebedingungen (\(T_{\xi A}=0\), im dargestellten Argument über DEC), \(f_R\ne0\). Positives \(f_R\) ist stärker. Flussfreiheit als zu prüfende Voraussetzung, nicht aus Stationarität allein für beliebige Materie abgeleitet.

**Eigene Gegenprüfung:** \(\kappa_h=|3-2/x_h|/(4M)\). Winkelkonstanz hier schon durch Sphärizität; kritisch \(\kappa=0\), daher nicht nicht-extremal. Welle-2-Vakuumtest weiter negativ. Konstante \(\kappa\) erfüllt nicht dadurch gewählte Feldgleichungen. Kein TIG-Existenz-/Entstehungsbeweis.

## Bessa/Garay — QIC-14/12

[Bessa, 2609.29046v1](https://arxiv.org/html/2609.29046v1), Eq. (1), §§III.1, III.4: \(R+\alpha R^2+\beta W^2\), flacher FLRW-Hintergrund, lineare skalare Staubstörungen, longitudinale Eichung, Unterhorizont-/Quasistatiknäherung. Formale IR-Fortsetzung kein kontrollierter Superhorizontbeweis; reduzierte Polfreiheit kein voller TIG-Stabilitätsnachweis.

Ersteinreichung/v1: **24.09.2026, 05:24:34 UTC**, [Datensatz](https://arxiv.org/abs/2609.29046v1). „Submitted to PRD“: Autorenangabe ohne verifiziertes Journal-Eingangsdatum. Keine Annahme/Publikation oder spätere Version ausgewiesen. Manuskriptkopf kein Journalzeitstempel; separates öffentliches Ankündigungsdatum unbestimmt.

[Garay et al., 2609.31123v1](https://arxiv.org/html/2609.31123v1): Two-vertex model, Global variables, Generalized Friedmann equation; diskrete LQG-Ausgangsstruktur und definierter Hamiltonian. Indirekter Vergleich, keine TIG-, Kubik- oder gewöhnliche QM-Ableitung. Alle drei Arbeiten werden jetzt an begrenzten Aussagepositionen in beiden Texten zitiert.

## QM-Rückgewinnung — QIC-11

[Chiribella/D'Ariano/Perinotti, 1011.6451v3](https://arxiv.org/html/1011.6451v3), §§II–III, XIII.5/Theorem 20, PRA 84, 012311 (2011), [Verlag](https://doi.org/10.1103/PhysRevA.84.012311): endlichdimensionale operational-probabilistische Theorie, fünf Informationsaxiome plus Purifikation. Zusätzliche Verpflichtungen, keine Synonyme von Integrität.

[Hardy, quant-ph/0101012v4](https://arxiv.org/abs/quant-ph/0101012v4), §2/fünf Axiome, v4 25.09.2001, hier Preprint: kontinuierliche reversible Verbindungen reiner Zustände als entscheidender Zusatz im gesamten Axiomensystem.

**Befund:** Keine TIG-spezifische QM-Rückgewinnung im geprüften Repo/Quellenset; kein Unmöglichkeits- oder weltweiter Nichtexistenzbeweis. Bestehender Non-Claim in topology/theory/structure/non_claims_and_scope_limits.md bleibt.

**Eigene Nachweisanforderungen:** Zustände, Effekte, Wahrscheinlichkeiten, Zusammensetzung/Transformationen unabhängig definieren; Rekonstruktionsvoraussetzungen herleiten; komplexen Zustandsraum/Born-Regel erklären; Dynamik und gewünschten nichtrelativistischen Grenzfall liefern. Quantisiertes LQG-Modell/Bounce schließt diese Lücke nicht. Prüfmaßstab, keine importierte TIG-Grundlage.

## Nachweisqualität

Volltexte materialisiert, benannte aussagentragende Abschnitte gelesen, bei Ghosh/Sarkar auch Appendix A. Kein unabhängiges Re-Audit fremder Theoreme. arXiv-Historie/Journalnachweis haben bei Daten Vorrang vor abweichendem HTML-Manuskriptkopf.

HTML-Abrufidentitäten/SHA-256: registry/repair_tracking.json, wave3.external_source_snapshots; kein Autoren-Quellcodehash. Keine fremden Volltexte im Repo. [Echo-Rechnung](../papers/derivations/echo_delay_with_boundaries.md) und [Ausführung](../docs/REPAIR_WAVE3_2026-10-02.md) binden den Stand. Auditverdikte/O1–O7 bleiben erhalten.
