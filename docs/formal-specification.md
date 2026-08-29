# ACFA Formal Specification

## 1. Purpose

This document defines the formal specification of the Adaptive Cognitive Field Architecture (ACFA).

ACFA is a minimal, deterministic and testable framework for representing state transitions, constraints, utility evaluation and measurable system behavior.

ACFA does not define intelligence, consciousness, emotion, memory or learning.

---

## 2. Scope

The ACFA core specification defines:

- State
- Transition
- Constraints
- Utility
- Transition Utility
- Metrics
- Benchmark execution
- Validation requirements

The specification is implementation-independent.

A conforming implementation must preserve the mathematical and behavioral properties defined in this document.

---

## 3. State

A state is a finite mapping of named variables to values.

Formally:

\[
S = \{x_1:v_1, x_2:v_2, ..., x_n:v_n\}
\]

where:

- \(x_i\) is a variable name
- \(v_i\) is its associated value
- \(n \geq 0\)

A state MUST be explicitly representable and comparable.

---

## 4. State Transition

A transition represents a directed change from one state to another.

\[
T = (S_{source}, S_{target})
\]

where:

- \(S_{source}\) is the source state
- \(S_{target}\) is the target state

A transition does not imply causality.

It only represents an observable relationship between two states.

---

## 5. Transition Validity

A transition is structurally valid when:

\[
S_{source} \neq null
\]

and

\[
S_{target} \neq null
\]

An implementation MUST reject invalid transition objects.

---

## 6. Constraints

A constraint defines a condition that a state or transition must satisfy.

Formally:

\[
C(S) \rightarrow \{True, False\}
\]

or, for transitions:

\[
C(T) \rightarrow \{True, False\}
\]

A constraint MUST produce a deterministic boolean result for the same input.

---

## 7. Utility

A utility is a measurable scalar function over a state.

\[
U(S) \rightarrow \mathbb{R}
\]

Each utility has:

- a unique name within an evaluation set
- a deterministic evaluation function
- a numeric result

The result MUST be representable as a finite floating-point value.

---

## 8. Transition Utility

A transition utility evaluates a transition instead of a single state.

\[
U_T(T) \rightarrow \mathbb{R}
\]

A transition utility may measure changes between source and target states.

Example:

\[
U_{energy}(T)
=
energy(S_{target}) - energy(S_{source})
\]

---

## 9. Utility Result

A utility evaluation produces a result containing:

- individual utility values
- total utility

For utilities:

\[
R = (V, Total)
\]

where:

\[
V = \{(name_i,value_i)\}
\]

and:

\[
Total = \sum_i value_i
\]

If no utilities are supplied:

\[
Total = 0
\]

and the result contains no utility values.

---

## 10. Transition Utility Result

Transition utility evaluation follows the same aggregation rule:

\[
Total_T = \sum_i U_i(T)
\]

If the evaluated utilities contain opposing values, the total is their algebraic sum.

For example:

\[
-0.2 + 0.2 = 0
\]

---

## 11. Numeric Requirements

Utility and metric results MUST be finite.

The following values are invalid:

- NaN
- positive infinity
- negative infinity

An implementation MUST raise a validation error when a utility evaluates to a non-finite value.

---

## 12. Metrics

Metrics provide observable measurements over transitions.

A transition metric MAY include:

- changed variable count
- total variable count
- change ratio

Metrics MUST NOT introduce domain-specific interpretations.

---

## 13. Changed Variable Count

For a transition:

\[
T=(S_{source},S_{target})
\]

the changed variable count is:

\[
N_{changed}
=
|\{x : S_{source}(x) \neq S_{target}(x)\}|
\]

Only variables present in the comparison domain are considered.

---

## 14. Change Ratio

The change ratio is:

\[
R_{change}
=
\frac{N_{changed}}{N_{total}}
\]

where \(N_{total}\) is the number of variables considered by the metric.

If:

\[
N_{total}=0
\]

the implementation MUST define the result as:

\[
R_{change}=0
\]

---

## 15. Benchmark

A benchmark is a repeatable evaluation over a collection of transitions.

\[
B = \{T_1,T_2,...,T_n\}
\]

The benchmark MUST produce deterministic summary metrics for deterministic input.

---

## 16. Benchmark Result

A benchmark result contains:

- transition count
- total changes
- mean change ratio

Formally:

\[
Count(B)=n
\]

\[
Changes(B)=\sum_{i=1}^{n}N_{changed}(T_i)
\]

and, when \(n>0\):

\[
MeanRatio(B)
=
\frac{1}{n}
\sum_{i=1}^{n}R_{change}(T_i)
\]

---

## 17. Empty Benchmark

For an empty benchmark:

\[
n=0
\]

the required result is:

\[
transition\_count=0
\]

\[
total\_changes=0
\]

\[
mean\_change\_ratio=0.0
\]

An implementation MUST NOT divide by zero.

---

## 18. Determinism

For identical input states, transitions, utilities and constraints, a conforming implementation MUST produce identical results.

No implicit randomness is permitted in the ACFA core.

---

## 19. Immutability

Core ACFA data structures SHOULD behave as immutable values after construction.

Evaluation functions MUST NOT mutate the input state or transition.

---

## 20. Referential Transparency

A pure utility function SHOULD return the same result for the same input.

Conceptually:

\[
f(x)=y
\]

for every identical evaluation of \(x\).

Side effects MUST NOT be required for core evaluation.

---

## 21. Validation

Validation MUST occur at the boundaries of the system.

Invalid inputs MUST produce explicit errors rather than silently producing undefined results.

Validation includes:

- structural validity
- numeric validity
- required fields
- constraint validity
- transition validity

---

## 22. Error Handling

Errors MUST be explicit and deterministic.

An implementation MUST NOT silently convert invalid numerical results into zero.

An implementation MUST NOT silently discard invalid utility values.

---

## 23. Variable Comparison

State comparison MUST use the defined variable names and values.

A variable is considered changed when its source and target values are not equal under the implementation's documented equality semantics.

---

## 24. Missing Variables

When a metric compares state variables, the implementation MUST define how missing variables are handled.

The reference implementation treats the comparison domain consistently across source and target states.

Missing values MUST NOT produce undefined numerical results.

---

## 25. Utility Naming

Utility names MUST be non-empty identifiers.

Within a single evaluation collection, utility names SHOULD be unique.

Duplicate names SHOULD be rejected or handled according to the implementation's documented policy.

---

## 26. Utility Aggregation

Utility aggregation is additive.

For:

\[
U_1,U_2,...,U_n
\]

the total is:

\[
Total=\sum_{i=1}^{n}U_i
\]

No implicit weighting is applied by the ACFA core.

---

## 27. Weighting

Weighted utilities are outside the minimal ACFA core specification unless explicitly introduced by a future specification revision.

The base utility model assumes:

\[
w_i=1
\]

for every utility.

---

## 28. Constraints and Evaluation

Constraints determine whether an input satisfies a defined condition.

Constraint evaluation MUST NOT modify the evaluated state.

A failed constraint MUST be observable to the caller.

---

## 29. Transition Evaluation

A transition MAY be evaluated through:

- structural validation
- constraints
- transition utilities
- transition metrics

These operations are logically independent.

A metric MUST NOT implicitly alter a transition.

---

## 30. Benchmark Reproducibility

A benchmark MUST be reproducible when supplied with identical input.

The benchmark runner MUST safely support finite iterables and one-shot iterators.

Input transitions MUST be materialized when necessary to prevent accidental multiple-consumption errors.

---

## 31. Reference Implementation

The reference implementation is written in Python.

The implementation MUST remain aligned with this formal specification.

The reference implementation provides:

- `State`
- `Transition`
- `Utility`
- `TransitionUtility`
- `UtilityResult`
- `Constraint`
- transition metrics
- benchmark execution

---

## 32. Testing Requirements

A conforming implementation SHOULD test:

- normal state construction
- state comparison
- transition construction
- utility evaluation
- transition utility evaluation
- NaN rejection
- infinite-value rejection
- empty utility collections
- empty benchmark collections
- metric calculation
- benchmark aggregation
- deterministic behavior

---

## 33. Benchmark Validation

Benchmark results MUST be validated against independently calculable expected values.

For example, given three transitions with change ratios:

\[
1.0,\frac{1}{2},\frac{1}{2}
\]

the mean change ratio is:

\[
\frac{1.0+0.5+0.5}{3}
=
\frac{2}{3}
\]

or approximately:

\[
0.6666666667
\]

---

## 34. Reference Benchmark

The reference benchmark uses three transitions:

\[
T_1:
(energy=1.0,focus=0.5)
\rightarrow
(energy=0.8,focus=0.7)
\]

\[
T_2:
(energy=0.8,focus=0.7)
\rightarrow
(energy=0.9,focus=0.7)
\]

\[
T_3:
(energy=0.9,focus=0.7)
\rightarrow
(energy=0.9,focus=0.6)
\]

The expected transition count is:

\[
3
\]

The expected total number of changed variables is:

\[
4
\]

The expected mean change ratio is:

\[
\frac{2}{3}
\approx
0.6666666667
\]

---

## 35. Compatibility

Future ACFA implementations MAY extend the system, but extensions MUST NOT invalidate the semantics of the core specification.

Extensions SHOULD remain modular and independently testable.

---

## 36. Versioning

Changes to the mathematical meaning of existing ACFA concepts require a specification revision.

Non-semantic documentation improvements MAY be made without changing the specification version.

---

## 37. Core Principle

ACFA defines observable state transitions and measurable evaluation.

It does not claim that these measurements represent intelligence, consciousness, emotion, agency or subjective experience.

The specification is intentionally minimal.

---

## 38. Conformance

An implementation conforms to this specification when:

1. Core entities are represented correctly.
2. State transitions are deterministic.
3. Utility evaluation produces finite numerical results.
4. Invalid numerical results are rejected.
5. Utility aggregation follows additive semantics.
6. Transition metrics follow the defined formulas.
7. Empty collections are handled safely.
8. Benchmark results are reproducible.
9. Evaluation does not mutate input data.
10. Tests verify the defined behavior.

---

## 39. Non-Goals

The ACFA core does not define:

- memory
- learning
- language models
- neural networks
- resonance
- attention
- consciousness
- emotions
- personality
- user interfaces
- web services
- authentication
- billing

These concerns belong to higher-level systems built on top of ACFA.

---

## 40. Relationship to Higher-Level Systems

ACFA is designed to function as an independent computational standard.

A higher-level system may use ACFA as a formal state-transition and evaluation layer.

Such systems may add memory, planning, reasoning, resonance, knowledge or language-model integration without changing the ACFA core.

---

## 41. Mathematical Consistency

All quantities defined by this specification MUST have well-defined domains and results.

Undefined operations MUST be rejected or explicitly defined by the specification.

Division by zero MUST NOT occur in conforming benchmark calculations.

---

## 42. Implementation Independence

The mathematical definitions in this document are normative.

Python is the current reference implementation language, but the specification does not require implementations to use Python.

Equivalent implementations MAY be created in other programming languages.

---

## 43. Reference Status

This document defines the formal behavioral contract for the ACFA core.

The reference implementation and test suite serve as executable validation of the specification.

Discrepancies between implementation and specification MUST be resolved explicitly rather than implicitly changing semantics.

---

## 44. Final Definition

ACFA can be reduced to the following core abstraction:

\[
State
\rightarrow
Transition
\rightarrow
Evaluation
\rightarrow
Metrics
\rightarrow
Validation
\]

The architecture remains intentionally small so that each component can be independently tested, measured and extended.

---

## 45. End of Specification

ACFA Formal Specification

Version: 1.0

Status: Reference Specification
