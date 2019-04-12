# -*- coding: utf-8 -*-
import pytest
from arithmetic import *

EPSILON = 1e-15

@pytest.mark.parametrize('p,q,expected', [
    (0, 0, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 2),
    # floating point
    (1.5, 1.5, 3),
])
def test_add(p, q, expected):
    assert add(p, q) == pytest.approx(expected)

@pytest.mark.parametrize('p,q,expected', [
    (0, 0, 0),
    (1, 0, 1),
    (0, 1, -1),
    (1, 1, 0),
    # floating point
    (1.5, 1.5, 0.0),
])
def test_subtract(p, q, expected):
    assert subtract(p, q) == pytest.approx(expected)

@pytest.mark.parametrize('p,q,expected', [
    (0, 0, 0),
    (1, 0, 0),
    (0, 1, 0),
    (1, 1, 1),
    # floating point
    (1.5, 1.5, 2.25),
    (1.5, -1.5, -2.25),
    (-1.5, 1.5, -2.25),
    (-1.5, -1.5, 2.25),
])
def test_multiply(p, q, expected):
    assert multiply(p, q) == pytest.approx(expected, rel=EPSILON)

@pytest.mark.parametrize('p,q,expected', [
    (0, 1, 0),
    (1, 1, 1),
    (9, 2, 4),
])
def test_divide(p, q, expected):
    assert divide(p, q) == pytest.approx(expected)

@pytest.mark.parametrize('method,p,q,exception', [
    (add, 0, "0", TypeError),
    (add, "0", 0, TypeError),
    (add, "0", "0", TypeError),
    (subtract, 0, "0", TypeError),
    (subtract, "0", 0, TypeError),
    (subtract, "0", "0", TypeError),
    (multiply, 0, "0", TypeError),
    (multiply, "0", 0, TypeError),
    (multiply, "0", "0", TypeError),
    (divide, 0, "0", TypeError),
    (divide, "0", 0, TypeError),
    (divide, "0", "0", TypeError),
    (divide, 1, 0, ZeroDivisionError),
    (modular, 0, "0", TypeError),
    (modular, "0", 0, TypeError),
    (modular, "0", "0", TypeError),
    (modular, 1, 0, ZeroDivisionError),
])
def test_exceptions(method, p, q, exception):
    with pytest.raises(exception):
        method(p, q)

