
from enum import Enum


class Color(Enum):
    BLACK = 0
    RED = 1

    @staticmethod
    def flip(c):
        return [Color.RED, Color.BLACK][c.value]


class Node:
    __slots__ = ('key', 'left', 'right', 'size', 'color', 'value')

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = Leaf
        self.right = Leaf
        self.size = 1
        self.color = Color.RED

    def is_red(self):
        return self.color == Color.RED

    def is_black(self):
        return self.color == Color.BLACK

    def __str__(self):
        if self.color == Color.RED:
            key = '*{}'.format(self.key)
        else:
            key = '{}'.format(self.key)
        return "{}[{}] ({}, {})".format(key, self.size,
                                        self.left, self.right)


class LeafNode(Node):
    def __init__(self):
        self.key = None
        self.value = None
        self.left = None
        self.right = None
        self.size = 0
        self.color = None

    def is_red(self):
        return False

    def is_black(self):
        return False

    def __str__(self):
        return '-'


Leaf = LeafNode()


class RedBlackBinarySearchTree:
    """Red Black Binary Search Tree with range, min, max.
    Originally impremented in the textbook
    Algorithms, 4th edition by Robert Sedgewick and Kevin Wayne,
    Addison-Wesley Professional, 2011, ISBN 0-321-57351-X.
    """

    def __init__(self):
        self.root = Leaf

    def put(self, key, value=None):
        def _put(node):
            if node is Leaf:
                node = Node(key, value)
            if node.key > key:
                node.left = _put(node.left)
            elif node.key < key:
                node.right = _put(node.right)
            else:
                node.value = value

            node = self._restore(node)

            node.size = node.left.size + node.right.size + 1
            return node

        self.root = _put(self.root)
        self.root.color = Color.BLACK

    def _rotate_left(self, node):
        assert node.right.is_red()
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = Color.RED
        node.size = node.left.size + node.right.size + 1
        return x

    def _rotate_right(self, node):
        assert node.left.is_red()
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = Color.RED
        node.size = node.left.size + node.right.size + 1
        return x

    def _flip_colors(self, node):
        node.color = Color.flip(node.color)
        node.left.color = Color.flip(node.left.color)
        node.right.color = Color.flip(node.right.color)
        return node

    def __contains__(self, key):
        def _contains(node):
            if node is Leaf:
                return False
            if node.key > key:
                return _contains(node.left)
            elif node.key < key:
                return _contains(node.right)
            else:
                return True
        return _contains(self.root)

    def get(self, key):
        def _get(node):
            if node is Leaf:
                return None
            if node.key > key:
                return _get(node.left)
            elif node.key < key:
                return _get(node.right)
            else:
                return node.value
        return _get(self.root)

    def delete(self, key):
        def _delete(node):
            if node is Leaf:
                return Leaf

            if node.key > key:
                if node.left is Leaf:
                    return self._balance(node)
                if not self._is_red_left(node):
                    node = self._red_left(node)
                node.left = _delete(node.left)
            else:
                if node.left.is_red():
                    node = self._rotate_right(node)
                if node.key == key and node.right is Leaf:
                    return Leaf
                elif node.right is Leaf:
                    return self._balance(node)
                if not self._is_red_right(node):
                    node = self._red_right(node)
                if node.key == key:
                    x = self._find_min(node.right)
                    node.key = x.key
                    node.value = x.value
                    node.right = self._delete_min(node.right)
                else:
                    node.right = _delete(node.right)

            return self._balance(node)

        if self.is_empty():
            raise ValueError('delete on empty tree')
        if not self.root.left.is_red() and not self.root.right.is_red():
            self.root.color = Color.RED
        self.root = _delete(self.root)
        if not self.is_empty():
            self.root.color = Color.BLACK
        assert self.is_balanced()

    def delete_max(self):
        if self.is_empty():
            raise ValueError('delete max on empty tree')
        if not self.root.left.is_red() and not self.root.right.is_red():
            self.root.color = Color.RED
        self.root = self._delete_max(self.root)
        if not self.is_empty():
            self.root.color = Color.BLACK
        assert self.is_balanced()

    def _delete_max(self, node):
        if node.left.is_red():
            node = self._rotate_right(node)
        if node.right is Leaf:
            return Leaf

        if not self._is_red_right(node):
            node = self._red_right(node)
        node.right = self._delete_max(node.right)
        return self._balance(node)

    def _red_right(self, node):
        node = self._flip_colors(node)
        if node.left.left.is_red():
            node = self._rotate_right(node)
        return node

    def _is_red_right(self, node):
        return (node.right.is_red() or
                (node.right.is_black() and node.right.left.is_red()))

    def delete_min(self):
        if self.is_empty():
            raise ValueError('delete min on empty tree')

        if not self.root.left.is_red() and not self.root.right.is_red():
            self.root.color = Color.RED
        self.root = self._delete_min(self.root)
        if not self.is_empty():
            self.root.color = Color.BLACK
        assert self.is_balanced()

    def _delete_min(self, node):
        if node.left is Leaf:
            return Leaf

        if not self._is_red_left(node):
            node = self._red_left(node)
        node.left = self._delete_min(node.left)
        return self._balance(node)

    def _red_left(self, node):
        node = self._flip_colors(node)
        if node.right.left.is_red():
            node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
        return node

    def _is_red_left(self, node):
        return (node.left.is_red() or
                (node.left.is_black() and node.left.left.is_red()))

    def _balance(self, node):
        if node.right.is_red():
            node = self._rotate_left(node)
        return self._restore(node)

    def _restore(self, node):
        if node.right.is_red() and not node.left.is_red():
            node = self._rotate_left(node)
        if node.left.is_red() and node.left.left.is_red():
            node = self._rotate_right(node)
        if node.left.is_red() and node.right.is_red():
            node = self._flip_colors(node)

        node.size = node.left.size + node.right.size + 1
        return node

    def is_empty(self):
        return self.root is Leaf

    def is_balanced(self):
        if self.is_empty():
            return True

        try:
            left = self._depth(self.root.left)
            right = self._depth(self.root.right)
            return left == right
        except Exception:
            return False

    @property
    def depth(self):
        return self._depth(self.root)

    def _depth(self, node):
        if node is Leaf:
            return 0
        if node.right.is_red():
            raise Exception('right red')
        left = self._depth(node.left)
        right = self._depth(node.right)
        if left != right:
            raise Exception('unbalanced')
        if node.is_red():
            return left
        else:
            return 1 + left

    def __len__(self):
        return self.root.size

    @property
    def max(self):
        if self.is_empty():
            raise ValueError('max on empty tree')
        return self._max(self.root)

    def _max(self, node):
        x = self._find_max(node)
        return x.key

    def _find_max(self, node):
        if node.right is Leaf:
            return node
        else:
            return self._find_max(node.right)

    @property
    def min(self):
        if self.is_empty():
            raise ValueError('min on empty tree')
        return self._min(self.root)

    def _min(self, node):
        x = self._find_min(node)
        return x.key

    def _find_min(self, node):
        if node.left is Leaf:
            return node
        else:
            return self._find_min(node.left)

    def range(self, min_, max_):
        def _range(node):
            if node is Leaf:
                return

            if node.key > max_:
                yield from _range(node.left)
            elif node.key < min_:
                yield from _range(node.right)
            else:
                yield from _range(node.left)
                yield (node.key, node.value)
                yield from _range(node.right)

        if min_ > max_:
            return
        yield from _range(self.root)


class BalancedBstCounter:
    def __init__(self):
        self.bst = RedBlackBinarySearchTree()
        self.count = 0

    def up(self, key):
        if key in self.bst:
            value = self.bst.get(key) + 1
        else:
            value = 1
        self.bst.put(key, value)
        self.count += 1

    def __contains__(self, key):
        if key in self.bst:
            return self.bst.get(key) > 0
        else:
            return False

    def get(self, key):
        if key in self.bst:
            return self.bst.get(key)
        else:
            return 0

    def down(self, key):
        if key in self.bst:
            value = self.bst.get(key)
            self.bst.put(key, 0)
            self.count -= value

    def range(self, a, b):
        for k, v in self.bst.range(a, b):
            for _ in range(v):
                yield k

    def __len__(self):
        return self.count

    def __str__(self):
        return str(self.bst.root)


def run():
    q = int(input())
    counter = BalancedBstCounter()

    for _ in range(q):
        command, *value = [int(x) for x in input().split()]
        if command == 0:
            counter.up(value[0])
            print(len(counter))
        elif command == 1:
            print(counter.get(value[0]))
        elif command == 2:
            counter.down(value[0])
        elif command == 3:
            for i in counter.range(*value):
                print(i)
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

