class BSTNode(object):
    '''Instantiate Node and add helper functions'''
    def __init__(self, value, parent=None, left_child=None, right_child=None):
        self.value = value
        self.parent = parent
        self.left = left_child
        self.right = right_child

    def is_root(self):
        '''Helper function for root node'''
        return not self.parent

    def is_leaf(self):
        ''''Helper function for acknowledging leaf'''
        return not (self.right_child or self.left_child)


class BST(object):
    '''Instantiate binary search tree'''
    def __init__(self, values=None):
        self.root = None
        self.size = 0

    def size(self):
        '''Will return integer size of BST'''
        return self._size

    def insert(self, value):
        '''Inserts the data in value into BST'''
        if self.root is None:
            self.root = BSTNode(value)
            self._size += 1
            return
        current_node = self.root
        while True:
            if current_node.value > value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BSTNode(value)
                    self._size += 1
                    break
            elif current_node.value < value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BSTNode(value)
                    self._size += 1
                    break
            else:
                break

    def contains(self, values):
        '''Returns true if data in value is in BST'''

    def depth(self):
        '''Returns total number of levels in BST as interger'''

    def balance(self):
        '''Return positive or negativ integer to represent ree balance'''
        ret_value = 0
        if self.root is None:
            return ret_value
        if self.root.left:
            ret_value += self._depth(1, self.root.left)
        if self.root.right:
            ret_value -= self._depth(1, self.root.right)
        return ret_value
