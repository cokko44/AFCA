"""
ACFA - Utility
==============

Utility evaluation for the Adaptive Cognitive Field Architecture.

Utility provides a scalar evaluation of a State or Transition.
It does not decide what is "good" universally; it provides an
explicit, deterministic evaluation supplied by the caller.

Design principles:
- Explicit evaluation
- Deterministic scoring
- Composable utility functions
- No domain-specific assumptions
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable

from .state import State
from .transition import Transition


StateUtility = Callable[[State], float]
TransitionUtility = Callable[[Transition], float]


@dataclass(frozen=True, slots=True)
class Utility:
    """
    Utility function evaluated against a State.

    Parameters
    ----------
    name:
        Human-readable utility name.
    function:
        Function returning a numeric utility value.
    """

    name: str
    function: StateUtility

    def evaluate(self, state: State) -> float:
        """Evaluate utility for a State."""
        value = float(self.function(state))

        if not value == value:
            raise ValueError(
                f"Utility '{self.name}' returned NaN."
            )

        return value


@dataclass(frozen=True, slots=True)
class TransitionUtility:
    """
    Utility function evaluated against a Transition.

    Parameters
    ----------
    name:
        Human-readable utility name.
    function:
        Function returning a numeric utility value.
    """

    name: str
    function: TransitionUtility

    def evaluate(self, transition: Transition) -> float:
        """Evaluate utility for a Transition."""
        value = float(self.function(transition))

        if not value == value:
            raise ValueError(
                f"Utility '{self.name}' returned NaN."
            )

        return value


@dataclass(frozen=True, slots=True)
class UtilityResult:
    """
    Result of evaluating multiple utility functions.

    Parameters
    ----------
    total:
        Sum of all utility values.
    values:
        Individual utility values by name.
    """

    total: float
    values: tuple[tuple[str, float], ...]

    def get(self, name: str, default: float = 0.0) -> float:
        """Return a utility value by name."""
        for utility_name, value in self.values:
            if utility_name == name:
                return value

        return default


def evaluate_utilities(
    state: State,
    utilities: Iterable[Utility],
) -> UtilityResult:
    """
    Evaluate multiple utilities against a State.
    """
    values = tuple(
        (utility.name, utility.evaluate(state))
        for utility in utilities
    )

    total = sum(value for _, value in values)

    return UtilityResult(
        total=total,
        values=values,
    )


def evaluate_transition_utilities(
    transition: Transition,
    utilities: Iterable[TransitionUtility],
) -> UtilityResult:
    """
    Evaluate multiple utilities against a Transition.
    """
    values = tuple(
        (utility.name, utility.evaluate(transition))
        for utility in utilities
    )

    total = sum(value for _, value in values)

    return UtilityResult(
        total=total,
        values=values,
    )
