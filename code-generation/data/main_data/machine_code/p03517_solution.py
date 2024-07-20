from collections import defaultdict
from heapq import *

def solve():
    n, m, k = map(int, input().split())
    c = list(map(int, input().split()))
    e = [tuple(map(int, input().split())) for _ in range(m)]

    g = defaultdict(list)
    for i,(a,b,w) in enumerate(e):
        if c[a-1] == c[b-1]:
            continue
        g[c[a-1],c[b-1]].append(w)
        g[c[b-1],c[a-1]].append(w)

    q, v = [(0, 0)], set()
    s = 0
    while q:
        w, i = heappop(q)
        if i in v:
            continue
        v.add(i)
        s += w
        for j in g:
            if j not in v:
                heappush(q, (min(g[j]), j))

    return s if len(v) == k else -1

print(solve())