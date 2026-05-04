![TIG vs Schwarzschild](papers/tig_schwarzschild_horizon_comparison.png)

# Topological Integrity Gravity (TIG)
## Reading Guide

* Start here: Conceptual overview and key properties below  
* Core theory: See the LaTeX source in `papers/tig-paper/main.tex`  
* Visual intuition: Check the `figures/` directory  
* Extensions and applications: See `applications/`  
* Architectural context: See `axioma/`  

---

## What is this?

This repository contains a minimal, consistent formulation of **Topological Integrity Gravity (TIG)**.

The core result is the existence of a **critical parameter** that separates:

- black hole configurations (with horizons)  
- compact objects without horizons  

---

## 🔗 Quick Links

- 📄 Main paper (LaTeX): [papers/tig-paper/main.tex](papers/tig-paper/main.tex)  
- 📊 Figures: [figures/](figures/)  
- 📁 Applications: [applications/](applications/)  
- 🧠 Axioma: [axioma/](axioma/)  
- 🧭 Strategy: [strategy/](strategy/)  

---

## 🧠 Conceptual Positioning

Topological Integrity Gravity (TIG) is not introduced as a generic extension of General Relativity, but as a structurally constrained theory in which admissible curvature corrections are restricted by consistency conditions.

In contrast to phenomenological f(R) models, TIG exhibits a discrete critical transition between horizon and non-horizon geometries. This indicates a deeper structural organization of gravitational configurations.

---

## What TIG is not

* not a generic parameter extension of General Relativity  
* not a phenomenological curve-fitting model  
* not based on arbitrary modification of the action  

TIG instead restricts the space of admissible theories by structural consistency requirements.

---

## Key Properties

* constrained quadratic f(R) gravity  
* regularized internal mass profile  
* cubic horizon equation with analytical structure  
* critical transition between horizon and non-horizon geometries  

Observable implications include:

* black hole imaging  
* gravitational lensing effects  
* gravitational wave signatures  

---

## Why this matters

Topological Integrity Gravity (TIG) introduces a structurally constrained extension of General Relativity in which not all curvature corrections are admissible.

The existence of a critical parameter separating horizon and non-horizon configurations suggests that gravitational systems may be organized by deeper consistency conditions rather than continuous deformation alone.

---

## Minimal Consistency Statement

In TIG, admissible curvature corrections are not arbitrary but must preserve the structural integrity of horizon formation.

This implies:

* a well-defined root structure of the horizon equation  
* transitions only via critical points  
* no continuous deformation without crossing a structural threshold  

As a consequence, not all \( f(R) \)-type extensions are physically admissible.

---

## Observable Consequences

The consistency constraints imposed by TIG have direct observational implications:

* characteristic scale separating horizon and non-horizon configurations  
* modifications to photon sphere structure and shadow profiles  
* deviations in gravitational wave signals near criticality  

These effects arise from structural constraints, not parameter tuning.

---

## First Concrete Prediction

Near the critical regime:

* enhanced sensitivity of photon sphere structure  
* non-linear shifts in shadow radius  
* amplified deviations in gravitational wave signatures  

---

## Scaling Behavior Near Criticality

Let \( \beta \) denote the control parameter and \( \beta_c \) the critical value.

Near criticality:

\[
\Delta \mathcal{O} \sim |\beta - \beta_c|^\alpha
\]

with a non-trivial exponent \( \alpha \neq 1 \).

This implies:

* enhanced sensitivity near \( \beta_c \)  
* deviation from linear response  
* potential universality  

---

## Comparison with General Relativity

In General Relativity:

\[
\Delta \mathcal{O}_{GR} \sim |\beta - \beta_c|
\]

In TIG:

\[
\Delta \mathcal{O}_{TIG} \sim |\beta - \beta_c|^\alpha
\]

This difference provides a direct observational discriminator.

---

![TIG vs Schwarzschild](papers/tig_schwarzschild_horizon_comparison.png)

---

## Numerical Illustration

The repository includes numerical illustrations of:

- horizon radius dependence  
- saddle-node transition structure  
- echo-delay enhancement  

Relevant figures:

- `tig_horizon_transition_publication.png`  
- `tig_echo_delay_prediction.png`  

---

## 📂 Repository Structure

- `applications/` — applications  
- `axioma/` — architecture  
- `figures/` — visualizations  
- `papers/` — scientific content  
- `strategy/` — publication strategy  

---

## Open Question

What is the exact scaling exponent \( \alpha \) and does it exhibit universality?

---

## 📊 Status

- model defined  
- analytical structure derived  
- numerical illustrations available  
- stability analysis in progress  

---

## ⚠️ Scope

Not yet included:

- full dynamical stability analysis  
- cosmological solutions  
- quantum formulation  

---

## 👤 Author

Kai Stefan Dietrich  
Independent Research
