# Topological Integrity Gravity (TIG)

**[Dokumentationskorrektur zum Preflight](docs/PREFLIGHT_REPAIR_CLOSEOUT_2026-10-03.md):** die fünf Befunde sind im begrenzten Text-/Verweisumfang repariert; Abschlussnachweise und Prüfumfang sind verknüpft. Der [ursprüngliche Preflight](docs/PREFLIGHT_QIC_2026-10-03.md) bleibt als Befund am damaligen Commit erhalten. Interne Prüfung AIL-0; unabhängige Prüfung und Veröffentlichungsfreigabe sind separate Schritte.

## Repository Repair Agent — Aufgabenliste

**[REPAIR_TODO.md v1.8 — aktuelle Arbeitsgrundlage](REPAIR_TODO.md): 24/24 Aufgaben ERLEDIGT.** Vier Arbeitswellen und abschließende historische Quellenzuordnung ausgeführt.

**[Reparaturbericht — alter Stand, neuer Stand, Delta und Rest](docs/REPAIR_REPORT_2026-10-02.md)** · **[QIC-20-Abschlussnachweis](docs/QIC20_SOURCE_BINDING_CLOSEOUT_2026-10-03.md)**. Bearbeitbare Markdown-Nachweise.

TIG3: elf Quellen importiert, Builds und 14-Seiten-Vergleich bestätigt. Vierseitiges TIG-Paper vom 3. Mai: unveränderte historische Hauptquelle rekonstruiert alle vier Seiten einschließlich der ungelösten Zitate und Bildplatzhalter. Die Quellen-/Versionszuordnung ist erledigt. Exakte ursprüngliche Compiler-/Eingabezustände bleiben als historische Provenienzgrenzen dokumentiert; der forensische Altbuild ist kein fehlerfreier aktueller Build.

[Welle 1](docs/REPAIR_WAVE1_2026-10-02.md) · [Welle 2](docs/REPAIR_WAVE2_2026-10-02.md) · [Welle 3](docs/REPAIR_WAVE3_2026-10-02.md) · [Welle 4](docs/REPAIR_WAVE4_2026-10-02.md) · [TIG3-Vergleich](docs/TIG3_SOURCE_COMPARISON_2026-10-03.md) · [Manuskriptzuordnung und Build](docs/BUILD_WORKFLOW.md) · [Quellenkarte](REPOSITORY_MAP.md).

[Literaturmatrix](research/tig_literature_matrix.md) · [Quellenprüfung](research/wave3_source_review.md) · [Aktuelle Exporte](submission/exports/wave4_2026-10-02/README.md) · [Artefaktzuordnung](docs/ARTIFACT_BINDINGS.md) · [DOI-Kette](docs/PUBLICATION_CHAIN.md).

**Forschungsstand:** QIC-RQ-01–06 sind im bestehenden [Forschungsfragen-Dokument](field_equations/open_questions.md#offene-forschungsfragen-aus-der-reparatur--2-oktober-2026) OFFEN und auf Nutzerauftrag zurückgestellt. Reparaturabschluss ist keine wissenschaftliche Lösung dieser Fragen. Anschließend Rücksprache; kein automatischer Forschungs-, SSC- oder Veröffentlichungsstart.

**Aktueller technischer Endstand:** Paper v1.4 und Einreichungsdraft Welle 4 bauen erfolgreich; das Quell-ZIP baut isoliert. Die beiden historischen Mai-PDFs behalten ihre ursprünglichen Bytes. Aktuelle Exporte sind Arbeitsartefakte ohne neue DOI-/Release- oder Einreichungsfreigabe. QIC-23 gilt vor jeder Veröffentlichung.

**Geprüfter Manuskriptstand Welle 2:** Die kubische Horizontgleichung und ihr kritischer Punkt gelten für das konkret gewählte Massenprofil. Diese Metrik ist bei M>0 und r_c>0 keine Vakuumlösung der geprüften konstanten quadratischen metrischen f(R)-Theorie. Die nachstehenden Architekturstatus werden damit nicht als positiver f(R)-Lösungsbeweis ausgegeben; eigenständige Dynamik, Materiequelle und bestehende Forschungsfragen bleiben offen. [Rechnung und Voraussetzungen](papers/derivations/quadratic_fr_and_horizon_checks.md).

**Geprüfter Manuskriptstand Welle 3:** Die repräsentative Metrik ist exakt eine umparametrisierte Hayward-Familie; ihre statische Horizontkoaleszenz ist bekannt. Der Echo-Exponent −1/2 gilt für die hergeleitete Laufzeit nur mit ausgewiesenen Integrationsgrenzen und Spiegelvorschriften. Physische TIG-Echos, dynamische Horizontentstehung und TIG-QM-Rückgewinnung bleiben offene Forschungsaufgaben. [Welle-3-Ergebnisse und Grenzen](docs/REPAIR_WAVE3_2026-10-02.md).

Topological Integrity Gravity (TIG) is a gravitational research program investigating structural admissibility and bounded-curvature representative geometries. The current manuscripts examine a specified static Hayward family, its horizon roots and a negative quadratic f(R) vacuum test. A complete dynamical theory remains a research objective.


---

## License and DOI-Version Boundary

The current `main` branch is governed by the **Canonical Integrity Research & Commercial Rights License v2.0**.

Commercial use, monetization, sale, paid distribution, commercial product/service integration, licensing, sublicensing, and other commercial exploitation of the current repository material require prior explicit written agreement with Kai Stefan Dietrich and expressly negotiated economic participation for Kai Stefan Dietrich.

**Historical DOI exception:** the public GitHub release `v1.0.0` from 2026-05-19 is a DOI-linked archival snapshot with its own release-specific license notice. That historical tagged/DOI-linked version is preserved as its own version-bound licensing object and is not retroactively rewritten by changes to current `main`.

See:
- `LICENSE`
- `LICENSE_DOI_TRANSITION_NOTICE.md`
- `CANONICAL_STATUS.md`

---

# Current Status

The current manuscripts establish the horizon polynomial and local root coalescence for the chosen static representative mass profile, examine its finite curvature, and show that the nontrivial metric is not a vacuum solution of the tested constant-coefficient quadratic metric f(R) theory. The geometric round-trip delay is conditional on stated endpoints and a prescribed reflector. [Manuscript calculation and assumptions](papers/derivations/quadratic_fr_and_horizon_checks.md).

The separate [effective field-equation architecture](field_equations/field_equation_1_0.md) retains the source classification **STRUCTURALLY VALIDATED RESEARCH CANDIDATE**, within its static spherical realization and assessed sector. Its [registered validation results](field_equations/validation_status.md) are separate source objects; this summary does not independently re-audit them or transfer their positive status to the quadratic f(R) vacuum claim, complete covariant dynamics, a fundamental independent tensor or empirical validation.

---

# Papers

The TIG framework currently consists of three primary research layers.

## TIG1

Foundational admissibility framework and horizon consistency structure.

## TIG2

Exact horizon bifurcation analysis based on:

```math
x^3 - x^2 + \beta^3 = 0
```

including:

- discriminant geometry,
- saddle-node criticality,
- admissible horizon sectors,
- structural transition analysis.

## TIG3

Historical bounded-curvature representative sector and separate effective architecture, including:

- effective field-equation architecture,
- integrity tensor realization,
- finite-curvature geometry,
- static horizon-root coalescence,
- observational research directions.

The historical TIG3 source/PDF binding has its [own comparison record](docs/TIG3_SOURCE_COMPARISON_2026-10-03.md). Its label does not prove a vacuum solution of the quadratic f(R) theory tested in the current manuscripts or a dynamical formation process.

---

# Canonical Field Equation Architecture

The separate architecture records the following field-equation form; its source status and assumptions are bound to [field_equations/field_equation_1_0.md](field_equations/field_equation_1_0.md):

```math
G_{\mu\nu}
=
I_{\mu\nu}[g,r_c]
```

where

- \(G_{\mu\nu}\) is the Einstein tensor,
- \(I_{\mu\nu}\) is the Integrity Tensor realization,
- \(g_{\mu\nu}\) is the metric,
- \(r_c\) is the integrity scale.

The current spherical realization uses

```math
m(r)
=
\frac{M r^3}
     {r^3+r_c^3}
```

leading to

```math
F(r)
=
1-
\frac{2Mr^2}
     {r^3+r_c^3}.
```

---

# Horizon Structure

The horizon condition becomes

```math
x^3-x^2+\beta^3=0
```

with

```math
x=\frac{r_H}{2M}
```

and

```math
\beta=\frac{r_c}{2M}.
```

The critical transition occurs at

```math
x_c=\frac{2}{3}
```

and

```math
\beta_c=
\left(\frac{4}{27}\right)^{1/3}.
```

For M>0 and r_c>0, this is the static Killing-horizon root structure of the specified Hayward mass profile. It does not establish dynamical horizon formation. At beta=0, polynomial zero roots are not positive Schwarzschild horizons. Known Hayward coalescence and the current parameterization are distinguished in the [source review](research/wave3_source_review.md).

---

# Registered Architecture Results and Their Scope

The positive statuses below are retained from [field_equations/validation_status.md](field_equations/validation_status.md) for the separate effective architecture, not newly awarded by this README or transferred to the current quadratic f(R) test. [Object/source boundaries](OBJECT_OWNERSHIP.md).

| Registered item | Object and boundary |
|---|---|
| P1 Tensor Construction | Effective tensor realization in the source architecture; independent fundamental tensor derivation remains O3 / QIC-RQ-02. |
| P2–P4 GR / Schwarzschild / Newtonian Recovery | Registered limits of that architecture and spherical realization; no complete covariant/dynamical-theory proof is inferred. |
| P5–P7 Horizon Derivation / Critical Transition / Finite Curvature | Stated representative static mass profile and its geometry; no dynamical formation or empirical confirmation is inferred. |
| P9 Structural Stability | Original positive status is limited to the source's analyzed perturbation sector. Complete gravitational perturbation dynamics and physical echo stability remain open. |
| P10 Admissibility Closure | Original status for established requirements of the stated realization; no universal closure or completion of the open research programs. |

P8 Effective Stress Tensor Analysis remains PRELIMINARY in its source. The detailed historical derivations and their original audits have not been independently revalidated in this documentation repair. [Open programs and QIC-RQ-01–06](field_equations/open_questions.md).

---

# Open Programs

The following programs remain active:

- Variational Formulation
- Covariant Extension
- Independent Integrity Tensor Definition
- Dynamical Closure
- Observational Predictions

See:

```text
field_equations/open_questions.md
```

---

# Observable Implications

The framework motivates structurally constrained analyses of:

- black-hole shadow deviations,
- gravitational lensing corrections,
- photon-sphere shifts,
- near-critical horizon transitions.

These implications are treated as model-dependent consequences requiring further observational and theoretical analysis.

---

# Repository Structure

```text
field_equations/
├── field_equation_1_0.md
├── validation_status.md
├── open_questions.md

papers/
├── tig-paper/
├── derivations/
├── topological-foundations-program/

figures/
theory/
topology/
applications/
strategy/
axioma/
```

---

# Scientific Position

TIG is not presented as a replacement for General Relativity.

The current objective is to investigate whether admissibility-driven geometric constraints can generate observable horizon phenomena while preserving established gravitational limits.

The present repository contains the canonical public TIG research layer.

---

# Repository Notes

The repository separates:

- published scientific results,
- validated field-equation architecture,
- active research programs,
- and open mathematical problems.

Historical development chains remain archived within the repository structure and are not removed when a canonical result is established.

---

# Author

Kai Stefan Dietrich

Independent Researcher

Contact:

kai.physics@protonmail.ch
