# MAS Integrity Simulation  
## TIG-Enhanced Multi-Agent Systems

---

## 🇩🇪 Deutsche Version

### 1. Ziel

Dieses Dokument erweitert klassische Multi-Agenten-Systeme (MAS) um das TIG-Integritätsfunktional.

Ziel ist es, nicht nur Verhalten zu simulieren, sondern ausschließlich zulässige Systemzustände zu erzeugen.

---

### 2. Klassisches MAS

Ein Standard-MAS besteht aus:

\[
A = \{A_1, A_2, ..., A_n\}
\]

mit:

- Agenten \( A_i \)
- Zuständen \( X \)
- Interaktionen \( I \)

Dynamik:

\[
\frac{dX}{dt} = F(X, A, I)
\]

---

### 3. Problem klassischer Systeme

Klassische Simulationen:

- erzeugen beliebige Zustände  
- besitzen keine globale Konsistenzprüfung  
- können instabile oder unmögliche Systemzustände erzeugen  

---

### 4. TIG-Erweiterung

Wir erweitern die Dynamik um:

\[
\mathcal{I}[X]
\]

Integritätsfunktional:

\[
\mathcal{I}[X] = \sum_i \| C_i(X) \|^2
\]

---

### 5. Erweiterte Dynamik

\[
\frac{dX}{dt}
=
F(X, A, I)
-
\lambda \nabla_X \mathcal{I}[X]
\]

---

### 6. Interpretation

Der neue Term:

\[
-\lambda \nabla_X \mathcal{I}
\]

wirkt als:

- Stabilisierung  
- Constraint Enforcement  
- Systemische Rückkopplung  

---

### 7. Agenten-Verhalten

Ein Agent entscheidet nicht mehr frei, sondern:

\[
Action = \arg\min (Cost + \lambda \mathcal{I})
\]

---

### 8. Emergenz unter Constraints

Klassisch:

\[
Emergenz = f(Interaktion)
\]

TIG:

\[
Emergenz = f(Interaktion \mid \mathcal{I} \text{ minimal})
\]

---

### 9. Simulation Loop

1. Agenten erzeugen Aktionen  
2. Zustand wird aktualisiert  
3. Integritätsfunktion wird berechnet  
4. Gradient korrigiert Zustand  
5. System stabilisiert sich  

---

### 10. Beispiel: Markt-Simulation

Ohne TIG:

- unrealistische Preisblasen  
- extreme Meinungsdrifts  

Mit TIG:

- stabilisierte Märkte  
- begrenzte Extremwerte  
- realistischere Dynamik  

---

### 11. Beispiel: Cybersecurity MAS

Agenten:

- Angreifer  
- Verteidiger  
- Nutzer  

Zustand:

\[
X = Netzwerkstruktur
\]

TIG:

- verhindert instabile Konfigurationen  
- zwingt System in sichere Zustände  

---

### 12. Unterschied zu MiroFish

| MiroFish | TIG-MAS |
|---------|--------|
| Meinungs-Simulation | Zustands-Simulation |
| probabilistisch | constraints-basiert |
| keine Stabilität | stabilitätsgetrieben |
| keine Physik | strukturierte Dynamik |

---

### 13. Erweiterung: Red Teaming

Agenten können bewusst versuchen:

\[
\max \mathcal{I}[X]
\]

System reagiert mit:

\[
\min \mathcal{I}[X]
\]

---

### 14. Strategischer Vorteil

Systeme werden:

- vorhersagbar  
- kontrollierbar  
- stabil  

---

### 15. Fazit

TIG transformiert MAS von:

👉 Verhaltenssimulation  
zu  
👉 zulässiger Systemdynamik  

---

## 🇬🇧 English Version

### 1. Objective

Extend MAS using TIG integrity functional.

---

### 2. Classical MAS

\[
\frac{dX}{dt} = F(X, A, I)
\]

---

### 3. Problem

No global consistency.

---

### 4. TIG Extension

\[
\mathcal{I}[X] = \sum_i \| C_i(X) \|^2
\]

---

### 5. Dynamics

\[
\frac{dX}{dt}
=
F(X)
-
\lambda \nabla_X \mathcal{I}[X]
\]

---

### 6. Agent Decision

\[
Action = \arg\min (Cost + \lambda \mathcal{I})
\]

---

### 7. Emergence

Constraint-driven emergence.

---

### 8. Simulation Loop

- update  
- evaluate  
- correct  

---

### 9. Result

Stable, admissible system behavior.
