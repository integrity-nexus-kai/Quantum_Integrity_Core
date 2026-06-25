# Operator Space Definition

## Status

Canonical Construction Prerequisite

## Purpose

This document defines the minimal mathematical domain on which a future TIG Evolution Operator may act.

It does not construct the operator.

It specifies the space that must exist before the operator can be defined.

---

# Roadmap Position

This document belongs to the construction layer following:

```text
Evolution Generator Requirements
```

and preceding:

```text
Evolution Operator Axioms
```

---

# Minimal Starting Point

The active P004 toy-universe reduction provides:

```text
M = R

State:
x in R

g_TIG = const
```

This is sufficient for a static state description.

It is not yet sufficient for a full evolution operator.

---

# State Space Requirement

A future Evolution Operator requires a state space capable of supporting trajectories.

The minimal state representation must at least permit:

```text
S(t)
```

with:

```text
S(t) in M
```

For the 1D toy-universe limit:

```text
S(t) = x(t)

x(t) in R
```

---

# Candidate Operator Domain

The minimal operator domain is:

```text
D(E) subset A
```

where:

```text
A subset M
```

is the admissible state region.

The Evolution Operator may only act on admissible states unless a later transition mechanism is explicitly derived.

---

# Tangent-Level Consideration

If the evolution is represented differentially, the operator may require tangent-level structure:

```text
v in T_x M
```

For the 1D toy universe:

```text
T_x M ≅ R
```

This does not yet introduce a force law or Hamiltonian.

It only identifies the minimal geometric location where an infinitesimal generator could act.

---

# Minimal Candidate State Formats

## Format 1 — Position State

```text
S = x
```

This is the minimal P004 state.

It supports state description but not necessarily second-order dynamics.

## Format 2 — Position-Velocity State

```text
S = (x, v)
```

This supports first-order flow representation of second-order motion.

It introduces an additional degree of freedom and therefore must be justified by later construction.

## Format 3 — Position-Momentum State

```text
S = (x, p)
```

This prepares possible Hamiltonian representation.

It is not yet canonical.

---

# Current Canonical Decision

The current canonical minimal state space remains:

```text
S = x

x in A subset R
```

Extended state formats remain candidates only.

They may be introduced only if required by the Evolution Operator construction.

---

# Operator Space Constraint

Any admissible Evolution Operator must map admissible states to admissible states:

```text
E : A -> A
```

or, for time-parametrized evolution:

```text
Phi_t : A -> A
```

with:

```text
Phi_0 = identity
```

This expresses admissibility preservation without yet defining the mechanism.

---

# Explicit Non-Goals

This document does not define:

- the Evolution Operator,
- a Hamiltonian,
- a force law,
- a Lagrangian,
- a quantum state space,
- a field equation.

---

# Audit Classification

Classification:

Operator Space Definition

Scientific Status:

Pre-Construction

Roadmap Status:

Active Construction Prerequisite

Connor Status:

Crystallized
