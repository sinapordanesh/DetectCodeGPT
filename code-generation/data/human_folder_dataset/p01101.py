from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

while True:
    n,m = inpl()
    if m == 0:
        break
    else:
        aa = inpl()
        aa.sort()
        ans = -1
        for i in range(n):
            x = aa[i]
            for j in range(n):
                y = aa[j]
                if i == j or x+y > m:
                    continue
                ans = max(x+y,ans)
        if ans == -1:
            print('NONE')
        else:
            print(ans)

