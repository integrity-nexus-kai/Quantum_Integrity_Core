# Linear Perturbation Roadmap  
## Topological Integrity Gravity (TIG)

---

## 🇩🇪 Deutsche Version

### 1. Ziel

Dieses Dokument definiert den nächsten mathematischen Schritt zur Stabilitätsprüfung der TIG-Schwarze-Loch-Lösung.

Ziel ist nicht, die vollständige Störungsrechnung bereits durchzuführen, sondern den exakten Weg dahin festzulegen.

---

## 2. Ausgangsmetrik

Die Hintergrundmetrik lautet:

\[
ds^2 =
-A(r)dt^2
+
\frac{dr^2}{A(r)}
+
r^2 d\Omega^2
\]

mit:

\[
A(r)
=
1-
\frac{2GM r^2}{r^3+r_0^3}
\]

---

## 3. Störungsansatz

Wir perturbieren die Metrik:

\[
g_{\mu\nu}
\rightarrow
g_{\mu\nu}
+
h_{\mu\nu}
\]

wobei:

\[
|h_{\mu\nu}| \ll |g_{\mu\nu}|
\]

---

## 4. Zerlegung der Störungen

Die Störungen werden in sphärische Harmonische zerlegt:

\[
h_{\mu\nu}(t,r,\theta,\phi)
=
\sum_{\ell,m}
h_{\mu\nu}^{\ell m}(t,r)
Y_{\ell m}(\theta,\phi)
\]

---

## 5. Paritätssektoren

Wie in Schwarzschild-Stabilitätsanalysen trennt man:

### Axiale Störungen

Odd parity:

\[
(-1)^{\ell+1}
\]

### Polare Störungen

Even parity:

\[
(-1)^\ell
\]

---

## 6. Master-Gleichung

Ziel ist es, eine Master-Gleichung der Form zu erhalten:

\[
\frac{d^2\Psi}{dr_*^2}
+
\left[
\omega^2
-
V_{\mathrm{eff}}(r)
\right]\Psi
=0
\]

---

## 7. Tortoise-Koordinate

Die Tortoise-Koordinate ist definiert durch:

\[
\frac{dr_*}{dr}
=
\frac{1}{A(r)}
\]

Sie bildet den Außenhorizont auf:

\[
r_* \rightarrow -\infty
\]

ab.

---

## 8. Effektives Potential

Für TIG muss bestimmt werden:

\[
V_{\mathrm{eff}}^{\mathrm{TIG}}(r)
\]

und mit Schwarzschild verglichen werden:

\[
V_{\mathrm{eff}}^{\mathrm{Schw}}(r)
\]

---

## 9. Stabilitätsbedingung

Eine lineare Mode ist stabil, wenn:

\[
\omega^2 > 0
\]

und keine wachsenden Moden existieren:

\[
\mathrm{Im}(\omega) < 0
\]

---

## 10. Zusätzlicher skalarer Modus

Da TIG im \(R^2\)-Grenzfall einen skalaren Modus besitzt, muss zusätzlich betrachtet werden:

\[
\delta R
\]

mit:

\[
(\Box - m^2)\delta R = 0
\]

im Vakuum.

---

## 11. Gekoppelte Störungen

Das vollständige System kann daher enthalten:

\[
h_{\mu\nu}
\]

und:

\[
\delta R
\]

als gekoppelte Freiheitsgrade.

---

## 12. Aufgabenliste

Die vollständige Analyse erfordert:

1. Hintergrundkrümmung berechnen  
2. linearisierte Feldgleichungen aufstellen  
3. axiale und polare Sektoren trennen  
4. Master-Variable definieren  
5. effektives Potential berechnen  
6. Randbedingungen setzen  
7. Quasinormalmoden bestimmen  
8. Stabilitätskriterium prüfen  

---

## 13. Randbedingungen

Für Quasinormalmoden gilt:

### Am Horizont

\[
\Psi \sim e^{-i\omega r_*}
\]

### Im Unendlichen

\[
\Psi \sim e^{+i\omega r_*}
\]

---

## 14. Vergleich mit GR

Wenn:

\[
r_0 \rightarrow 0
\]

muss gelten:

\[
V_{\mathrm{eff}}^{\mathrm{TIG}}
\rightarrow
V_{\mathrm{eff}}^{\mathrm{Schw}}
\]

Dies ist eine notwendige Konsistenzbedingung.

---

## 15. Erwartete TIG-Abweichungen

TIG kann Abweichungen erzeugen durch:

- modifizierte Kernstruktur  
- inneren Horizont  
- zusätzlichen skalaren Modus  
- geänderte Quasinormalmoden  
- mögliche Echo-Strukturen  

---

## 16. Minimaler nächster Rechenschritt

Der nächste konkrete mathematische Schritt ist:

\[
A'(r),\ A''(r)
\]

und daraus:

\[
V_{\mathrm{eff}}(r)
\]

für axiale Störungen herzuleiten.

---

## 17. Fazit

Die lineare Stabilität ist noch nicht bewiesen.

Dieses Dokument definiert jedoch den exakten Weg:

\[
A(r)
\rightarrow
V_{\mathrm{eff}}(r)
\rightarrow
\omega_n
\rightarrow
\text{Stabilität}
\]

---

## 🇬🇧 English Version

### 1. Objective

This document defines the next mathematical step for testing the stability of the TIG black-hole solution.

It does not yet perform the full perturbation calculation, but defines the exact roadmap.

---

## 2. Background Metric

\[
ds^2 =
-A(r)dt^2
+
\frac{dr^2}{A(r)}
+
r^2 d\Omega^2
\]

with:

\[
A(r)
=
1-
\frac{2GM r^2}{r^3+r_0^3}
\]

---

## 3. Perturbation Ansatz

\[
g_{\mu\nu}
\rightarrow
g_{\mu\nu}
+
h_{\mu\nu}
\]

with:

\[
|h_{\mu\nu}| \ll |g_{\mu\nu}|
\]

---

## 4. Harmonic Decomposition

\[
h_{\mu\nu}(t,r,\theta,\phi)
=
\sum_{\ell,m}
h_{\mu\nu}^{\ell m}(t,r)
Y_{\ell m}(\theta,\phi)
\]

---

## 5. Parity Sectors

Axial perturbations:

\[
(-1)^{\ell+1}
\]

Polar perturbations:

\[
(-1)^\ell
\]

---

## 6. Master Equation

The goal is to obtain:

\[
\frac{d^2\Psi}{dr_*^2}
+
\left[
\omega^2
-
V_{\mathrm{eff}}(r)
\right]\Psi
=0
\]

---

## 7. Tortoise Coordinate

\[
\frac{dr_*}{dr}
=
\frac{1}{A(r)}
\]

---

## 8. Effective Potential

One must compute:

\[
V_{\mathrm{eff}}^{\mathrm{TIG}}(r)
\]

and compare with:

\[
V_{\mathrm{eff}}^{\mathrm{Schw}}(r)
\]

---

## 9. Stability Criterion

Stable modes require:

\[
\omega^2 > 0
\]

and no growing modes:

\[
\mathrm{Im}(\omega)<0
\]

---

## 10. Scalar Mode

TIG contains a scalar curvature mode:

\[
(\Box - m^2)\delta R = 0
\]

in vacuum.

---

## 11. Coupled Perturbations

The full system may include:

\[
h_{\mu\nu}
\]

and:

\[
\delta R
\]

as coupled degrees of freedom.

---

## 12. Required Tasks

1. compute background curvature  
2. derive linearized field equations  
3. separate parity sectors  
4. define master variables  
5. compute effective potential  
6. impose boundary conditions  
7. compute quasinormal modes  
8. test stability  

---

## 13. Boundary Conditions

At the horizon:

\[
\Psi \sim e^{-i\omega r_*}
\]

At infinity:

\[
\Psi \sim e^{+i\omega r_*}
\]

---

## 14. GR Limit

For:

\[
r_0 \rightarrow 0
\]

one must recover:

\[
V_{\mathrm{eff}}^{\mathrm{TIG}}
\rightarrow
V_{\mathrm{eff}}^{\mathrm{Schw}}
\]

---

## 15. Expected TIG Deviations

Possible deviations include:

- modified core structure  
- inner horizon  
- scalar mode  
- shifted quasinormal modes  
- echo-like structures  

---

## 16. Minimal Next Step

The next concrete calculation is to derive:

\[
A'(r),\ A''(r)
\]

and then:

\[
V_{\mathrm{eff}}(r)
\]

for axial perturbations.

---

## 17. Conclusion

Linear stability has not yet been proven.

The roadmap is:

\[
A(r)
\rightarrow
V_{\mathrm{eff}}(r)
\rightarrow
\omega_n
\rightarrow
\text{stability}
\]
