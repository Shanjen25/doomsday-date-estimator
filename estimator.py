#!/usr/bin/env python3
"""
Doomsday Date Estimator
A simple probabilistic model for educational purposes.
"""

import math
from datetime import datetime

CURRENT_YEAR = datetime.now().year

def estimate(p_annual: float):
    """Given annual probability p, return expected and median years."""
    if p_annual <= 0 or p_annual >= 1:
        raise ValueError("Annual probability must be between 0 and 1 (exclusive)")

    expected_years = 1.0 / p_annual
    median_years = math.log(2) / p_annual  # ln(2) ≈ 0.693

    expected_date = CURRENT_YEAR + expected_years
    median_date = CURRENT_YEAR + median_years

    return {
        "annual_p": p_annual,
        "expected_years": expected_years,
        "median_years": median_years,
        "expected_year": expected_date,
        "median_year": median_date,
    }

def print_result(label: str, result: dict):
    print(f"\n=== {label} ===")
    print(f"Annual probability: {result['annual_p']*100:.4f}%")
    print(f"Expected waiting time: {result['expected_years']:.1f} years → ~{result['expected_year']:.0f}")
    print(f"Median (50% cumulative chance by): {result['median_years']:.1f} years → ~{result['median_year']:.0f}")

def main():
    print("Doomsday Date Estimator")
    print("=" * 40)
    print(f"Current year: {CURRENT_YEAR}")
    print("\nThis is a toy model using a constant annual hazard rate.")
    print("It is NOT a prediction. Risks can change with policy and technology.\n")

    # Preset scenarios based on literature
    scenarios = [
        ("Nuclear catastrophe (expert median-ish, ~0.25%/yr)", 0.0025),
        ("Nuclear significant event (higher estimate ~1%/yr)", 0.01),
        ("Existential nuclear risk (very low end ~0.01%/century)", 0.000001),
        ("Natural extinction upper bound (~1/14000 per year)", 1/14000),
        ("Natural extinction more typical bound (~1/87000)", 1/87000),
        ("Combined illustrative (nuclear dominated ~0.3%/yr)", 0.003),
    ]

    for label, p in scenarios:
        try:
            res = estimate(p)
            print_result(label, res)
        except ValueError as e:
            print(f"Error for {label}: {e}")

    print("\n" + "=" * 40)
    print("Custom input:")
    try:
        user_p = float(input("Enter annual probability (e.g. 0.005 for 0.5%): ").strip())
        res = estimate(user_p)
        print_result("Your custom estimate", res)
    except (ValueError, EOFError):
        print("Skipping custom input.")

    print("\nRemember: these numbers are highly uncertain. Focus on reducing risks.")

if __name__ == "__main__":
    main()
