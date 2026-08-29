"""
ACFA - Metrics
==============

Metrics for measuring state and transition behavior in ACFA.

Metrics describe observable properties of the system.
They do not interpret those properties as intelligence,
consciousness, emotion, or any other domain-specific concept.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Any

from .state import State
from .transition import Transition


@dataclass(frozen=True, slots=True)
class TransitionMetrics:
    """
    Measurable properties of a State transition.

    Attributes
    ----------
    changed_count:
        Number of state variables that changed.
    source_size:
        Number of variables in the source state.
    target_size:
        Number of variables in the target state.
    change_ratio:
        Fraction of involved variables that changed.
    """

    changed_count: int
    source_size: int
    target_size: int
    change_ratio: float


def transition_metrics(transition: Transition) -> TransitionMetrics:
    """
    Calculate basic metrics for a transition.
    """
    changed_count = len(transition.changed_keys())

    total_keys = len(
        set(transition.source.values)
        | set(transition.target.values)
    )

    change_ratio = (
        changed_count / total_keys
        if total_keys > 0
        else 0.0
    )

    return TransitionMetrics(
        changed_count=changed_count,
        source_size=len(transition.source),
        target_size=len(transition.target),
        change_ratio=change_ratio,
    )


def numeric_distance(
    source: State,
    target: State,
) -> float:
    """
    Calculate Euclidean distance between shared numeric state values.

    Non-numeric values are ignored.

    Returns
    -------
    float
        Euclidean distance between numeric variables shared by both states.
    """
    squared_distance = 0.0

    shared_keys = (
        set(source.values)
        & set(target.values)
    )

    for key in shared_keys:
        source_value = source.values[key]
        target_value = target.values[key]

        if (
            isinstance(source_value, (int, float))
            and isinstance(target_value, (int, float))
            and not isinstance(source_value, bool)
            and not isinstance(target_value, bool)
        ):
            difference = float(target_value) - float(source_value)
            squared_distance += difference * difference

    return sqrt(squared_distance)


def state_delta(
    source: State,
    target: State,
) -> dict[str, Any]:
    """
    Return the changed values between two states.

    Only variables whose values differ are included.
    """
    keys = (
        set(source.values)
        | set(target.values)
    )

    return {
        key: (
            source.values.get(key),
            target.values.get(key),
        )
        for key in keys
        if source.values.get(key) != target.values.get(key)
    }
