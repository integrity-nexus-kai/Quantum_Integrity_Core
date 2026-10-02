# QIC — priorisierte Reparatur-To-do-Liste

**Dokument-ID:** QIC-REPAIR-TODO-2026-10-02  
**Version:** 1.0  
**Datum:** 2026-10-02  
**Objektklasse:** operative Aufgabenliste / REPAIR_TASK_LIST  
**Repository:** integrity-nexus-kai/Quantum_Integrity_Core  
**Branch:** main  
**Ablage-Basiscommit:** a61ef4f6fc5e13ac9d59ce2e60fed6fca4d4aa3a  
**Status:** 24 Aufgaben OFFEN; Liste abgelegt, Reparaturen nicht ausgeführt  
**Human Authority:** Kai Stefan Dietrich

## Einstieg für den Repository Repair Agent

Dies ist die vom Nutzer zur Ablage freigegebene, vollständige QIC-Liste aus dem Audit-/Strukturabgleich. Beginne mit QIC-01 und arbeite in der aufgeführten Prioritätsreihenfolge. QIC-23 ist vor jeder Veröffentlichung zu erfüllen, unabhängig von seiner Tabellenposition.

Vor einer Reparatur aktuellen Branch/HEAD und betroffene Quellen frisch lesen und den übernommenen Befund prüfen. Die Liste ist ein Arbeitsauftrag mit früheren Auditbefunden und strukturellen Prüfpunkten; ein Dateiname oder eine fehlende Ordnerkategorie allein beweist keinen Defekt. Bereits erfüllte Funktionen feststellen und vorhandene Register weiterverwenden. Keine Doppelstrukturen erzeugen.

Der Auftrag dieses Ablagelaufs umfasst diese Aufgabenliste und ihre Einstiegsverweise. Die konkrete Ausführung richtet sich nach dem Auftrag des Repair Agents. Eine abgelegte Aufgabe ist keine erfolgte Reparatur, keine Claim-Promotion, keine OQ-Closure und keine Veröffentlichung.

## Priorisierte Aufgaben

| ID | Priorität | Aufgabe | Herkunft | Bearbeitungsstand |
|---|---|---|---|---|
| QIC-01 | Kritisch | α-/μ-Normierung prüfen und korrigieren. Die festgestellte Inkonsistenz zwischen Definitionen und Gleichungen auflösen; alle betroffenen Manuskriptstellen nachführen. | A10 | OFFEN |
| QIC-02 | Kritisch | Metrik gegen die f(R)-Feldgleichungen prüfen. Voraussetzungen und tatsächlichen Lösungsnachweis klären. Aussagen über eine bewiesene Lösung auf den belegten Stand begrenzen. | A12 | OFFEN |
| QIC-03 | Kritisch | Begründung der kubischen Strukturgleichung reparieren. Die allgemeine Behauptung einer kubischen Notwendigkeit für Faltenbifurkationen korrigieren; die spezifische TIG-Gleichung gesondert begründen. | A11 | OFFEN |
| QIC-04 | Kritisch | Echo-Delay herleiten. Exponent, Integrationsgrenzen und Reflexions-/Randmodell überprüfen; unbelegte Vorhersagen korrigieren oder entsprechend kennzeichnen. | A13 | OFFEN |
| QIC-05 | Hoch | Voraussetzungen des Horizontbeweises vervollständigen. Beim Ghosh-/Sarkar-Eintrag die tragenden Annahmen, den Gültigkeitsbereich und die Übertragbarkeit auf TIG ausdrücklich erfassen. | A3 | OFFEN |
| QIC-06 | Hoch | Aussagen und Nachweise gemeinsam erschließen. Aussagen, Annahmen, Beweispflichten, Abhängigkeiten und Nachweise verbinden. Bestehende Register nutzen; nur fehlende Funktionen ergänzen. | B1 | OFFEN |
| QIC-07 | Hoch | Quellen–Aussagen-Zuordnung präzisieren. Verwendete Quellenversionen und relevante Passagen oder Gleichungen angeben. Direkte Unterstützung, Analogie und offene Übertragung unterscheiden. | A7 | OFFEN |
| QIC-08 | Hoch | Audit- und Reparaturübersicht herstellen. Verstreute Befunde mit betroffenen Dateien, Reparaturen, erneuten Prüfungen und belegtem Bearbeitungsstand verbinden. | A18, B3 | OFFEN |
| QIC-09 | Hoch | Offene Fragen und Gegenprüfung ordnen. Forschungsfragen, Grenzen, Gegenargumente, Gegenmodelle, Widerlegungsbedingungen und negative Ergebnisse gemeinsam erschließen; Mehrfacheinträge zusammenführen. | B2 | OFFEN |
| QIC-10 | Hoch | Quellen zur Horizontbildung ergänzen. Ergebnisse über bestehende oder stationäre Horizonte von Ergebnissen über ihre Entstehung unterscheiden und die Abdeckungslücke bearbeiten. | A4 | OFFEN |
| QIC-11 | Hoch | Quellen zur Rückgewinnung von QM bearbeiten. Direkte, belastbare Quellen suchen und einordnen. Eine fortbestehende Abdeckungslücke ausdrücklich ausweisen. | A9 | OFFEN |
| QIC-12 | Hoch | Neue Quellen in die Manuskripte integrieren. Für die drei aufgenommenen Quellen prüfen, welche Aussagen sie tatsächlich stützen, und passende Zitate an diesen Stellen ergänzen. | A1 | OFFEN |
| QIC-13 | Hoch | Ausgabe des Literaturverzeichnisses korrigieren. Die festgestellte unsrt-Problematik beheben, damit erforderliche arXiv-Kennungen, DOI und Links im erzeugten Literaturverzeichnis erscheinen. | A2 | OFFEN |
| QIC-14 | Mittel | Bessa-Datumsangaben klären. Preprint-Veröffentlichung, Versionsdatum und gegebenenfalls Zeitschrifteneinreichung eindeutig unterscheiden. | A8 | OFFEN |
| QIC-15 | Mittel | Recherchezeitraum dokumentieren. Vorherigen Berichtsstichtag und aktuelles Suchfenster festhalten; neue Arbeiten von neuen Versionen unterscheiden. | A5 | OFFEN |
| QIC-16 | Mittel | Literaturpriorisierung nachvollziehbar machen. TIG-Relevanz, Neuigkeitswert und wissenschaftliche Belastbarkeit getrennt bewerten und die Auswahlreihenfolge begründen. | A6 | OFFEN |
| QIC-17 | Mittel | Beide LaTeX-Pakete eindeutig zuordnen. Verhältnis zwischen papers/tig-paper/ und submission/arxiv/ klären; gegebenenfalls maßgebliche Quelle und Exportweg festlegen. | A14, B6 | OFFEN |
| QIC-18 | Mittel | Zuständigkeiten der Theorieverzeichnisse klären. Repository-Karte gegen die tatsächlichen Ablagen prüfen. Für Grundlagen, Kandidaten, Ableitungen und Paper-Auszüge den maßgeblichen Ablageort ausweisen. | A21, B5 | OFFEN |
| QIC-19 | Mittel | Literaturmatrix in die Navigation aufnehmen. Die Auffindbarkeit von research/tig_literature_matrix.md über vorhandene Einstiegs- und Übersichtsdateien prüfen und fehlende Verweise ergänzen. | A20 | OFFEN |
| QIC-20 | Mittel | PDFs ihren Quellen zuordnen. Insbesondere für TIG3_Vacuum_Structure.pdf die zugehörige Manuskriptquelle und Version ermitteln und dokumentieren. | A19, B7 | OFFEN |
| QIC-21 | Mittel | Abbildungen zuordnen und bereinigen. Verteilte, gleichnamige und mit (1) bezeichnete Bilder vergleichen; maßgebliche Quellen, Verwendung und Exportfassungen festlegen. | A16, B7 | OFFEN |
| QIC-22 | Mittel | Arbeits-, Build- und Prüfablauf dokumentieren. Bestehende Repo- und Overleaf-Abläufe erfassen; die Erzeugung von Manuskript, Literaturverzeichnis, Abbildungen und PDF nachvollziehbar machen. | A17, B8 | OFFEN |
| QIC-23 | Vor Veröffentlichung zwingend | Veröffentlichungskette und DOI-Zuordnung dokumentieren. Manuskriptquelle, PDF, Einreichungspaket, veröffentlichte Fassung und DOI eindeutig verbinden. | B4 | OFFEN |
| QIC-24 | Bereinigung | Auffällige Dateinamen korrigieren. Endungen, Schreibfehler, problematische Sonderzeichen und versehentliche Leerzeichen kontrolliert vereinheitlichen; Verweise und Manuskript-Erzeugung anschließend prüfen. | A15, B9 | OFFEN |

## Bearbeitungsnachweis

Pro ID knapp dokumentieren: verifizierter Ausgangsbefund mit Quellenpfad und Snapshot → ausgeführte Änderung oder begründet verworfener Verdacht → Prüfung/Readback → verbleibende wissenschaftliche Fragen → tatsächlicher Bearbeitungsstand. IDs und Herkunft bleiben stabil. Redaktionelle Reparatur und wissenschaftlicher Nachweis bleiben getrennt.

## Herkunft und Listen-Preflight

Quelle: die am 2. Oktober 2026 im Chat „TIG Research Radar“ ausgegebenen Audit- und Strukturaufgaben; A = erste Liste mit 21 Punkten, B = zweite Liste mit elf Punkten. Die Herkunftskennungen referenzieren diese Ausgangslisten, nicht neue wissenschaftliche Objekt-IDs.

Die 32 Ausgangseinträge wurden mit sichtbarer Herkunft auf 26 Aufgaben konsolidiert: 24 für QIC und zwei für SSC. Der gemeinsame B7-Eintrag wurde in QIC-20 (PDF-Quellen) und QIC-21 (Abbildungen) getrennt erhalten. Keine Herkunft fehlt.

Listen-Preflight: Vollständigkeit, eindeutige Repo-Zuordnung und Herkunftsabdeckung geprüft; alle Aufgaben zunächst OFFEN. Same-run-Selbstprüfung (AIL-0); kein unabhängiger Audit und keine erneute wissenschaftliche Prüfung der Befunde.
