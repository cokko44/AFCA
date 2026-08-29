from __future__ import annotations

import json
from pathlib import Path

from acfa.benchmark import run_benchmark
from acfa.state import State
from acfa.transition import Transition


def build_benchmark_transitions() -> tuple[Transition, ...]:
    return (
        Transition(
            State({"energy": 1.0, "focus": 0.5}),
            State({"energy": 0.8, "focus": 0.7}),
        ),
        Transition(
            State({"energy": 0.8, "focus": 0.7}),
            State({"energy": 0.9, "focus": 0.7}),
        ),
        Transition(
            State({"energy": 0.9, "focus": 0.7}),
            State({"energy": 0.9, "focus": 0.6}),
        ),
    )


def run() -> dict[str, float | int]:
    result = run_benchmark(build_benchmark_transitions())

    return {
        "transition_count": result.transition_count,
        "total_changes": result.total_changes,
        "mean_change_ratio": result.mean_change_ratio,
    }


def main() -> None:
    results = run()

    output_path = Path(__file__).with_name("sample_results.json")

    output_path.write_text(
        json.dumps(
            results,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
