from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
from bisect import bisect_left, bisect_right
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from copy import deepcopy

INF = 10 ** 20
sys.setrecursionlimit(2147483647)

def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7

n=I()
G=[[]for _ in range(n)]
r=-1
for _ in range(n-1):
    a,b=LI()
    G[a]+=[b]
    G[b]+=[a]
    if len(G[a])>2:
        r=a
    if len(G[b]) > 2:
        r=b

visited=[0]*n
visited[r]=1
def f(x):
    ret=0
    cnt=0
    for v in G[x]:
        if visited[v]:
            continue
        visited[v] = 1
        r=f(v)
        ret+=r
        if r==0:
            cnt+=1
    if cnt>1:
        ret+=cnt-1
    return ret

print(1 if r == -1 else f(r))

