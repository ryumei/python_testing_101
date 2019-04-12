# -*- coding: utf-8 -*-
import pytest
from arithmetic import *

@pytest.mark.parametrize('p,q,expected', [
    (0, 0, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 2),
    # floating point
    (1.5, 1.5, 3),
])
def test_add(p, q, expected):
    assert add(p, q) == expected

@pytest.mark.parametrize('p,q,exception', [
    (0, "0", TypeError),
    ("0", 0, TypeError),
    ("0", "0", TypeError),
])
def test_add_exceptions(p, q, exception):
    with pytest.raises(exception):
        add(p, q)



