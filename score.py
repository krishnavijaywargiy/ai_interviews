"""Automated scoring for the document-ingestion coding interview."""

import re
import subprocess
import sys
from typing import Tuple

TASKS = [
    ("task_setup", "Environment Setup", 10),
    ("task_pydantic", "Pydantic Models", 15),
    ("task_fastapi", "FastAPI Endpoints", 15),
    ("task_python", "Python Fundamentals", 10),
    ("task_exceptions", "Exception Handling", 15),
    ("task_testing", "Write Tests", 15),
]


def run_tests(marker: str) -> Tuple[int, int, int]:
    """Run tests for a marker and return passed, failed, and error counts."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "-m", marker, "-q", "--tb=no", "--no-header"],
            capture_output=True,
            text=True,
        )
    except OSError:
        return 0, 0, 0

    output = result.stdout + result.stderr
    if "No module named pytest" in output or "pytest: command not found" in output:
        return 0, 0, 0

    def count(pattern: str) -> int:
        match = re.search(pattern, output)
        return int(match.group(1)) if match else 0

    return count(r"(\d+) passed"), count(r"(\d+) failed"), count(r"(\d+) error")


def score() -> Tuple[int, int]:
    """Score the interview across all tasks."""
    total_possible = sum(points for _, _, points in TASKS)
    total_earned = 0

    print("=" * 60)
    print(" SCORING: Document Ingestion Coding Interview")
    print("=" * 60)
    for task, name, points in TASKS:
        passed, failed, errors = run_tests(task)
        total_tests = passed + failed + errors
        if total_tests == 0:
            status = "SKIP"
            earned = 0
        elif failed == 0 and errors == 0:
            status = "PASS"
            earned = points
        else:
            status = "PARTIAL" if passed else "FAIL"
            earned = int(passed / total_tests * points)
        total_earned += earned
        print(f"{name:<25} {status:<10} {earned:>2}/{points} pts  ({passed}/{total_tests} tests)")

    percentage = round(100 * total_earned / total_possible)
    print("-" * 60)
    print(f"{'TOTAL':<25} {percentage:>9}% {total_earned:>2}/{total_possible} pts")
    print("=" * 60)
    return total_earned, total_possible


if __name__ == "__main__":
    score()
    sys.exit(0)
