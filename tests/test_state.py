from acfa.state import State


def test_state_creation():
    state = State({
        "energy": 1.0,
        "focus": 0.5,
    })

    assert state.get("energy") == 1.0
    assert state.get("focus") == 0.5


def test_state_get_default():
    state = State({
        "energy": 1.0,
    })

    assert state.get("missing") is None
    assert state.get("missing", 42) == 42


def test_state_has():
    state = State({
        "energy": 1.0,
    })

    assert state.has("energy")
    assert not state.has("missing")


def test_state_with_value_returns_new_state():
    state = State({
        "energy": 1.0,
    })

    new_state = state.with_value("energy", 0.5)

    assert state.get("energy") == 1.0
    assert new_state.get("energy") == 0.5
    assert state is not new_state


def test_state_without_returns_new_state():
    state = State({
        "energy": 1.0,
        "focus": 0.5,
    })

    new_state = state.without("energy")

    assert state.has("energy")
    assert not new_state.has("energy")
    assert new_state.has("focus")


def test_state_to_dict():
    state = State({
        "energy": 1.0,
        "focus": 0.5,
    })

    values = state.to_dict()

    assert values == {
        "energy": 1.0,
        "focus": 0.5,
    }


def test_state_contains():
    state = State({
        "energy": 1.0,
    })

    assert "energy" in state
    assert "missing" not in state


def test_state_length():
    state = State({
        "energy": 1.0,
        "focus": 0.5,
    })

    assert len(state) == 2
