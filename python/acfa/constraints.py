"""
ACFA - Constraints
==================

Constraint evaluation for the Adaptive Cognitive Field Architecture.

Constraints define conditions that a State or Transition must satisfy.

Design principles:
- Explicit validation
- Composable constraints
- Deterministic evaluation
- No domain-specific assumptions
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable

from .state import State
from .transition import Transition


ConstraintPredicate = Callable[[State], bool]
TransitionPredicate = Callable[[Transition], bool]


@dataclass(frozen=True, slots=True)
class Constraint:
    """
    A constraint evaluated against a State.

    Parameters
    ----------
    name:
        Human-readable constraint name.
    predicate:
        Function returning True when the constraint is satisfied.
    """

    name: str
    predicate: ConstraintPredicate

    def check(self, state: State) -> bool:
        """Evaluate the constraint against a State."""
        return bool(self.predicate(state))


@dataclass(frozen=True, slots=True)
class TransitionConstraint:
    """
    A constraint evaluated against a Transition.

    Parameters
    ----------
    name:
        Human-readable constraint name.
    predicate:
        Function returning True when the transition is valid.
    """

    name: str
    predicate: TransitionPredicate

    def check(self, transition: Transition) -> bool:
        """Evaluate the constraint against a Transition."""
        return bool(self.predicate(transition))


@dataclass(frozen=True, slots=True)
class ConstraintResult:
    """
    Result of evaluating a collection of constraints.

    Parameters
    ----------
    valid:
        True when every constraint passes.
    failed:
        Names of constraints that failed.
    """

    valid: bool
    failed: tuple[str, ...]

    @property
    def passed(self) -> bool:
        """Alias for valid."""
        return self.valid


def evaluate_constraints(
    state: State,
    constraints: Iterable[Constraint],
) -> ConstraintResult:
    """
    Evaluate all constraints against a State.
    """
    failed = tuple(
        constraint.name
        for constraint in constraints
        if not constraint.check(state)
    )

    return ConstraintResult(
        valid=not failed,
        failed=failed,
    )


def evaluate_transition_constraints(
    transition: Transition,
    constraints: Iterable[TransitionConstraint],
) -> ConstraintResult:
    """
    Evaluate all constraints against a Transition.
    """
    failed = tuple(
        constraint.name
        for constraint in constraints
        if not constraint.check(transition)
    )

    return ConstraintResult(
        valid=not failed,
        failed=failed,
    )
