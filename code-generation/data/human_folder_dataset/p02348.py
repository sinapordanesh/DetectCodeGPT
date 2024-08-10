#!/usr/bin/env python3
# DSL_2_D: Range Update Query


class SegmentTree:
    INITIAL_VALUE = 2**31 - 1
    DIVIDED = -1

    def __init__(self, n):
        size = 1
        while size < n:
            size *= 2
        self.size = 2*size - 1
        self.data = [-1] * self.size
        self.data[0] = self.INITIAL_VALUE

    def set_range(self, lo, hi, v):
        def _set_range(r, i, j, vv):
            if j < lo or i > hi:
                if vv != self.DIVIDED:
                    self.data[r] = vv
            elif lo <= i and j <= hi:
                self.data[r] = v
            else:
                if self.data[r] != self.DIVIDED:
                    if vv == self.DIVIDED:
                        vv = self.data[r]
                    self.data[r] = self.DIVIDED
                mid = i + (j - i)//2
                _set_range(r*2 + 1, i, mid, vv)
                _set_range(r*2 + 2, mid+1, j, vv)

        _set_range(0, 0, self.size//2, self.DIVIDED)

    def get(self, i):
        def _get(r, lo, hi):
            if self.data[r] != self.DIVIDED:
                return self.data[r]
            mid = lo + (hi - lo)//2
            if i <= mid:
                return _get(r*2 + 1, lo, mid)
            else:
                return _get(r*2 + 2, mid+1, hi)

        return _get(0, 0, self.size//2)


def run():
    n, q = [int(x) for x in input().split()]
    t = SegmentTree(n)

    for _ in range(q):
        com, *args = [x for x in input().split()]
        if com == '0':
            i, j, v = [int(x) for x in args]
            t.set_range(i, j, v)
        elif com == '1':
            i = int(args[0])
            print(t.get(i))


if __name__ == '__main__':
    run()

