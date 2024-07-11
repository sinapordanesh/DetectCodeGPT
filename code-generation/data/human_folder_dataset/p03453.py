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

def dijkstra(s):
    hq=[(0,s)]
    dist=[INF]*n
    dp=[0]*n
    dp[s]=1
    dist[s]=0
    checked=[0]*n
    while hq:
        min_dist,u=heappop(hq)
        if checked[u]:
            continue
        checked[u]=1
        for v,c in G[u]:
            if dist[u]+c<dist[v]:
                dist[v]=dist[u]+c
                dp[v]=dp[u]
                heappush(hq,(dist[v],v))
            elif dist[u]+c==dist[v]:
                dp[v]+=dp[u]
                dp[v]%=mod
    return dp, dist

n, m = LI()
s, t = LI()
G = [[] for _ in range(n)]
for _ in range(m):
    a,b, d = LI()
    G[a - 1] += [(b - 1, d)]
    G[b - 1] += [(a - 1, d)]

dp1,dist1=dijkstra(s-1)
dp2,dist2=dijkstra(t-1)
total=dist1[t-1]
ans=dp1[t-1]*dp2[s-1]%mod
for i in range(n):
    if dist1[i]==dist2[i]==total/2:
        ans-=pow(dp1[i]*dp2[i]%mod,2,mod)

for j in range(n):
    for k, ci in G[j]:
        if dist1[j]+dist2[k]+ci==total and dist1[j]<total/2 and dist2[k]<total/2:
            ans-=pow(dp1[j]*dp2[k]%mod,2,mod)

print(ans%mod)






