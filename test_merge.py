from merge_sort import m_sort
import random
import pytest


def test_sort_one():
    x = random.sample(range(10), 10)
    assert m_sort(x) == range(10)


def test_sort_two():
    x = range(10, 0, -1)
    assert m_sort(x) == range(10)
