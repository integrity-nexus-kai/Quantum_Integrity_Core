# Curvature Check  
## Topological Integrity Gravity (TIG)

---

## 🇩🇪 Deutsche Version

### 1. Ziel

Dieses Dokument überprüft, ob die TIG-Schwarze-Loch-Lösung tatsächlich frei von Singularitäten ist.

Die zentrale Frage lautet:

👉 Bleiben alle Krümmungsinvarianten für \( r \to 0 \) endlich?

---

### 2. Ausgangsmetrik

Die betrachtete Metrik lautet:

\[
ds^2 = -A(r)\,dt^2 + \frac{dr^2}{A(r)} + r^2 d\Omega^2
\]

mit:

\[
A(r) = 1 - \frac{2GM r^2}{r^3 + r_0^3}
\]

---

### 3. Relevante Invarianten

Zur Prüfung werden folgende Größen betrachtet:

#### Ricci-Skalar
\[
R
\]

#### Ricci-Tensor-Quadrat
\[
R_{\mu\nu}R^{\mu\nu}
\]

#### Kretschmann-Skalar
\[
K = R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}
\]

---

### 4. Verhalten für große Radien

Für \( r \gg r_0 \):

\[
A(r) \approx 1 - \frac{2GM}{r}
\]

👉 entspricht Schwarzschild

Daraus folgt:

- \( R \approx 0 \)  
- \( R_{\mu\nu}R^{\mu\nu} \approx 0 \)  
- \( K \sim \frac{1}{r^6} \to 0 \)

---

### 5. Verhalten nahe \( r = 0 \)

Für kleine Radien gilt:

\[
A(r) \approx 1 - \frac{2GM}{r_0^3} r^2
\]

Dies entspricht einer de-Sitter-Metrik.

---

### 6. Konsequenzen

Für eine de-Sitter-Struktur gilt:

- \( R = \text{konstant} \)
- \( R_{\mu\nu}R^{\mu\nu} = \text{konstant} \)
- \( K = \text{konstant} \)

👉 Es treten **keine Divergenzen** auf.

---

### 7. Vergleich mit Schwarzschild

| Größe | Schwarzschild | TIG |
|------|-------------|-----|
| \( R \) | 0 | endlich |
| \( K \) | \( \sim 1/r^6 \) → ∞ | endlich |
| Zentrum | Singularität | regulärer Kern |

---

### 8. Ergebnis

Die TIG-Metrik ist:

- vollständig regulär  
- frei von Krümmungssingularitäten  
- physikalisch konsistent  

---

### 9. Interpretation

Der Parameter \( r_0 \) wirkt als:

- geometrischer Regulator  
- minimale effektive Längenskala  
- Schutzmechanismus gegen Divergenzen  

---

## 🇬🇧 English Version

### 1. Objective

This document verifies whether the TIG black hole solution is truly free of singularities.

---

### 2. Metric

\[
ds^2 = -A(r)\,dt^2 + \frac{dr^2}{A(r)} + r^2 d\Omega^2
\]

\[
A(r) = 1 - \frac{2GM r^2}{r^3 + r_0^3}
\]

---

### 3. Invariants

We consider:

- Ricci scalar \( R \)  
- Ricci tensor squared  
- Kretschmann scalar  

---

### 4. Large Radius Limit

\[
A(r) \approx 1 - \frac{2GM}{r}
\]

---

### 5. Near-Core Limit

\[
A(r) \approx 1 - \frac{2GM}{r_0^3} r^2
\]

This corresponds to de Sitter geometry.

---

### 6. Result

All curvature invariants remain finite.

---

### 7. Conclusion

The TIG solution is free of curvature singularities.
