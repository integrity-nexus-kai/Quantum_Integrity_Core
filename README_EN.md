# Quantum Integrity Core — public TIG research repository

## Current scope

This repository contains TIG research and two separately maintained manuscripts. Their current object is a specified static, spherically symmetric representative geometry:

```math
m(r)=\frac{Mr^3}{r^3+r_c^3},\qquad F(r)=1-\frac{2Mr^2}{r^3+r_c^3},\qquad M>0,\ r_c>0.
```

This is a reparameterized Hayward family with finite core curvature. Its static Killing-horizon roots do not establish a new dynamical theory. The manuscripts test the metric against constant-coefficient quadratic metric f(R) gravity. The result is **negative**: the nontrivial representative metric is not a vacuum solution of that tested theory. A specified matter source or a different dynamical completion remains open. [Assumptions and calculation](papers/derivations/quadratic_fr_and_horizon_checks.md).

## Results within the representative geometry

For the chosen mass profile:

```math
x^3-x^2+\beta^3=0,\qquad x=\frac{r_H}{2M},\quad\beta=\frac{r_c}{2M}.
```

Two positive roots coalesce at `x_c = 2/3`, `beta_c = (4/27)^(1/3)`. Above the critical beta there is no positive root. At beta = 0, the polynomial zero roots are not positive Schwarzschild horizons. This is static branch structure, not a dynamical black-hole formation proof. The Hayward origin and known coalescence result are acknowledged in the [source review](research/wave3_source_review.md).

A geometric round-trip delay is derived for explicit integration endpoints and a prescribed reflector. Its scaling depends on these boundary choices. Physical TIG echoes, gravitational perturbation dynamics, an evaporation remnant and QM recovery are not established by those calculations. [Delay assumptions and boundaries](papers/derivations/echo_delay_with_boundaries.md).

## Manuscripts and working exports

| Object | Source | Bound output / scope |
|---|---|---|
| Paper v1.4 | [papers/tig-paper/main.tex](papers/tig-paper/main.tex) | 12-page working paper; representative geometry, negative vacuum test, conditional delay |
| arXiv draft | [submission/arxiv/main.tex](submission/arxiv/main.tex) | Separate six-page manuscript with its own bibliography; no submission performed |
| Current PDFs and source ZIP | [Export overview](submission/exports/wave4_2026-10-02/README.md) | Derived working artifacts; source ZIP builds in isolation |
| Active figure | [Horizon branches](figures/tig_horizon_branches.png) | Static cubic roots; [generator](tools/generate_horizon_figure.py), [metadata](figures/tig_horizon_branches.json) |

The manuscripts are distinct text objects. Historical May PDFs are preserved separately and are not exports of the current main.tex files. Their [qualified source/version bindings](docs/QIC20_SOURCE_BINDING_CLOSEOUT_2026-10-03.md) do not confirm exact original compiler states or complete original historical input bundles. The four-page forensic reconstruction retains missing citations and image placeholders; it is not a clean current build.

The paper gives a photon-sphere orbit equation. Quantitative photon-sphere/shadow predictions and physical gravitational-wave signals remain research questions; legacy plots are not automatically current evidence.

## Architecture status and research boundaries

The separate effective field-equation architecture retains its [own source](field_equations/field_equation_1_0.md) and [registered validation status](field_equations/validation_status.md). That structural status applies to its stated realization and assessed sector. It is not transferred to a quadratic f(R) vacuum-solution claim, an independent fundamental tensor, complete covariant dynamics or empirical validation. [Object ownership](OBJECT_OWNERSHIP.md).

Six [research questions QIC-RQ-01–06](field_equations/open_questions.md#offene-forschungsfragen-aus-der-reparatur--2-oktober-2026) remain OPEN and deferred by the author: dynamics/matter/covariance, independent tensor construction, dynamical horizon formation, physical echoes, TIG-specific QM recovery and quantitative observable predictions. Original research-program and audit statuses remain separately bound.

## Repair and documentation

The original [repair list v1.8](REPAIR_TODO.md) records 24/24 completed operational tasks. This does not solve the research questions. [Repair report](docs/REPAIR_REPORT_2026-10-02.md) · [Build workflow](docs/BUILD_WORKFLOW.md) · [Repository map](REPOSITORY_MAP.md) · [Publication chain](docs/PUBLICATION_CHAIN.md).

The [initial preflight](docs/PREFLIGHT_QIC_2026-10-03.md) records findings at its pre-correction snapshot. Their subsequent correction and review state are tracked in the [documentation closeout](docs/PREFLIGHT_REPAIR_CLOSEOUT_2026-10-03.md). Builds and internal checks do not authorize a scientific release, DOI or submission.

## Author and license

Kai Stefan Dietrich · Independent Researcher.

Current main: [LICENSE](LICENSE). Historical DOI-linked snapshots retain their version-specific license boundary: [Transition notice](LICENSE_DOI_TRANSITION_NOTICE.md).
