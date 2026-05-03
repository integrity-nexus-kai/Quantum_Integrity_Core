# Integrity Tensor Derivation  
## Topological Integrity Gravity (TIG)

---

## 🇩🇪 Deutsche Version

### 1. Ziel

Dieses Dokument leitet den effektiven Integritäts-Tensor \( \mathcal{I}_{\mu\nu} \) im Niedrigenergie-Grenzfall her.

Ziel ist es, die TIG-Feldgleichung

\[
G_{\mu\nu} + \mathcal{I}_{\mu\nu} = 8\pi G T_{\mu\nu}
\]

mathematisch kontrolliert aus einer effektiven Krümmungswirkung zu erhalten.

---

### 2. Effektive Wirkung

Im Low-Energy-Limit der spektralen TIG-Wirkung betrachten wir die skalare Krümmungstrunkierung:

\[
S_{\mathrm{eff}} =
\frac{1}{16\pi G}
\int d^4x \sqrt{-g}
\left(
R + \frac{\alpha}{\Lambda^2} R^2
\right)
+ S_m
\]

Dabei ist:

- \( \Lambda \): fundamentale Energieskala
- \( \alpha \): dimensionsloser Kopplungsparameter
- \( S_m \): Materiewirkung

---

### 3. Allgemeine \( f(R) \)-Form

Wir schreiben:

\[
F(R) = R + \frac{\alpha}{\Lambda^2}R^2
\]

Dann gilt:

\[
F_R \equiv \frac{dF}{dR}
= 1 + \frac{2\alpha}{\Lambda^2}R
\]

---

### 4. Feldgleichung einer \( f(R) \)-Theorie

Die Variation nach der Metrik liefert:

\[
F_R R_{\mu\nu}
-
\frac{1}{2}F(R)g_{\mu\nu}
+
\left(
g_{\mu\nu}\Box
-
\nabla_\mu\nabla_\nu
\right)F_R
=
8\pi G T_{\mu\nu}
\]

---

### 5. Umformung in TIG-Form

Wir schreiben die Gleichung als:

\[
G_{\mu\nu} + \mathcal{I}_{\mu\nu}
=
8\pi G T_{\mu\nu}
\]

mit:

\[
G_{\mu\nu}
=
R_{\mu\nu}
-
\frac{1}{2}Rg_{\mu\nu}
\]

Daraus folgt allgemein:

\[
\mathcal{I}_{\mu\nu}
=
(F_R - 1)R_{\mu\nu}
-
\frac{1}{2}(F-R)g_{\mu\nu}
+
\left(
g_{\mu\nu}\Box
-
\nabla_\mu\nabla_\nu
\right)F_R
\]

---

### 6. Explizite Form für \( R^2 \)-TIG

Einsetzen von:

\[
F(R)=R+\frac{\alpha}{\Lambda^2}R^2
\]

ergibt:

\[
F_R - 1 = \frac{2\alpha}{\Lambda^2}R
\]

und:

\[
F-R = \frac{\alpha}{\Lambda^2}R^2
\]

Damit folgt:

\[
\mathcal{I}_{\mu\nu}
=
\frac{2\alpha}{\Lambda^2}R R_{\mu\nu}
-
\frac{\alpha}{2\Lambda^2}R^2 g_{\mu\nu}
+
\frac{2\alpha}{\Lambda^2}
\left(
g_{\mu\nu}\Box R
-
\nabla_\mu\nabla_\nu R
\right)
\]

---

### 7. Interpretation

Der Integritäts-Tensor enthält drei Typen von Termen:

#### 7.1 Krümmungs-Rückkopplung

\[
R R_{\mu\nu}
\]

Dieser Term koppelt die lokale Krümmung an die Ricci-Geometrie.

#### 7.2 Energieartige Krümmungskorrektur

\[
R^2 g_{\mu\nu}
\]

Dieser Term wirkt wie ein effektiver geometrischer Energiedichte-Beitrag.

#### 7.3 Dynamische Glättung

\[
g_{\mu\nu}\Box R
-
\nabla_\mu\nabla_\nu R
\]

Dieser Term beschreibt die räumlich-zeitliche Glättung von Krümmungsgradienten.

---

### 8. Niedrigenergie-Grenzfall

Für:

\[
R \ll \Lambda^2
\]

gilt:

\[
\mathcal{I}_{\mu\nu} \to 0
\]

und damit:

\[
G_{\mu\nu} = 8\pi G T_{\mu\nu}
\]

Die Allgemeine Relativitätstheorie wird reproduziert.

---

### 9. Hochkrümmungs-Regime

Für große Krümmung wird:

\[
\mathcal{I}_{\mu\nu} \neq 0
\]

Der Tensor wirkt dann als nichtlinearer Rückkopplungsmechanismus gegen divergente Krümmungsentwicklung.

---

### 10. Status der Herleitung

Diese Ableitung ist exakt innerhalb der \( R^2 \)-Trunkierung.

Der vollständige spektrale TIG-Ansatz kann zusätzliche Invarianten enthalten:

\[
R_{\mu\nu}R^{\mu\nu}
\]

\[
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
\]

Diese müssen in einer erweiterten Version separat behandelt werden.

---

## 🇬🇧 English Version

### 1. Objective

This document derives the effective integrity tensor \( \mathcal{I}_{\mu\nu} \) in the low-energy limit.

The goal is to obtain the TIG field equation

\[
G_{\mu\nu} + \mathcal{I}_{\mu\nu} = 8\pi G T_{\mu\nu}
\]

from a controlled effective curvature action.

---

### 2. Effective Action

In the low-energy limit of the spectral TIG action, we consider the scalar-curvature truncation:

\[
S_{\mathrm{eff}} =
\frac{1}{16\pi G}
\int d^4x \sqrt{-g}
\left(
R + \frac{\alpha}{\Lambda^2} R^2
\right)
+ S_m
\]

where:

- \( \Lambda \): fundamental energy scale
- \( \alpha \): dimensionless coupling parameter
- \( S_m \): matter action

---

### 3. General \( f(R) \) Form

Define:

\[
F(R) = R + \frac{\alpha}{\Lambda^2}R^2
\]

Then:

\[
F_R \equiv \frac{dF}{dR}
= 1 + \frac{2\alpha}{\Lambda^2}R
\]

---

### 4. Field Equation of \( f(R) \) Gravity

Metric variation yields:

\[
F_R R_{\mu\nu}
-
\frac{1}{2}F(R)g_{\mu\nu}
+
\left(
g_{\mu\nu}\Box
-
\nabla_\mu\nabla_\nu
\right)F_R
=
8\pi G T_{\mu\nu}
\]

---

### 5. Rewriting in TIG Form

We rewrite the equation as:

\[
G_{\mu\nu} + \mathcal{I}_{\mu\nu}
=
8\pi G T_{\mu\nu}
\]

with:

\[
G_{\mu\nu}
=
R_{\mu\nu}
-
\frac{1}{2}Rg_{\mu\nu}
\]

This gives:

\[
\mathcal{I}_{\mu\nu}
=
(F_R - 1)R_{\mu\nu}
-
\frac{1}{2}(F-R)g_{\mu\nu}
+
\left(
g_{\mu\nu}\Box
-
\nabla_\mu\nabla_\nu
\right)F_R
\]

---

### 6. Explicit Form for \( R^2 \)-TIG

Substituting:

\[
F(R)=R+\frac{\alpha}{\Lambda^2}R^2
\]

gives:

\[
F_R - 1 = \frac{2\alpha}{\Lambda^2}R
\]

and:

\[
F-R = \frac{\alpha}{\Lambda^2}R^2
\]

Therefore:

\[
\mathcal{I}_{\mu\nu}
=
\frac{2\alpha}{\Lambda^2}R R_{\mu\nu}
-
\frac{\alpha}{2\Lambda^2}R^2 g_{\mu\nu}
+
\frac{2\alpha}{\Lambda^2}
\left(
g_{\mu\nu}\Box R
-
\nabla_\mu\nabla_\nu R
\right)
\]

---

### 7. Interpretation

The integrity tensor contains three types of contributions:

#### 7.1 Curvature Feedback

\[
R R_{\mu\nu}
\]

This term couples local scalar curvature to Ricci geometry.

#### 7.2 Curvature Energy Correction

\[
R^2 g_{\mu\nu}
\]

This behaves like an effective geometric energy-density contribution.

#### 7.3 Dynamical Smoothing

\[
g_{\mu\nu}\Box R
-
\nabla_\mu\nabla_\nu R
\]

This term smooths curvature gradients dynamically.

---

### 8. Low-Energy Limit

For:

\[
R \ll \Lambda^2
\]

we have:

\[
\mathcal{I}_{\mu\nu} \to 0
\]

and therefore:

\[
G_{\mu\nu} = 8\pi G T_{\mu\nu}
\]

General Relativity is recovered.

---

### 9. High-Curvature Regime

For large curvature:

\[
\mathcal{I}_{\mu\nu} \neq 0
\]

The tensor acts as a nonlinear feedback mechanism against divergent curvature evolution.

---

### 10. Status of the Derivation

This derivation is exact within the \( R^2 \)-truncation.

The full spectral TIG framework may contain additional invariants:

\[
R_{\mu\nu}R^{\mu\nu}
\]

\[
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
\]

These must be treated separately in an extended version.
