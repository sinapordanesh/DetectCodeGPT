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
    n,r = inpl()
    if n == 0:
        break
    else:
        yama = [n-i for i in range(n)]
        for _ in range(r):
            p,c = inpl()
            next_yama = yama[p-1:p-1+c] + yama[:p-1] + yama[p-1+c:]
            yama = next_yama
        print(yama[0])

