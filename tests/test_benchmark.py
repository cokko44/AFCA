from acfa.benchmark import benchmark_single, run_benchmark
from acfa.state import State
from acfa.transition import Transition


def test_run_benchmark():
    source = State({
        "energy": 1.0,
        "focus": 0.5,
    })

    target = State({
        "energy": 0.8,
        "focus": 0.7,
    })

    transition = Transition(source, target)

    result = run_benchmark([transition])

    assert result.transition_count == 1
    assert result.total_changes == 2
    assert result.mean_change_ratio == 1.0


def test_run_benchmark_multiple_transitions():
    state_a = State({
        "energy": 1.0,
        "focus": 0.5,
    })

    state_b = State({
        "energy": 0.8,
        "focus": 0.5,
    })

    state_c = State({
        "energy": 0.8,
        "focus": 0.9,
    })

    transitions = [
        Transition(state_a, state_b),
        Transition(state_b, state_c),
    ]

    result = run_benchmark(transitions)

    assert result.transition_count == 2
    assert result.total_changes == 2
    assert result.mean_change_ratio == 0.5


def test_run_benchmark_empty():
    result = run_benchmark([])

    assert result.transition_count == 0
    assert result.total_changes == 0
    assert result.mean_change_ratio == 0.0


def test_benchmark_single():
    source = State({
        "value": 1.0,
    })

    target = State({
        "value": 2.0,
    })

    transition = Transition(source, target)

    result = benchmark_single(transition)

    assert result.transition_count == 1
    assert result.total_changes == 1
    assert result.mean_change_ratio == 1.0
