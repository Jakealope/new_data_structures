from bst import BST
import pytest
import random


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
