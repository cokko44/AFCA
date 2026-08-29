"""
ACFA - Transition
=================

Core transition representation for the Adaptive Cognitive Field Architecture.

A Transition describes how one State is transformed into another State.

Design principles:
- Explicit state transition
- Immutable transition records
- Deterministic transformation
- No memory, LLM, resonance, UI or web dependencies
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from .state import State


StateTransformer = Callable[[State], State]


@dataclass(frozen=True, slots=True)
class Transition:
    """
    Represents a state transition in ACFA.

    Parameters
    ----------
    source:
        Initial state.
    target:
        Resulting state.
    """

    source: State
    target: State

    def apply(self) -> State:
        """
        Return the target state produced by this transition.
        """
        return self.target

    def changed_keys(self) -> frozenset[str]:
        """
        Return the set of state variables whose values changed.
        """
        source_values = self.source.values
        target_values = self.target.values

        keys = set(source_values) | set(target_values)

        return frozenset(
            key
            for key in keys
            if source_values.get(key) != target_values.get(key)
        )

    def is_identity(self) -> bool:
        """
        Return True if source and target states are equal.
        """
        return self.source == self.target

    def has_changed(self, key: str) -> bool:
        """
        Return True if a specific state variable changed.
        """
        return (
            self.source.values.get(key) != self.target.values.get(key)
        )

    @classmethod
    def from_transform(
        cls,
        source: State,
        transform: StateTransformer,
    ) -> Transition:
        """
        Create a Transition by applying a transformation to a State.

        The transformer must return a State.
        """
        target = transform(source)

        if not isinstance(target, State):
            raise TypeError(
                "Transition transform must return a State instance."
            )

        return cls(
            source=source,
            target=target,
        )
