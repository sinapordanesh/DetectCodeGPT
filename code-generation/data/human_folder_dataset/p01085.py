from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

while True:
    m,nmin,nmax = inpl()
    if m == 0:
        break
    else:
        pp = [int(input()) for _ in range(m)]
        pp.sort(reverse=True)
        ans = 0
        ansgap = -1
        for n in range(nmin,nmax+1):
            gap = pp[n-1] - pp[n]
            if ansgap <= gap:
                ansgap = gap
                ans = n

        print(ans)

