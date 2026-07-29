"""Simple calculator: reads two numbers and prints basic results.

This version consolidates the arithmetic into a single `compute_results`
function, uses explicit None checks (so 0 is handled correctly),
and improves input parsing and division-by-zero handling.
"""

from typing import Optional, Dict


def compute_results(a: float | None, b: float | None) -> Dict[str, Optional[float]]:
    if a is None or b is None:
        return {"addition": None, "subtraction": None, "multiplication": None, "division": None}
    results = {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": None if b == 0 else a / b,
    }
    return results


def main() -> None:
    try:
        no1 = float(input("Enter first number: "))
        no2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    results = compute_results(no1, no2)
    print(f"addition : {results['addition']}")
    print(f"subtraction : {results['subtraction']}")
    print(f"multiplication : {results['multiplication']}")
    div = results["division"]
    print(f"division : {div if div is not None else 'undefined (division by zero)'}")


if __name__ == "__main__":
    main()




