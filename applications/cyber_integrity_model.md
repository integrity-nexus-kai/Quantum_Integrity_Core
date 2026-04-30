# Cyber Integrity Model  
## TIG-based System Stability Framework

---

## 🇩🇪 Deutsche Version

### 1. Ziel

Dieses Dokument definiert ein konkretes Cybersecurity-Modell basierend auf dem TIG-Integritätsfunktional.

Ziel ist es, Sicherheit nicht als Reaktion auf Angriffe zu verstehen, sondern als Stabilisierung zulässiger Systemzustände.

---

### 2. Systemdefinition

Ein IT-System wird beschrieben durch:

\[
X =
\{
U, S, P, D, A
\}
\]

mit:

- \( U \): Benutzer  
- \( S \): Services  
- \( P \): Berechtigungen  
- \( D \): Datenflüsse  
- \( A \): Angriffsflächen  

---

### 3. Zustandsraum

Ein Zustand ist definiert als:

\[
X(t)
\]

und enthält:

- aktuelle Berechtigungen  
- aktive Verbindungen  
- laufende Prozesse  
- Zugriffspfade  

---

### 4. Integritätsbedingungen

Wir definieren Constraints:

\[
C_i(X) = 0
\]

Typische Bedingungen:

1. **No Privilege Escalation**
2. **No Cyclic Trust Chains**
3. **Controlled Data Flow**
4. **No Single Point of Failure**
5. **Valid State Transitions**

---

### 5. Integritätsfunktional

\[
\mathcal{I}_{cyber}[X]
=
\sum_i
\| C_i(X) \|^2
\]

Optional erweitert:

\[
\mathcal{I}_{cyber}
=
\sum_i w_i \cdot C_i(X)^2
\]

---

### 6. Dynamik eines Angriffs

Ein Angriff ist eine Zustandsänderung:

\[
X(t) \rightarrow X(t+\Delta t)
\]

mit:

\[
\frac{d}{dt}\mathcal{I}_{cyber}[X] > 0
\]

👉 Integrität wird verletzt

---

### 7. Verteidigungsprinzip

Statt Signaturerkennung:

\[
\frac{dX}{dt}
=
F(X)
-
\lambda \nabla_X \mathcal{I}_{cyber}[X]
\]

---

### 8. Interpretation

Der Integritäts-Term:

- erkennt kritische Zustände früh  
- verhindert Eskalation  
- stabilisiert das System  

---

### 9. Beispiel: Privilege Escalation

Constraint:

\[
C_{priv}(X) =
\text{ActualPrivileges} - \text{AllowedPrivileges}
\]

Wenn:

\[
C_{priv}(X) \neq 0
\]

→ Integritätsverletzung

---

### 10. Beispiel: Datenfluss

\[
C_{flow}(X) =
\text{UncontrolledFlow}
\]

---

### 11. Beispiel: Trust Graph

Graph \( G \) mit Knoten = Systeme

Constraint:

\[
C_{trust}(X) =
\text{CycleCount}(G)
\]

---

### 12. Angriff als Trajektorie

Ein Angriff ist kein Event, sondern:

\[
X_0 \rightarrow X_1 \rightarrow X_2 \rightarrow ...
\]

mit wachsendem:

\[
\mathcal{I}_{cyber}
\]

---

### 13. Systemreaktion

Statt:

- Alert  
- Logging  

→ aktive Rückführung:

\[
\Delta X = -\lambda \nabla_X \mathcal{I}
\]

---

### 14. Vorteil gegenüber klassischen Systemen

| Klassisch | TIG |
|----------|-----|
| reaktiv | proaktiv |
| signaturbasiert | zustandsbasiert |
| lokal | systemisch |
| Event-Fokus | Dynamik-Fokus |

---

### 15. Erweiterung: Multi-Agenten-Systeme

Agenten:

\[
A_i
\]

Interaktion:

\[
A_i \leftrightarrow A_j
\]

Mit TIG:

\[
\text{nur Zustände mit niedriger } \mathcal{I}
\]

---

### 16. Strategische Bedeutung

Cybersecurity wird:

👉 ein Stabilitätsproblem  
statt  
👉 ein Angriffsproblem  

---

## 🇬🇧 English Version

### 1. Objective

Define a cybersecurity model based on the TIG integrity functional.

---

### 2. System Definition

\[
X =
\{
U, S, P, D, A
\}
\]

---

### 3. State Space

\[
X(t)
\]

---

### 4. Constraints

\[
C_i(X) = 0
\]

---

### 5. Integrity Functional

\[
\mathcal{I}_{cyber}[X]
=
\sum_i \| C_i(X) \|^2
\]

---

### 6. Attack Dynamics

\[
\frac{d}{dt}\mathcal{I}_{cyber}[X] > 0
\]

---

### 7. Defense

\[
\frac{dX}{dt}
=
F(X)
-
\lambda \nabla_X \mathcal{I}_{cyber}[X]
\]

---

### 8. Interpretation

Security = dynamic stabilization

---

### 9. Conclusion

TIG transforms cybersecurity into a system stability problem.
