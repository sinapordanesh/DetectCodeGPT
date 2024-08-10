import sys
import numpy as np
import numba
from numba import njit, b1, i4, i8
from numba.types import Omitted

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit((i8, i8), cache=True)
def find_min_length(a, b):
    if a < b:
        a, b = b, a
    return (a + b) // (b + 1)

@njit((i8, i8, i8, i8), cache=True)
def f(a, b, c, d):
    L = find_min_length(a, b)
    ret = ''

    def test(a, b, L):
        # ...B の直後に A を a 個、B を b 個置けるかどうか
        ok = a >= 0 and b >= 0
        if a == 0:
            ok = ok and (b <= L - 1)
        else:
            ok = ok and (a <= L * (b + 1))
            ok = ok and (1 + b <= L * (a + 1))
        return ok

    def add(s, x, t, y, n):
        # 文字列に (s*x + t*y)*n を追加
        nonlocal c, d, ret
        if (x + y) * n < c:
            c -= (x + y) * n
            d -= (x + y) * n
            return
        m = (c - 1) // (x + y)
        c -= m * (x + y)
        d -= m * (x + y)
        n -= m
        while n and c <= d:
            if d <= x:
                ret += s * (d - c + 1)
                d = 0
                return
            if 1 <= c <= x:
                ret += s * (x - c + 1)
                c = x + 1
            ret += t * (min(d, x + y) - c + 1)
            c = 1
            d -= x + y
            n -= 1

    # AAABAAAB と n セット並べてしまって大丈夫かどうか
    l, r = 0, b + 100
    while l + 1 < r:
        m = (l + r) >> 1
        a1, b1 = a - L * m, b - m
        if test(a1, b1, L):
            l = m
        else:
            r = m
    n = l
    flag = n == 0
    add('A', L, 'B', 1, n)
    a -= L * n
    b -= n
    # 次に、A^kB
    l, r = 0, L
    while l + 1 < r:
        m = (l + r) // 2
        if test(a - m, b - 1, L):
            l = m
        else:
            r = m
    k = l
    flag = flag and k == 0
    if k:
        add('A', k, 'B', 1, 1)
        a -= k
        b -= 1
    # 以降は、Aは高々ひとつずつ
    if not a:
        add('B', b, 'A', 0, 1)
        return ret
    if not b:
        add('A', a, 'B', 0, 1)
        return ret

    # B^kA、kはなるべく少なく
    l, r = -1, L - 1
    if flag:
        r = L
    while l + 1 < r:
        m = (l + r) // 2
        if test(a, b - m, L) and b - m <= a * L:
            r = m
        else:
            l = m
    k = r

    if k >= 0:
        add('B', k, 'A', 1, 1)
        a -= 1
        b -= k
    # B^LA をいくつか
    n = min(b // L, a)
    add('B', L, 'A', 1, n)
    a -= n
    b -= n * L
    add('B', b, 'A', 0, 1)
    add('B', 0, 'A', a, 1)
    return ret

ABCD = np.array(read().split(), np.int64)[1:]

for a, b, c, d in ABCD.reshape(-1, 4):
    print(f(a, b, c, d))