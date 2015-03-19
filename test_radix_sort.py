import random
from radix_sort import sort_radix


def test_sort_one():
    sr = sort_radix(random.sample(range(100), 100))
    assert sr == range(100)


def test_sort_two():
    sr = sort_radix(range(1000, 0, -1))
    assert sr == range(1000)


def test_sort_three():
    sr = ['of', 'words', 'n', 'shit']
    assert sr == ['n', 'of', 'shit', 'words']
