# TIG Friedmann Equation Derivation  
## (Deutsch / English)

---

## 1. Action / Wirkung

**Deutsch:**
Wir starten mit der modifizierten Wirkung:

$$
S = \int d^4x \sqrt{-g} \left[ \frac{1}{16\pi}(R - 2\Lambda) + \alpha R^2 \right]
$$

**English:**
We start from the modified gravitational action:

$$
S = \int d^4x \sqrt{-g} \left[ \frac{1}{16\pi}(R - 2\Lambda) + \alpha R^2 \right]
$$

---

## 2. f(R)-Form

**Deutsch:**
Die Theorie ist äquivalent zu:

$$
f(R) = R - 2\Lambda + \mu R^2
$$

mit:

$$
\mu = 16\pi\alpha
$$

**English:**
The theory is equivalent to:

$$
f(R) = R - 2\Lambda + \mu R^2
$$

with:

$$
\mu = 16\pi\alpha
$$

---

## 3. Feldgleichungen / Field Equations

$$
f'(R) R_{\mu\nu}
- \frac{1}{2} f(R) g_{\mu\nu}
+ (g_{\mu\nu}\Box - \nabla_\mu \nabla_\nu) f'(R)
= 8\pi T_{\mu\nu}
$$

---

## 4. Ableitung / Derivative

$$
f'(R) = 1 + 2\mu R
$$

---

## 5. FLRW-Metrik

$$
ds^2 = -dt^2 + a(t)^2 d\vec{x}^2
$$

---

## 6. Ricci-Skalar

$$
R = 6(\dot{H} + 2H^2)
$$

---

## 7. Friedmann-Gleichung (00-Komponente)

$$
3 f'(R) H^2 = 8\pi \rho + \frac{1}{2}(f'(R)R - f(R)) - 3H \dot{f}'(R)
$$

---

## 8. Terme einsetzen

$$
f'(R) = 1 + 2\mu R
$$

$$
f'(R)R - f(R) = \mu R^2
$$

$$
\dot{f}'(R) = 2\mu \dot{R}
$$

---

## 9. Ergebnis

$$
3(1+2\mu R)H^2
=
8\pi \rho
+
\frac{\mu}{2}R^2
-
3\mu H \dot{R}
+
\Lambda
$$

---

## 10. Nach H² auflösen

$$
H^2 =
\frac{
8\pi \rho + \Lambda + \frac{\mu}{2}R^2 - 3\mu H \dot{R}
}{
3(1 + 2\mu R)
}
$$

---

## 11. TIG-Form einsetzen

$$
H^2 =
\frac{
8\pi \rho + \Lambda + 8\pi\alpha R^2 - 48\pi\alpha H \dot{R}
}{
3(1 + 32\pi\alpha R)
}
$$

---

# 🔥 Final Result / Endergebnis

**Deutsch:**
Konkrete TIG-Friedmann-Gleichung.

**English:**
Explicit TIG-modified Friedmann equation.

---

## GR Grenzfall / GR limit

$$
\alpha \to 0 \Rightarrow H^2 = \frac{8\pi}{3}\rho + \frac{\Lambda}{3}
$$

---

## Bedeutung / Interpretation

**Deutsch:**
- Keine Black Box mehr  
- Vollständig berechenbar  
- Stärkste Effekte bei hoher Krümmung  

**English:**
- No longer symbolic  
- Fully computable  
- Strongest in high-curvature regimes
