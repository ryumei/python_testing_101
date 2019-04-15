# -*- coding: utf-8 -*-
from mypkg.leap import *

def test_leap_year():
    assert is_leap(2019) == False
    assert is_leap(2020) == True
    assert is_leap(2021) == False

def test_next_leap_year():
    assert next_leap_year(2019) == 2020
