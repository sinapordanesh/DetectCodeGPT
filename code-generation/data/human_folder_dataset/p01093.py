from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

while True:
    n = int(input())
    if n == 0:
        break
    else:
        aa = inpl()
        aa.sort()
        ans = INF
        for i in range(1,n):
            ans = min(aa[i] - aa[i-1],ans)
        print(ans)

