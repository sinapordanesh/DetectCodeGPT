#!/usr/bin/env pypy3
# DSL_2_C: Range Search(kD Tree)

from bisect import bisect_left, bisect_right
from collections import deque
from functools import lru_cache
from itertools import islice
from math import floor, log2, sqrt
from operator import itemgetter
from sys import stdin, stdout


def sort3(i, j, k):
    if i > j:
        if j > k:
            return (2, 1, 0)
        elif i > k:
            return (1, 2, 0)
        else:
            return (1, 0, 2)
    else:
        if i > k:
            return (2, 0, 1)
        elif j > k:
            return (0, 2, 1)
        else:
            return (0, 1, 2)


def partition(ps, lo, hi, dim):
    mid = (lo + hi) // 2
    ns = (lo, mid, hi)
    n0, n1, n2 = sort3(ps[lo][dim], ps[mid][dim], ps[hi][dim])
    ps[lo], ps[mid], ps[hi] = ps[ns[n1]], ps[ns[n0]], ps[ns[n2]]
    v = ps[lo][dim]
    i, j = lo, hi
    while True:
        i, j = i+1, j-1
        while ps[i][dim] < v:
            i += 1
        while ps[j][dim] > v:
            j -= 1
        if i >= j:
            break
        ps[i], ps[j] = ps[j], ps[i]
    ps[j], ps[lo] = ps[lo], ps[j]
    return j


def sort(ps, lo, hi, dim):
    for i, p in enumerate(sorted(ps[lo:hi+1], key=itemgetter(dim))):
        ps[lo+i] = p


def halve(ps, s, t, dim):
    mid = (s+t) // 2
    while t - s > 100:
        i = partition(ps, s, t, dim)
        if i > mid:
            t = i - 1
        elif i < mid:
            s = i + 1
        else:
            return mid

    sort(ps, s, t, dim)
    return mid


def build(ps, n, sz, _dim):
    q = deque([(0, n-1, 0)])
    while q:
        s, t, lv = q.popleft()
        dim, _ = _dim(lv)
        if t - s < sz:
            sort(ps, s, t, dim)
            continue
        mid = halve(ps, s, t, dim)
        if mid-1 > s:
            q.append((s, mid-1, lv+1))
        if t > mid+1:
            q.append((mid+1, t, lv+1))


def search(ps, vs, n, sz, _dim, s, t):
    q = deque([(0, n-1, 0)])
    ret = []
    while q:
        i, j, lv = q.popleft()
        dim, rdim = _dim(lv)
        sd, td, sr, tr = s[dim], t[dim], s[rdim], t[rdim]
        if j - i < sz:
            left = bisect_left(vs[dim], sd, i, j+1)
            right = bisect_right(vs[dim], td, i, j+1)
            ret.extend([p[2] for p in ps[left:right] if sr <= p[rdim] <= tr])
            continue

        mid = (i+j) // 2
        if td < ps[mid][dim]:
            q.append((i, mid-1, lv+1))
        elif sd > ps[mid][dim]:
            q.append((mid+1, j, lv+1))
        else:
            if sr <= ps[mid][rdim] <= tr:
                ret.append(ps[mid][2])
            q.append((i, mid-1, lv+1))
            q.append((mid+1, j, lv+1))

    ret.sort()
    return ret


def dimension(ps, n):
    @lru_cache(maxsize=n)
    def _dimension(lv):
        return pat[lv % len(pat)]

    cx = len(set([p[0] for p in ps]))
    cy = len(set([p[1] for p in ps]))

    if cx < cy:
        m, s = 1, 0
        ratio = min(cy // cx, floor(log2(n)))
    else:
        m, s = 0, 1
        ratio = min(cx // cy, floor(log2(n)))

    pat = []
    for _ in range(ratio):
        pat.append((m, s))
    pat.append((s, m))

    return _dimension


def run():
    n = int(input())
    sz = floor(sqrt(n))
    ps = []
    for i, line in enumerate(islice(stdin, n)):
        x, y = map(int, line.split())
        ps.append((x, y, i))

    dim = dimension(ps, n)
    build(ps, n, sz, dim)

    input()  # q
    vs = ([p[0] for p in ps], [p[1] for p in ps])
    for line in stdin:
        sx, tx, sy, ty = [int(v) for v in line.split()]
        s = "".join([f"{id_}\n" for id_ in
                     search(ps, vs, n, sz, dim, (sx, sy), (tx, ty))])
        stdout.write(s + "\n")


if __name__ == '__main__':
    run()

