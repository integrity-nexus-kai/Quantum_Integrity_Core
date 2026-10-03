# QIC — Preflight vom 3. Oktober 2026

**Ergebnis: technische Wiederholungsprüfung PASS; öffentliche Texte und Verweise benötigen Korrekturen (`REQUEST_CHANGES`).** Fünf dokumentierte Befunde: zwei hoch, zwei mittel, einer niedrig. Der qualifizierte operative Abschluss **24/24** ist in der Arbeitsliste und den Abschlussregistern konsistent. Die sechs Forschungsfragen bleiben **OFFEN / ZURÜCKGESTELLT**.

Geprüfter Stand: `main @ 4e1d4cbbc80664e130e19b2d32cf215b6152e5a7`. Modus `L1_ONE_REPO_DRY_RUN`, dieselbe produzierende Instanz, **AIL-0**. Der Bericht ist ein begrenzter Preflight, kein unabhängiger Wissenschaftsaudit. Prüfzeit: `2026-10-03T10:27:23.450023+00:00`.

## Prüfstand und Umfang

Alle 296 getrackten Dateiobjekte wurden gegen ihre Git-Blobs geprüft und mit SHA-256 inventarisiert. Eine Inhaltsprüfung jeder Forschungsnotiz wird dadurch nicht behauptet. Die semantisch geprüften Pfade und die analytische Artefaktklassifikation sind im [maschinenlesbaren Bericht](../registry/qic_preflight_2026-10-03.json) beziehungsweise [Inventar](evidence/preflight_2026-10-03/inventory.json) benannt. Archivobjekte wurden ausschließlich auf Identität/Hash geprüft; der historische Fehlerbuild wurde nicht erneut ausgeführt.

Die aktuelle Quellen-/Versionszuordnung QIC-20 ist nachvollziehbar und bleibt qualifiziert erledigt. Das vollständige ursprüngliche Eingabepaket und der exakte damalige Compilerzustand sind weiterhin nicht bestätigt. Die alten Compiler-Exitcodes 1/2/1/1 sind im bestehenden Abschlussnachweis ausdrücklich erhalten; sie werden hier nicht als erfolgreicher aktueller Manuskriptbuild umgedeutet.

Zehn aktuelle Governancequellen aus Integrity_Nexus wurden am Commit `bdcc02a8fec6bd2dc7f70585a028aab1a52e0952` gelesen; im öffentlichen Bericht stehen nur Quellenidentitäten/Hashes, keine privaten Quelltexte. Das aktuelle Nexus-Inventar beschreibt neun Repositories; der achtteilige Skill-Bootstrap ist dafür kein aktuelles Inventar. Der Auftrag bleibt auf QIC begrenzt. QIC als Repositoryname wird nicht mit einem vollständigen QIC-Quantenobjekt gleichgesetzt. Eine Gesamtprüfung aller 14 Repositories erfolgt in diesem Lauf nicht.

## Technische Wiederholungsprüfung

| Prüfung | Ergebnis |
|---|---|
| Git-Identität aller getrackten Dateien | 296/296 PASS; sauberer Arbeitsbaum während der Prüfung |
| JSON-Syntax bestehender Register | 8/8 PASS |
| Lokale Markdown-Linkziele außerhalb von Codeblöcken | 260 Ziele in 225 Dateien; kein fehlendes Ziel |
| Quellen-/PDF-/ZIP-/Grafik-/Migrationsbindungen und Aufgabenstatus | 46/46 PASS |
| Aktuelle Paperquelle | Build erfolgreich; 12 Seiten |
| Aktuelles arXiv-Manuskript | Build erfolgreich; 6 Seiten |
| Isoliertes Quell-ZIP | Build erfolgreich; 6 Seiten; fünf exakt gebundene Quelldateien |
| Finale TeX-Logs | Keine Warning-/Overfull-/undefined-Marker in allen drei Läufen |
| Mathematische Prüfung Welle 2 | 27/27 Bedingungen PASS; negativer Vakuum-f(R)-Test bestätigt |
| Mathematische Prüfung Welle 3 | 18 exakte + fünf numerische Prüfungen PASS; 60 Dezimalstellen |
| PDF-Inhalts-/Rendervergleich | Alle 24 Seiten gerendert und gesichtet; Text und Render pixelgleich mit dem jeweiligen bestehenden Export bzw. direkten Build |
| Deterministisches Quell-ZIP | Bytegleich mit dem eingecheckten Welle-4-ZIP |

Die Gleichheit betrifft den Seiteninhalt und den Render mit MuPDF bei Faktor 1,3. PDF-Dateibytes können durch Zeitstempel abweichen. Die PDF-Prüfung liefert keine wissenschaftliche Freigabe. Aktuelle Exporte und die beiden historischen Mai-PDFs wurden nicht ersetzt.

Die vorhandenen Python-Prüfprogramme wurden nach Quellprüfung ausgeführt. Im Standardinterpreter fehlte zunächst SymPy; ein alter venv-Launcher war ebenfalls nicht verfügbar. Die erfolgreichen Läufe nutzten Python 3.12 mit den vorhandenen SymPy-1.14.0-/mpmath-1.3.0-Paketen über PYTHONPATH. Keine Repoquelle wurde dafür geändert. TeX Live 2023/Debian, pdfTeX 1.40.25, latexmk 4.83. [Laufergebnisse und Fingerprints](evidence/preflight_2026-10-03/checks.json).

Linkprüfung: lokale Inline-Markdown-Ziele, keine Live-Prüfung externer URLs, Referenzstil-Links oder automatisch erzeugter GitHub-Anker. Historische Snapshotpfade werden über bestehende Migrationsbindungen aufgelöst; frühere datierte Zwischenstände sind keine aktuellen Fehlstatus.

## Befunde am festgehaltenen Commit

| ID | Priorität | Ort | Befund und konkrete Korrektur |
|---|---|---|---|
| QIC-PF-001 | Hoch | README_EN.md, Zeilen 9–13, 28–36, 49–59, 85 | Weiterhin positive quadratische f(R)-Modell-/Herleitungsdarstellung und ungebundene Beschreibung des aktuellen PDFs. Englischen Einstieg auf repräsentative Hayward-Geometrie, negativen Vakuumtest, bedingte Laufzeit und tatsächlich gebundene Exporte aktualisieren. |
| QIC-PF-002 | Hoch | abstract.md, Zeilen 8–26 und 32–50 | Unmarkierte spektrale Herleitung, Parameter-/Materiekopplung und Verdampfungs-Remnant überschreiten die aktive Nachweiskette. Mit aktuellem Manuskript abgleichen oder als historisches/hypothetisches Objekt samt Quelle und Grenzen kennzeichnen. Eine statische Temperaturgrenze belegt keinen Verdampfungsverlauf. |
| QIC-PF-003 | Mittel | README.md, Zeilen 89–97, 172, 176–196 | Der korrekte neue Vorspann begrenzt den Haupttext nicht an jeder betroffenen Aussage: horizon dynamics/formation und pauschale Validierungsbegriffe bleiben missverständlich. Statische Koaleszenz benennen und positive Architekturstatus an ihr eigenes Objekt und den geprüften Sektor binden. |
| QIC-PF-004 | Mittel | papers/tig-paper/README.md, Zeile 5 | QIC-20 wird noch als teilbearbeitet ausgegeben. Auf den qualifizierten Zuordnungsabschluss und dessen Nachweis verweisen; verbleibende Originalpaket-/Compilergrenzen erhalten. |
| QIC-PF-005 | Niedrig | field_equations/open_questions.md, Zeile 255 | Redaktioneller Ausdruck technischer Quellenrest QIC-20 ist überholt. Verweis aktualisieren; alle Forschungsfragen bleiben offen. |

Alle Fundstellen beziehen sich auf den oben genannten Prüfcommit, vor der gesonderten Berichtsablage. Detaillierte Belegpfade, Regeln G-01 bis G-17 und Auswirkungsobjekte stehen im [JSON-Bericht](../registry/qic_preflight_2026-10-03.json). Die ersten beiden Befunde verhindern einen pauschalen inhaltlichen PASS für die öffentlichen Zusammenfassungen. Sie sind keine neue Widerlegung jeder TIG-Theorie oder der getrennten effektiven Tensorarchitektur.

## Fünf getrennte Bewertungsachsen

| Achse | Wert | Begründung |
|---|---|---|
| CONTENT_VERDICT | REQUEST_CHANGES | Öffentliche Aussagen und zwei aktuelle Verweise benötigen die benannten Korrekturen. |
| SYNC_STATE | UNVERIFIABLE | Lokaler Git-Stand stimmt mit beobachtetem main überein. In den zehn geladenen Nexusquellen ist jedoch kein erwarteter QIC-Zielcommit gebunden; globale Synchronität ist nicht attestierbar. |
| PERMISSION_STATE | READ_ONLY | Die Assurancephase hat keine Repo-/Statusmutation ausgeführt. Die spätere Berichtsablage ist eine separate autorisierte Dokumentationsintegration. |
| RELEASE_STATE | REVIEW_REQUIRED | Keine Veröffentlichung aus diesem Preflight; öffentliche Textbefunde, globale Bindung und unabhängige Prüfung bleiben zu behandeln. |
| ASSURANCE_LEVEL | AIL-0 | Selbstprüfung derselben Instanz; für routinemäßige unabhängige Assurance wäre mindestens ein separater AIL-1-Lauf erforderlich. |

`assessment_state = PARTIAL`: Der definierte technische Preflight ist abgeschlossen; der gesamte wissenschaftliche Korpus, historische positive Audits und globale Hin-/Rückabhängigkeiten wurden nicht unabhängig vollständig geprüft. Daher keine Aussage RELEASE_READY und kein Vollständigkeitsurteil über das gesamte Forschungsprogramm.

## Alter Stand, neuer Befund und nächster Schritt

**Alter Stand:** Arbeitsliste v1.8, 24 qualifiziert erledigte Reparaturaufgaben; aktuelle Manuskripte/Exporte und Forschungszurückstellung dokumentiert.

**Neuer Befund:** Der technische Stand ist reproduzierbar. Fünf verbleibende Dokumentationsprobleme sind an aktuellen öffentlichen Einstiegspfaden belegt. Sie sind zusätzliche Preflightbefunde; die abgeschlossenen ursprünglichen Aufgaben werden dadurch nicht stillschweigend neu geöffnet.

**Delta dieses Auftrags:** Prüfbericht, maschinenlesbares Urteil, Inventar-/Laufnachweise und direkte Einstiegsverweise. Keine Manuskript-, Lizenz-, Export-, historischen PDF-, ursprünglichen Audit- oder Forschungsstatusänderung. Keine zweite aktive Reparaturliste.

**Als Nächstes ausführbar:** Die fünf Befunde durch eine gesonderte kontrollierte Dokumentationskorrektur behandeln. Das benötigt keine neue Physikrechnung. Forschung bleibt zurückgestellt. Globale Zielcommitbindung gehört zum zuständigen Governance-Owner; ein lokaler technischer PASS ersetzt sie nicht. Anschließend getrennte Prüfung und Rücksprache vor einer wissenschaftlichen Veröffentlichung.

Dieser Bericht und seine Evidenz sind abgeleitete Prüfobjekte. Vorhandene wissenschaftliche Owner, ursprüngliche O1–O7-Status und sechs QIC-RQ-Status bleiben maßgeblich. Keine Forschung, SSC-Reparatur, externe Nachricht, Einreichung oder DOI-/Releaseerzeugung erfolgt automatisch.
