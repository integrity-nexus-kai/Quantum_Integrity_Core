# Quantum Integrity Core

Dieses Repository enthält Forschungsarbeiten zu modifizierter Gravitation und systemischer Integritätsbewertung, organisiert in zwei klar getrennten Ebenen:

* **Topological Integrity Gravity (TIG)** — eine quadratische (f(R))-Erweiterung der Allgemeinen Relativitätstheorie
* **AXIOMA** — ein Framework zur Bewertung der Integrität komplexer Systeme

---

# 1. Topological Integrity Gravity (TIG)

## Überblick

Topological Integrity Gravity (TIG) ist eine Erweiterung der Allgemeinen Relativitätstheorie durch einen quadratischen Krümmungsterm der Form:

[
f(R) = R + \alpha R^2
]

Das Modell entspricht einer kontrollierten (f(R))-Modifikation mit wohldefinierten höherordentlichen Feldgleichungen.

Im Niedrigkrümmungsbereich reproduziert TIG die Standard-Gravitation, während im Hochkrümmungsregime systematische Korrekturen auftreten.

---

## Zentrale Eigenschaften

* Quadratische (f(R))-Gravitation (Starobinsky-Struktur)
* Erhält Ricci-flache Vakuumlösungen ((R = 0))
* Führt Korrekturen bei hoher Krümmung ein
* Kompatibel mit schwachen Gravitationsfeldern

---

## Wissenschaftlicher Einstiegspunkt

Das zentrale Dokument ist das vollständige Paper:

```text id="kuy8jv"
papers/tig-paper/main.tex
```

Dieses enthält:

* Modellformulierung
* Feldgleichungen
* Horizonstruktur
* Photonensphäre und Schattenradius

---

# 2. AXIOMA

## Überblick

AXIOMA ist ein Framework zur Bewertung des globalen Zustands komplexer Systeme.

Im Gegensatz zu klassischen Sicherheitsansätzen, die einzelne Ereignisse betrachten, bewertet AXIOMA die Integrität des Gesamtsystems.

---

## Konzeptionelle Verschiebung

Klassische Security fragt:

> „Gab es einen Angriff?“

AXIOMA fragt:

> „Befindet sich das System noch in einem gültigen Gesamtzustand?“

---

## Einstiegspunkte

* `axioma/axioma_whitepaper.md`
* `axioma/axioma_architecture.md`
* `axioma/axioma_use_cases.md`

---

# 3. Repository-Struktur

```text id="5v9qzj"
papers/
  tig-paper/
    main.tex
    abstract.tex
    references.bib

figures/
  tig_horizon_radius_prediction.png

axioma/
  axioma_whitepaper.md
  axioma_architecture.md
  axioma_use_cases.md

applications/
strategy/
```

---

# 4. Einordnung

Dieses Repository trennt klar:

* **Theoretische Physik (TIG)**
* **Systemarchitektur (AXIOMA)**

---

# 5. Beiträge

Beiträge sind willkommen in Form von:

* mathematischer Analyse
* kritischer Überprüfung
* Simulationen
* Modellvalidierung

---

# 6. Status

* TIG: erste Forschungs-Veröffentlichung
* AXIOMA: konzeptionelle Entwicklung

---

**Autor:** Kai Stefan Dietrich
