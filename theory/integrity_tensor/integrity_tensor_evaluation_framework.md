# Integrity Tensor Evaluation Framework

## Purpose

This document defines the canonical evaluation framework for all Integrity Tensor Candidates.

The objective is to provide a uniform audit procedure that can be applied to every candidate registered within the TIG Integrity Tensor Program.

Candidate definitions remain stored in:

```text
theory/integrity_tensor/candidates/
```

Candidate registration remains stored in:

```text
integrity_tensor_candidates.md
```

This document defines only the evaluation procedure.

No evaluation results are stored here.

---

# Evaluation Principle

A candidate may only advance if it satisfies the requirements defined in:

```text
integrity_tensor_requirements.md
```

The evaluation process is identical for all candidates.

No candidate receives special treatment.

---

# Evaluation Outcomes

Each requirement receives one of the following classifications:

```text
PASS
```

Requirement satisfied.

---

```text
FAIL
```

Requirement violated.

---

```text
OPEN
```

Insufficient information available.

---

```text
NOT APPLICABLE
```

Requirement not yet testable.

---

# Evaluation Criteria

## R1

General Relativity Recovery

Question:

Does the candidate recover General Relativity in the appropriate limit?

Required Result:

```text
Iμν → 0
```

and

```text
Gμν = 0
```

must be recovered.

---

## R2

Covariance

Question:

Can the candidate be expressed as a covariant rank-two tensor?

Required Result:

Coordinate-independent tensor structure.

---

## R3

Conservation Consistency

Question:

Does the candidate permit conservation consistency?

Required Result:

```text
∇μ Iμν = 0
```

or equivalent consistency condition.

---

## R4

Newtonian Recovery

Question:

Does the candidate recover the Newtonian limit?

Required Result:

Standard weak-field behavior.

---

## R5

Horizon Compatibility

Question:

Can the candidate reproduce the established TIG horizon structure?

Required Result:

```text
x³ − x² + β³ = 0
```

must emerge as a consequence.

---

## R6

Finite Curvature Compatibility

Question:

Can the candidate support bounded-curvature realizations?

Required Result:

No curvature divergence required.

---

## R7

Structural Admissibility

Question:

Does the candidate preserve the TIG admissibility framework?

Required Result:

Admissibility remains fundamental.

---

## R8

Vacuum Compatibility

Question:

Can the candidate support TIG vacuum sectors?

Required Result:

Compatibility with bounded-curvature vacuum realizations.

---

# Candidate Classification

A candidate may be classified as:

```text
EXPLORATORY
```

Initial research concept.

---

```text
CANDIDATE
```

Explicit mathematical realization exists.

---

```text
ADVANCED CANDIDATE
```

Most requirements satisfied.

---

```text
VALIDATED
```

All requirements satisfied.

---

```text
CANONICAL
```

Accepted into the TIG framework.

---

# Promotion Rules

EXPLORATORY → CANDIDATE

Requires:

- explicit mathematical formulation.

---

CANDIDATE → ADVANCED CANDIDATE

Requires:

- majority of requirements satisfied.

---

ADVANCED CANDIDATE → VALIDATED

Requires:

- all requirements satisfied.

---

VALIDATED → CANONICAL

Requires:

- independent review,
- repository approval,
- canonical adoption.

---

# Repository Role

This document defines the official Integrity Tensor evaluation procedure.

All candidate assessments must use this framework.

No evaluation results are stored here.
