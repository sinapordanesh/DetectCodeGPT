#!/usr/bin/env python3
# DSL_2_I: RSQ and RUQ
# Range Sum Query and Range Update Query

import sys


class SegmentTree:

    def __init__(self, n):
        size = 2 ** (n.bit_length())
        self.size = 2*size - 1
        self.data = [0] * self.size
        self.lazy = [None] * self.size

    def update(self, lo, hi, v):
        def _update(r, i, j, lz):
            left, right = r*2 + 1, r*2 + 2
            if lz is None:
                lz = lazy[r]
            lazy[r] = None

            if lo <= i and j <= hi:
                data[r] = v * (j - i + 1)
                if i < j:
                    lazy[left] = v
                    lazy[right] = v
            else:
                mid = (i + j) // 2
                if mid >= lo:
                    lv = _update(left, i, mid, lz)
                else:
                    if lz is not None:
                        lazy[left] = lz
                        lv = lz * (mid - i + 1)
                    elif lazy[left] is not None:
                        lv = lazy[left] * (mid - i + 1)
                    else:
                        lv = data[left]

                if mid < hi:
                    rv = _update(right, mid+1, j, lz)
                else:
                    if lz is not None:
                        lazy[right] = lz
                        rv = lz * (j - mid)
                    elif lazy[right] is not None:
                        rv = lazy[right] * (j - mid)
                    else:
                        rv = data[right]

                data[r] = lv + rv

            return data[r]

        data = self.data
        lazy = self.lazy
        _update(0, 0, self.size//2, None)

    def sum(self, lo, hi):
        def _sum(r, i, j, lz):
            if lz is None:
                lz = lazy[r]
            lazy[r] = None
            if lz is not None:
                data[r] = lz * (j - i + 1)

            left, right = r*2 + 1, r*2 + 2
            if lo <= i and j <= hi:
                if lz is not None and i < j:
                    lazy[left] = lz
                    lazy[right] = lz
                return data[r]
            else:
                mid = (i + j) // 2
                lv, rv = 0, 0

                if mid >= lo:
                    lv = _sum(left, i, mid, lz)
                else:
                    if lz is not None:
                        lazy[left] = lz
                if mid < hi:
                    rv = _sum(right, mid+1, j, lz)
                else:
                    if lz is not None:
                        lazy[right] = lz
                return lv + rv

        data = self.data
        lazy = self.lazy
        return _sum(0, 0, self.size//2, None)


def run():
    n, q = [int(i) for i in input().split()]
    tree = SegmentTree(n)

    for line in sys.stdin:
        com, *args = line.split()
        if com == '0':
            s, t, x = [int(i) for i in args]
            tree.update(s, t, x)
        elif com == '1':
            s, t = [int(i) for i in args]
            print(tree.sum(s, t))


if __name__ == '__main__':
    run()

