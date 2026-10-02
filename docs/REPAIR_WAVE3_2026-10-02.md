# QIC — Reparaturnachweis Welle 3

Version 1.0 · 2026-10-02 · beauftragter Repair-Lauf / keine zweite Arbeitsliste.

Auftrag: „welle 3 bitte“. Eingang main @ `da326a4041054c01f2574d02312826870616670c`, Tree `4308f46358899bd5fecba9fd65b73c744336a448`. 251 Blobs inventarisiert, 231 Textdateien gegen Git-Blob-SHAs verifiziert; zwölf zentrale Dateien frisch über den GitHub-Connector gelesen, unveränderte materialisierte Quellen wiederverwendet. Ziel: die acht Aufgaben der Welle 3 in der allein aktiven [Arbeitsliste v1.4](../REPAIR_TODO.md). Keine erneute vollständige wissenschaftliche Prüfung aller Repo-Dateien oder der 14 Repositories.

## Reparaturergebnisse

ERLEDIGT bezeichnet den begrenzten Reparaturauftrag einschließlich sichtbarer Gegenbefunde oder verbleibender Forschungsfragen, keinen positiven Theoriebeweis.

| ID | Verifizierter Befund und ausgeführte Reparatur | Beleg / verbleibende Grenze |
|---|---|---|
| QIC-15 | Matrixstichtag bekannt, tatsächlicher früherer Suchschluss nicht rekonstruierbar; Fenster 01.09. bis Abruf 02.10.2026 und ergänzende ältere Primärsuche dokumentiert. | [Suchprotokoll](../research/wave3_source_review.md); Trefferdeckung unvollständig, kein Anspruch weltweiter Vollständigkeit. |
| QIC-16 | Direkter Prüfwert, Aktualität/Version und Belastbarkeit getrennt bewertet; Beweispflicht vor bloßer Neuigkeit. | [Literaturmatrix v1.1](../research/tig_literature_matrix.md); sieben versionierte Primärtexte an aussagentragenden Passagen geprüft. |
| QIC-10 | Hayward Eq. (5) exakt umgerechnet: m=M, ℓ²=r_c³/(2M). Dynamische Eqs. (10)–(19) mit variabler Masse/Fluss als Vergleich ergänzt. | [Quellenprüfung](../research/wave3_source_review.md); statische Familie und Koaleszenz bekannt, keine TIG-Evolution hergeleitet. |
| QIC-05 | Ghosh/Sarkar §§II–III und Appendix A geprüft; glatter stationärer Killing-Horizont, on-shell/Fluss-/Kompaktheitsbedingungen, Kopplungs- und Extremalitätsausnahmen explizit. | Beide Manuskripte; kritischer Horizont extremal, quadratischer Vakuumtest negativ. Zeroth law kein Entstehungsbeweis. |
| QIC-11 | Hardy v4 und Chiribella/D’Ariano/Perinotti v3 als direkte QM-Rekonstruktionsmaßstäbe ergänzt; states/effects, Wahrscheinlichkeiten, Komposition, Axiome/Born-Regel und Dynamik als TIG-Beweispflichten benannt. | TIG-spezifische Rückgewinnung im geprüften Set weiter unbelegt; kein Unmöglichkeits-/Nichtexistenzsatz. Garay setzt quantisierte LQG-Strukturen voraus. |
| QIC-14 | Bessa-Ersteinreichung/v1 24.09.2026, 05:24:34 UTC; Autorenangabe „Submitted to PRD“ von Journal-Eingang/Annahme/Publikation getrennt. | Journal-Eingangsdatum unbestimmt, keine weitere arXiv-Version beim Abruf angezeigt. |
| QIC-12 | Ghosh/Sarkar, Bessa und Garay an begrenzten Aussagepositionen in beide Manuskripte integriert; Bib-Begleitobjekte nachgeführt. | Ghosh stationäre Horizonte; Bessa lineare FLRW-SHA/QSA, keine kontrollierte Superhorizontfortsetzung; Garay indirekter LQG-Vergleich. Bibliografische Linkausgabe bleibt QIC-13. |
| QIC-04 | Dr*/dr=1/F, Laufzeitintegral, Beobachteruhr, Reflexions-/Grenzmodell und beide Seiten der Schwelle hergeleitet; pauschale Echo-Vorhersage ersetzt. | [Vollständige Ableitung](../papers/derivations/echo_delay_with_boundaries.md), [Prüfskript](../tools/verify_wave3.py); geometrische Laufzeit kein physischer TIG-Echo-Nachweis. |

## Wesentliche fachliche Grenzen

Die repräsentative Metrik ist die umparametrisierte Hayward-Familie. Bei festem ℓ läuft r_c³=2M(v)ℓ² mit; eine Variation bei festem r_c ist nicht dieselbe Entwicklung. Bekannte statische Geometrie und Horizontkoaleszenz werden in Abstract, Einleitung und Schluss beider Manuskripte als Vorläuferkenntnis ausgewiesen. Dynamische Horizontentstehung, eine TIG-Materiequelle und gewöhnliche QM aus TIG bleiben offen. Das negative quadratische Vakuumresultat aus Welle 2 bleibt gültig.

Für M>0, asymptotisch normierte Zeit und eine horizontlose volle Engpassdurchquerung mit festen Grenzen x_ref<x_c<x_b gilt:

$$T\sim\frac{16\pi M}{9\sqrt{3}\,\beta_c}(\beta-\beta_c)^{-1/2}.$$

Unterhalb der Schwelle liefert ein fester Außenspiegel mit x_ref>x_c einen endlichen Grenzwert. Nur eine zusätzliche Vorschrift x_ref=x_++(q−1)s, q>1, s=√3β_c√(β_c−β), erzeugt dort den berechneten −1/2-Vorfaktor. Bei festem β und Spiegelannäherung an den einfachen Horizont ist die Divergenz logarithmisch; genau kritisch ergibt sich eine inverse Abstandsdivergenz. Alle Fälle binden Grenzen, Grenzübergang und Uhr. Kein Hauptwert durch einen Zukunftshorizont als zurückkehrendes Signal; ein Testskalar mit vorgegebener Reflexion ist keine gravitative Echo-/Stabilitätsableitung.

Die Reviewer-Antwortgrundlage wurde an diese Grenzen angepasst: keine durchgeführte QNM-Rechnung, pauschale Skalarstabilität, neue Hayward-Metrik oder unbelegte Größenordnungskonsistenz mit GW150914 behauptet. Pfadbereinigung selbst bleibt QIC-24.

## Prüfung und Fortschreibung

- 18 exakte Bedingungen und fünf numerische Bedingungen mit 60 Dezimalstellen bestanden (SymPy 1.14.0, mpmath 1.3.0). Die numerischen Integrale prüfen vollständige Engpassdurchquerung, mitlaufende und feste Außengrenzen samt asymptotischen Vorfaktoren; keine Spiegelphysik vorausgesetzt als TIG-Nachweis.
- Beide Manuskripte mit dem bestehenden Buildskript in frischen Ausgabeordnern gebaut; je zwei explizite finale pdflatex-Pässe und erneutes Fingerprint-Readback. Paper zwölf, Einreichung sieben Seiten, alle 19 finalen Seiten gerendert und visuell geprüft. Zitate aufgelöst, finale LaTeX-Logs ohne Warnungen oder Overfull-Boxen. [Buildablauf](BUILD_WORKFLOW.md).
- Gemeinsame [Nachweissicht](../registry/repair_tracking.json) unter wave3 ergänzt. Historische Welle-1/2-Quellen-/Buildnachweise, die zwölf Tracking-Identitäten, Auditverdikte, ursprüngliche OQs und deren Owner bleiben erhalten; kein bestehendes OQ geschlossen und kein Release erzeugt.
- README, AGENTS, Ownership und Arbeitsliste fortgeschrieben. Alle 24 Aufträge, IDs, Herkunft, Dringlichkeiten, Positionen, Wellen und Abschlussbindungen erhalten. Welle-3-Ergebnis: acht Reparaturen erledigt; Gesamtstand 13 erledigt, fünf teilbearbeitet, sechs offen.

Das ist eine Same-run-Selbstprüfung, kein unabhängiger wissenschaftlicher Audit. Versions-/Passagenprüfung fremder Primärtexte ist keine unabhängige Wiederholung ihrer gesamten Beweise. Suchlücken, unverifizierte Publikationsdaten und Übertragungsgrenzen bleiben explizit. Alte PDFs, Abbildungen und DOI-/Archivobjekte wurden nicht ersetzt.

## Ablage und nächster Einstieg

Vor Commit: Originalaufträge/Abhängigkeiten und Quellenfingerprints abgleichen, Register-/Link-/Rechenprüfung und frischen main-HEAD prüfen. Nach Commit: main-HEAD, vollständigen Tree und jede geänderte Datei frisch zurücklesen und mit dem geschriebenen Inhalt vergleichen; der Abschluss berichtet das tatsächlich ausgeführte Readback. Kein Commit-Selbstbezug nötig.

**Nächster Einstieg ist Welle 4 mit QIC-19.** QIC-19/20/21/24/13/23 bleiben offen; Abschlussbuild, unsrt-Linkausgabe, Endlayout und eigenständiger Export folgen dort. Welle 4 wird in diesem Auftrag nicht begonnen.
