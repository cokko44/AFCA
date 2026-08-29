import pytest

from acfa.state import State
from acfa.transition import Transition
from acfa.utility import (
    Utility,
    TransitionUtility,
    UtilityResult,
    evaluate_utilities,
    evaluate_transition_utilities,
)


def test_utility_evaluation():
    state = State({
        "energy": 0.8,
    })

    utility = Utility(
        name="energy",
        function=lambda s: s.get("energy", 0.0),
    )

    assert utility.evaluate(state) == 0.8


def test_utility_converts_result_to_float():
    state = State({
        "value": 5,
    })

    utility = Utility(
        name="value",
        function=lambda s: s.get("value"),
    )

    assert utility.evaluate(state) == 5.0
    assert isinstance(utility.evaluate(state), float)


def test_utility_rejects_nan():
    state = State({
        "value": 1.0,
    })

    utility = Utility(
        name="invalid",
        function=lambda s: float("nan"),
    )

    try:
        utility.evaluate(state)
    except ValueError:
        return

    raise AssertionError("Expected ValueError for NaN utility.")


def test_evaluate_utilities():
    state = State({
        "energy": 0.8,
        "focus": 0.6,
    })

    utilities = [
        Utility(
            name="energy",
            function=lambda s: s.get("energy", 0.0),
        ),
        Utility(
            name="focus",
            function=lambda s: s.get("focus", 0.0),
        ),
    ]

    result = evaluate_utilities(state, utilities)

    assert isinstance(result, UtilityResult)
    assert result.total == 1.4
    assert result.get("energy") == 0.8
    assert result.get("focus") == 0.6


def test_utility_result_default():
    result = UtilityResult(
        total=1.0,
        values=(("energy", 1.0),),
    )

    assert result.get("missing") == 0.0
    assert result.get("missing", -1.0) == -1.0


def test_empty_utilities():
    state = State({
        "value": 1.0,
    })

    result = evaluate_utilities(state, [])

    assert result.total == 0.0
    assert result.values == ()


def test_transition_utility_evaluation():
    source = State({
        "energy": 1.0,
    })

    target = State({
        "energy": 0.8,
    })

    transition = Transition(source, target)

    utility = TransitionUtility(
        name="energy_change",
        function=lambda t: (
            t.target.get("energy")
            - t.source.get("energy")
        ),
    )

    assert utility.evaluate(transition) == pytest.approx(-0.2)


def test_evaluate_transition_utilities():
    source = State({
        "energy": 1.0,
        "focus": 0.5,
    })

    target = State({
        "energy": 0.8,
        "focus": 0.7,
    })

    transition = Transition(source, target)

    utilities = [
        TransitionUtility(
            name="energy_change",
            function=lambda t: (
                t.target.get("energy")
                - t.source.get("energy")
            ),
        ),
        TransitionUtility(
            name="focus_change",
            function=lambda t: (
                t.target.get("focus")
                - t.source.get("focus")
            ),
        ),
    ]

    result = evaluate_transition_utilities(
        transition,
        utilities,
    )

    assert result.total == 0.0
    assert result.get("energy_change") == pytest.approx(-0.2)
    assert result.get("focus_change") == pytest.approx(0.2)


def test_empty_transition_utilities():
    source = State({
        "value": 1.0,
    })

    target = State({
        "value": 2.0,
    })

    transition = Transition(source, target)

    result = evaluate_transition_utilities(
        transition,
        [],
    )

    assert result.total == 0.0
    assert result.values == ()
