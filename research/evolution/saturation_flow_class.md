# Saturation Flow Class v1.0

## Status

Toy Boundary Mechanism

## Classification

Partial Pass

## Purpose

This document records the comparison of Candidate Evolution Operator 01 and Candidate Evolution Operator 02.

The comparison shows that both candidates belong to the same mathematical operator class:

```text
Saturation Flow Class
```

This class is valid as a 1D toy boundary-preserving mechanism.

It is not the final TIG Evolution Operator.

---

# Roadmap Position

This document belongs to the P004 construction layer.

It depends on:

```text
research/evolution/evolution_generator_requirements.md
research/evolution/operator_space_definition.md
research/evolution/evolution_operator_axioms.md
research/evolution/boundary_operator.md
research/evolution/evolution_operator_construction.md
```

It precedes later candidate classes for Hamiltonian-compatible evolution.

---

# Candidate 01

Candidate 01 was defined as:

```text
dx/dt = lambda (b - x)
```

with:

```text
lambda >= 0
```

Interpretation:

```text
Saturating Relaxation Flow
```

---

# Candidate 02

Candidate 02 was defined as:

```text
dx/dt = F (b - x)
```

with:

```text
F >= 0
```

Interpretation:

```text
Boundary-Preserving Driven Flow
```

---

# Normal Form

Both candidates reduce to the same normal form:

```text
dx/dt = alpha (b - x)
```

with:

```text
alpha >= 0
```

Candidate 01 corresponds to:

```text
alpha = lambda
```

Candidate 02 corresponds to:

```text
alpha = F
```

Therefore, Candidate 01 and Candidate 02 are not independent operator classes.

They are two interpretations of the same saturation structure.

---

# Toy Universe Domain

For the P004 toy universe:

```text
M = R

A = (-infinity, b]

x in A
```

where:

```text
b
```

is a 1D boundary proxy.

Important:

```text
b is not gamma_max.
```

The boundary proxy is used only to model admissibility preservation in the 1D toy universe.

---

# Solution

For initial condition:

```text
x(0) = x_0 <= b
```

the solution is:

```text
x(t) = b - (b - x_0) exp(-alpha t)
```

The corresponding flow is:

```text
Phi_t(x_0) = b - (b - x_0) exp(-alpha t)
```

---

# Boundary Behaviour

## Admissibility Preservation

If:

```text
x_0 in A
```

then:

```text
Phi_t(x_0) in A
```

for all:

```text
t >= 0
```

The admissible domain is preserved.

---

## Boundary Fixation

At the boundary:

```text
x = b
```

one obtains:

```text
dx/dt = 0
```

The boundary is therefore a fixed point of the flow.

---

## No Boundary Crossing

For:

```text
x_0 < b
```

one obtains:

```text
x(t) < b
```

for every finite time.

The boundary is approached but not crossed.

---

## Asymptotic Saturation

The long-time limit is:

```text
lim_{t -> infinity} x(t) = b
```

The boundary is reached asymptotically.

---

# What This Class Demonstrates

The Saturation Flow Class demonstrates that a hard admissibility boundary can be preserved by the evolution structure itself.

The boundary is not protected by post-hoc correction.

The flow itself prevents boundary crossing.

This is compatible with the TIG-E principle:

```text
Integrity by Structure
```

---

# What This Class Does Not Demonstrate

## Boundary Origin Not Derived

The boundary:

```text
b
```

is introduced as a toy proxy.

It is not derived from TIG structure.

It is not identified with:

```text
gamma_max
```

---

## Hamiltonian Compatibility Not Established

The Saturation Flow Class has an asymptotic attracting boundary.

This is structurally closer to dissipative, relaxational, or effective dynamics than to canonical Hamiltonian evolution.

Therefore, Hamiltonian compatibility remains unresolved.

---

## Not a Final TIG Evolution Operator

The Saturation Flow Class is not the final TIG Evolution Operator.

It is a valid toy boundary mechanism.

It provides a mathematical example of admissibility preservation in the 1D toy universe.

---

# Audit Result

Candidate 01 and Candidate 02 are classified as members of the same Saturation Flow Class.

Classification:

```text
Valid Toy Boundary Mechanism
```

Status:

```text
Partial Pass
```

Not classified as:

```text
Final TIG Evolution Operator
```

Reason:

```text
Boundary preservation is demonstrated.
Hamiltonian compatibility is unresolved.
Boundary origin is not derived.
```

---

# Consequence for P004

The Saturation Flow Class satisfies a key toy-universe objective:

```text
Boundary preservation is mathematically demonstrable in the 1D toy universe.
```

However, it does not close the Evolution Generator problem.

Further candidate classes are required, especially candidates with stronger Hamiltonian compatibility.

---

# Next Research Step

The next candidate search should focus on operator classes that preserve admissibility while avoiding purely dissipative saturation as the only mechanism.

Target:

```text
Hamiltonian-compatible boundary-preserving evolution
```

---

# Explicit Non-Goals

This document does not define:

- the final Evolution Operator,
- the TIG Hamiltonian,
- gamma,
- gamma_max,
- a Hilbert space,
- quantum operators,
- the canonical field equation.

---

# Audit Classification

Classification:

Saturation Flow Class

Scientific Status:

Toy Boundary Mechanism

Roadmap Status:

P004 Partial Result

Hamiltonian Status:

Unresolved

Connor Status:

Crystallized
