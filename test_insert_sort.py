from insert_sort import sorter
import pytest
import random


def test_sorter():
    xlist = [12, 45, 23, 98, 54, 234]
    assert sorter(xlist) == [12, 23, 45, 54, 98, 234]


def test_bigger_insert():
    x = range(99, 0, -1)
    assert sorter(x) == range(1, 100)


def test_random_insert():
    x = random.sample(range(100), 100)
    assert sorter(x) == range(100)


def test_big_insert():
    x = random.sample(range(10000), 10000)
    assert sorter(x) == range(10000)
