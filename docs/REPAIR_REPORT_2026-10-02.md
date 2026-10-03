# QIC — Reparaturbericht: alter Stand, neuer Stand und Delta

**Version:** 1.2 · **Datum:** 3. Oktober 2026  
**Repository:** integrity-nexus-kai/Quantum_Integrity_Core · **Branch:** main  
**Umfang:** die 24 beauftragten QIC-Reparaturen, Wellen 1–4  
**Ergebnis:** **23 erledigt, 1 teilbearbeitet, 0 unbegonnen**  
**Human Authority:** Kai Stefan Dietrich

Dieser Markdown-Bericht dokumentiert die ausgeführte Reparatur und ihren Restumfang. Die einzige aktive Arbeitsliste bleibt [REPAIR_TODO.md v1.7](../REPAIR_TODO.md); dieser Bericht ist keine zusätzliche Aufgabenliste. **Abschluss-Ergänzung:** Die sechs fachlichen Punkte sind jetzt als [offene Forschungsfragen QIC-RQ-01–06](../field_equations/open_questions.md#offene-forschungsfragen-aus-der-reparatur--2-oktober-2026) dokumentiert und auf Nutzerauftrag für später zurückgestellt. Die zusätzliche gesamte erreichbare Historienprüfung hat einen inhaltlich passenden Hauptquellkandidaten für das vierseitige Mai-Paper gefunden. TIG3 ist inzwischen durch einen erfolgreichen Quellenimport/Build/Vergleich gebunden; das vollständige ursprüngliche Erzeugungspaket des vierseitigen Papers bleibt unbestätigt. QIC-20 bleibt deshalb teilbearbeitet. [Abschlussnachweis](REPAIR_CLOSEOUT_2026-10-02.md). Die folgenden Welle-4-Vergleichssnapshots bleiben ihre historischen Bezugsstände.

Die PDFs sind erzeugte Manuskriptfassungen und Prüfarbeitsartefakte. Der Reparaturbericht selbst liegt hier als bearbeitbare Repo-Datei vor.

## 1. Alter und neuer Stand

| Vergleich | Alter Stand | Neuer Stand |
|---|---|---|
| Bezugsstand | [main vor der Reparatur: b247bde](https://github.com/integrity-nexus-kai/Quantum_Integrity_Core/tree/b247bdefdf5d50b28dbad60b31f9f2e0f15a8975) | [main nach Welle 4: 4b7dec0](https://github.com/integrity-nexus-kai/Quantum_Integrity_Core/tree/4b7dec0e2118c165732c6960e7a8635d2a818ef5) |
| Arbeitsliste | [v1.0: 24 Aufgaben OFFEN](https://github.com/integrity-nexus-kai/Quantum_Integrity_Core/blob/b247bdefdf5d50b28dbad60b31f9f2e0f15a8975/REPAIR_TODO.md), nach Dringlichkeit aufgereiht | [v1.5: 23 ERLEDIGT, QIC-20 TEILBEARBEITET](https://github.com/integrity-nexus-kai/Quantum_Integrity_Core/blob/4b7dec0e2118c165732c6960e7a8635d2a818ef5/REPAIR_TODO.md), vier Wellen mit Abhängigkeiten |
| Quellen und Pakete | Zwei unterschiedliche Manuskriptpakete; ihre Rollen und Quellenbindungen waren ein Prüfauftrag | Beide Pakete gesondert zugeordnet; Quellenkarte, Objektzuständigkeiten und gemeinsamer Reparaturnachweis vorhanden |
| Kernbehauptungen | Inkonsistente α-/μ-Schreibweise, stärkerer quadratischer f(R)-Lösungsanspruch, allgemeine kubische Fold-Behauptung und unbegründete Echo-Skalierung | Normierung korrigiert, konkreter Vakuumanspruch analytisch widerlegt, Kubik modellgebunden hergeleitet, Echo-Laufzeit mit ausdrücklichen Grenzen und Reflexionsannahmen |
| Literatur | Neue Quellen vorhanden, aber noch nicht an begrenzte Aussagen im Haupttext gebunden; Voraussetzungen und Ausgabe zu prüfen | Primärquellen und Versionen geprüft, Aussagen begrenzt, Zitate integriert, DOI-/arXiv-Angaben und Klickziele in den Endausgaben kontrolliert |
| Erzeugung und Dateien | Zwei technische Ausgangsbuildfehler, auffällige Pfade und ungeklärte Abbildungsrollen | Beide Manuskripte bauen ohne finale Warnungen; zehn Pfade kontrolliert umbenannt; aktuelle Grafik reproduzierbar erzeugt; Quell-ZIP isoliert gebaut |
| Historische PDFs und DOI | Quellen-/Versionszuordnung und Veröffentlichungskette ungeklärt | PDF-Identitäten und historische DOI-/Tag-/Archivkette belegt; passende Original-LaTeX-Pakete der Mai-PDFs fehlen weiterhin |

Der alte Aufgabenstatus allein beweist noch keinen fachlichen Defekt. Die Einzelbefunde wurden während der Reparatur gegen die Quellen geprüft. Die Gegenüberstellung bezieht sich auf QIC; sie ist kein vollständiger wissenschaftlicher Audit der 14 Repositories.

## 2. Verlauf der vier Wellen

Die Zahlen zählen den jeweiligen Gesamtstand aller 24 Aufgaben. In Welle 1 begonnene Nachweis- und Buildaufgaben wurden bis Welle 4 weitergeführt.

| Stand | Erledigt | Teilbearbeitet | Offen / unbegonnen | Ausgeführtes Delta |
|---|---:|---:|---:|---|
| Ausgangsliste v1.0 | 0 | 0 | 24 | Aufgaben abgelegt; noch keine Reparatur |
| Nach Welle 1 / v1.2 | 2 | 5 | 17 | Paket-/Quellenzuordnung, Ausgangsregister, technische Buildreparaturen |
| Nach Welle 2 / v1.3 | 5 | 5 | 14 | QIC-01–03: Normierung, negatives Vakuumergebnis, konkrete Horizontkubik |
| Nach Welle 3 / v1.4 | 13 | 5 | 6 | Acht Literatur-/Echo-Aufträge abgeschlossen; Forschungsgrenzen ausgewiesen |
| Nach Welle 4 / v1.5 | 23 | 1 | 0 | Fünf Welle-4-Aufträge und fünf fortlaufende Aufgaben abgeschlossen; QIC-20 teilweise geklärt |

Nachweise: [Welle 1](REPAIR_WAVE1_2026-10-02.md), [Welle 2](REPAIR_WAVE2_2026-10-02.md), [Welle 3](REPAIR_WAVE3_2026-10-02.md), [Welle 4](REPAIR_WAVE4_2026-10-02.md). Historische Zwischenstände dieser Nachweise bleiben zeitgebunden; der Endstand steht in diesem Bericht und der aktuellen Arbeitsliste.

## 3. Delta für alle 24 Aufgaben

Alle Aufgaben standen in der Ausgangsliste auf OFFEN. „Erledigt“ bedeutet Abschluss des jeweils beauftragten Reparaturumfangs. Eine dokumentierte wissenschaftliche Lücke kann das korrekte Ergebnis einer abgeschlossenen Quellenprüfung sein.

| Welle | ID / Gegenstand | Verifizierter alter Befund oder Prüfbedarf | Ausgeführte Änderung / neuer Stand | Ergebnis |
|---|---|---|---|---|
| 1 | QIC-17 · Manuskriptpakete | Verhältnis von papers/tig-paper/ und submission/arxiv/ ungeklärt | Zwei eigenständige Pakete mit ihren Literatur-/Bildbindungen dokumentiert; keine automatische Quellgleichheit angenommen | ERLEDIGT |
| 1 | QIC-18 · Theorieablagen | Quellenkarte und tatsächliche Verzeichnisse abzugleichen | Tatsächliche Ablagen und bestehende Objektzuständigkeiten in REPOSITORY_MAP und OBJECT_OWNERSHIP gebunden | ERLEDIGT |
| 1→4 | QIC-22 · Buildablauf | Font-Erweiterung und Bildpfad verhinderten Ausgangsbuilds; Endexport ungeprüft | Technische Fehler korrigiert, Build-/Exportwerkzeuge dokumentiert; beide Endbuilds und eigenständiges Quell-ZIP erfolgreich geprüft | ERLEDIGT |
| 1→4 | QIC-08 · Reparaturübersicht | Auditbefunde und Reparatur-/Prüfstände verteilt | Bestehende Befunde mit Quellen, Wellen, Reprüfungen und Restpunkt in einer gemeinsamen Nachweissicht verbunden | ERLEDIGT |
| 1→4 | QIC-06 · Aussagen und Nachweise | Gemeinsame Erschließung von Annahmen, Beweispflichten und Nachweisen erforderlich | Zwölf zentrale Aussagegruppen mit Quellen, Abhängigkeiten, Gegenprüfungen und Endartefakten erschlossen | ERLEDIGT |
| 1→4 | QIC-07 · Quellenbindung | Quellversionen, relevante Stellen und Unterstützungsart zu präzisieren | Versionen/Passagen gebunden; direkte Unterstützung, Analogie und offene TIG-Übertragung unterschieden | ERLEDIGT |
| 1→4 | QIC-09 · Offene Fragen | Forschungsfragen, negative Ergebnisse und Gegenmodelle zusammenzuführen | Bestehende OQs und Gegenprüfungen erschlossen und fortgeschrieben; ursprüngliche Forschungsstatus erhalten | ERLEDIGT |
| 2 | QIC-01 · α-/μ-Normierung | α stand innerhalb des Einstein-Vorfaktors, gleichzeitig wurde μ=16πα verwendet | Bestehende μ-Konvention konsistent gemacht: αR² außerhalb des Vorfaktors; alternative Konvention ausdrücklich unterschieden | ERLEDIGT |
| 2 | QIC-02 · f(R)-Vakuumanspruch | Einreichung behauptete eine demonstrierte quadratische f(R)-Horizontlösung ohne Einsetzung | Metrik und notwendige Vakuumspur geprüft: für M>0, r_c>0 und konstante endliche Parameter verletzt; beide Texte auf das belegte Ergebnis begrenzt | ERLEDIGT |
| 2 | QIC-03 · Kubik und Fold | Allgemeine kubische Notwendigkeit und β³ allein aus Dimensionslosigkeit behauptet | Konkrete Kubik aus dem gewählten Massenprofil hergeleitet; allgemeiner Fold getrennt; kritischer Punkt, Wurzeln und β=0-Artefakt geprüft | ERLEDIGT |
| 3 | QIC-15 · Suchzeitraum | Vorheriger Stichtag und Suchfenster nicht ausreichend gebunden | Suchfenster und tatsächlicher Abrufstand dokumentiert; unbekannter früherer Stichtag ausdrücklich offengelegt | ERLEDIGT |
| 3 | QIC-16 · Literaturauswahl | Auswahlpriorität zu begründen | TIG-Relevanz, Neuigkeitswert und Belastbarkeit getrennt bewertet; Quellen mit ihrem konkreten Aussageumfang priorisiert | ERLEDIGT |
| 3 | QIC-10 · Horizontbildung | Bestehende Horizonte und dynamische Entstehung nicht ausreichend getrennt | Exakte Hayward-Herkunft der repräsentativen Metrik gebunden; statische Koaleszenz von dynamischer TIG-Entstehung getrennt | ERLEDIGT |
| 3 | QIC-05 · Horizontsatz | Tragende Ghosh-/Sarkar-Annahmen und TIG-Übertragbarkeit unvollständig | Stationarität, Feldgleichungen, Fluss-/Kopplungsbedingungen und Gültigkeitsgrenzen geprüft; kein Entstehungsbeweis daraus behauptet | ERLEDIGT |
| 3 | QIC-11 · QM-Rückgewinnung | Vorhandene Treffer belegten keine TIG-spezifische QM-Rekonstruktion | Direkte operationale Rekonstruktionsmaßstäbe ergänzt; fortbestehende TIG-Abdeckungslücke dokumentiert | ERLEDIGT |
| 3 | QIC-14 · Bessa-Daten | Preprint-Datum und Zeitschrifteneinreichung zu unterscheiden | arXiv-v1-Datum verifiziert; „Submitted to PRD“ als Autorenangabe behandelt; kein unbelegtes Journal-Eingangsdatum ergänzt | ERLEDIGT |
| 3 | QIC-12 · Quellenintegration | Drei neue Quellen vorhanden, aber im Haupttext noch nicht passend zitiert | Alle drei Quellen an ihre tatsächlich gestützten, begrenzten Aussagen in beiden Manuskripten gebunden | ERLEDIGT |
| 3 | QIC-04 · Echo-Laufzeit | −1/2-Exponent ohne vollständige Grenzen und Reflexionsvorschrift | Bedingte geometrische Hin-/Rücklaufzeit hergeleitet; Vorfaktoren und unterschiedliche Grenzfälle geprüft; unbelegte universelle Echo-Vorhersage entfernt | ERLEDIGT |
| 4 | QIC-19 · Navigation | Literaturmatrix über Einstiege nicht hinreichend auffindbar | Matrix in README, AGENTS und Quellenkarte verlinkt | ERLEDIGT |
| 4 | QIC-20 · Historische PDF-Quellen | Herkunft und Erzeugungsquellen der beiden Mai-PDFs ungeklärt | Titel, Daten, Uploadcommits, PDF-Bytes und historische Ablage belegt; TIG3-Import/Build/Vergleich bestätigt, vollständiges ursprüngliches vierseitiges Erzeugungspaket unbestätigt | TEILBEARBEITET |
| 4 | QIC-21 · Abbildungen | Gleichnamige/duplizierte Bilder und ihre Verwendung ungeklärt | Formate und elf echte PNGs geprüft; zwei Dublettengruppen gebunden; vermeintliche PNG als Text erkannt; neue aktive Horizontgrafik reproduzierbar erzeugt | ERLEDIGT |
| 4 | QIC-24 · Dateinamen | Tippfehler, Sonderzeichen, Leerzeichen und falsche Endungen | Zehn Pfade ohne Inhaltsänderung umbenannt; Referenzen repariert; alte Identitäten über die Migrationssicht erhalten | ERLEDIGT |
| 4 | QIC-13 · Literaturausgabe | unsrt-Ausgabe zeigte erforderliche Identifier/Links nicht ausreichend | unsrtnat/natbib und DOI-/URL-Ausgabe eingerichtet; Bibliografien und klickbare Ziele in beiden End-PDFs geprüft | ERLEDIGT |
| 4 | QIC-23 · Veröffentlichungskette | Quelle, PDF, Paket, historische Veröffentlichung und DOI zu verbinden | Aktuelle Quellen-/PDF-/ZIP-Fingerprints dokumentiert; historisches v1.0.0-Archiv vollständig gegen Tag geprüft; Versions- und Konzept-DOI getrennt gebunden | ERLEDIGT |

Einzelnachweise: [Nachweisregister](../registry/repair_tracking.json), [Kernrechnung](../papers/derivations/quadratic_fr_and_horizon_checks.md), [Literaturmatrix](../research/tig_literature_matrix.md), [Primärquellenprüfung](../research/wave3_source_review.md), [Echo-Ableitung](../papers/derivations/echo_delay_with_boundaries.md), [Artefakt-/Pfadzuordnung](ARTIFACT_BINDINGS.md), [Veröffentlichungskette](PUBLICATION_CHAIN.md).

## 4. Was bleibt aus dem Reparaturauftrag übrig?

**Ein Restpunkt: QIC-20 — vollständiges ursprüngliches Erzeugungspaket des vierseitigen Mai-Papers. TIG3-Teil erledigt; siehe Fortschreibung vom 3. Oktober.**

| Historisches Objekt | Bereits geklärt | Noch benötigt |
|---|---|---|
| [TIG3_Vacuum_Structure.pdf](../papers/tig-paper/TIG3_Vacuum_Structure.pdf) | 14 Seiten, Titel „Topological Integrity Gravity III: Conditional Vacuum Admissibility and Bounded Curvature Structure“, Druckdatum 17. Mai 2026; PDF-Identität, Upload und DOI-Archiv belegt | TIG3-Teil erledigt: elf Paketdateien importiert, Builds und 14-Seiten-Vergleich bestätigt; exakte historische Quellbytes nicht zurückgewonnen |
| [TIG_Paper.pdf](../papers/tig-paper/TIG_Paper.pdf) | Vier Seiten, Titel „Topological Integrity Gravity (TIG): A Quadratic f(R) Model with a Critical Horizon Transition“, Druckdatum 3. Mai 2026; PDF-Identität, Upload und DOI-Archiv belegt | Das genau dazugehörige ursprüngliche LaTeX-Paket einschließlich Literatur, Abbildungen und eingebundener Dateien |

Die in Welle 4 geprüften Kandidaten im aktuellen Repository, den Upload-/Tag-Ständen und dem veröffentlichten Archiv hatten abweichende Titel oder Inhalte. Die zusätzliche vollständige erreichbare Historienprüfung findet nun einen inhaltlich passenden Hauptquellkandidaten für das vierseitige Mai-Paper. Das vollständige Originalpaket und die genaue Erzeugungsbindung sind weiterhin nicht bestätigt; TIG3 ist durch den späteren Autorenimport und den Vergleich vom 3. Oktober gebunden. Suche, Vergleich, Rekonstruktion und Dokumentation übernimmt der Repair Agent nach Zugriff auf die erforderlichen Quellen. Ein benachbartes main.tex oder ein aktuelles Reparaturmanuskript schließt die verbleibende Quellenlücke nicht. [Erweiterter Quellenbefund](REPAIR_CLOSEOUT_2026-10-02.md).

Nach Eingang der Pakete kann der Repair Agent sämtliche Eingaben inventarisieren und mit Fingerprints sichern, den Build rekonstruieren, Titel/Text/Literatur/Abbildungen gegen das jeweilige Mai-PDF vergleichen und die bestätigte Quellen-/Versionsbindung dokumentieren. Erst danach kann QIC-20 auf ERLEDIGT gesetzt werden. Byteidentische PDF-Ausgabe ist bei anderen Compilerständen nicht automatisch zu erwarten; die tatsächliche Reproduktionsgrenze ist festzuhalten.

## 5. Was bleibt wissenschaftlich offen?

Diese Forschungsfragen sind vollständig als QIC-RQ-01–06 im [bestehenden Forschungsfragen-Dokument](../field_equations/open_questions.md#offene-forschungsfragen-aus-der-reparatur--2-oktober-2026) aufgenommen. Alle sind OFFEN; ihre Bearbeitung ist auf ausdrücklichen Nutzerauftrag für später ZURÜCKGESTELLT. Sie bestehen zusätzlich zum einzelnen technischen Restpunkt. Ihre Erschließung ist erledigt; ihre wissenschaftliche Lösung wurde durch die Reparatur nicht erreicht.

| Offener Gegenstand | Geprüfter Stand / verbleibende Arbeit |
|---|---|
| Dynamik, Materiequelle und kovariante Herleitung | Die geprüfte repräsentative Geometrie erfüllt den untersuchten konstanten quadratischen Vakuum-f(R)-Ansatz nicht. Eine eigenständige konsistente Dynamik beziehungsweise spezifizierte Materiequelle bleibt zu liefern. |
| Unabhängiger Integrity Tensor und bestehende Statusfragen | Effektive Realisierung, unabhängige Herleitung und historische Auditobjekte behalten ihre jeweiligen Scopes. Unterschiedliche Statusangaben werden durch den Paperrepair nicht vereinheitlicht oder als neue Validierung ausgegeben. |
| Dynamische Horizontentstehung | Die Metrik ist eine umparametrisierte Hayward-Familie; statische Wurzelkoaleszenz ist keine abgeleitete TIG-Entstehungsdynamik. |
| Physische Echos und Beobachtbarkeit | Geometrische Laufzeit ist unter gewählten Grenzen/Spiegelannahmen hergeleitet. Physische Reflexion, gravitative Störungsdynamik, Wellenform und Messbarkeit bleiben offen. |
| TIG-spezifische Rückgewinnung von QM | Direkte Rekonstruktionsmaßstäbe sind gebunden; eine entsprechende TIG-Herleitung fehlt im geprüften Quellenbestand. |
| Quantitative Photonensphäre, Schatten und weitere Vorhersagen | Orbitgleichung und Annahmen sind zu präzisieren und durch gebundene Rechnungen/Kurven zu belegen. Die alten, nicht rekonstruierbaren Grafiken dienen dafür nicht als aktueller Nachweis. |

Maßgebliche bestehende Forschungsobjekte: [field_equations/open_questions.md](../field_equations/open_questions.md), die Objektquellen in [OBJECT_OWNERSHIP.md](../OBJECT_OWNERSHIP.md) und die gebundenen Gegenprüfungen im [Nachweisregister](../registry/repair_tracking.json). Bestehende OQs wurden nicht geschlossen; historische Auditverdikte wurden nicht überschrieben.

## 6. Was wurde geprüft und abgelegt?

| Prüfung | Dokumentiertes Ergebnis |
|---|---|
| Welle 2 · Kernrechnung | 27 exakte symbolische Checks bestanden; negatives Ergebnis für den konkreten Vakuumanspruch |
| Welle 3 · Echo/Kernregression | 18 exakte und fünf numerische Prüfbedingungen bestanden; Welle-2-Kernprüfung erhalten |
| Welle 4 · Endbuild | Paper zwölf Seiten, Einreichungsfassung sechs Seiten; keine finalen Warnungen, offenen Zitate/Querverweise oder Overfull-Boxen |
| Visuelle Endkontrolle | Alle 18 finalen Seiten gesichtet; sechs zusätzliche Repository-Einreichungsrender pixelgleich zum isolierten Export |
| Isoliertes Quellpaket | Fünf erwartete ZIP-Mitglieder; frischer isolierter Build erfolgreich; keine externen Repository-Bildabhängigkeiten |
| Historische DOI-Bindung | Alle 156 Dateien des Zenodo-Archivs exakt mit den Git-Blobs des v1.0.0-Tags abgeglichen |
| Welle-4-Strukturprüfung | 273 Aufgaben-, Quellen-, Link-, Byte-, Pfad- und Exportprüfungen bestanden |
| Welle-4-Ablage | Commit 4b7dec0, Parent und vollständiger Tree geprüft; alle 35 geschriebenen Dateien frisch zurückgelesen und verglichen |

Die geprüften Endartefakte und ihre Fingerprints stehen im [Exportverzeichnis](../submission/exports/wave4_2026-10-02/README.md). Der Build-/Exportweg steht in [BUILD_WORKFLOW.md](BUILD_WORKFLOW.md). Die hier berichteten Prüfungen stammen aus den jeweiligen Reparaturwellen; für diesen zusätzlichen Markdown-Bericht werden Aufgabenabdeckung, Konsistenz, lokale Links und Ablage geprüft, ohne erneut Manuskripte zu erzeugen.

Der Endstand ist eine beauftragte Reparatur mit Selbstprüfung derselben Instanz. Eine unabhängige wissenschaftliche Prüfung oder Veröffentlichungsfreigabe folgt daraus nicht. Live-Overleaf wurde nicht verifiziert. Historische PDF-, Tag-, DOI- und Lizenzobjekte behalten ihre Identität; kein neues Release, kein neuer DOI und keine Einreichung wurden ausgeführt. SSC ist nicht Gegenstand dieses Berichts.

## 7. Abschluss-Ergänzung v1.1

Eingang main @ `b6adebbec1ccd504a48ba36b32af82b45541f6b6`. Sechs offene Forschungsfragen beim vorhandenen Dokumentationsort aufgenommen; Bearbeitung zurückgestellt. QIC-20 durch zusätzliche vollständige erreichbare Historienprüfung präzisiert. Alle 24 Reparaturaufträge sind bearbeitet; 23 erledigt, einer aufgrund unbestätigter Original-Erzeugungspakete weiterhin teilbearbeitet/quellenblockiert. Dieser Stand ist kein vollständiger Erledigt-Status. Alle derzeit ausführbaren Arbeiten abgeschlossen; anschließend Rücksprache. [Abschlussnachweis](REPAIR_CLOSEOUT_2026-10-02.md).

## Fortschreibung — TIG3-Quellenbindung, 3. Oktober 2026

Die vorstehenden Wellen-/Historienbefunde behalten ihre geprüften Bezugsstände. Neu: [TIG3-Quellstand](../papers/tig3-vacuum/README.md) aus dem Autoren-ZIP vom 3. Oktober bytegleich importiert; erfolgreiche Builds mit 16 Seiten (Originaleinstellung) und 14 Seiten (kontrollierte 11pt-/Mai-Rekonstruktion). Auf allen 14 Vergleichsseiten gleicher Text nach alleiniger Aufzählungszeichen-Normalisierung, fünf RGB-identische Abbildungen, gleiche 32 nummerierte Gleichungen und 20 Literaturangaben. [Vollständiger Vergleich](TIG3_SOURCE_COMPARISON_2026-10-03.md), [Manifest](../registry/tig3_source_binding_2026-10-03.json).

TIG3-Teil von QIC-20 erledigt; Gesamtaufgabe bleibt teilbearbeitet wegen des vollständigen ursprünglichen Erzeugungspakets des vierseitigen `TIG_Paper.pdf`. Die exakten Mai-TIG3-Quellbytes und der damalige Compilerstand sind nicht zurückgewonnen; die Rekonstruktion ist entsprechend bezeichnet. Quellenimport ersetzt weder wissenschaftliche Owner noch reparierte Manuskripte, historische PDF-/DOI-Objekte oder Forschungsstatus.
