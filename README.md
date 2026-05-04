\documentclass[11pt,final]{article}

\usepackage[a4paper,margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{float}
\usepackage{microtype}

\title{Topological Integrity Gravity (TIG):\\
Critical Horizon Transitions in Quadratic $f(R)$ Gravity}

\author{Kai Stefan Dietrich\\
Independent Research}

\date{May 2026}

\begin{document}

\maketitle

\begin{abstract}

We introduce Topological Integrity Gravity (TIG), a structurally constrained extension of General Relativity in which admissible curvature corrections are restricted by consistency conditions.

The theory predicts the existence of a critical parameter separating horizon and non-horizon configurations, leading to a discrete transition in the space of gravitational solutions. In contrast to phenomenological $f(R)$ models, this transition is not arbitrary but arises from structural constraints on the horizon equation.

Near the critical regime, TIG implies non-linear scaling behavior of observable quantities, in contrast to the linear response expected in General Relativity. This leads to enhanced sensitivity of photon sphere structure, shadow radius, and gravitational wave signatures close to the transition.

We argue that these effects are direct consequences of the underlying consistency structure and provide a concrete observational signature of structurally constrained gravity theories.

\end{abstract}

\section{Introduction}

General Relativity provides an accurate description of gravitational phenomena across a wide range of scales \cite{einstein1915,wald1984}. Extensions such as $f(R)$ gravity introduce higher-curvature corrections and additional degrees of freedom \cite{sotiriou2010,defelice2010}.

The existence of a critical transition in horizon formation suggests that the presence or absence of horizons may not be a binary property, but rather the result of an underlying structural condition.

In this work, we identify such a mechanism within a quadratic $f(R)$ framework and show that it leads to a universal critical transition governed by structural constraints on the horizon equation.

\section{Consistency Constraint}

A generic extension of General Relativity allows arbitrary curvature corrections, leading to a large space of admissible models. However, not all such extensions are physically consistent.

Horizon formation must satisfy a structural stability requirement: small perturbations should not produce unphysical changes in the number of horizons except at well-defined critical points.

The minimal structure capable of producing such a transition is cubic. This follows from the theory of structurally stable bifurcations: the simplest mechanism by which the number of real solutions can change under smooth parameter variation is the saddle-node bifurcation, whose universal normal form is cubic.

Thus, the horizon equation takes the form
\begin{equation}
x^3 - x^2 + \beta^3 = 0 .
\end{equation}

This constraint selects a restricted class of admissible extensions, distinguishing TIG from generic phenomenological modifications of General Relativity.

\section{Quadratic $f(R)$ Framework}

We consider the action
\begin{equation}
S=\int d^4x\sqrt{-g}
\left[
\frac{1}{16\pi}(R-2\Lambda+\alpha R^2)
\right]
+S_{\mathrm{matter}} .
\end{equation}

Defining
\begin{equation}
f(R)=R-2\Lambda+\mu R^2,
\qquad
\mu=16\pi\alpha ,
\end{equation}
we obtain a quadratic $f(R)$ model.

The scalar degree of freedom is
\begin{equation}
\phi=f'(R)=1+2\mu R ,
\end{equation}
with effective mass
\begin{equation}
m_\phi^2=\frac{1}{6\mu}.
\end{equation}

\section{Effective Geometry}

We consider a static, spherically symmetric metric
\begin{equation}
ds^2=-F(r)dt^2+\frac{dr^2}{F(r)}+r^2d\Omega^2 .
\end{equation}

We introduce the effective mass profile
\begin{equation}
m(r)=\frac{Mr^3}{r^3+r_c^3},
\end{equation}
leading to
\begin{equation}
F(r)=1-\frac{2m(r)}{r}.
\end{equation}

This interpolates between a regular core and Schwarzschild asymptotics.

\section{Critical Horizon Structure}

Horizons satisfy
\begin{equation}
F(r_H)=0.
\end{equation}

This yields
\begin{equation}
r_H^3-2Mr_H^2+r_c^3=0.
\end{equation}

Introducing
\begin{equation}
x=\frac{r_H}{2M},
\qquad
\beta=\frac{r_c}{2M},
\end{equation}
the parameter $\beta$ is the dimensionless ratio between the internal regularization scale $r_c$ and the gravitational radius $2M$.

We obtain
\begin{equation}
x^3-x^2+\beta^3=0.
\end{equation}

The critical value is
\begin{equation}
\beta_c=\left(\frac{4}{27}\right)^{1/3}.
\end{equation}

At this point, the corresponding critical radius is given by $x_c = 2/3$, where the two real roots coincide.

The existence of horizons is controlled by the discriminant of the cubic equation. At $\beta=\beta_c$, two real roots merge, signaling a saddle-node bifurcation and the disappearance of the outer horizon branch.

As shown in Fig.~\ref{fig:horizon-transition}, the inner and outer horizon branches merge at the critical point $(\beta_c,x_c)$, producing a saddle-node transition beyond which no horizon solution exists and the spacetime transitions to a horizonless configuration.

\begin{figure}[H]
\centering
\includegraphics[width=0.82\textwidth]{tig_horizon_transition_publication.png}
\caption{
Publication-style visualization of the TIG horizon transition compared with the Schwarzschild reference. The inner and outer horizon branches merge at the critical point $(\beta_c,x_c)$, producing a saddle-node transition beyond which no horizon solution exists.
}
\label{fig:horizon-transition}
\end{figure}

\section{Photon Sphere}

The photon sphere satisfies
\begin{equation}
rF'(r)-2F(r)=0.
\end{equation}

Near the critical regime, deviations in $F(r)$ shift the photon sphere and may alter observable shadow properties.

\section{Echo Physics}

The echo delay is estimated as
\begin{equation}
\Delta t_{\mathrm{echo}} \simeq 2\int \frac{dr}{F(r)}.
\end{equation}

Near $\beta_c$,
\begin{equation}
\Delta t_{\mathrm{echo}}\rightarrow\infty .
\end{equation}

This indicates the formation of an effectively extended optical cavity and is analogous to critical slowing down.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{tig_echo_delay_prediction.png}
\caption{
Echo-delay scaling near $\beta_c$. The divergence indicates an extended optical cavity in the near-critical regime.
}
\label{fig:echo-delay}
\end{figure}

\section{Quantitative Prediction}

The horizon equation is
\begin{equation}
f(x,\beta)=x^3-x^2+\beta^3=0 .
\end{equation}

The critical point is
\begin{equation}
x_c=\frac{2}{3},
\qquad
\beta_c=\left(\frac{4}{27}\right)^{1/3}.
\end{equation}

We expand around criticality by writing
\begin{equation}
x=x_c+\delta x,
\qquad
\beta=\beta_c-\delta\beta ,
\end{equation}
with $\delta\beta>0$.

A Taylor expansion gives
\begin{equation}
0 \approx
\frac{1}{2}f_{xx}(x_c,\beta_c)(\delta x)^2
-
f_\beta(x_c,\beta_c)\delta\beta .
\end{equation}

Since
\begin{equation}
f_{xx}(x_c,\beta_c)=2,
\qquad
f_\beta(x_c,\beta_c)=3\beta_c^2,
\end{equation}
we obtain
\begin{equation}
(\delta x)^2 \approx 3\beta_c^2\delta\beta .
\end{equation}

Therefore,
\begin{equation}
x_\pm-x_c
\approx
\pm \sqrt{3}\,\beta_c(\beta_c-\beta)^{1/2}.
\end{equation}

This square-root behavior is a universal feature of saddle-node bifurcations and is independent of the specific details of the underlying model.

\section{Conclusion}

We have demonstrated that quadratic $f(R)$ gravity admits a structurally controlled critical transition in horizon formation.

\clearpage

\nocite{*}
\bibliographystyle{unsrt}
\bibliography{references}

\end{document}


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
