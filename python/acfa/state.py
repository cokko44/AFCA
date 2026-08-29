"""
ACFA - State
============

Core state representation for the Adaptive Cognitive Field Architecture.

A State is an immutable snapshot of a system at a given point in time.

Design principles:
- Minimal core
- Explicit state representation
- Deterministic behavior
- No memory, LLM, resonance, UI or web dependencies
"""

from __future__ import annotations

from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Any, Mapping


@dataclass(frozen=True, slots=True)
class State:
    """
    Immutable ACFA system state.

    Parameters
    ----------
    values:
        State variables represented as key-value pairs.
    """

    values: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Freeze the underlying mapping so that State remains immutable.
        """
        object.__setattr__(
            self,
            "values",
            MappingProxyType(dict(self.values)),
        )

    def get(self, key: str, default: Any = None) -> Any:
        """Return a state value."""
        return self.values.get(key, default)

    def has(self, key: str) -> bool:
        """Return True if the state contains the given key."""
        return key in self.values

    def with_value(self, key: str, value: Any) -> State:
        """
        Return a new State with one value changed.

        The current State is never mutated.
        """
        updated = dict(self.values)
        updated[key] = value
        return State(updated)

    def without(self, key: str) -> State:
        """
        Return a new State without the given key.

        The current State is never mutated.
        """
        updated = dict(self.values)
        updated.pop(key, None)
        return State(updated)

    def to_dict(self) -> dict[str, Any]:
        """Return a mutable dictionary copy of the state."""
        return dict(self.values)

    def __contains__(self, key: str) -> bool:
        """Support: 'key' in state."""
        return key in self.values

    def __len__(self) -> int:
        """Return the number of state variables."""
        return len(self.values)
