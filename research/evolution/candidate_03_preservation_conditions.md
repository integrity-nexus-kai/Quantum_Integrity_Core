# Candidate 03 Preservation Conditions v1.0

## Status

Conditional Preservation Result

## Classification

Dependency-Compliant Candidate Skeleton Analysis

## Purpose

This document records the dependency-compliant analysis of Candidate 03 after the introduction of constraint-induced admissibility.

It consolidates the following steps:

```text
Candidate 03 Re-Admission Conditions
Dependency-Compliant Candidate 03 Skeleton
Candidate 03 Skeleton Audit
Candidate 03 Preservation Problem
```

This document does not define the final TIG Evolution Operator.

It does not define the TIG Hamiltonian.

It does not identify C with gamma or C_max with gamma_max.

---

# Roadmap Position

This document belongs to the P004 construction layer.

It depends on:

```text
research/evolution/saturation_flow_class.md
research/evolution/saturation_flow_deficiency_analysis.md
research/evolution/constraint_induced_admissibility.md
```

It follows the documented deficiency that the Saturation Flow Class preserves a toy boundary but does not provide Hamiltonian-compatible structure.

---

# Background

The Saturation Flow Class established a minimal toy boundary mechanism:

```text
dx/dt = alpha (b - x)
```

with boundary preservation in the 1D toy universe.

However, it remained weak with respect to:

```text
Hamiltonian compatibility
phase-space structure
generator functional
internal constraint origin
```

The dependency layer:

```text
Constraint-Induced Admissibility
```

replaced the externally imposed boundary by:

```text
A_C = { s in S | C(s) <= C_max }
```

with boundary candidate:

```text
Sigma_C = { s in S | C(s) = C_max }
```

Candidate 03 is only considered after this dependency layer.

---

# Candidate 03 Status

Candidate 03 is not accepted as a final operator.

It is treated only as a dependency-compliant pre-candidate skeleton.

Classification:

```text
Hamiltonian-compatible constraint-generated toy skeleton
```

Not classified as:

```text
TIG Hamiltonian
Final TIG Evolution Operator
Gamma construction
Gamma_max derivation
```

---

# Re-Admission Conditions

Candidate 03 may only be formulated under the following conditions.

## R3-1 — State Space Declaration

The state space must be declared before any Hamiltonian-compatible claim is made.

For Hamiltonian-ready toy analysis:

```text
S = T*Q
```

In the minimal 1D toy case:

```text
Q = R
S = T*Q ~= R x R
s = (x,p)
```

Hamiltonian language without phase space is not admissible.

---

## R3-2 — Constraint Functional First

The constraint functional must be defined before the dynamics.

Required ordering:

```text
1. define C
2. define C_max
3. define A_C
4. evaluate or construct evolution
```

Post-hoc fitting of C to a desired trajectory is not admissible.

---

## R3-3 — Constraint-Induced Admissible Region

The admissible region must be induced by C:

```text
A_C = { s in S | C(s) <= C_max }
```

An externally imposed boundary such as:

```text
A = (-infinity, b]
```

is no longer primary at this stage.

A toy value b may only appear as a reduction such as:

```text
b = C^(-1)(C_max)
```

where this inverse is meaningful.

---

## R3-4 — Boundary Regularity

The boundary candidate is:

```text
Sigma_C = { s in S | C(s) = C_max }
```

For a regular boundary, require:

```text
C in C^1
dC != 0 on Sigma_C
```

Equivalently:

```text
C_max is a regular value of C.
```

---

## R3-5 — Hamiltonian-Ready Regularity

If the candidate is presented in Hamiltonian-compatible form, require:

```text
C in C^2
```

at least on the admissible interior.

This is a preparatory regularity condition, not a proof of final Hamiltonian validity.

---

## R3-6 — No Post-Hoc Projection

Boundary preservation must follow from the evolution structure.

Not allowed:

```text
boundary crossing
-> projection back into A_C
```

Required preservation target:

```text
s_0 in A_C
=>
Phi_t(s_0) in A_C
```

---

## R3-7 — Constant Drive Compatibility

The future candidate must represent a constant drive toward the boundary.

Toy notation:

```text
F = const
```

The drive must not imply boundary crossing if preservation is claimed.

---

## R3-8 — No TIG Identification

The following identifications are not allowed at this stage:

```text
C = gamma
C_max = gamma_max
H = TIG Hamiltonian
B(C) = TIG integrity potential
Candidate 03 = final Evolution Generator
```

---

## R3-9 — Barrier Legitimacy Not Assumed

If a barrier function is used:

```text
B(C)
```

then it is classified only as a toy boundary-enforcement mechanism.

It must not be called a TIG-derived integrity potential unless separately derived.

---

# Dependency-Compliant Candidate 03 Skeleton

Under the above conditions, a dependency-compliant skeleton may be written as follows.

Let:

```text
S = T*Q
```

with minimal 1D toy reduction:

```text
Q = R
S ~= R x R
s = (x,p)
```

Let:

```text
C : Q -> R
C_max in R
```

and define:

```text
A_C = { (x,p) in S | C(x) <= C_max }
```

with boundary candidate:

```text
Sigma_C = { (x,p) in S | C(x) = C_max }
```

Then a Hamiltonian-compatible toy skeleton is:

```text
H(x,p) = p^2/(2m) + B(C(x)) - F x
```

with:

```text
m > 0
F = const
```

and:

```text
B(C) = toy barrier profile
```

The term:

```text
-F x
```

represents a constant drive because:

```text
Force = -d(-F x)/dx = F
```

---

# Barrier Skeleton Assumption

The barrier profile is assumed to diverge near the constraint boundary:

```text
B(C) -> infinity as C -> C_max from below
```

If differentiability is used, one may also require:

```text
B'(C) -> infinity as C -> C_max from below
```

This assumption is not a TIG derivation.

It is a toy mechanism for testing boundary preservation in a Hamiltonian-compatible setting.

---

# Hamiltonian Equations

From:

```text
H(x,p) = p^2/(2m) + B(C(x)) - F x
```

one obtains formally:

```text
dx/dt = partial H / partial p = p/m
```

and:

```text
dp/dt = - partial H / partial x
```

hence:

```text
dp/dt = F - B'(C(x)) C'(x)
```

This expresses:

```text
constant drive
+
constraint-induced barrier response
```

---

# Preservation Target

The target preservation statement is:

```text
(x_0,p_0) in A_C
=>
Phi_t(x_0,p_0) in A_C
```

Equivalently:

```text
C(x_0) <= C_max
=>
C(x(t)) <= C_max
```

for admissible times.

This is not assumed by definition.

It must follow from the Hamiltonian structure and the barrier conditions.

---

# Candidate 03 Preservation Problem

The central question is:

```text
Under which conditions does
H(x,p) = p^2/(2m) + B(C(x)) - F x
prevent reaching or crossing Sigma_C?
```

The mechanism is:

```text
finite conserved energy
+
divergent effective barrier
=>
energetic exclusion of the boundary
```

---

# Effective Potential

The relevant potential term is not merely:

```text
B(C(x))
```

because the Hamiltonian also contains:

```text
-F x
```

The effective potential is therefore:

```text
V_eff(x) = B(C(x)) - F x
```

The true boundary exclusion condition is:

```text
V_eff(x) -> infinity
```

when the state approaches the constraint boundary from the admissible interior.

In 1D notation:

```text
B(C(x)) - F x -> infinity
as
C(x) -> C_max from below.
```

This condition ensures that the constant drive term does not cancel the barrier divergence.

---

# Preservation Condition Set

The Candidate 03 skeleton prevents boundary reaching under the following conditions.

## PC1 — Autonomous Energy Conservation

H is autonomous and the Hamiltonian flow conserves H:

```text
H(x(t),p(t)) = H(x_0,p_0) = E
```

---

## PC2 — Interior Initial Data

Initial data lie in the admissible interior:

```text
C(x_0) < C_max
```

---

## PC3 — Finite Initial Energy

Initial energy is finite:

```text
H(x_0,p_0) < infinity
```

---

## PC4 — Regular Constraint Boundary

The constraint boundary is regular:

```text
C in C^1
dC != 0 on Sigma_C
```

Equivalently:

```text
C_max is a regular value of C.
```

---

## PC5 — Hamiltonian Well-Defined in the Interior

The Hamiltonian must be finite and sufficiently smooth inside the admissible region.

A preparatory condition is:

```text
C in C^2 on the admissible interior
B in C^1 on C < C_max
```

---

## PC6 — Divergent Effective Barrier

The effective potential must diverge at the boundary:

```text
V_eff(x) = B(C(x)) - F x -> infinity
```

as the trajectory approaches Sigma_C from the admissible interior.

---

## PC7 — No Post-Hoc Projection

Preservation must follow from energy conservation and the barrier mechanism.

No projection back into A_C is allowed.

---

# Preservation Argument

Assume:

```text
C(x_0) < C_max
H(x_0,p_0) = E < infinity
```

and suppose that a trajectory approaches the boundary:

```text
C(x(t)) -> C_max from below.
```

By PC6:

```text
V_eff(x(t)) = B(C(x(t))) - F x(t) -> infinity.
```

Since:

```text
p(t)^2/(2m) >= 0
```

we obtain:

```text
H(x(t),p(t)) = p(t)^2/(2m) + V_eff(x(t)) -> infinity.
```

This contradicts energy conservation:

```text
H(x(t),p(t)) = E < infinity.
```

Therefore, under the listed assumptions, the boundary cannot be reached by finite-energy trajectories.

In particular:

```text
C(x(t)) < C_max
```

for all times for which the Hamiltonian solution exists.

---

# What Is Shown

Under the preservation conditions, Candidate 03 provides a conditional finite-energy boundary exclusion mechanism.

It shows:

```text
finite-energy initial data in the admissible interior
+
divergent effective barrier
=>
no reaching of Sigma_C
```

This is stronger than the Saturation Flow Class in one specific sense:

```text
it supports a generator-based phase-space formulation.
```

---

# What Is Not Shown

This document does not prove global existence for all time.

It does not exclude other possible obstructions such as:

```text
escape to x -> -infinity
uncontrolled momentum growth
interior singularities
pathological C
pathological B
```

It does not derive:

```text
C
C_max
B(C)
gamma
gamma_max
TIG Hamiltonian
final TIG Evolution Operator
```

---

# Locked Classification

Candidate 03 Preservation Problem:

```text
Conditionally solvable
```

Result:

```text
finite-energy boundary exclusion
```

Not result:

```text
global existence proof
TIG Hamiltonian
final Evolution Generator
gamma / gamma_max derivation
```

---

# Final Audit Statement

The Candidate 03 skeleton prevents reaching or crossing the constraint boundary Sigma_C only under explicit preservation conditions.

The decisive condition is that the effective potential:

```text
V_eff(x) = B(C(x)) - F x
```

diverges to infinity as the boundary is approached from the admissible interior, while the Hamiltonian energy remains finite and conserved.

This gives a conditional toy-level finite-energy boundary exclusion mechanism, not a final TIG evolution theory.

---

# Connor Status

Crystallized
