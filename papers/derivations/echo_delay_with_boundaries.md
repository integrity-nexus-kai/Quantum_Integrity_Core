# QIC — Echo-Laufzeit mit explizitem Randmodell

Version 1.0 · 2026-10-02 · QIC-04 · bedingte geometrische Rechnung / kein Nachweis physischer TIG-Echos.

Eingang main @ da326a4041054c01f2574d02312826870616670c. [Kernrechnung](quadratic_fr_and_horizon_checks.md) und [Quellenprüfung](../../research/wave3_source_review.md) gelten weiter. Keine Vakuumlösung der getesteten quadratischen metrischen \(f(R)\)-Wirkung.

## 1. Modell, Ränder und Uhr

\[
ds^2=-Fdt^2+dr^2/F+r^2d\Omega^2,\quad F=P/D,\quad
P=x^3-x^2+\beta^3,\quad D=x^3+\beta^3,\quad x=r/(2M),\quad\beta=r_c/(2M).
\]

Festes \(M>0\), \(G=c=1\), asymptotisch normiertes \(t\). Radiale Nullbahnen erfüllen innerhalb einer zusammenhängenden Region \(F>0\) \(dt=\pm dr/F\). **Zusätzlich vorgegeben:** innerer reflektierender Rand \(r_{\rm ref}=2Mx_{\rm ref}>0\), äußerer partiell reflektierender/transmittierender Streurand \(r_b=2Mx_b\). Beide reflektieren im untersuchten Frequenzband; der Außenrand ermöglicht Auskopplung. Nicht aus TIG hergeleitet.

Geometrische Rundlaufzeit:
\[
T_{\rm rt}=2\int_{r_{\rm ref}}^{r_b}\frac{dr}{F}
=4M\int_{x_{\rm ref}}^{x_b}\frac{D}{P}\,dx.
\]

Ein fester Außenbeobachter \(r_{\rm obs}>r_b\), mit endlichem positivem Grenzwert von \(F(r_{\rm obs})\), misst \(\Delta\tau_{\rm obs}=\sqrt{F(r_{\rm obs})}T_{\rm rt}\); gleiche führende Potenz. Echo-Sequenz erfordert zusätzlich Anregung/Streuung. Keine Amplitude, kein Spektrum, keine Detektierbarkeit bewiesen. Der Streurand ist nicht automatisch exakt die Photonensphäre. Dispersive Laufzeit/Reflexionsphase können zusätzliche Beiträge liefern.

Explizites **Testfeld**, nicht TIG-Gravitationsdynamik: minimal gekoppeltes masseloses Skalarfeld,
\[
(-\partial_t^2+\partial_{r_*}^2-V_\ell)\psi_\ell=0,\quad
dr_*/dr=1/F,\quad V_\ell=F[\ell(\ell+1)/r^2+F'/r].
\]
Ein idealer Dirichlet-Rand \(\psi_\ell(r_{\rm ref})=0\) reflektiert. Physische Entstehung, Anregung/Stabilität nicht bewiesen. Keine TIG-Gravitationsperturbationsgleichung.

[Cardoso/Franzin/Pani, 1602.07309v4](https://arxiv.org/html/1602.07309v4), §§III–V, Eq. (6): methodischer Vergleich mit anderer Geometrie, eigener Wellengleichung/Randbindung. Ihr Integral ist eine **einfache** Strecke; unser Faktor zwei folgt aus dem Rundlauf.

## 2. Oberhalb: horizontloser Engpass

\[
x_c=2/3,\quad\beta_c=(4/27)^{1/3},\quad D_0=4/9,\quad
\eta=\beta-\beta_c>0,\quad\delta=x-x_c.
\]
Exakt:
\[
P(x_c+\delta,\beta_c+\eta)=
\delta^2+\delta^3+3\beta_c^2\eta+3\beta_c\eta^2+\eta^3.
\]
Für \(\beta>\beta_c\) ist \(F>0\) für alle \(x>0\): \(P(x,\beta_c)=(x-x_c)^2(x+1/3)\ge0\) und die Zunahme von \(\beta^3\) positiv. Feste \(0<x_{\rm ref}<x_c<x_b\) durchqueren den ganzen Engpass. Mit \(s=\sqrt3\beta_c\sqrt\eta\):
\[
F\sim(\delta^2+s^2)/D_0,\quad
T_{\rm rt}\sim(4MD_0/s)[\arctan(\delta/s)]_{\delta_{\rm ref}}^{\delta_b}.
\]
Klammer \(\to\pi\), somit
\[
\boxed{T_{\rm rt}\sim\frac{16\pi M}{9\sqrt3\beta_c}
(\beta-\beta_c)^{-1/2}\quad(\beta\downarrow\beta_c,\ \beta>\beta_c).}
\]
Quotient der vollständigen Laufzeit und des führenden Terms \(\to1\). Für \(y=\delta/s\) ist lokal der skalierte Integrand durch \(C/(1+y^2)\) beschränkt; außerhalb bleibt die Laufzeit beschränkt. Dominierte Konvergenz liefert den Koeffizienten, **nicht** allein der Wurzelexponent. Koeffizient \(6.0939839981M\).

Fester Endpunkt bei \(x_c\): halber Engpass/halber Koeffizient. Beide festen Endpunkte streng auf derselben Seite: endlicher Grenzwert. Bewegliche Endpunkte ändern Grenzen und eventuell Skalierung. Kein randunabhängiger/universeller Echoexponent.

## 3. Unterhalb: Außenkavität

\[
\epsilon=\beta_c-\beta>0,\quad s=\sqrt3\beta_c\sqrt\epsilon,\quad
F\sim(\delta^2-s^2)/D_0,\quad x_\pm=x_c\pm s+O(\epsilon).
\]
Zurückkehrender Rundlauf für Außenbeobachter: statischer Außenbereich \(x>x_+\). Ein Integral durch den äußeren zukünftigen Horizont ist keine außen beobachtbare Rundlaufzeit; Cauchy-Hauptwert löst das kausale Problem nicht.

**Fester Außenspiegel:** Feste \(x_c<x_{\rm ref}<x_b\) halten Abstand von \(x_c\); Laufzeit bleibt bei hinreichend kleinem \(\epsilon\) endlich.

**Nachgeführter Außenspiegel:** Zusätzliche Vorschrift
\[
x_{\rm ref}=x_+ +(q-1)s,\qquad q>1\text{ fest}
\]
gibt \(\delta_{\rm ref}/s\to q\). Aus
\[
\int\frac{d\delta}{\delta^2-s^2}
=\frac1{2s}\ln\left|\frac{\delta-s}{\delta+s}\right|
\]
folgt bei festem \(x_b>x_c\)
\[
T_{\rm rt}\sim\frac{2MD_0}{\sqrt3\beta_c}
\ln\frac{q+1}{q-1}\,\epsilon^{-1/2}.
\]
Koordinatenabstandsregel, kein fester Eigenabstand oder hergeleiteter TIG-Control. Für \(q=2\): Koeffizient \(1.0655305199M\).

Bei **festem** \(\beta<\beta_c\), \(h=r_{\rm ref}-r_+\to0^+\), einfacher Horizont:
\[
F\sim2\kappa_+(r-r_+),\quad T_{\rm rt}=-\kappa_+^{-1}\ln(h/L)+O(1),
\quad\kappa_h=|3-2/x_h|/(4M).
\]
\(L>0\) fest; \(O(1)\) bezüglich \(h\). Beim Grenzübergang \(\epsilon\to0\): \(\kappa_+\sim s/(2MD_0)\). Beide Grenzübergänge benötigen die Randvorschrift. Unterhalb automatisch \(\epsilon^{-1/2}\) für beliebige Ränder zu behaupten ist falsch.

## 4. Exakte Kritikalität

\(\beta=\beta_c\): positiver Doppelnullpunkt. Bei \(x_{\rm ref}=x_c+d,\ d\to0^+\), festem \(x_b>x_c\):
\[
T_{\rm rt}\sim4MD_0/d=16M/(9d).
\]
Kein endlicher Rundlauf durch \(x_c\); die Nicht-Extremalität des betreffenden fremden Zeroth-Law-Beweises fehlt hier.

## 5. Ergebnis und Gegenprüfung

QIC-04 als Reparatur erledigt: Grenzen, Randmodell, Uhr, Seite und Gegenfälle explizit. Alter unbedingter Ansatz \((\beta_c-\beta)^{-1/2}\) durch bedingte Resultate ersetzt. **Physische TIG-Echos unbewiesen.**

Ausführung: python tools/verify_wave3.py; SymPy einschließlich mpmath. Geprüft mit SymPy 1.14.0/mpmath 1.3.0: 18 exakte Identitäten, fünf numerische Bedingungen, 60 Dezimalstellen. Numerik ist Gegenprüfung, kein Asymptotikbeweis.

| Abstand | Horizontlos / führender Term | Nachgeführter Spiegel / führender Term | Fester Außenspiegel \(T/M\) |
|---|---|---|---|
| \(10^{-2}\) | 0.996433218 | 1.621934505 | 13.098086943 |
| \(10^{-4}\) | 1.000035020 | 1.145233892 | 12.592827306 |
| \(10^{-6}\) | 1.000008982 | 1.022271808 | 12.588047289 |
| \(10^{-8}\) | 1.000000955 | 1.002996181 | 12.587999515 |

Beispiel \(M=1\); oberhalb \(x_{\rm ref}=0.4,\ x_b=1.5\); unterhalb \(q=2\) oder festes \(x_{\rm ref}=0.9,\ x_b=1.5\). Fester kritischer Grenzwert \(12.587999032M\). Langsamere Annäherung des nachgeführten Falls sichtbar.

Offen: Dynamik/Quelle, physische Reflexion/Streuung, Gravitationsperturbationen, Anregung, Übertragung/Stabilität. Bestehende Forschungs-OQs bleiben erhalten; kein Echo-Bild als repariert ausgegeben.
