# QIC — Arbeitsliste v1.5 für den Repository Repair Agent

**Dokument-ID:** QIC-REPAIR-TODO-2026-10-02  
**Version:** 1.5  
**Datum:** 2026-10-02  
**Objektklasse:** operative Aufgabenliste / REPAIR_TASK_LIST  
**Repository:** integrity-nexus-kai/Quantum_Integrity_Core  
**Branch:** main  
**Integrationsbasis / geprüfter Eingang:** 9f6cdf096716c6d070685b0d88555f403f6db8fa  
**Status:** AKTUELLE ARBEITSGRUNDLAGE / VIER WELLEN / WELLEN 1 BIS 4 AUSGEFÜHRT / 23 Aufgaben erledigt, 1 teilbearbeitet, 0 unbegonnen
**Human Authority:** Kai Stefan Dietrich

## Verbindlicher Einstieg

Diese Fassung ist die aktuelle Arbeitsgrundlage für den beauftragten QIC-Reparaturlauf. Sie ersetzt v1.4 am selben Pfad; die [historische Fassung](https://github.com/integrity-nexus-kai/Quantum_Integrity_Core/blob/9f6cdf096716c6d070685b0d88555f403f6db8fa/REPAIR_TODO.md) bleibt über die Versionshistorie erhalten. Es gibt keine zweite aktive QIC-Reparaturliste.

**Wellen 1 bis 4 sind ausgeführt. Restpunkt: QIC-20 — die passenden Original-LaTeX-Pakete der beiden Mai-PDFs fehlen.** Die nachstehende Ausführungsfolge und ihre Abhängigkeiten gelten weiter; die Nachweissichten aus Welle 1 werden laufend fortgeschrieben. Aufgaben-IDs und Herkunft bleiben unverändert; die ID-Nummer bezeichnet nicht die Ausführungsposition. Die ursprüngliche Dringlichkeitsklasse bleibt sichtbar. Vorbereitende Quellen-/Scope-Arbeit ermöglicht die weiterhin kritischen Kernprüfungen.

Vor jeder Reparatur [AGENTS.md](AGENTS.md), [README.md](README.md), diese Liste, Branch/HEAD und die betroffenen Quellen frisch prüfen. Übernommene Auditbefunde zuerst gegen die tatsächlichen Quellen verifizieren. Ein Dateiname oder eine fehlende Ordnerkategorie allein beweist keinen Defekt. Bereits erfüllte Funktionen und dokumentierte Reparaturen berücksichtigen; bestehende Register verwenden.

**QIC-23 gilt ab Arbeitsbeginn vor jeder Veröffentlichung**, unabhängig von der Position seines Abschlusses. Listenpflege, Reparatur, wissenschaftlicher Nachweis und Veröffentlichungsfreigabe sind getrennte Zustände.

## Vier Arbeitswellen

| Welle | Arbeitsblock | Aufgabenfolge | Stand |
|---|---|---|---|
| 1 | Arbeitsgrundlage und Nachweise | QIC-17 → QIC-18 → QIC-22 → QIC-08 → QIC-06 → QIC-07 → QIC-09 | AUSGEFÜHRT — Ausgangsbasis; laufende Aufgabenanteile bleiben sichtbar |
| 2 | Normierung, Feldgleichungen und Horizontbegründung | QIC-01 → QIC-02 → QIC-03 | AUSGEFÜHRT — Normierung korrigiert; Vakuumanspruch widerlegt; konkrete Kubik bestätigt |
| 3 | Literatur und Echo-Prüfung | QIC-15 → QIC-16 → QIC-10 → QIC-05 → QIC-11 → QIC-14 → QIC-12 → QIC-04 | AUSGEFÜHRT — Quellen geprüft; bedingte Laufzeit hergeleitet |
| 4 | Ausgabe, Abschlussbuild und Veröffentlichungskette | QIC-19 → QIC-20 → QIC-21 → QIC-24 → QIC-13 → QIC-23 | AUSGEFÜHRT MIT QUELLENLÜCKE — QIC-20 teilbearbeitet |

Welle 1 umfasst die bisherigen Phasen 1 und 2; Welle 2 Phase 3; Welle 3 die Phasen 4 und 5; Welle 4 die Phasen 6 und 7. Alle 24 Aufgaben und ihre Reihenfolge bleiben erhalten. Die Wellen bündeln Arbeitsblöcke; sie erklären fortlaufende Nachweisarbeit nicht automatisch für abgeschlossen.

QIC-22: Ausgangsbuild und Buildablauf in Welle 1, Abschlussbuild am reparierten Endstand in Welle 4. QIC-06/07/08/09: Ausgangssicht in Welle 1 und Fortschreibung bis zum Abschluss. QIC-23 gilt weiterhin ab Beginn vor jeder Veröffentlichung. Unabhängige Literaturvorbereitung darf vor Welle 3 stattfinden, sobald ihre Quellenabhängigkeiten geklärt sind. QIC-11 blockiert die Horizont- oder Echo-Prüfung nicht automatisch.

[Welle-1-Arbeitsnachweis](docs/REPAIR_WAVE1_2026-10-02.md) · [Welle-2-Arbeitsnachweis](docs/REPAIR_WAVE2_2026-10-02.md) · [Welle-3-Arbeitsnachweis](docs/REPAIR_WAVE3_2026-10-02.md) · [Welle-4-Arbeitsnachweis](docs/REPAIR_WAVE4_2026-10-02.md) · [Kernrechnungen](papers/derivations/quadratic_fr_and_horizon_checks.md) · [Build und Manuskriptzuordnung](docs/BUILD_WORKFLOW.md) · [Gemeinsame abgeleitete Nachweissicht](registry/repair_tracking.json). Diese Artefakte dokumentieren Arbeit und Quellen; sie sind keine zweite aktive Aufgabenliste.

## Aufgaben — maßgebliche Ausführungsfolge

Alle 24 Originalaufgaben, Herkunftskennungen und Dringlichkeitsklassen bleiben erhalten.

| Position | Welle | ID | Dringlichkeit | Aufgabe | Herkunft | Bearbeitungsstand | Abhängigkeit / Abschlussbindung |
|---|---|---|---|---|---|---|---|
| 1 | 1 | QIC-17 | Mittel | Beide LaTeX-Pakete eindeutig zuordnen. Verhältnis zwischen papers/tig-paper/ und submission/arxiv/ klären; gegebenenfalls maßgebliche Quelle und Exportweg festlegen. | A14, B6 | ERLEDIGT — strukturelle Paketzuordnung | Zuerst: Verhältnis und geltenden Scope beider Pakete prüfen; keine Autorität aus Versionsnummer oder Pfad ableiten. |
| 2 | 1 | QIC-18 | Mittel | Zuständigkeiten der Theorieverzeichnisse klären. Repository-Karte gegen die tatsächlichen Ablagen prüfen. Für Grundlagen, Kandidaten, Ableitungen und Paper-Auszüge den maßgeblichen Ablageort ausweisen. | A21, B5 | ERLEDIGT — strukturelle Quellenkarte | Vor fachlichen Änderungen: maßgebliche Theoriequellen und bestehende Owner-/Statusbindungen feststellen. |
| 3 | 1 | QIC-22 | Mittel | Arbeits-, Build- und Prüfablauf dokumentieren. Bestehende Repo- und Overleaf-Abläufe erfassen; die Erzeugung von Manuskript, Literaturverzeichnis, Abbildungen und PDF nachvollziehbar machen. | A17, B8 | ERLEDIGT — beide Abschlussbuilds und isolierter Quell-ZIP-Build PASS | Früh: Build und vorhandenen Overleaf-Ablauf erfassen, Ausgangsbuild versuchen und Ergebnis dokumentieren. Abschlussbuild nach den Reparaturen. |
| 4 | 1 | QIC-08 | Hoch | Audit- und Reparaturübersicht herstellen. Verstreute Befunde mit betroffenen Dateien, Reparaturen, erneuten Prüfungen und belegtem Bearbeitungsstand verbinden. | A18, B3 | ERLEDIGT — Wellen 1–4 mit Reparaturstand und verbleibender Quellenlücke gebunden | Nach Arbeitsgrundlage: schlanke Übersicht der vorhandenen Befunde beginnen; während aller Reparaturen fortschreiben. |
| 5 | 1 | QIC-06 | Hoch | Aussagen und Nachweise gemeinsam erschließen. Aussagen, Annahmen, Beweispflichten, Abhängigkeiten und Nachweise verbinden. Bestehende Register nutzen; nur fehlende Funktionen ergänzen. | B1 | ERLEDIGT — zwölf Aussagegruppen mit Quellen, Grenzen und Endartefakten erschlossen | Auf Ausgangsbefunde und Quellen stützen; für den ersten Reparaturblock beginnen und fortschreiben. |
| 6 | 1 | QIC-07 | Hoch | Quellen–Aussagen-Zuordnung präzisieren. Verwendete Quellenversionen und relevante Passagen oder Gleichungen angeben. Direkte Unterstützung, Analogie und offene Übertragung unterscheiden. | A7 | ERLEDIGT — Quellversionen/Passagen und direkte versus indirekte Unterstützung gebunden | Quellversionen und Aussagen zunächst für die Kernprüfungen binden; neue Literatur in Welle 3 ergänzen. |
| 7 | 1 | QIC-09 | Hoch | Offene Fragen und Gegenprüfung ordnen. Forschungsfragen, Grenzen, Gegenargumente, Gegenmodelle, Widerlegungsbedingungen und negative Ergebnisse gemeinsam erschließen; Mehrfacheinträge zusammenführen. | B2 | ERLEDIGT — Gegenprüfungen, negative Ergebnisse und offene Forschungsfragen erschlossen | Bestehende offene Fragen und Gegenprüfungen aufnehmen; neue Erkenntnisse fortschreiben. |
| 8 | 2 | QIC-01 | Kritisch | α-/μ-Normierung prüfen und korrigieren. Die festgestellte Inkonsistenz zwischen Definitionen und Gleichungen auflösen; alle betroffenen Manuskriptstellen nachführen. | A10 | ERLEDIGT — Wirkung/μ-Konvention korrigiert und geprüft | Nach Quellen-/Scope-Zuordnung; Normierung vor der Prüfung des betroffenen f(R)-Lösungsanspruchs. |
| 9 | 2 | QIC-02 | Kritisch | Metrik gegen die f(R)-Feldgleichungen prüfen. Voraussetzungen und tatsächlichen Lösungsnachweis klären. Aussagen über eine bewiesene Lösung auf den belegten Stand begrenzen. | A12 | ERLEDIGT — Vakuumanspruch widerlegt; Manuskripte begrenzt | Mit geklärter Normierung und Paketzuordnung; repräsentative Geometrie und behauptete Feldgleichungslösung unterscheiden. |
| 10 | 2 | QIC-03 | Kritisch | Begründung der kubischen Strukturgleichung reparieren. Die allgemeine Behauptung einer kubischen Notwendigkeit für Faltenbifurkationen korrigieren; die spezifische TIG-Gleichung gesondert begründen. | A11 | ERLEDIGT — modellgebundene Kubik und lokaler Fold nachgewiesen | Spezifische Horizontgleichung und allgemeine Bifurkationsbegründung gesondert prüfen; Ergebnis vor QIC-04 binden. |
| 11 | 3 | QIC-15 | Mittel | Recherchezeitraum dokumentieren. Vorherigen Berichtsstichtag und aktuelles Suchfenster festhalten; neue Arbeiten von neuen Versionen unterscheiden. | A5 | ERLEDIGT — Suchfenster und unbekannter Vorlauf offengelegt | Suchfenster vor erneuter Recherche festhalten; parallel zu Welle 2 möglich. |
| 12 | 3 | QIC-16 | Mittel | Literaturpriorisierung nachvollziehbar machen. TIG-Relevanz, Neuigkeitswert und wissenschaftliche Belastbarkeit getrennt bewerten und die Auswahlreihenfolge begründen. | A6 | ERLEDIGT — getrennte Auswahlkriterien und Quellenbewertung | Auswahlkriterien vor der neuen Literaturauswahl festlegen; keine bloße Rangfolge nach Aktualität. |
| 13 | 3 | QIC-10 | Hoch | Quellen zur Horizontbildung ergänzen. Ergebnisse über bestehende oder stationäre Horizonte von Ergebnissen über ihre Entstehung unterscheiden und die Abdeckungslücke bearbeiten. | A4 | ERLEDIGT — Hayward-Vorläufer und dynamische Abdeckungslücke gebunden | Recherche nach geklärtem Suchrahmen; Horizontbildung von Eigenschaften bestehender Horizonte trennen. |
| 14 | 3 | QIC-05 | Hoch | Voraussetzungen des Horizontbeweises vervollständigen. Beim Ghosh-/Sarkar-Eintrag die tragenden Annahmen, den Gültigkeitsbereich und die Übertragbarkeit auf TIG ausdrücklich erfassen. | A3 | ERLEDIGT — Satzvoraussetzungen und TIG-Übertragungsgrenze geprüft | Mit QIC-10 bearbeiten; Quellvoraussetzungen und tatsächliche TIG-Übertragbarkeit ausdrücklich prüfen. |
| 15 | 3 | QIC-11 | Hoch | Quellen zur Rückgewinnung von QM bearbeiten. Direkte, belastbare Quellen suchen und einordnen. Eine fortbestehende Abdeckungslücke ausdrücklich ausweisen. | A9 | ERLEDIGT — direkte QM-Prüfmaßstäbe; TIG-Rückgewinnung weiter offen | Eigener Recherche-/Theoriepunkt; kein pauschaler Blocker der Horizont- oder Echo-Prüfung. |
| 16 | 3 | QIC-14 | Mittel | Bessa-Datumsangaben klären. Preprint-Veröffentlichung, Versionsdatum und gegebenenfalls Zeitschrifteneinreichung eindeutig unterscheiden. | A8 | ERLEDIGT — arXiv-v1-Datum; Journal-Eingangsdatum unbestimmt | Vor Integration der betreffenden Quelle ihre Datums- und Versionsangaben verifizieren. |
| 17 | 3 | QIC-12 | Hoch | Neue Quellen in die Manuskripte integrieren. Für die drei aufgenommenen Quellen prüfen, welche Aussagen sie tatsächlich stützen, und passende Zitate an diesen Stellen ergänzen. | A1 | ERLEDIGT — drei Quellen an begrenzten Aussagen in beiden Texten zitiert | Nach Prüfung der jeweiligen Quellen und Aussagen; keine automatische Übernahme aller drei Quellen als TIG-Nachweis. |
| 18 | 3 | QIC-04 | Kritisch | Echo-Delay herleiten. Exponent, Integrationsgrenzen und Reflexions-/Randmodell überprüfen; unbelegte Vorhersagen korrigieren oder entsprechend kennzeichnen. | A13 | ERLEDIGT — bedingte Laufzeit hergeleitet; physische TIG-Echos offen | Nach QIC-01–03, soweit ihre Ergebnisse das verwendete Modell betreffen; relevante Horizontvoraussetzungen aus QIC-05/10 berücksichtigen. |
| 19 | 4 | QIC-19 | Mittel | Literaturmatrix in die Navigation aufnehmen. Die Auffindbarkeit von research/tig_literature_matrix.md über vorhandene Einstiegs- und Übersichtsdateien prüfen und fehlende Verweise ergänzen. | A20 | ERLEDIGT — Literaturmatrix in README, AGENTS und Quellenkarte verlinkt | Vorhandene Literaturmatrix verlinken; unabhängige reversible Vorarbeit kann früher erfolgen. |
| 20 | 4 | QIC-20 | Mittel | PDFs ihren Quellen zuordnen. Insbesondere für TIG3_Vacuum_Structure.pdf die zugehörige Manuskriptquelle und Version ermitteln und dokumentieren. | A19, B7 | TEILBEARBEITET — Mai-PDFs identifiziert; passende Original-LaTeX-Pakete fehlen | Quellen- und Versionsbindung vor dem Abschluss von QIC-23; fehlende oder mehrdeutige Herkunft sichtbar halten. |
| 21 | 4 | QIC-21 | Mittel | Abbildungen zuordnen und bereinigen. Verteilte, gleichnamige und mit (1) bezeichnete Bilder vergleichen; maßgebliche Quellen, Verwendung und Exportfassungen festlegen. | A16, B7 | ERLEDIGT — Formate, Dubletten, Rollen und reproduzierbare aktuelle Grafik gebunden | Verwendung und Originalquellen vor Bereinigung prüfen; Auswirkungen im Abschlussbuild kontrollieren. |
| 22 | 4 | QIC-24 | Bereinigung | Auffällige Dateinamen korrigieren. Endungen, Schreibfehler, problematische Sonderzeichen und versehentliche Leerzeichen kontrolliert vereinheitlichen; Verweise und Manuskript-Erzeugung anschließend prüfen. | A15, B9 | ERLEDIGT — zehn geprüfte Pfade umbenannt; Bytes und Verweise erhalten | Nach Pfad-/Verwendungsabgleich kontrolliert ändern; anschließend Verweise und Build prüfen. |
| 23 | 4 | QIC-13 | Hoch | Ausgabe des Literaturverzeichnisses korrigieren. Die festgestellte unsrt-Problematik beheben, damit erforderliche arXiv-Kennungen, DOI und Links im erzeugten Literaturverzeichnis erscheinen. | A2 | ERLEDIGT — DOI/arXiv/Links in beiden finalen PDF-Bibliografien geprüft | Im maßgeblichen Build arXiv, DOI und Links prüfen; Änderung anschließend im erzeugten Literaturverzeichnis verifizieren. |
| 24 | 4 | QIC-23 | Vor Veröffentlichung zwingend | Veröffentlichungskette und DOI-Zuordnung dokumentieren. Manuskriptquelle, PDF, Einreichungspaket, veröffentlichte Fassung und DOI eindeutig verbinden. | B4 | ERLEDIGT — Quelle/PDF/Quell-ZIP und historische Versions-/Konzept-DOIs gebunden | Gilt ab Beginn vor jeder Veröffentlichung. Zuordnung am geprüften Endstand abschließen; keine neue Releasefreigabe durch Listenpflege. |

## Bearbeitungsnachweis

Der [konsolidierte Reparaturbericht als Markdown](docs/REPAIR_REPORT_2026-10-02.md) stellt den alten und neuen Stand, das Delta aller 24 Aufgaben, die erledigten Reparaturen und den verbleibenden Rest gegenüber. Diese Arbeitsliste bleibt die einzige aktive Aufgabenliste; der Bericht ergänzt die Nachweisführung ohne Statusänderung.

Pro ID knapp dokumentieren: verifizierter Ausgangsbefund mit Quellenpfad und Snapshot → ausgeführte Änderung oder begründet verworfener Verdacht → Prüfung/Readback → verbleibende wissenschaftliche Fragen → tatsächlicher Bearbeitungsstand. IDs und Herkunft bleiben stabil. Redaktionelle Reparatur und wissenschaftlicher Nachweis bleiben getrennt.

## Herkunft und Listen-Preflight

Quelle: die am 2. Oktober 2026 im Chat „TIG Research Radar“ ausgegebenen Audit- und Strukturaufgaben; A = erste Liste mit 21 Punkten, B = zweite Liste mit elf Punkten. Die Herkunftskennungen referenzieren diese Ausgangslisten, nicht neue wissenschaftliche Objekt-IDs.

Die 32 Ausgangseinträge wurden mit sichtbarer Herkunft auf 26 Aufgaben konsolidiert: 24 für QIC und zwei für SSC. Der gemeinsame B7-Eintrag wurde in QIC-20 (PDF-Quellen) und QIC-21 (Abbildungen) getrennt erhalten. Keine Herkunft fehlt.

Ursprünglicher Listen-Preflight v1.0: Vollständigkeit, eindeutige Repo-Zuordnung und Herkunftsabdeckung geprüft; alle Aufgaben zunächst OFFEN. Same-run-Selbstprüfung (AIL-0); kein unabhängiger Audit und keine erneute wissenschaftliche Prüfung der Befunde.

## Begründung der Reihenfolge — erhaltene Ausgangsbewertung v1.1

Der auf main @ b247bdefdf5d50b28dbad60b31f9f2e0f15a8975 gelesene [Papertext](papers/tig-paper/main.tex) beschreibt die Geometrie ausdrücklich als repräsentativen Sektor und nicht als vollständige Lösung neuer kovarianter Feldgleichungen. Das [arXiv-Paket](submission/arxiv/main.tex) enthält dagegen eine quadratische f(R)-Wirkung, eine α-/μ-Zuordnung und einen stärkeren Schluss über demonstrierte f(R)-Horizontübergänge. Vor Änderungen muss QIC-17 die Rollen, Quellenbindung und den jeweils geltenden Aussageumfang dieser Pakete feststellen. Die Fassungsdifferenz ist ein belegter Prüfgrund; daraus folgt keine ungeprüfte Wahl eines Scientific Owners.

Normierung, Lösungsanspruch und spezifische Horizontbegründung tragen die nachgeordneten Echo-Aussagen. Deshalb bleiben QIC-01–03 kritisch und QIC-04 folgt auf die für sein Modell benötigten Ergebnisse. Neue Literatur wird erst nach ihrer Quellen-/Aussagenprüfung integriert. Literaturausgabe und Dateiordnung werden am reparierten Build verifiziert.

Die in [field_equations/open_questions.md](field_equations/open_questions.md) geführten Forschungsprogramme behalten ihre eigenen Quellen, Status und Prioritäten. Die Listenumsortierung behauptet weder ihre Schließung noch ihre automatische Blockierwirkung für jeden begrenzten Paperclaim. Ein offener Forschungsgegenstand wird nicht durch eine redaktionelle Reparatur gelöst.

Der Auftrag des Versionslaufs v1.1 war die ausdrücklich freigegebene Korrektur der Arbeitsliste und ihrer direkten README-/AGENTS-Einstiege. Wissenschaftliche Manuskripte, Claimstatus, Auditverdikte, historische DOI-Fassungen und Releaseobjekte wurden in diesem Versionslauf nicht verändert.

## Ausführung und Entscheidungspunkte

Der Repair Agent kann Inventar und Quellenvergleich, bestehende Nachweise und Register, Literaturrecherche mit Primärquellen, überprüfbare mathematische Prüfungen, kontrollierte Text-/Referenzkorrekturen sowie lokale Build-/PDF-Prüfungen bearbeiten. Ein benötigter Zugriff oder nicht rekonstruierbarer Quellenstand wird mit seinem konkreten Umfang dokumentiert.

Bei QIC-01–04 und QIC-05 muss das Ergebnis aus der Rechnung beziehungsweise Quelle folgen: bestätigter Nachweis, begrenzter Claim, begründeter No-Defect-Befund oder sichtbar verbleibender offener Punkt. Ein gewünschter Lösungsnachweis wird nicht vorausgesetzt. Ist eine wissenschaftliche Bedeutungswahl oder eine nicht belegbare Authority-Zuordnung erforderlich, erstellt der Agent die vollständige Entscheidungsvorlage mit den betroffenen Quellen und Konsequenzen; keine stille Festlegung.

Ein Same-run-Selbstcheck ist kein unabhängiger Audit. Externe Prüfung, Freigabe eines konkreten Veröffentlichungspakets und eine neue DOI-/Release-Veröffentlichung erhalten keine Autorisierung durch die Aufgabenliste. Reine technische Prüfung oder bereits belegte Fehlerkorrektur erzeugen keine Claim-Promotion.

## Versionsnachweis v1.1

- Human-Authority-Auftrag: Arbeitsliste gemäß der am 2. Oktober besprochenen Reihenfolge korrigieren und als neue Arbeitsgrundlage ablegen.
- Eingang: main @ b247bdefdf5d50b28dbad60b31f9f2e0f15a8975; ursprüngliche Liste v1.0 mit 24 offenen Aufgaben.
- Änderung: sieben Ausführungsphasen, QIC-17 als Einstieg, klare Abhängigkeiten und vorbereitende/finale Bindung von QIC-22 und QIC-23.
- Keine Aufgabe entfallen, keine ID oder Herkunft umnummeriert, kein Aufgabenstatus auf erledigt gesetzt.
- Listenprüfung vor Ablage: 24/24 Aufgaben mit identischen Originalaufträgen, Herkunft und Dringlichkeitsklassen erhalten; jede ID genau einmal in der maßgeblichen Aufgabentabelle; keine zyklische harte Abschlussabhängigkeit; lokale Markdown-Verweise geprüft.
- Assurance: Same-run-Selbstprüfung / AIL-0 für operative Listenpflege; kein neues wissenschaftliches Audit.
- Readback, Routing- und HEAD-Prüfung erfolgen nach dem Ablagecommit; der Abschlussnachweis berichtet das tatsächlich geprüfte Ergebnis.

## Versionsnachweis v1.2 / Welle 1

Auftrag: „bitte in vier wellen aufteilen. jetzt welle 1“. Quellenfreeze main @ `8fb4989d43382ccf303c8c52b2c7af746fa35034`. Zwei strukturelle Zuordnungsaufgaben erledigt, fünf Ausgangs-/Nachweisaufgaben teilbearbeitet, 17 Aufgaben offen. Die beiden technischen Buildfehler sind korrigiert; fachliche Kernprüfungen, externe Primärquellenprüfung, Endexport und Veröffentlichung folgen in ihren Wellen.

Materialisierte Nachweise und tatsächliche Grenzen stehen im [Welle-1-Arbeitsnachweis](docs/REPAIR_WAVE1_2026-10-02.md). Neue Arbeitsdateien ersetzen keine Scientific Owner. Kein Claim, wissenschaftliches Auditfinding oder bestehendes OQ wurde durch Welle 1 promoviert oder geschlossen. Readback und HEAD-Prüfung erfolgen nach dem Ablagecommit; Ergebnis im Abschlussnachweis.

## Versionsnachweis v1.3 / Welle 2

Auftrag: „jetzt welle 2“. Frisch gelesener Eingang main @ `88fef45371dbefe89ee35dce4e8accc5e8eb6baa`. QIC-01–03 sind als beauftragte Reparaturen erledigt: konsistente Alpha-/Mu-Konvention, explizites negatives Vakuum-f(R)-Ergebnis mit begrenzten Manuskriptclaims, konkrete kubische Horizontableitung und lokaler Fold. Kein positiver f(R)-Lösungsnachweis wird behauptet. Das eigenständige Dynamik-/Materieprogramm bleibt offen; Abschluss dieser Reparatur-IDs schließt keine bestehenden Forschungs-OQs.

27 symbolische Checks bestanden; beide Manuskriptbuilds erfolgreich, zehn plus sechs PDF-Seiten visuell geprüft. Die Nachweissicht aus Welle 1 ist fortgeschrieben. Alle 24 IDs, Originalaufträge, Dringlichkeitsklassen, Herkunft und Wellenzuordnungen bleiben erhalten. Stand: fünf erledigt (darunter zwei strukturelle Zuordnungen), fünf teilbearbeitet, 14 offen. [Welle-2-Arbeitsnachweis](docs/REPAIR_WAVE2_2026-10-02.md) und [vollständige Kernrechnung](papers/derivations/quadratic_fr_and_horizon_checks.md). Readback und HEAD-Prüfung erfolgen nach dem Ablagecommit und werden im Abschlussbericht bestätigt.

## Versionsnachweis v1.4 / Welle 3

Auftrag: „welle 3 bitte“. Frisch gelesener Eingang main @ `da326a4041054c01f2574d02312826870616670c`. Alle acht Reparaturaufträge QIC-15/16/10/05/11/14/12/04 sind mit ihrem begrenzten Ergebnis erledigt: nachvollziehbarer Suchrahmen und Priorisierung, Hayward-Herkunft und dynamische Lücke, geprüfte Ghosh-/Sarkar-Voraussetzungen, direkte QM-Rekonstruktionsmaßstäbe und fortbestehende TIG-Lücke, korrekte Bessa-Metadaten, Integration der drei Quellen in beide Manuskripte sowie bedingte Echo-Laufzeit samt Grenzen/Vorfaktoren. Eine Quellenlücke wird durch ihren Reparaturabschluss nicht zum wissenschaftlichen Nachweis.

18 exakte und fünf numerische Prüfbedingungen bestanden; Welle-2-Kernprüfung unverändert erhalten. Beide Manuskripte gebaut, zwölf plus sieben finale PDF-Seiten visuell geprüft; keine offenen Zitate oder finalen LaTeX-Warnungen. Vorhandene PDFs, Abbildungen, Archivfassungen und DOI-Objekte bleiben eigene ungeänderte Objekte. Welle 4 behält ihre sechs offenen Aufgaben einschließlich unsrt-Ausgabe, Endlayout und Export-/Veröffentlichungskette.

Alle 24 IDs, Originalaufträge, Dringlichkeiten, Herkunft, Wellen und Abschlussbindungen bleiben erhalten. Stand: 13 erledigt, fünf teilbearbeitet, sechs offen. [Arbeitsnachweis](docs/REPAIR_WAVE3_2026-10-02.md), [Quellenprüfung](research/wave3_source_review.md), [bedingte Laufzeit](papers/derivations/echo_delay_with_boundaries.md) und [Nachweissicht](registry/repair_tracking.json). Kein bestehender Auditverdikt oder OQ-Status geändert; keine unabhängige Prüfung oder Releasefreigabe. Readback und HEAD-Prüfung erfolgen nach dem Ablagecommit; der Abschluss berichtet das tatsächlich geprüfte Ergebnis.

## Versionsnachweis v1.5 / Welle 4

Auftrag: „welle 4 bitte“. Eingang main @ `9f6cdf096716c6d070685b0d88555f403f6db8fa`. Navigation, kontrollierte Dateinamen, Abbildungszuordnung, Literaturausgabe, Abschlussbuild und Veröffentlichungskette ausgeführt. Aktuelle Paper-/Einreichungs-PDFs und isoliert gebautes Quell-ZIP liegen als eindeutig abgeleitete Exportobjekte vor. Der historische Release v1.0.0 ist mit seinem Versions-DOI und Konzept-DOI über das vollständig abgeglichene Zenodo-Archiv gebunden. Kein neues Release oder DOI, keine Einreichung.

**QIC-20 bleibt TEILBEARBEITET.** Die PDF-Identitäten, Mai-Daten, Uploadcommits und historische DOI-Ablage sind gesichert. Im gesamten aktuellen Tree, den Upload-/Tag-Snapshots und dem publizierten Archiv fehlen jedoch die passenden Original-LaTeX-Pakete; benachbarte main.tex-Dateien haben andere Titel/Inhalte. Restanforderung: Originalquellen der Mai-PDFs vom wissenschaftlichen Autor beschaffen und ihre vollständige Quellen-/PDF-Zuordnung prüfen. Keine Quellenidentität aus gleichem Verzeichnis ableiten.

QIC-06/07/08/09/22 sind am begrenzten Reparatur-Endstand abgeschlossen; ihre operative Übersicht schließt keine Forschungsfragen. Alle 24 Originalaufträge, IDs, Herkunft, Dringlichkeiten, Positionen, Wellen und Abschlussbindungen bleiben erhalten. Gesamtstand: **23 erledigt, eine Aufgabe teilbearbeitet, keine unbegonnen**. Ein technischer Restpunkt bleibt; das Repository wird nicht als vollständig quellenrekonstruiert oder veröffentlichungsfreigegeben bezeichnet.

[Arbeitsnachweis](docs/REPAIR_WAVE4_2026-10-02.md) · [Artefaktzuordnung](docs/ARTIFACT_BINDINGS.md) · [Veröffentlichungskette](docs/PUBLICATION_CHAIN.md) · [Exportobjekte](submission/exports/wave4_2026-10-02/README.md). Finale Builds ohne Warnungen; alle finalen Seiten visuell geprüft, DOI/arXiv/Links im PDF geprüft; isolierter Export und Repository-Build pixelgleich. Same-run-Selbstprüfung; bestehende Auditverdikte, Forschungs-OQs, Lizenz-/Tag-/DOI-Objekte unverändert. Commit-, Tree- und vollständiges Datei-Readback folgen der Ablage; der Abschluss berichtet das tatsächlich geprüfte Ergebnis.
