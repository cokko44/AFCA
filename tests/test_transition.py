from acfa.state import State
from acfa.transition import Transition


def test_transition_creation():
    source = State({
        "energy": 1.0,
    })

    target = State({
        "energy": 0.8,
    })

    transition = Transition(source, target)

    assert transition.source == source
    assert transition.target == target


def test_transition_apply():
    source = State({
        "energy": 1.0,
    })

    target = State({
        "energy": 0.8,
    })

    transition = Transition(source, target)

    assert transition.apply() == target


def test_changed_keys():
    source = State({
        "energy": 1.0,
        "focus": 0.5,
    })

    target = State({
        "energy": 0.8,
        "focus": 0.5,
    })

    transition = Transition(source, target)

    assert transition.changed_keys() == frozenset({"energy"})


def test_changed_keys_detects_added_value():
    source = State({
        "energy": 1.0,
    })

    target = State({
        "energy": 1.0,
        "focus": 0.5,
    })

    transition = Transition(source, target)

    assert transition.changed_keys() == frozenset({"focus"})


def test_changed_keys_detects_removed_value():
    source = State({
        "energy": 1.0,
        "focus": 0.5,
    })

    target = State({
        "energy": 1.0,
    })

    transition = Transition(source, target)

    assert transition.changed_keys() == frozenset({"focus"})


def test_identity_transition():
    state = State({
        "energy": 1.0,
    })

    transition = Transition(state, state)

    assert transition.is_identity()


def test_non_identity_transition():
    source = State({
        "energy": 1.0,
    })

    target = State({
        "energy": 0.5,
    })

    transition = Transition(source, target)

    assert not transition.is_identity()


def test_has_changed():
    source = State({
        "energy": 1.0,
        "focus": 0.5,
    })

    target = State({
        "energy": 0.8,
        "focus": 0.5,
    })

    transition = Transition(source, target)

    assert transition.has_changed("energy")
    assert not transition.has_changed("focus")


def test_from_transform():
    source = State({
        "energy": 1.0,
    })

    transition = Transition.from_transform(
        source,
        lambda state: state.with_value("energy", 0.5),
    )

    assert transition.source == source
    assert transition.target.get("energy") == 0.5


def test_from_transform_requires_state():
    source = State({
        "energy": 1.0,
    })

    try:
        Transition.from_transform(
            source,
            lambda state: {"energy": 0.5},
        )
    except TypeError:
        return

    raise AssertionError(
        "Expected TypeError when transform does not return State."
    )
