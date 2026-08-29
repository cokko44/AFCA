from acfa.metrics import (
    numeric_distance,
    state_delta,
    transition_metrics,
)
from acfa.state import State
from acfa.transition import Transition


def test_transition_metrics_detect_changes():
    source = State({
        "energy": 1.0,
        "focus": 0.5,
    })

    target = State({
        "energy": 0.8,
        "focus": 0.7,
    })

    transition = Transition(source, target)

    metrics = transition_metrics(transition)

    assert metrics.changed_count == 2
    assert metrics.source_size == 2
    assert metrics.target_size == 2
    assert metrics.change_ratio == 1.0


def test_transition_metrics_identity():
    state = State({
        "energy": 1.0,
    })

    transition = Transition(state, state)

    metrics = transition_metrics(transition)

    assert metrics.changed_count == 0
    assert metrics.change_ratio == 0.0


def test_numeric_distance():
    source = State({
        "x": 0.0,
        "y": 0.0,
    })

    target = State({
        "x": 3.0,
        "y": 4.0,
    })

    assert numeric_distance(source, target) == 5.0


def test_numeric_distance_ignores_non_numeric_values():
    source = State({
        "x": 1.0,
        "label": "a",
    })

    target = State({
        "x": 4.0,
        "label": "b",
    })

    assert numeric_distance(source, target) == 3.0


def test_state_delta():
    source = State({
        "energy": 1.0,
        "focus": 0.5,
    })

    target = State({
        "energy": 0.8,
        "focus": 0.5,
    })

    delta = state_delta(source, target)

    assert delta == {
        "energy": (1.0, 0.8),
    }
