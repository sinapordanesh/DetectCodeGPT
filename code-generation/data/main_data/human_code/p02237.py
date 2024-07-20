# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10 ** 9)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
INF=float('inf')

N=INT()
G=[[0]*N for i in range(N)]
for i in range(N):
    l=LIST()
    u=l[0]
    l=l[2:]
    for v in l:
        G[u-1][v-1]=1

for i in range(N):
    print(*G[i])

