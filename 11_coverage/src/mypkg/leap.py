# -*- coding: utf-8 -*-
# leap year:
#  * https://en.wikipedia.org/wiki/Leap_year
#  * https://eco.mtk.nao.ac.jp/koyomi/wiki/A5B0A5ECA5B4A5EAA5AACEF1.html
from datetime import date

def is_leap(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True

def next_leap_year(year=None):
    if year is None:
        year = date.today().year
    while True:
        year += 1
        if is_leap(year):
            break
    return year
