# Integrity Tensor Requirements

## Purpose

This document defines the mandatory requirements for any candidate realization of the TIG Integrity Tensor.

The objective is not to construct the tensor.

The objective is to identify the minimal set of properties required for consistency with the current TIG framework.

No candidate may be accepted unless all requirements are satisfied.

---

# Current Context

TIG Field Equation 1.0 is currently expressed as:

Gμν = Iμν[g,r_c]

where:

- Gμν is the Einstein Tensor
- Iμν is the Integrity Tensor
- gμν is the metric
- r_c is the Integrity Scale

The current realization is:

Iμν[g,r_c]
=
Gμν[g,m(r)]
-
Gμν[g,M]

This realization is structurally validated.

The purpose of this document is to determine which properties are fundamental and which properties are implementation-specific.

---

# Requirement R1

## General Relativity Recovery

Any Integrity Tensor candidate must satisfy:

r_c → 0

↓

Iμν → 0

Result:

The TIG field equation must reduce to:

Gμν = 0

Requirement Status:

MANDATORY

---

# Requirement R2

## Schwarzschild Recovery

For:

r ≫ r_c

the Integrity Tensor contribution must vanish sufficiently rapidly.

Result:

The Schwarzschild solution must be recovered.

Requirement Status:

MANDATORY

---

# Requirement R3

## Newtonian Recovery

The weak-field limit must remain unchanged.

Result:

Classical gravitational dynamics must be preserved.

Requirement Status:

MANDATORY

---

# Requirement R4

## Horizon Consistency

The Integrity Tensor must reproduce the validated TIG horizon structure.

Required Result:

x³ − x² + β³ = 0

Requirement Status:

MANDATORY

---

# Requirement R5

## Critical Transition Preservation

The Integrity Tensor must preserve the validated critical point:

x_c = 2/3

β_c = (4/27)^(1/3)

Requirement Status:

MANDATORY

---

# Requirement R6

## Finite Curvature

The Integrity Tensor must prevent curvature divergence within the validated spherical realization.

Required Result:

Finite curvature invariants.

Requirement Status:

MANDATORY

---

# Requirement R7

## Admissibility Compatibility

The Integrity Tensor must remain compatible with the TIG admissibility framework.

Integrity must constrain geometry.

Geometry must not define integrity.

Requirement Status:

MANDATORY

---

# Requirement R8

## Covariant Compatibility

A future covariant extension must remain possible.

The tensor may not contain assumptions that prohibit general covariance.

Requirement Status:

MANDATORY

---

# Requirement R9

## Structural Minimality

The Integrity Tensor should introduce the minimum number of new structures required for consistency.

Requirement Status:

DESIRABLE

---

# Requirement R10

## Independent Definition

The Integrity Tensor should eventually admit a definition independent of the current effective mass realization.

Requirement Status:

PRIMARY RESEARCH OBJECTIVE

---

# Current Assessment

At present, the requirements are known.

The tensor itself remains unresolved.

The next stage is candidate generation.

---
