from merge_sort import m_sort
import random


def test_sort_one():
    x = random.sample(range(10), 10)
    assert m_sort(x) == range(10)


def test_sort_two():
    x = range(10, 0, -1)
    assert m_sort(x) == range(1, 11)


def test_sort_three():
    x = random.sample(range(1000), 1000)
    assert m_sort(x) == range(1000)


def test_sort_four():
    x = random.sample(range(100000), 100000)
    assert m_sort(x) == range(100000)
