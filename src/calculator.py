from __future__ import annotations


class Calculator:
    """Basic arithmetic calculator with error handling."""

    def add(self, a: float | int, b: float | int) -> float:
        return a + b

    def subtract(self, a: float | int, b: float | int) -> float:
        return a - b

    def multiply(self, a: float | int, b: float | int) -> float:
        return a * b

    def divide(self, a: float | int, b: float | int) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
