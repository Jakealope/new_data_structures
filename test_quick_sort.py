from quick_sort import q_sort
import random


def test_sort_one():
    x = range(10)
    assert q_sort(x) == x


def test_sort_two():
    x = range(10, 0, -1)
    assert q_sort(x) == range(1, 11)


def test_sort_big():
    x = range(100)
    assert q_sort(x) == x


def test_sort_big_backwards():
    x = range(100, 0, -1)
    assert q_sort(x) == range(1, 101)


def test_sort_random():
    x = random.sample(range(100), 100)
    assert q_sort(x) == range(100)
