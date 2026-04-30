# Spectral Derivation  
## From Dirac Geometry to TIG Effective Gravity

---

## 🇩🇪 Deutsche Version

### 1. Ziel

Dieses Dokument leitet die effektive gravitative TIG-Wirkung aus der spektralen Struktur des Dirac-Operators ab.

Ziel ist es zu zeigen, wie aus

\[
S_{\mathrm{spec}} = \mathrm{Tr}\, f(D/\Lambda)
\]

im Niedrigenergie-Grenzfall eine Wirkung der Form

\[
S_{\mathrm{eff}}
=
\frac{1}{16\pi G}
\int d^4x \sqrt{-g}
\left(
R + \frac{\alpha}{\Lambda^2}R^2 + \cdots
\right)
\]

entsteht.

---

### 2. Spektrales Triple

Die fundamentale geometrische Struktur ist ein Spektraltriple:

\[
(\mathcal{A}, \mathcal{H}, D)
\]

mit:

- \( \mathcal{A} \): Algebra der Observablen
- \( \mathcal{H} \): Hilbertraum
- \( D \): Dirac-Operator

Die Geometrie wird nicht primär durch Punkte beschrieben, sondern durch das Spektrum von \(D\).

---

### 3. Dirac-Operator

Für eine glatte Spin-Mannigfaltigkeit gilt:

\[
D = i\gamma^\mu \nabla_\mu
\]

wobei:

- \( \gamma^\mu \): Clifford-/Dirac-Matrizen
- \( \nabla_\mu \): kovariante Ableitung inklusive Spinverbindung

---

### 4. Lichnerowicz-Formel

Ein zentrales Resultat lautet:

\[
D^2 =
-\nabla^\mu \nabla_\mu
+
\frac{1}{4}R
\]

Diese Formel zeigt, dass das Quadrat des Dirac-Operators direkt die skalare Krümmung enthält.

Damit gilt strukturell:

\[
D^2 \sim -\Box + \frac{1}{4}R
\]

Die Lichnerowicz-Formel ist der zentrale mathematische Übergang von Spektrum zu Geometrie.

---

### 5. Spektrale Wirkung

Die spektrale Wirkung lautet:

\[
S_{\mathrm{spec}}
=
\mathrm{Tr}\, f\left(\frac{D}{\Lambda}\right)
\]

wobei:

- \(f\): Cutoff- oder Testfunktion
- \(\Lambda\): fundamentale Energieskala

---

### 6. Heat-Kernel-Expansion

Für große \(\Lambda\) kann die spektrale Wirkung über die Heat-Kernel-Expansion entwickelt werden:

\[
\mathrm{Tr}\, f(D/\Lambda)
\sim
\sum_{n}
f_n \Lambda^{4-n} a_n(D^2)
\]

Dabei sind:

- \(f_n\): Momente der Funktion \(f\)
- \(a_n(D^2)\): Seeley-DeWitt-Koeffizienten

---

### 7. Erste geometrische Terme

Die ersten Terme liefern:

\[
a_0 \sim \int d^4x \sqrt{-g}
\]

\[
a_2 \sim \int d^4x \sqrt{-g}\, R
\]

\[
a_4 \sim \int d^4x \sqrt{-g}
\left(
R^2,
R_{\mu\nu}R^{\mu\nu},
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma},
\Box R
\right)
\]

---

### 8. Niedrigenergie-Trunkierung

Für die erste TIG-Näherung behalten wir die skalaren Terme:

\[
S_{\mathrm{eff}}
=
\frac{1}{16\pi G}
\int d^4x \sqrt{-g}
\left(
R + \frac{\alpha}{\Lambda^2}R^2
\right)
+ S_m
\]

Dies ist keine vollständige Spektralwirkung, sondern eine kontrollierte \(R^2\)-Trunkierung.

---

### 9. Rolle des Integritätsfunktionals

TIG ergänzt die spektrale Wirkung durch:

\[
\mathcal{I}[D]
=
\mathrm{Tr}\,\log\left(1+\frac{D^2}{\Lambda^2}\right)
\]

Für kleine \(D^2/\Lambda^2\) gilt:

\[
\log\left(1+\frac{D^2}{\Lambda^2}\right)
=
\frac{D^2}{\Lambda^2}
-
\frac{D^4}{2\Lambda^4}
+
\cdots
\]

Da \(D^2\) Krümmungsterme enthält, erzeugt diese Expansion zusätzliche geometrische Korrekturen.

---

### 10. Effektive TIG-Wirkung

Damit ergibt sich im ersten effektiven Grenzfall:

\[
S_{\mathrm{TIG}}
=
\frac{1}{16\pi G}
\int d^4x \sqrt{-g}
\left(
R + \frac{\alpha}{\Lambda^2}R^2
\right)
+ S_m
+
\cdots
\]

Diese Wirkung bildet die Grundlage für:

- Integritäts-Tensor
- Trace Equation
- skalaren Modus
- Stabilitätsanalyse
- Black-Hole-Regularisierung
- kosmologische Korrekturen

---

### 11. Status der Ableitung

Diese Ableitung zeigt:

\[
\mathrm{Spektrum}(D)
\rightarrow
D^2
\rightarrow
R
\rightarrow
R^2\text{-Korrekturen}
\rightarrow
\mathrm{TIG}_{\mathrm{eff}}
\]

Sie ist kontrolliert im Niedrigenergie- und Trunkierungsregime.

---

### 12. Offene Erweiterungen

Die vollständige spektrale Wirkung enthält weitere Terme:

\[
R_{\mu\nu}R^{\mu\nu}
\]

\[
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
\]

sowie mögliche Beiträge aus:

- Torsion
- Eichfeldern
- Fermionen
- interner Geometrie

Diese müssen in einer erweiterten TIG-Version systematisch behandelt werden.

---

## 🇬🇧 English Version

### 1. Objective

This document derives the effective gravitational TIG action from the spectral structure of the Dirac operator.

The goal is to show how

\[
S_{\mathrm{spec}} = \mathrm{Tr}\, f(D/\Lambda)
\]

leads, in the low-energy limit, to an effective action of the form

\[
S_{\mathrm{eff}}
=
\frac{1}{16\pi G}
\int d^4x \sqrt{-g}
\left(
R + \frac{\alpha}{\Lambda^2}R^2 + \cdots
\right)
\]

---

### 2. Spectral Triple

The fundamental geometric structure is a spectral triple:

\[
(\mathcal{A}, \mathcal{H}, D)
\]

where:

- \( \mathcal{A} \): algebra of observables
- \( \mathcal{H} \): Hilbert space
- \( D \): Dirac operator

Geometry is encoded spectrally rather than primarily pointwise.

---

### 3. Dirac Operator

On a smooth spin manifold:

\[
D = i\gamma^\mu \nabla_\mu
\]

where:

- \( \gamma^\mu \): Clifford / Dirac matrices
- \( \nabla_\mu \): covariant derivative including spin connection

---

### 4. Lichnerowicz Formula

A central result is:

\[
D^2 =
-\nabla^\mu \nabla_\mu
+
\frac{1}{4}R
\]

This shows that the square of the Dirac operator directly contains scalar curvature.

Structurally:

\[
D^2 \sim -\Box + \frac{1}{4}R
\]

The Lichnerowicz formula is the key mathematical bridge from spectrum to geometry.

---

### 5. Spectral Action

The spectral action is:

\[
S_{\mathrm{spec}}
=
\mathrm{Tr}\, f\left(\frac{D}{\Lambda}\right)
\]

where:

- \(f\): cutoff or test function
- \(\Lambda\): fundamental energy scale

---

### 6. Heat-Kernel Expansion

For large \(\Lambda\), the spectral action admits an asymptotic expansion:

\[
\mathrm{Tr}\, f(D/\Lambda)
\sim
\sum_{n}
f_n \Lambda^{4-n} a_n(D^2)
\]

where:

- \(f_n\): moments of \(f\)
- \(a_n(D^2)\): Seeley-DeWitt coefficients

---

### 7. First Geometric Terms

The first terms yield:

\[
a_0 \sim \int d^4x \sqrt{-g}
\]

\[
a_2 \sim \int d^4x \sqrt{-g}\, R
\]

\[
a_4 \sim \int d^4x \sqrt{-g}
\left(
R^2,
R_{\mu\nu}R^{\mu\nu},
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma},
\Box R
\right)
\]

---

### 8. Low-Energy Truncation

For the first TIG approximation, we retain the scalar curvature terms:

\[
S_{\mathrm{eff}}
=
\frac{1}{16\pi G}
\int d^4x \sqrt{-g}
\left(
R + \frac{\alpha}{\Lambda^2}R^2
\right)
+ S_m
\]

This is not the full spectral action, but a controlled \(R^2\)-truncation.

---

### 9. Role of the Integrity Functional

TIG extends the spectral action by:

\[
\mathcal{I}[D]
=
\mathrm{Tr}\,\log\left(1+\frac{D^2}{\Lambda^2}\right)
\]

For small \(D^2/\Lambda^2\):

\[
\log\left(1+\frac{D^2}{\Lambda^2}\right)
=
\frac{D^2}{\Lambda^2}
-
\frac{D^4}{2\Lambda^4}
+
\cdots
\]

Since \(D^2\) contains curvature, this expansion generates additional geometric corrections.

---

### 10. Effective TIG Action

Thus, in the first effective limit:

\[
S_{\mathrm{TIG}}
=
\frac{1}{16\pi G}
\int d^4x \sqrt{-g}
\left(
R + \frac{\alpha}{\Lambda^2}R^2
\right)
+ S_m
+
\cdots
\]

This action underlies:

- integrity tensor
- trace equation
- scalar mode
- stability analysis
- black hole regularization
- cosmological corrections

---

### 11. Status of the Derivation

This derivation establishes:

\[
\mathrm{Spec}(D)
\rightarrow
D^2
\rightarrow
R
\rightarrow
R^2\text{-corrections}
\rightarrow
\mathrm{TIG}_{\mathrm{eff}}
\]

It is controlled in the low-energy and truncation regime.

---

### 12. Open Extensions

The full spectral action contains additional terms:

\[
R_{\mu\nu}R^{\mu\nu}
\]

\[
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
\]

and possible contributions from:

- torsion
- gauge fields
- fermions
- internal geometry

These must be treated systematically in an extended TIG version.
