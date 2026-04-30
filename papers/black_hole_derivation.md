# Black Hole Derivation  
## Topological Integrity Gravity (TIG)

---

## 🇩🇪 Deutsche Version

### 1. Ziel

Dieses Dokument leitet die effektive reguläre Schwarze-Loch-Metrik im TIG-Modell her:

\[
A(r) = 1 - \frac{2GM r^2}{r^3 + r_0^3}
\]

Ziel ist zu zeigen, wie diese Form aus begrenzter Krümmung und einer effektiven Integritätsskala entsteht.

---

### 2. Metrischer Ansatz

Wir beginnen mit einer statisch-sphärisch symmetrischen Raumzeit:

\[
ds^2 = -A(r)dt^2 + \frac{dr^2}{A(r)} + r^2 d\Omega^2
\]

Die Metrikfunktion wird über eine effektive Massenfunktion geschrieben:

\[
A(r) = 1 - \frac{2G M(r)}{r}
\]

---

### 3. Physikalische Anforderungen

Die Massenfunktion muss zwei Bedingungen erfüllen.

#### 3.1 Schwarzschild-Grenzfall

Für große Abstände gilt:

\[
M(r) \to M \quad \text{für} \quad r \gg r_0
\]

Damit folgt:

\[
A(r) \to 1 - \frac{2GM}{r}
\]

---

#### 3.2 Regulärer Kern

Nahe des Ursprungs muss die Geometrie endlich bleiben.  
Dafür ist erforderlich:

\[
M(r) \sim r^3 \quad \text{für} \quad r \to 0
\]

Dann bleibt:

\[
A(r) = 1 - \frac{2G M(r)}{r}
\]

endlich und verhält sich wie:

\[
A(r) \sim 1 - C r^2
\]

Dies entspricht einer de-Sitter-artigen Kernstruktur.

---

### 4. Minimale interpolierende Massenfunktion

Die einfachste glatte Funktion, die beide Grenzfälle erfüllt, ist:

\[
M(r) = M \frac{r^3}{r^3 + r_0^3}
\]

---

### 5. Resultierende Metrikfunktion

Einsetzen in:

\[
A(r) = 1 - \frac{2G M(r)}{r}
\]

ergibt:

\[
A(r) = 1 - \frac{2GM r^2}{r^3 + r_0^3}
\]

---

### 6. Verhalten im Kernbereich

Für \( r \to 0 \):

\[
A(r) \approx 1 - \frac{2GM}{r_0^3} r^2
\]

Vergleich mit:

\[
A(r) = 1 - \frac{\Lambda_{\mathrm{eff}}}{3}r^2
\]

liefert:

\[
\Lambda_{\mathrm{eff}} = \frac{6GM}{r_0^3}
\]

---

### 7. Interpretation von \( r_0 \)

Der Parameter \( r_0 \) ist die Integritätsskala des TIG-Modells.

---

### 8. Status der Herleitung

Diese Herleitung ist effektiv und basiert auf physikalischen Anforderungen, nicht auf einer vollständigen Variation der TIG-Wirkung.

---

## 🇬🇧 English Version

### 1. Objective

This document derives the effective regular black hole metric used in TIG:

\[
A(r) = 1 - \frac{2GM r^2}{r^3 + r_0^3}
\]

---

### 2. Metric Ansatz

We start with a static, spherically symmetric spacetime:

\[
ds^2 = -A(r)dt^2 + \frac{dr^2}{A(r)} + r^2 d\Omega^2
\]

---

### 3. Physical Requirements

The mass function must satisfy:

- Schwarzschild behavior at large radius  
- regular core at small radius  

---

### 4. Interpolating Mass Function

\[
M(r) = M \frac{r^3}{r^3 + r_0^3}
\]

---

### 5. Resulting Metric

\[
A(r) = 1 - \frac{2GM r^2}{r^3 + r_0^3}
\]

---

### 6. Near-Core Limit

\[
A(r) \approx 1 - \frac{2GM}{r_0^3} r^2
\]

---

### 7. Interpretation

The parameter \( r_0 \) represents the integrity scale of the TIG framework.

---

### 8. Status

This is an effective derivation based on physical constraints.
