from insert_sort import sorter
import pytest


def test_sorter():
    xlist = [12, 45, 23, 98, 54, 234]
    x = sorter(xlist)
    assert x == range(10)
