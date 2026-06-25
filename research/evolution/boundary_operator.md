# Boundary Operator Specification v1.0

## Status

Canonical Construction Candidate Specification

## Purpose

This document defines the role of the admissibility boundary in the future TIG Evolution Operator construction.

It does not define the full Evolution Operator.

It specifies how the boundary must be treated by any admissible evolution.

---

# Dependency Position

This document depends on:

```text
research/evolution/evolution_generator_requirements.md
research/evolution/operator_space_definition.md
research/evolution/evolution_operator_axioms.md
```

It precedes:

```text
research/evolution/evolution_operator_construction.md
```

---

# Boundary Context

The admissible domain is:

```text
A subset M
```

For the P004 toy universe:

```text
M = R

A subset R
```

The boundary of admissibility is denoted abstractly as:

```text
partial A
```

The integrity limit is represented by:

```text
gamma <= gamma_max
```

The exact construction of gamma remains open.

Therefore, this document treats the boundary structurally rather than metrically.

---

# Core Requirement

The admissibility boundary must be invariant under admissible evolution.

An admissible evolution may not map an admissible state into the forbidden exterior:

```text
Phi_t(A) subset A
```

for all admissible times.

---

# Boundary Operator Role

A Boundary Operator is any mathematical mechanism responsible for ensuring that the Evolution Operator respects the admissible domain.

It may act as:

- a projection mechanism,
- a saturation mechanism,
- a reflective mechanism,
- a degeneracy mechanism,
- a constraint-preserving flow condition,
- or another mathematically derived boundary-preserving structure.

No option is canonical yet.

---

# Candidate Boundary Mechanisms

## Candidate B1 — Projection

A projection mechanism maps attempted boundary-violating states back into the admissible domain.

Status:

Candidate only.

Risk:

May introduce discontinuity or external correction if not derived internally.

---

## Candidate B2 — Saturation

A saturation mechanism causes evolution to asymptotically approach the boundary without crossing it.

Status:

Candidate only.

Risk:

Requires a derived slowing or limiting mechanism.

---

## Candidate B3 — Reflection

A reflection mechanism reverses the boundary-crossing component of evolution.

Status:

Candidate only.

Risk:

May require additional metric or tangent-space structure.

---

## Candidate B4 — Degeneracy

A degeneracy mechanism makes the forbidden direction mathematically unavailable at the boundary.

Status:

Candidate only.

Risk:

Requires proof that the operator loses the violating component by necessity.

---

## Candidate B5 — Constraint-Preserving Flow

A constraint-preserving flow is tangent to the admissible boundary and never develops an outward component.

Status:

Candidate only.

Risk:

Requires a well-defined tangent boundary condition.

---

# Current Canonical Decision

No concrete Boundary Operator is canonical yet.

The current canonical result is only:

```text
Any admissible Evolution Operator must preserve A.
```

The exact mechanism remains a construction problem.

---

# Boundary Audit Rule

Every future Evolution Operator candidate must answer:

```text
Why can this evolution not leave A?
```

Acceptable answers must be mathematical.

Unacceptable answers include:

- because the framework declares it forbidden,
- because an external controller stops it,
- because the trajectory is manually corrected,
- because violation is ignored.

---

# Relationship to gamma_max

The boundary is ultimately expected to correspond to the integrity condition:

```text
gamma <= gamma_max
```

However, because gamma is not yet fully constructed, the current boundary treatment remains structural.

A later milestone must connect this structural boundary to a formal gamma-evaluation mechanism.

---

# Explicit Non-Goals

This document does not define:

- gamma,
- gamma_max,
- the Evolution Operator,
- the TIG Hamiltonian,
- a metric tensor,
- a quantum boundary condition,
- a field equation.

---

# Audit Classification

Classification:

Boundary Operator Specification

Scientific Status:

Candidate Space Defined

Roadmap Status:

Active Construction Layer

Connor Status:

Crystallized
