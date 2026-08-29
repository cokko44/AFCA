# ACFA Benchmark Specification

**Document Type:** Benchmark Specification

**Scope:** Repeatable Measurement of ACFA State Transitions

**Status:** v1.0

---

## 1. Purpose

This document defines the benchmark specification for the Adaptive Cognitive
Field Architecture (ACFA).

The benchmark system provides a deterministic and reproducible method for
measuring observable properties of state transitions.

The benchmark does not measure or claim:

- intelligence
- consciousness
- emotion
- subjective experience
- general reasoning ability
- biological equivalence

It measures only explicitly defined computational properties.

---

## 2. Benchmark Objectives

The ACFA benchmark system is designed to:

1. evaluate state transitions;
2. measure observable changes;
3. aggregate transition-level metrics;
4. produce reproducible results;
5. support regression testing;
6. provide implementation-independent validation targets.

---

## 3. Benchmark Input

A benchmark consists of an ordered collection of transitions:

\[
B=(T_1,T_2,\ldots,T_n)
\]

where every transition is:

\[
T_i=(S_{source},S_{target})
\]

The benchmark input MUST be explicitly defined.

---

## 4. Benchmark Output

A benchmark produces a `BenchmarkResult` containing:

- `transition_count`
- `total_changes`
- `mean_change_ratio`

The output MUST be deterministic for identical input.

---

## 5. Transition Count

The transition count is:

\[
N_T(B)=n
\]

where \(n\) is the number of transitions evaluated.

For an empty benchmark:

\[
N_T(B)=0
\]

---

## 6. Changed Variable Count

For each transition:

\[
T=(S_s,S_t)
\]

the changed variable count is:

\[
N_c(T)
=
|\{x:S_s(x)\neq S_t(x)\}|
\]

according to the documented state comparison semantics.

---

## 7. Total Changes

The benchmark total change count is:

\[
C_{total}(B)
=
\sum_{i=1}^{n}N_c(T_i)
\]

For an empty benchmark:

\[
C_{total}(B)=0
\]

---

## 8. Change Ratio

For each transition:

\[
R_c(T)
=
\frac{N_c(T)}{N_v(T)}
\]

where:

\[
N_v(T)
=
|Dom(S_s)\cup Dom(S_t)|
\]

If:

\[
N_v(T)=0
\]

the reference result is:

\[
R_c(T)=0
\]

---

## 9. Mean Change Ratio

For a non-empty benchmark:

\[
\overline{R_c}(B)
=
\frac{1}{n}
\sum_{i=1}^{n}R_c(T_i)
\]

For an empty benchmark:

\[
\overline{R_c}(B)=0
\]

The implementation MUST NOT divide by zero.

---

## 10. Result Bounds

Every individual change ratio must satisfy:

\[
0\leq R_c(T)\leq1
\]

Every non-empty benchmark mean must satisfy:

\[
0\leq\overline{R_c}(B)\leq1
\]

A result outside these bounds indicates an implementation error.

---

## 11. Reference Benchmark

The reference benchmark contains three transitions.

### Transition 1

```text
energy: 1.0 → 0.8
focus:  0.5 → 0.7
