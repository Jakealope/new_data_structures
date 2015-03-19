from quick_sort import Q_sort
import random


def test_sort_one():
    x = range(10)
    assert Q_sort(x) == x


def test_sort_two():
    x = range(10, 1, -1)
    assert Q_sort(x) == range(10)


def test_sort_big():
    x = range(1000)
    assert Q_sort(x) == x


def test_sort_big_backwards():
    x = range(1000, 1, -1)
    assert Q_sort(x) == x


def test_sort_random():
    x = random.sample(range(100), 100)
    assert Q_sort(x) == range(100)
