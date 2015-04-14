import random
from radix_sort import r_sort, string_radix


def test_sort_one():
    x = random.sample(range(100000), 100000)
    assert r_sort(x) == range(100000)


def test_sort_two():
    sr = r_sort(range(10000, -1, -1))
    assert sr == range(0, 10001)


def test_sort_three():
    somestring = ("of", "words", "shit", "n")
    assert string_radix(somestring) == ['n', 'of', 'shit', 'words']


def test_big_strings():
    bigstring = ["this is a big string", "Here is a big one too",
                 "honestly I'm not too sure what to put in this one"]
    assert string_radix(bigstring) == ['Here is a big one too',
                                       "honestly I'm not too sure what to put in this one",
                                       'this is a big string']


def test_huge_input():
    # open the file and name it afile
    with open("/usr/share/dict/words", "r") as afile:
        # loop through all the words in the file and bind them to 'word'
        word = [i for i in afile]
        # radix sort the words, they then need to be asserted to a sorted
        # version of the same file because radix orders the capitol letters
        # first where they come all mixed up
        assert string_radix(word) == sorted(word)
