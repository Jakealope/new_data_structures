class HashTable(object):
    """Implment hash table"""

    def __init__(self, size=0000000):
        self._list_size = size
        self._hash_list = [[] for hash in xrange(0, size)]

    def hash(self, key):
        if not isinstance(key, basestring):
            raise TypeError("key must be in string format")
        ord_val = 0
        for letter in key:
            ord_val += ord(letter)
        return ord_val % self._list_size
