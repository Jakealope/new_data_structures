class HashTable(object):
    """Implment hash table"""

    def __init__(self, size=0000000):
        self._list_size = size
        self._hash_list = [[] for _hash in xrange(0, size)]

    def hash(self, key):
        if not isinstance(key, basestring):
            raise TypeError("Key must be in string format")
        ord_val = 0
        for letter in key:
            ord_val += ord(letter)
        return ord_val % self._list_size

    def set(self, key, value):
        hash = self.hash(key)
        for item in self._hash_list[hash]:
            if item[0] == key:
                item[1] = value
                return
        self._hash_list[hash].append([key, value])

    def get(self, key):
        hash = self.hash(key)
        for item in self._hash_list[hash]:
            if item[0] == key:
                return item[1]
        raise KeyError("Key not found")
