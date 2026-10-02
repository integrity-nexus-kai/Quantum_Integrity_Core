# QIC — Normierung, quadratische f(R)-Prüfung und konkrete Horizontbifurkation

**Version:** 1.0 · **Datum:** 2026-10-02  
**Aufgaben:** QIC-01, QIC-02, QIC-03  
**Objektklasse:** lokale Ableitungs- und Gegenprüfungsnotiz  
**Status:** Rechnungen ausgeführt / Manuskriptkorrekturen daraus abgeleitet / keine unabhängige Auditfreigabe  
**Quellenfreeze:** `integrity-nexus-kai/Quantum_Integrity_Core/main` @ `88fef45371dbefe89ee35dce4e8accc5e8eb6baa`  
**Assurance:** Same-run-Selbstprüfung / AIL-0

## 1. Gegenstand und Voraussetzungen

Geprüft wurden die beiden eigenständigen [Paper](../tig-paper/main.tex)- und [Einreichungsmanuskripte](../../submission/arxiv/main.tex), die effektiven Ableitungsnotizen [black_hole_R2_derivation.md](black_hole_R2_derivation.md) und [explicit_black_hole_solution.md](explicit_black_hole_solution.md) sowie die [explorative kubische Rekonstruktion](../../topology/tig_cubic_reconstruction.md). Ihre eingelesenen Blobfassungen und die ausgeführten Rechnungen sind in [repair_tracking.json](../../registry/repair_tracking.json) gebunden.

Voraussetzungen: metrischer f(R)-Formalismus, torsionsfreie Levi-Civita-Verbindung, Signatur (−,+,+,+), G=c=1, M>0, r_c>0, r>0 und konstante endliche μ und Λ. M hat in diesen Einheiten Längendimension. Gegenstand ist genau die Ein-Funktions-Metrik

$$
ds^2=-F(r)dt^2+\frac{dr^2}{F(r)}+r^2d\Omega^2,
\qquad F(r)=1-\frac{2Mr^2}{r^3+r_c^3}.
$$

Eine allgemeinere sphärische Metrik mit unabhängigen A(r) und B(r), andere Wirkungen oder eine eigenständig spezifizierte Materiequelle werden dadurch nicht ausgeschlossen. Statische Horizontnullstellen ersetzen keinen Nachweis ihrer dynamischen Entstehung.

## 2. QIC-01 — Eindeutige Normierung

Im ursprünglichen Einreichungstext stand der gesamte Ausdruck R−2Λ+αR² innerhalb des Vorfaktors 1/(16π), gleichzeitig wurde μ=16πα angegeben. Diese beiden Definitionen stimmen für dasselbe α nicht überein.

Die Reparatur erhält die vorhandene Konvention μ=16πα und schreibt α als Koeffizienten **außerhalb** des Einstein-Vorfaktors:

$$
S_g=\int d^4x\sqrt{-g}\left[\frac{R-2\Lambda}{16\pi}+\alpha R^2\right]
=\frac{1}{16\pi}\int d^4x\sqrt{-g}\,(R-2\Lambda+\mu R^2),
\qquad \mu=16\pi\alpha.
$$

Damit folgt f_R=1+2μR. Der skalare Krümmungsmodus besitzt bei Linearisierung um einen konstanten Vakuum-Krümmungshintergrund m_φ²=1/(6μ). μ>0 ergibt ein positives Massenquadrat; das beweist keine vollständige Hintergrundstabilität. φ=f_R ist hier die Jordan-Frame-Variable, keine behauptete kanonisch normierte Einstein-Frame-Feldkoordinate.

Für eine vollständig eingeklammerte Schreibweise mit α_in wäre dagegen μ=α_in. Bei wieder explizitem G gilt für den außerhalb stehenden Koeffizienten μ=16πGα_out. Die beiden Konventionen sind ineinander umrechenbar; es wird kein zusätzlicher Messwert oder Kopplungszusammenhang festgelegt. In G=c=1 gilt [μ]=[α]=L² und [R]=[Λ]=L⁻². Der Λ-Term in dieser Wirkung ist die kosmologische Konstante.

Die Arbeitsnotizen [_friedmann_derivation.md](_friedmann_derivation.md), [friedmann_equation.md](friedmann_equation.md) und [entropy_integrity_framework.md](entropy_integrity_framework.md) führen bereits α außerhalb und μ=16πα; dort wird kein zusätzlicher Normierungsfehler behauptet. Andere Notizen wie [integrity_tensor_derivation.md](integrity_tensor_derivation.md) verwenden einen dimensionslosen α-Parameter und eine inverse-Längen-Skala Λ in α/Λ². Das ist eine andere Notation; diese Λ-Skala darf nicht still mit der kosmologischen Konstante gleichgesetzt werden. Diese älteren Konventionen werden nicht global umnummeriert oder zu identischen Parametern erklärt.

## 3. QIC-02 — Notwendige Feldgleichungsprüfung

Im metrischen Formalismus gilt mit f_R=∂f/∂R:

$$
\mathcal E_{\mu\nu}
=f_R R_{\mu\nu}-\frac12fg_{\mu\nu}
+(g_{\mu\nu}\Box-\nabla_\mu\nabla_\nu)f_R
=8\pi T_{\mu\nu}.
$$

Die Konventionen und diese Gleichung sind anhand De Felice/Tsujikawa, **f(R) Theories**, Abschnitt 2.1, Gleichungen (2.1), (2.4) und (2.7), geprüft: [DOI 10.12942/lrr-2010-3](https://doi.org/10.12942/lrr-2010-3). Diese allgemeine Quelle belegt die Feldgleichungen; sie beweist die TIG-Metrik nicht. Die nachfolgenden Einsetzungen sind die eigene Rechnung dieses Reparaturlaufs.

Für f(R)=R−2Λ+μR² lautet die Spur:

$$
\mathcal E^\nu{}_{\nu}=6\mu\Box R-R+4\Lambda=8\pi T.
$$

Setze a=r_c³. Aus den Christoffelsymbolen der angegebenen Metrik ergibt sich

$$
R=-F''-\frac{4F'}r+\frac{2(1-F)}{r^2}
=\frac{12Ma(2a-r^3)}{(r^3+a)^3},
\qquad
\Box R=\frac1{r^2}\frac{d}{dr}\left(r^2F R'\right).
$$

Eine Vakuumlösung verlangt den identisch verschwindenden Rest

$$
\mathcal T(r)=6\mu\Box R-R+4\Lambda.
$$

**Außenbereich:** lim_(r→∞) 𝒯(r)=4Λ. Wegen der asymptotisch flachen angegebenen Metrik ist Λ=0 eine notwendige Vakuumbedingung. Mit dieser Bedingung erhält man

$$
R=-\frac{12Ma}{r^6}+O(r^{-9}),\qquad
\Box R=-\frac{360Ma}{r^8}+O(r^{-9}),
\qquad
\lim_{r\to\infty}r^6\mathcal T(r)=12Ma\ne0.
$$

Der r⁻⁶-Term kann durch keinen endlichen konstanten μ im r⁻⁸-Term aufgehoben werden. Das widerlegt bereits die behauptete exakte Vakuumlösung.

**Kernbereich:** R→24M/a und □R→0 bei r→0⁺. Deshalb gilt zusätzlich

$$
\lim_{r\to0^+}\mathcal T(r)=-\frac{24M}{a}\ne0
\qquad (\Lambda=0).
$$

Das ist ein skalarer Grenzwert von r>0 aus; es wird keine singuläre Koordinatenkomponente am Zentrum als Argument benutzt.

**Komponenten-Gegencheck:** Für die Ein-Funktions-Metrik sind R^t_t=R^r_r und

$$
\mathcal E^t{}_t-\mathcal E^r{}_r=2\mu F R''.
$$

Für μ≠0 erfordert Vakuum auf jedem offenen Intervall mit F≠0 also R''=0. Das nicht konstante rationale R(r) des repräsentativen Profils erfüllt diese Bedingung ebenfalls nicht identisch. Der stärkere Spur-Gegenbeweis gilt auch bei μ=0. Für r_c=0 und r>0 ist hingegen die Schwarzschild-Metrik mit R_μν=0 eine separate Vakuumlösung bei Λ=0.

**Ergebnis:** Die nichttriviale angegebene Metrik ist unter den oben genannten Voraussetzungen **keine exakte Vakuumlösung** der konstanten quadratischen metrischen f(R)-Theorie. Ein positiver Lösungsnachweis wurde nicht durch Umbenennung ersetzt. Die Manuskripte enthalten jetzt den negativen Test; der stärkere Titel, Abstract und Schluss des Einreichungstexts wurden nachgeführt.

Mit Materie müsste 8πT_μν=𝓔_μν durch eine unabhängig spezifizierte Materiewirkung samt Materiegleichungen realisiert werden. Eine Definition des effektiven Tensors aus der Metrik ist dafür kein eigenständiger Lösungsbeweis. Eine Beziehung r_c(μ,M,…) ist in den geprüften Manuskripten nicht hergeleitet. Die separate effektive TIG-Architektur G_μν=I_μν wird nicht mit diesem Vakuum-f(R)-Test gleichgesetzt; ihre bisherigen Owner, Auditverdikte und unabhängigen Forschungsfragen bleiben bestehen.

## 4. QIC-03 — Modellgebundene Kubik statt universeller Notwendigkeit

Mit dem **gewählten** Profil m(r)=Mr³/(r³+r_c³) folgt für r_H>0 aus F(r_H)=0:

$$
r_H^3-2Mr_H^2+r_c^3=0,
\qquad x=\frac{r_H}{2M},\quad\beta=\frac{r_c}{2M},
\qquad P(x,\beta)=x^3-x^2+\beta^3=0.
$$

Dabei ist F=P/(x³+β³). Für x>0 und β>0 ist der Nenner strikt positiv, sodass die Horizontäquivalenz gilt. Bei β=0 sind die beiden Nullstellen x=0 des ausmultiplizierten x²(x−1) außerhalb des Äquivalenzbereichs: Sie sind keine zusätzlichen Schwarzschild-Horizonte und kein bewiesener interner physikalischer Sektor. Für r_c>0 gilt F(0)=1.

β³ stammt konkret aus dem r_c³-Term des gewählten Nenners. Die Dimensionslosigkeit von β erzwingt weder die dritte Potenz noch dieses Profil. Ein Gegenmodell für die behauptete Eindeutigkeit ist

$$
\widetilde m(r)=\frac{Mr^3}{(r^2+r_c^2)^{3/2}}.
$$

Es erfüllt ebenfalls m→M im Außenbereich und m/r³→M/r_c³ im Kern, führt aber zu einer anderen Horizontgleichung. Seine vollständige Dynamik wird hier ebenfalls nicht behauptet.

Die lokale Fold-Gleichung y²−λ=0 ist quadratisch. Das zugehörige Potential V=y³/3−λy ist kubisch; Potential und stationäre Gleichung dürfen nicht verwechselt werden. Schon Q(x,λ)=x²−x+λ hat bei λ=0 eine normierte Schwarzschild-Referenzwurzel x=1 und einen nichtdegenerierten Fold bei (x,λ)=(1/2,1/4). Damit ist eine allgemeine kubische Notwendigkeit widerlegt. Geprüfte mathematische Quelle: Chasnov, **Applied Linear Algebra and Differential Equations**, Abschnitt 11.2.1, gedruckte Seite 141, PDF-Seite 149 (einsbasiert), Vorwort Januar 2020: [HKUST-Original](https://www.math.hkust.edu.hk/~machas/applied-linear-algebra-and-differential-equations.pdf). Die Quelle belegt den quadratischen Fold, nicht die Auswahl des TIG-Massenprofils.

## 5. Erhaltene und rechnerisch bestätigte Ergebnisse

Für das konkrete P gilt

$$
\Delta=\beta^3(4-27\beta^3),\qquad
x_c=\frac23,\qquad\beta_c=\left(\frac4{27}\right)^{1/3},
\qquad P(x,\beta_c)=\left(x-\frac23\right)^2\left(x+\frac13\right).
$$

Für 0<β<β_c existieren zwei positive und eine negative reelle Wurzel; bei β_c eine positive Doppelwurzel und eine negative; darüber nur eine negative reelle Wurzel. Das folgt aus P(0)>0, dem Minimum P(2/3)=β³−4/27 und der Monotonie in den drei durch P_x=x(3x−2) getrennten Bereichen. Radien sind positiv; die negative Wurzel ist kein Horizont.

Mit δ=x−x_c und ε=β_c−β>0 lautet die exakte Entwicklung

$$
P(x_c+\delta,\beta_c-\epsilon)
=\delta^2+\delta^3-3\beta_c^2\epsilon+3\beta_c\epsilon^2-\epsilon^3.
$$

Da P_xx=2 und P_β=3β_c² am kritischen Punkt nicht verschwinden, ist die lokale Falte nichtdegeneriert. Ihre beiden Äste erfüllen

$$
\delta_\pm=\pm\sqrt3\,\beta_c\epsilon^{1/2}+O(\epsilon).
$$

Der Exponent 1/2 beschreibt die Horizontwurzelverschiebung bei dieser Parameterwahl. Die Wurzelpositionen verlaufen bis zur Koaleszenz kontinuierlich; ihre Anzahl ändert sich. Daraus folgt kein diskontinuierlicher Sprung jeder Observablen, keine dynamische Stabilität und kein Echo-Exponent. Der Echo-Schätzwert bleibt QIC-04/Welle 3 zugeordnet und ist in der Einreichung jetzt ausdrücklich ungeprüft.

## 6. Reproduzierbare Prüfung und verbleibender Forschungsumfang

[tools/verify_wave2.py](../../tools/verify_wave2.py) rekonstruiert die Christoffelsymbole und Ricci-Komponenten, prüft die radiale d'Alembert-Gleichung und 27 exakte Identitäten beziehungsweise Nichtdegeneriertheits-/Gegenmodellbedingungen. Abhängigkeit: SymPy; ausgeführte Version 1.14.0. Aus der Repositorywurzel:

```bash
python tools/verify_wave2.py
```

Der JSON-Nachweis enthält die vollständigen rationalen Ausdrücke für □R und den Spurrest sowie die ausgeführten Checks. Ergebnis dieses Laufs: PASS für die Rechnungsprüfung, **negatives** Ergebnis für den konkreten Vakuumlösungsanspruch. Dies ist eine Selbstprüfung desselben Reparaturlaufs, kein unabhängiger Audit und keine Freigabe einer neuen kanonischen Theorie.

Die beauftragten Reparaturen QIC-01–03 sind mit den begrenzten, expliziten Ergebnissen erledigt. Offen bleiben das eigenständige Dynamik-/Materieprogramm, eine nicht angenommene topologische Eindeutigkeitsherleitung, die bereits bestehenden O1–O7, Literatur-/Horizontvoraussetzungen, Echo-Physik und der Abschluss-/Exportbuild in den folgenden Wellen. Kein bestehendes Forschungs-OQ wird durch diese Reparatur geschlossen.
