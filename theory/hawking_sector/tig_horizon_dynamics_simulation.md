# TIG Horizon Dynamics Simulation

## Purpose

This document defines a first heuristic simulation model for TIG-related horizon dynamics near structural criticality.

The objective is to visualize how a TIG horizon may relax, soften, oscillate, or become metastable near the critical transition.

This is not a numerical relativity simulation and not a solution of the Einstein field equations.

Status:
heuristic / exploratory / non-rigorous.

---

## Core Question

What happens to a TIG horizon when the structural parameter approaches the critical value?

\[
\beta \rightarrow \beta_c
\]

with:

\[
\beta_c = \left(\frac{4}{27}\right)^{1/3}
\]

and:

\[
x_c = \frac{2}{3}
\]

---

## Simulation Variables

The first simulation should track:

- horizon radius \(r_H(t)\),
- dimensionless horizon state \(x(t)\),
- structural parameter \(\beta(t)\),
- effective surface gravity \(\kappa_{\mathrm{eff}}(t)\),
- effective temperature response \(T_{\mathrm{eff}}(t)\),
- relaxation time \(\tau(t)\),
- and perturbation amplitude \(A(t)\).

---

## TIG Horizon Equation

The structural horizon equation is:

\[
x^3 - x^2 + \beta^3 = 0
\]

where:

\[
x = \frac{r_H}{2M}
\]

and:

\[
\beta = \frac{r_c}{2M}
\]

The simulation should numerically track how the admissible horizon branch changes as \(\beta\) approaches \(\beta_c\).

---

## Heuristic Dynamical Model

A first-order relaxation model may be used:

\[
\frac{dx}{dt} = -\gamma \frac{\partial V(x,\beta)}{\partial x}
\]

where \(V(x,\beta)\) is an effective structural potential.

A minimal candidate potential is:

\[
V(x,\beta) = \frac{1}{2}\left(x^3 - x^2 + \beta^3\right)^2
\]

This makes the horizon equation correspond to minima of the effective potential.

---

## Critical Slowing Down

Near the saddle-node transition, relaxation may slow down.

A heuristic relaxation time can be modeled as:

\[
\tau(\beta) \sim \frac{1}{|\beta_c - \beta|^\alpha}
\]

where \(\alpha > 0\) is a phenomenological critical exponent.

This is not yet derived.

---

## Effective Surface Gravity Response

The simulation may define:

\[
\kappa_{\mathrm{eff}}(t) = \kappa_0 \cdot F(\beta(t))
\]

with:

\[
\kappa_0 = \frac{1}{4M}
\]

and \(F(\beta)\) a structural correction factor.

A first heuristic model could be:

\[
F(\beta) = 1 - \left(\frac{\beta}{\beta_c}\right)^p
\]

for \(0 \leq \beta < \beta_c\).

This is an exploratory ansatz only.

---

## Effective Temperature

The effective Hawking-like temperature response is then:

\[
T_{\mathrm{eff}}(t) = \frac{\kappa_{\mathrm{eff}}(t)}{2\pi}
\]

The simulation should show whether temperature response is suppressed, delayed, or destabilized near criticality.

---

## Echo-Like Perturbation Response

A perturbation amplitude may be modeled by:

\[
A(t) = A_0 e^{-\lambda t}\cos(\omega t)
\]

with critical damping:

\[
\lambda(\beta) \rightarrow 0
\]

as:

\[
\beta \rightarrow \beta_c
\]

This represents possible delayed relaxation or echo-like near-horizon response.

---

## Simulation Outputs

The first version should plot:

1. \(x(t)\)
2. \(r_H(t)\)
3. \(\kappa_{\mathrm{eff}}(t)\)
4. \(T_{\mathrm{eff}}(t)\)
5. perturbation amplitude \(A(t)\)
6. relaxation time \(\tau(\beta)\)

---

## Scientific Boundaries

This simulation does not claim:

- a full black hole evaporation model,
- a replacement of Hawking radiation,
- a numerical relativity solution,
- or proof of information preservation.

It is a controlled heuristic model for TIG-inspired horizon dynamics near criticality.

---

## Research Purpose

The purpose is to identify whether the TIG critical horizon structure may generate:

- delayed relaxation,
- metastable behavior,
- critical slowing down,
- modified thermodynamic response,
- and possible echo-like signatures.

These would become candidate observables for later mathematical and numerical study.
