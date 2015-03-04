from bst import BST
import pytest


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
    assert t.balance() == 1


def test_negative_input():
    t = BST()
    for i in range(10, -10, -1):
        t.insert(i)
    assert t.contains() is True
