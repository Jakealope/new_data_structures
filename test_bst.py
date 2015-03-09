from bst import BST
import pytest
import random


@pytest.fixture(scope="function")
def tree_maker():
    t = BST()
    t.insert(1)
    t.insert(2)
    t.insert(4)
    t.insert(7)
    t.insert(9)
    return t


@pytest.fixture(scope="function")
def tree_test(tree_maker):
    tree_maker.insert(15)
    tree_maker.insert(5)
    tree_maker.insert(3)
    tree_maker.insert(20)
    tree_maker.insert(6)
    return tree_maker


def test_insert():
    t = BST()
    for i in range(5):
        t.insert(i)
    assert t.contains(i) is True


def test_big_insert():
    t = BST()
    for i in range(1000):
        t.insert(i)
    assert t.contains(i) is True


def test_size():
    t = BST()
    for i in range(10):
        t.insert(i)
    assert t.size() == 10


def test_big_size():
    t = BST()
    for i in range(1000):
        t.insert(i)
    assert t.size() == 1000


def test_balance():
    t = BST()
    for i in range(10):
        t.insert(i)
    assert t.balance() == -9


def test_negative_input():
    t = BST()
    for i in range(10, -10, -1):
        t.insert(i)
    assert t.contains(i) is True


def test_negative_input_balance():
    t = BST()
    for i in range(10, -10, -1):
        t.insert(i)
    assert t.balance() == 19


def test_depth():
    t = BST()
    for i in range(10):
        t.insert(i)
    assert t.depth() == 10


def test_random():
    t = BST()
    for i in random.sample(range(100), 100):
        t.insert(i)
    assert t.size() == 100


def test_in_order(tree_test):
    expected = [1, 2, 3, 4, 5, 6, 7, 9, 15, 20]
    actual = tree_test.in_order()
    for value in expected:
        assert value == actual.next()
    with pytest.raises(StopIteration):
        actual.next()


def test_pre_order(tree_test):
    expected = [1, 2, 4, 3, 7, 5, 6, 9, 15, 20]
    actual = tree_test.pre_order()
    for value in expected:
        assert value == actual.next()
    with pytest.raises(StopIteration):
        actual.next()


def test_post_order(tree_test):
    expected = [3, 6, 5, 20, 15, 9, 7, 4, 2, 1]
    actual = tree_test.post_order()
    for value in expected:
        assert value == actual.next()
    with pytest.raises(StopIteration):
        actual.next()


def test_breadth_traversal(tree_test):
    expected = [1, 2, 4, 3, 7, 5, 9, 6, 15, 20]
    actual = tree_test.breadth_traversal()
    for value in expected:
        assert value == actual.next()
    with pytest.raises(StopIteration):
        actual.next()


def test_delete_func(tree_test):
    expected = [3, 6, 5, 20, 15, 9, 7, 4, 2, 1]
    actual = tree_test.delete('15')
    for x in expected:
        assert x == actual.next()
    with pytest.raises(StopIteration):
        x.next()
