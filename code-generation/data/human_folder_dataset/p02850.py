#!/usr/bin/env python3
from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(500000)
INF = float("inf")
YES, Yes, yes, NO, No, no = "YES", "Yes", "yes", "NO", "No", "no"
dy4, dx4 = [0, 1, 0, -1], [1, 0, -1, 0]
dy8, dx8 = [0, -1, 0, 1, 1, -1, -1, 1], [1, 0, -1, 0, 1, 1, -1, -1]


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ceil(a, b):
    return (a + b - 1) // b


def sum_of_arithmetic_progression(s, d, n):
    return n * (2 * s + (n - 1) * d) // 2


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    g = gcd(a, b)
    return a / g * b


def dfs(u, p, c, color, tree):
    color[(u, p)] = c
    color[(p, u)] = c

    now = 0
    for v in tree[u]:
        if v == p:
            continue
        if now == c:
            now += 1

        dfs(v, u, now, color, tree)
        now += 1


def solve():
    N = int(input())

    tree = [[] for _ in range(N)]
    edges = []
    for _ in range(N - 1):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        tree[A].append(B)
        tree[B].append(A)
        edges.append((A, B))

    color = dict()
    dfs(0, -1, -1, color, tree)

    print(max(color.values()) + 1)
    for e in edges:
        print(color[e] + 1)


def main():
    solve()


if __name__ == '__main__':
    main()
