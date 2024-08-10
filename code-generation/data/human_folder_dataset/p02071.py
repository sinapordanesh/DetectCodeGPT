#! /usr/bin/env python3

import sys
from fractions import Fraction

class PotentializedUnionFind(object):
    def __init__(self, n):
        self.tree = [-1 for i in range(n)]
        self.cost = [Fraction(1) for i in range(n)]

    def find(self, v):
        if self.tree[v] < 0: return v
        r = self.find(self.tree[v])
        self.cost[v] *= self.cost[self.tree[v]]
        self.tree[v] = r
        return r

    def unite(self, u, v, w):
        ru = self.find(u)
        rv = self.find(v)

        # w /= self.cost[u] / self.cost[v]
        # w *= self.cost[v] / self.cost[u]
        w = w * Fraction(self.cost[v], self.cost[u])
        if -self.tree[ru] >= -self.tree[rv]:
            ru, rv = rv, ru
            u, v = v, u
            w = 1 / w

        if ru == rv:
            if w != 1:
                # print(f'uniting {u} and {v} with {w}')
                raise ValueError('tsurai')

            return False

        self.tree[rv] += self.tree[ru]
        self.tree[ru] = rv
        self.cost[ru] = w
        return True

def main():
    sys.setrecursionlimit(300000)
    n, m = map(int, input().split())

    puf = PotentializedUnionFind(n)
    for i in range(m):
        a, b, x = map(int, input().split())
        a -= 1
        b -= 1
        try:
            puf.unite(a, b, Fraction(x))
        except ValueError:
            print('No')
            return 0

    print('Yes')
    return 0

main()

