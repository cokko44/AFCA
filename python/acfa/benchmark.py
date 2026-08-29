"""
ACFA - Benchmark
================

Benchmark utilities for the Adaptive Cognitive Field Architecture.

Benchmarks provide repeatable experiments over ACFA state transitions.
They measure observable system behavior without making claims about
intelligence, consciousness, emotion, or other domain-specific concepts.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .metrics import TransitionMetrics, transition_metrics
from .transition import Transition


@dataclass(frozen=True, slots=True)
class BenchmarkResult:
    """
    Summary of a benchmark run.

    Attributes
    ----------
    transition_count:
        Number of transitions evaluated.
    total_changes:
        Total number of changed state variables.
    mean_change_ratio:
        Mean ratio of changed variables across transitions.
    """

    transition_count: int
    total_changes: int
    mean_change_ratio: float


def run_benchmark(
    transitions: Iterable[Transition],
) -> BenchmarkResult:
    """
    Evaluate a collection of transitions.

    The input transitions are materialized once so generators and other
    one-shot iterables are supported safely.
    """
    transition_list = tuple(transitions)

    metrics: tuple[TransitionMetrics, ...] = tuple(
        transition_metrics(transition)
        for transition in transition_list
    )

    transition_count = len(metrics)

    total_changes = sum(
        metric.changed_count
        for metric in metrics
    )

    mean_change_ratio = (
        sum(metric.change_ratio for metric in metrics)
        / transition_count
        if transition_count > 0
        else 0.0
    )

    return BenchmarkResult(
        transition_count=transition_count,
        total_changes=total_changes,
        mean_change_ratio=mean_change_ratio,
    )


def benchmark_single(
    transition: Transition,
) -> BenchmarkResult:
    """
    Run a benchmark containing a single transition.
    """
    return run_benchmark((transition,))
