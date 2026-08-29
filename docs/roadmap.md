# ACFA Roadmap

**Adaptive Cognitive Field Architecture**

**Status:** Active Development  
**Current Version:** v1.0 Core Candidate

---

## 1. Foundation

- [x] Repository initialized
- [x] Reference Mathematics v1.0
- [x] Formal Specification
- [x] Architecture Definition
- [x] Validation Specification

---

## 2. Reference Implementation

- [x] State model
- [x] Transition model
- [x] Constraints
- [x] Utility
- [x] Metrics
- [x] Benchmark engine
- [x] Python package structure
- [x] Automated test suite

---

## 3. Benchmark Suite

- [x] Benchmark specification
- [x] Reference benchmark
- [x] Benchmark runner
- [x] Sample benchmark results
- [x] Deterministic result generation
- [x] CI benchmark execution

---

## 4. Experimental Validation

- [x] Validation methodology
- [x] Reproducibility requirements
- [x] Observable transition measurements
- [x] Regression testing
- [ ] Extended benchmark scenarios
- [ ] Cross-implementation validation
- [ ] Independent replication

---

## 5. Core Stabilization

- [ ] Freeze mathematical core
- [ ] Freeze formal specification
- [ ] Finalize API surface
- [ ] Finalize reference implementation
- [ ] Complete documentation consistency review
- [ ] Full test and benchmark verification

---

## 6. Release v1.0.0

- [ ] Final repository audit
- [ ] Final README review
- [ ] Final CHANGELOG update
- [ ] License verification
- [ ] CI fully green
- [ ] Create Git tag v1.0.0
- [ ] Publish first GitHub release

---

## 7. Research Publication

- [ ] Prepare technical research paper
- [ ] Document mathematical foundations
- [ ] Document benchmark methodology
- [ ] Document validation results
- [ ] Publish reproducibility materials
- [ ] Prepare archival research release

---

## 8. Python Package

- [ ] Prepare package metadata
- [ ] Validate installation from clean environment
- [ ] Build distribution artifacts
- [ ] Publish `acfa` package
- [ ] Verify installation from package index

---

## 9. Long-Term Research

- [ ] Larger benchmark suite
- [ ] Independent implementations
- [ ] Comparative experiments
- [ ] Extended transition models
- [ ] Formal property testing
- [ ] Performance evaluation
- [ ] Community contributions
- [ ] Research collaborations

---

## 10. Relationship With Nunaye

ACFA remains an independent mathematical and computational standard.

NexusCore is the reference implementation.

Nunaye may use ACFA as a computational foundation, but ACFA itself does
not depend on Nunaye.

The ACFA core does not include:

- memory systems
- resonance systems
- LLM adapters
- user interfaces
- web services
- application-specific logic

These belong to higher-level systems built on top of ACFA.

---

## 11. Development Principle

ACFA development follows the sequence:

```text
Mathematics
    ↓
Formal Specification
    ↓
Reference Implementation
    ↓
Tests
    ↓
Benchmarks
    ↓
Validation
    ↓
Release
    ↓
Independent Research
