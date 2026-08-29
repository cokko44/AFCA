from acfa.constraints import (
    Constraint,
    ConstraintResult,
    TransitionConstraint,
    evaluate_constraints,
    evaluate_transition_constraints,
)
from acfa.state import State
from acfa.transition import Transition


def test_constraint_passes():
    state = State({
        "energy": 1.0,
    })

    constraint = Constraint(
        name="energy_positive",
        predicate=lambda s: s.get("energy", 0.0) > 0.0,
    )

    assert constraint.check(state)


def test_constraint_fails():
    state = State({
        "energy": -1.0,
    })

    constraint = Constraint(
        name="energy_positive",
        predicate=lambda s: s.get("energy", 0.0) > 0.0,
    )

    assert not constraint.check(state)


def test_evaluate_constraints_all_pass():
    state = State({
        "energy": 1.0,
        "focus": 0.8,
    })

    constraints = [
        Constraint(
            name="energy_positive",
            predicate=lambda s: s.get("energy", 0.0) > 0.0,
        ),
        Constraint(
            name="focus_positive",
            predicate=lambda s: s.get("focus", 0.0) > 0.0,
        ),
    ]

    result = evaluate_constraints(state, constraints)

    assert isinstance(result, ConstraintResult)
    assert result.valid
    assert result.passed
    assert result.failed == ()


def test_evaluate_constraints_reports_failures():
    state = State({
        "energy": -1.0,
        "focus": 0.8,
    })

    constraints = [
        Constraint(
            name="energy_positive",
            predicate=lambda s: s.get("energy", 0.0) > 0.0,
        ),
        Constraint(
            name="focus_positive",
            predicate=lambda s: s.get("focus", 0.0) > 0.0,
        ),
    ]

    result = evaluate_constraints(state, constraints)

    assert not result.valid
    assert not result.passed
    assert result.failed == ("energy_positive",)


def test_transition_constraint_passes():
    source = State({
        "energy": 1.0,
    })

    target = State({
        "energy": 0.8,
    })

    transition = Transition(source, target)

    constraint = TransitionConstraint(
        name="energy_decreases",
        predicate=lambda t: (
            t.target.get("energy") < t.source.get("energy")
        ),
    )

    assert constraint.check(transition)


def test_transition_constraint_fails():
    source = State({
        "energy": 0.8,
    })

    target = State({
        "energy": 1.0,
    })

    transition = Transition(source, target)

    constraint = TransitionConstraint(
        name="energy_decreases",
        predicate=lambda t: (
            t.target.get("energy") < t.source.get("energy")
        ),
    )

    assert not constraint.check(transition)


def test_evaluate_transition_constraints():
    source = State({
        "energy": 1.0,
    })

    target = State({
        "energy": 0.8,
    })

    transition = Transition(source, target)

    constraints = [
        TransitionConstraint(
            name="energy_decreases",
            predicate=lambda t: (
                t.target.get("energy")
                < t.source.get("energy")
            ),
        ),
    ]

    result = evaluate_transition_constraints(
        transition,
        constraints,
    )

    assert result.valid
    assert result.failed == ()


def test_empty_constraints_are_valid():
    state = State({
        "value": 1.0,
    })

    result = evaluate_constraints(state, [])

    assert result.valid
    assert result.passed
    assert result.failed == ()
