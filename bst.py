# http://blog.shayanjaved.com/2012/01/14/binary-search-tree-in-python/

# http://interactivepython.org/XSKWZ/LpOMZ/courselib/static/pythonds/Trees/bst.html
import timeit
import random
import subprocess
from collections import deque


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

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.value, self.left.value)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.value, self.right.value)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)


class BST(object):
    '''Instantiate binary search tree'''
    def __init__(self, values=None):
        self.root = None
        self._size = 0

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

    def contains(self, value):
        '''Returns true if data in value is in BST'''
        if self.root is None:
            return False
        current_node = self.root
        while True:
            if current_node.value > value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    return False
            elif current_node.value < value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    return False
            else:
                return True

    def depth(self):
        '''Returns total number of levels in BST as interger'''
        if self.root is None:
            return 0
        return self._depth(1, self.root)

    def _depth(self, curr_depth, local_root):
        '''Helper function for depth'''
        l_depth = r_depth = 0
        if local_root.left:
            l_depth = self._depth(curr_depth + 1, local_root.left)
        if local_root.right:
            r_depth = self._depth(curr_depth + 1, local_root.right)
        return max(curr_depth, l_depth, r_depth)

    def balance(self):
        '''Return positive or negative integer to represent tree balance'''
        ret_value = 0
        if self.root is None:
            return ret_value
        if self.root.left:
            ret_value += self._depth(1, self.root.left)
        if self.root.right:
            ret_value -= self._depth(1, self.root.right)
        return ret_value

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.root.value is None else (
            "\t%s;\n%s\n" % (
                self.root.value,
                "\n".join(self.root._get_dot())
            )
        ))

    def in_order(self):
        return self._in_order(self.root)

    def _in_order(self, leaf):
        if leaf is None:
            return
        for value in self._in_order(leaf.left):
            yield value
        yield leaf.value
        for value in self._in_order(leaf.right):
            yield value

    def pre_order(self):
        return self._pre_order(self.root)

    def _pre_order(self, leaf):
        if leaf is None:
            return
        yield leaf.value
        for value in self._pre_order(leaf.left):
            yield value
        for value in self._pre_order(leaf.right):
            yield value

    def post_order(self):
        return self._post_order(self.root)

    def _post_order(self, leaf):
        if leaf is None:
            return
        for value in self._post_order(leaf.left):
            yield value
        for value in self._post_order(leaf.right):
            yield value
        yield leaf.value

    def breadth_traversal(self):
        x = deque()
        x.append(self.root)
        while x:
            leaf = x.popleft()
            yield leaf.value
            if leaf.left:
                x.append(leaf.left)
            if leaf.right:
                x.append(leaf.right)

    def delete(self, val):
        self.root = self._delete(val, self.root)
        return None

    def _delete(self, val, node):
        def _descendants(node):
            if node.left:
                return _descendants(node.left)
            else:
                return node.value

        if not node:
            return None

        if node.value == val:
            self._size -= 1
            if node.left and node.right:
                node.value = _descendants(node.right)
                node.right = self._delete(node.value, node.right)
                return node
            elif node.left and not node.right:
                return node.left
            elif not node.left and node.right:
                return node.right
            else:
                return None

        elif node.value < val:
            if node.right:
                node.right = self._delete(val, node.right)
            return node

        else:
            if node.left:
                node.left = self._delete(val, node.left)
            return node



if __name__ == '__main__':

    # x = range(100)
    # bst = BST()
    # for i in x:
    #     bst.insert(i)
    # bst.insert(42.1)
    # dot_graph = bst.get_dot()
    # t = subprocess.Popen(["dot", "-Tpng"], stdin=subprocess.PIPE)
    # t.communicate(dot_graph)

    def easy_tree():
        x = random.sample(range(100), 100)
        bst = BST()
        bst.insert(50)
        for i in x:
            bst.insert(i)
        bst.insert(42.1)
        bst.contains(42.1)

    def hard_tree():
        x = range(100)
        bst = BST()
        for i in x:
            bst.insert(i)
        bst.insert(42.1)
        bst.contains(42.1)

    print(timeit.Timer("easy_tree()", setup="from __main__ import easy_tree").timeit(number=1000))
    print(timeit.Timer("hard_tree()", setup="from __main__ import hard_tree").timeit(number=1000))
