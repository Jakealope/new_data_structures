from hash_table import HashTable
import pytest


@pytest.fixture(scope='function')
def _small():
    h = HashTable()
    h.set('batman', 'batman')
    h.set('robin', 'robin')
    return h


def test_one(_small):
    x = _small
    assert x.get('batman') == 'batman'
    assert x.get('batman') != 'robin'


# def test_dict():
#     x = HashTable()
#     with open("/usr/share/dict/words", "r") as afile:
#         for word in afile:
#             word.strip()
#             if not word:
#                 break
#             x.set(word, word)
#         assert x.get(word) == word


def test_ordval():
    x = HashTable()
    x.set('this is a really big sentence to break it',
          'this is a really big sentence to break it')
    assert x.get('this is a really big sentence to break it') == 'this is a really big sentence to break it'

'''Write test that inputs identical keys, with different values
   And check size. To make sure that it doens't just overwrite it.'''


def test_identical():
    x = HashTable()
    x.set('vortex', 'vortex')
    x.set('peter', 'peter')
    x.set('vortex', 'vortex')
    assert x.get('vortex') == 'vortex'
    assert x.get('vortex') == 'vortex'
    assert x.get('vortex') == 'vortex'
