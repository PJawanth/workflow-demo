import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

import math
import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_add_integers(calc):
    assert calc.add(2, 3) == 5


def test_add_floats(calc):
    assert math.isclose(calc.add(2.5, 0.1), 2.6)


def test_subtract_negative(calc):
    assert calc.subtract(3, 5) == -2


def test_multiply_zero(calc):
    assert calc.multiply(10, 0) == 0


def test_multiply_negatives(calc):
    assert calc.multiply(-4, -3) == 12


def test_divide_basic(calc):
    assert calc.divide(10, 2) == 5


def test_divide_float_result(calc):
    assert math.isclose(calc.divide(3, 2), 1.5)


def test_divide_by_zero_raises(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)


def test_large_integers(calc):
    big = 10**18
    assert calc.add(big, big) == 2 * big
    assert calc.multiply(big, 2) == 2 * big


def test_edge_negative_division(calc):
    assert calc.divide(-9, 3) == -3
