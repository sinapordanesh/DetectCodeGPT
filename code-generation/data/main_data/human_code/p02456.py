
import math


class LinearProbingIntSet:
    def __init__(self):
        self.count = 0
        self.size = 1
        self.keys = [None] * self.size

    def add(self, key):
        i = self._hash(key)
        for j in range(self.size):
            k = (i + j) % self.size
            if self.keys[k] is None:
                self.keys[k] = key
                self.count += 1
                break
            elif self.keys[k] == key:
                break
        else:
            raise RuntimeError('set is full')

        if self.count > self.size // 2:
            size = int(2 ** (math.log2(self.size+1)+1)) - 1
            self._resize(size)

    def delete(self, key):
        i = self._hash(key)
        while self.keys[i] is not None and self.keys[i] != key:
            i = (i + 1) % self.size

        if self.keys[i] != key:
            return
        self.keys[i] = None
        self.count -= 1

        i = (i + 1) % self.size
        while self.keys[i] is not None:
            key = self.keys[i]
            if i != self._hash(key):
                self.keys[i] = None
                self.count -= 1
                self.add(key)
            i = (i + 1) % self.size

        if self.count <= self.size // 4:
            size = max(1, int(2 ** (math.log2(self.size+1)-1)) - 1)
            self._resize(size)

    def __contains__(self, key):
        i = self._hash(key)
        for j in range(self.size):
            k = (i + j) % self.size
            if self.keys[k] is None:
                return False
            elif self.keys[k] == key:
                return True
        raise RuntimeError('set is full')

    def _hash(self, key):
        return (key * 13) % self.size

    def _resize(self, size):
        old_keys = self.keys
        self.count = 0
        self.size = size
        self.keys = [None] * self.size

        for key in old_keys:
            if key is None:
                continue
            self.add(key)


def run():
    q = int(input())
    s = LinearProbingIntSet()

    for _ in range(q):
        command, value = [int(x) for x in input().split()]
        if command == 0:
            s.add(value)
            print(s.count)
        elif command == 1:
            if value in s:
                print(1)
            else:
                print(0)
        elif command == 2:
            s.delete(value)
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

