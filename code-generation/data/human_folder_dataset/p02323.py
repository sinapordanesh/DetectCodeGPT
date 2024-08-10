# http://www.geocities.jp/m_hiroi/light/pyalgo65.html

def memoize(f):
    table = {}
    def func(*args):
        if not args in table:
            table[args] = f(*args)
        return table[args]
    return func

@memoize
def tsp(p, v):
    if (1 << point_size) - 1 == v:
        return distance_table[p][0]
    else:
        return min(distance_table[p][x] + tsp(x, v | (1 << x)) for x in range(point_size) if not (v & (1 << x)))

from sys import stdin
from collections import defaultdict
from math import isinf

readline = stdin.readline

point_size, e = map(int, readline().split())
distance_table = [[float('inf')] * point_size for _ in range(point_size)]
for _ in range(e):
    s, t, d = map(int, readline().split())
    distance_table[s][t] = d
ans = tsp(0,1)
print(-1 if isinf(ans) else ans)