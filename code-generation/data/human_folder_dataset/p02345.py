
import random


class Node:
    __slots__ = ('x', 'y', 'left', 'right', 'valid')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.valid = True

    def __str__(self):
        if self.valid:
            return "({} [{},{}] {})".format(self.left, self.x,
                                            self.y, self.right)
        else:
            return "({} *[{},{}] {})".format(self.left, self.x,
                                             self.y, self.right)


class KdTree:
    MAX = 2**31-1

    def __init__(self, size):
        self.root = None
        self.index = [None] * size

    def insert(self, x, y):
        self._delete(self.index[x])
        self.root = self._insert(self.root, x, y)

    def _insert(self, node, x, y, level=0):
        if node is None:
            node = Node(x, y)
            self.index[x] = node
            return node
        if level % 2 == 0:
            if node.x > x:
                node.left = self._insert(node.left, x, y, level+1)
            else:
                node.right = self._insert(node.right, x, y, level+1)
        else:
            if node.y > y:
                node.left = self._insert(node.left, x, y, level+1)
            else:
                node.right = self._insert(node.right, x, y, level+1)
        return node

    def miny(self, x1, x2):
        def _miny(node, y, level):
            if node is None:
                return y
            left, right = self.MAX, self.MAX
            if level % 2 == 0:
                if x2 < node.x:
                    left = _miny(node.left, y, level+1)
                elif x1 > node.x:
                    right = _miny(node.right, y, level+1)
                else:
                    if self._is_valid(node) and node.y < y:
                        y = node.y
                    left = _miny(node.left, y, level+1)
                    if left < y:
                        y = left
                    right = _miny(node.right, y, level+1)
            else:
                if node.y > y:
                    left = _miny(node.left, y, level+1)
                elif node.y < y:
                    if x1 <= node.x <= x2 and self._is_valid(node):
                        left = _miny(node.left, node.y, level+1)
                    else:
                        left = _miny(node.left, y, level+1)
                        if left < y:
                            y = left
                        right = _miny(node.right, y, level+1)
                else:
                    left = _miny(node.left, y, level+1)

            if left < y:
                y = left
            if right < y:
                y = right
            return y

        assert x1 <= x2
        return _miny(self.root, self.MAX, 0)

    def _delete(self, node):
        if node is not None:
            node.valid = False

    def _is_valid(self, node):
        if node is not None:
            return node.valid
        else:
            return False


def run():
    n, q = [int(i) for i in input().split()]
    tree = KdTree(n)
    buff = {}
    k = 0

    for _ in range(q):
        com, u, v = [int(i) for i in input().split()]
        if com == 0:
            if u not in buff:
                k += 1
            buff[u] = v
        elif com == 1:
            if k > 0:
                for x, y in random.sample(buff.items(), k=k):
                    tree.insert(x, y)
                buff = {}
                k = 0
            print(tree.miny(u, v))
        else:
            raise ValueError('invalid command: {}'.format(com))


if __name__ == '__main__':
    run()


