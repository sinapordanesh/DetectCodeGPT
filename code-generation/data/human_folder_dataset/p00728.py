from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

while True:
    n = inp()
    if n == 0:
        break
    else:
        aa = [inp() for i in range(n)]
        aa.sort()
        print(sum(aa[1:n-1])//(n-2))

