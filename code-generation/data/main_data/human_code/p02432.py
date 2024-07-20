
from math import ceil, floor, log2


class Node:
    __slots__ = ('value', 'prev', 'next', 'pskip', 'nskip')

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        self.pskip = None
        self.nskip = None

    def __str__(self):
        return '<Node({})>'.format(self.value)


class Deque:
    SKIPSIZE = 128

    def __init__(self):
        self.count = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.index = []
        self.tail.prev = self.head

    def push(self, value):
        node = Node(value)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.count += 1
        self._add_index(node)
        self._add_pskip(node)

    def push_left(self, value):
        node = Node(value)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.count += 1
        self._add_index_left(node)
        self._add_nskip(node)

    def pop(self):
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        self.count -= 1
        self._remove_index()
        self._remove_pskip(node)
        return node.value

    def pop_left(self):
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        self.count -= 1
        self._remove_index_left()
        self._remove_nskip(node)
        return node.value

    def _add_pskip(self, node):
        if self.count >= self.SKIPSIZE:
            if node.prev.pskip is None:
                pnode = node
                for _ in range(self.SKIPSIZE):
                    pnode = pnode.prev
            else:
                pnode = node.prev.pskip.next
            node.pskip = pnode
            pnode.nskip = node

    def _add_nskip(self, node):
        if self.count >= self.SKIPSIZE:
            if node.next.nskip is None:
                nnode = node
                for _ in range(self.SKIPSIZE):
                    nnode = nnode.next
            else:
                nnode = node.next.nskip.prev
            node.nskip = nnode
            nnode.pskip = node

    def _remove_pskip(self, node):
        if node.pskip is not None:
            node.pskip.nskip = None
            node.pskip = None

    def _remove_nskip(self, node):
        if node.nskip is not None:
            node.nskip.pskip = None
            node.nskip = None

    def _add_index(self, node):
        exp = ceil(log2(self.count))
        if self.count == 2**exp:
            # print('add_index', self.count)
            self.index.append(node)

    def _add_index_left(self, node):
        self.index = [n.prev for n in self.index]
        self._add_index(self.tail.prev)

    def _remove_index(self):
        if self.count == 0:
            # print('remove_index', self.count)
            self.index.pop()
            return
        exp = ceil(log2(self.count))
        if self.count == 2**exp - 1:
            # print('remove_index', self.count)
            self.index.pop()

    def _remove_index_left(self):
        index = [n.next for i, n in enumerate(self.index) if i > 0]
        index.insert(0, self.head.next)
        self.index = index
        self._remove_index()

    def _select_index(self, n):
        exp = floor(log2(n+1))
        p1 = 2**exp
        p2 = 2**(exp+1)
        step = n - p1 + 1
        chunksize = min(p2, self.count) - p1 + 1
        if step > chunksize // 2:
            if p2 > self.count:
                node = self.tail.prev
                step -= chunksize-1
            else:
                node = self.index[exp+1]
                step -= chunksize-1
            while -step > self.SKIPSIZE:
                if node.pskip is None:
                    break
                node = node.pskip
                step += self.SKIPSIZE
        else:
            node = self.index[exp]
            while step > self.SKIPSIZE:
                if node.nskip is None:
                    break
                node = node.nskip
                step -= self.SKIPSIZE
        return (node, step)

    def __getitem__(self, key):
        if key is slice:
            raise NotImplemented()

        n = int(key)
        if n < 0:
            n = self.count + n
        if n >= self.count or n < 0:
            raise IndexError()

        node, sp = self._select_index(n)
        # print([str(n) for n in self.index])
        # print(n, 'index', node, 'sup', sp)
        if sp < 0:
            for i in range(-sp):
                node = node.prev
        else:
            for i in range(sp):
                node = node.next

        return node.value


def run():
    n = int(input())
    deque = Deque()

    for _ in range(n):
        command = input()
        if command.startswith('0'):
            sub, val = [int(x) for x in command[2:].split()]
            if sub == 0:
                deque.push_left(val)
            elif sub == 1:
                deque.push(val)
            else:
                raise ValueError('subcommand of push')
        elif command.startswith('1'):
            i = int(command[2:])
            print(deque[i])
        elif command.startswith('2'):
            sub = int(command[2:])
            if sub == 0:
                deque.pop_left()
            elif sub == 1:
                deque.pop()
            else:
                raise ValueError('subcommand of pop')
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

