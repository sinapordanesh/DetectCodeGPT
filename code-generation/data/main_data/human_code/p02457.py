
from enum import Enum
import math


class Color(Enum):
    BLACK = 0
    RED = 1

    @staticmethod
    def flip(c):
        return [Color.RED, Color.BLACK][c.value]


class RedBlackBinarySearchTree:
    """Red Black Binary Search Tree with range, min, max.
    """

    class Node:
        __slots__ = ('key', 'left', 'right', 'count', 'color')

        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.count = 0
            self.color = Color.RED

        def __str__(self):
            if self.color == Color.RED:
                key = '*{}'.format(self.key)
            else:
                key = '{}'.format(self.key)
            return "{}[{}] ({}, {})".format(key, self.count,
                                            self.left, self.right)

    def __init__(self):
        self.root = None

    def put(self, key):
        def _put(node):
            if node is None:
                node = self.Node(key)
            if node.key > key:
                node.left = _put(node.left)
            elif node.key < key:
                node.right = _put(node.right)

            node = self._restore(node)

            node.count = self._size(node.left) + self._size(node.right) + 1
            return node

        self.root = _put(self.root)
        self.root.color = Color.BLACK

    def _is_red(self, node):
        if node is None:
            return False
        else:
            return node.color == Color.RED

    def _is_black(self, node):
        if node is None:
            return False
        else:
            return node.color == Color.BLACK

    def _is_2node(self, node):
        if node is None:
            return False
        elif self._is_red(node):
            return False
        else:
            return (self._is_black(node) and
                    not self._is_red(node.left) and
                    not self._is_red(node.right))

    def _is_34node(self, node):
        if node is None:
            return False
        elif self._is_red(node):
            return True
        else:
            return (self._is_black(node) and
                    self._is_red(node.left) and
                    not self._is_red(node.right))

    def _rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = Color.RED
        node.count = self._size(node.left) + self._size(node.right) + 1
        return x

    def _rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = Color.RED
        node.count = self._size(node.left) + self._size(node.right) + 1
        return x

    def _flip_colors(self, node):
        node.color = Color.flip(node.color)
        node.left.color = Color.flip(node.left.color)
        node.right.color = Color.flip(node.right.color)
        return node

    def __contains__(self, key):
        def _contains(node):
            if node is None:
                return False
            if node.key > key:
                return _contains(node.left)
            elif node.key < key:
                return _contains(node.right)
            else:
                return True
        return _contains(self.root)

    def delete(self, key):
        def _delete_from(node):
            if node is None:
                return None
            else:
                assert not self._is_2node(node)

                if node.key > key:
                    node = self._convert_left(node)
                    # print('_convert_left', node)
                    node.left = _delete_from(node.left)
                    node = self._restore(node)
                    # print('_restore', node)
                elif node.key < key:
                    node = self._convert_right(node)
                    # print('_convert_right', node)
                    node.right = _delete_from(node.right)
                    node = self._restore(node)
                    # print('_restore', node)
                else:
                    node = _remove(node)

            if node is not None:
                node.count = self._size(node.right) + self._size(node.left) + 1
            return node

        def _remove(node):
            if node.left is None:
                return None
            elif node.right is None:
                if self._is_red(node.left):
                    node.left.color = Color.BLACK
                return node.left
            else:
                node = self._convert_right(node)
                if node.key == key:
                    x = self._find_min(node.right)
                    node.key = x.key
                    node.right = self._delete_min(node.right)
                else:
                    # print(node)
                    node.right = _delete_from(node.right)
                node = self._restore(node)
                # print('min', x.key, 'node', node.key)
                return node

        if self.root is None:
            return
        # print('initial', self.root)
        if not self._is_red(self.root.left):
            self.root.color = Color.RED
        self.root = _delete_from(self.root)
        if self.root is not None:
            self.root.color = Color.BLACK

    def delete_max(self):
        if self.root is None:
            raise ValueError('remove max on empty tree')
        if self.root.left is None:
            self.root = None
            return
        if not self._is_red(self.root.left):
            self.root.color = Color.RED
        self.root = self._delete_max(self.root)
        self.root.color = Color.BLACK

    def _delete_max(self, node):
        if node.right is None:
            if self._is_red(node.left):
                node.left.color = Color.BLACK
            return node.left
        else:
            assert not self._is_2node(node)
            node = self._convert_right(node)
            node.right = self._delete_max(node.right)
            node = self._restore(node)
            return node

    def _convert_right(self, node):
        if self._is_2node(node.right):
            if self._is_2node(node.left):
                self._flip_colors(node)
            elif self._is_red(node.left) and self._is_2node(node.left.right):
                node = self._rotate_right(node)
                self._flip_colors(node.right)
            elif self._is_red(node.left):
                x = node.left.right
                node.left.right = x.left
                node.left, node.right, x.left, x.right = \
                    x.right, node.right.left, node.left, node.right
                x.right.left = node
                x.color = Color.BLACK
                node.color = Color.RED
                if self._is_red(x.left.right):
                    x.left.right.color = Color.BLACK
                node.count = (self._size(node.left) +
                              self._size(node.right) + 1)
                x.left.count = (self._size(x.left.left) +
                                self._size(x.left.right) + 1)
                node = x
            elif self._is_34node(node.left):
                x = node.left
                node.left, node.right, x.right = \
                    x.right, node.right.left, node.right
                x.right.left = node
                x.color = node.color
                if self._is_red(x.left):
                    x.left.color = Color.BLACK
                if self._is_black(x.right.left):
                    x.right.left.color = Color.RED
                node.count = (self._size(node.left) +
                              self._size(node.right) + 1)
                x.left.count = (self._size(x.left.left) +
                                self._size(x.left.right) + 1)
                node = x
        return node

    def delete_min(self):
        if self.root is None:
            raise ValueError('remove min on empty tree')
        if self.root.left is None:
            self.root = None
            return
        if not self._is_red(self.root.left):
            self.root.color = Color.RED
        self.root = self._delete_min(self.root)
        self.root.color = Color.BLACK

    def _delete_min(self, node):
        if node.left is None:
            return None
        else:
            node = self._convert_left(node)
            node.left = self._delete_min(node.left)
            node = self._restore(node)
            return node

    def _convert_left(self, node):
        if self._is_2node(node.left):
            if self._is_2node(node.right):
                self._flip_colors(node)
            elif self._is_34node(node.right):
                x = node.right.left
                node.right.left = x.right
                x.left, x.right, node.right = node, node.right, x.left
                x.color = node.color
                node.color = Color.BLACK
                node.left.color = Color.RED
                x.right.count = (self._size(x.right.left) +
                                 self._size(x.right.right) + 1)
                node = x
        return node

    def _restore(self, node):
        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            node = self._flip_colors(node)

        node.count = self._size(node.left) + self._size(node.right) + 1
        return node

    def _is_balanced(self, node):
        def depth(node):
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            if left != right:
                raise Exception('unbalanced')
            if self._is_black(node):
                return 1 + left
            else:
                return left

        if node is None:
            return True

        try:
            left = depth(node.left)
            right = depth(node.right)
            return left == right
        except Exception:
            return False

    @property
    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        else:
            return node.count

    @property
    def max(self):
        if self.root is None:
            raise ValueError('max on empty tree')
        return self._max(self.root)

    def _max(self, node):
        x = self._find_max(node)
        return x.key

    def _find_max(self, node):
        if node.right is None:
            return node
        else:
            return self._find_max(node.right)

    @property
    def min(self):
        if self.root is None:
            raise ValueError('min on empty tree')
        return self._min(self.root)

    def _min(self, node):
        x = self._find_min(node)
        return x.key

    def _find_min(self, node):
        if node.left is None:
            return node
        else:
            return self._find_min(node.left)

    def range(self, min_, max_):
        def _range(node):
            if node is None:
                return

            if node.key > max_:
                yield from _range(node.left)
            elif node.key < min_:
                yield from _range(node.right)
            else:
                yield from _range(node.left)
                yield node.key
                yield from _range(node.right)

        if min_ > max_:
            return
        yield from _range(self.root)


class BalancedBstSet:
    def __init__(self):
        self.bst = RedBlackBinarySearchTree()

    def add(self, key):
        self.bst.put(key)

    def __contains__(self, key):
        return key in self.bst

    def delete(self, key):
        self.bst.delete(key)

    def range(self, a, b):
        for k in self.bst.range(a, b):
            yield k

    @property
    def count(self):
        return self.bst.size

    def __str__(self):
        return str(self.bst.root)


def run():
    q = int(input())
    s = BalancedBstSet()

    for _ in range(q):
        command, *value = [int(x) for x in input().split()]
        if command == 0:
            s.add(value[0])
            print(s.count)
        elif command == 1:
            if value[0] in s:
                print(1)
            else:
                print(0)
        elif command == 2:
            s.delete(value[0])
        elif command == 3:
            for i in s.range(*value):
                print(i)
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

