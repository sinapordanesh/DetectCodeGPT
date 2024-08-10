# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10 ** 9)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
INF=float('inf')

N,M=MAP()
nodes=[[] for i in range(N)]
for i in range(M):
    u,v=MAP()
    nodes[u].append(v)
    nodes[v].append(u)

visited=[False]*N
timer=1
prenum=[0]*(N+1)
parent=[0]*(N+1)
lowest=[0]*(N+1)
def rec(cur, prev):
    global timer
    # curを訪問した直後の処理
    prenum[cur]=lowest[cur]=timer
    timer+=1

    visited[cur]=True
    for nxt in nodes[cur]:
        if not visited[nxt]:
            # curからvへ訪問する直前の処理
            parent[nxt]=cur
            rec(nxt, cur)
            # vの探索が終了した直後の処理
            lowest[cur]=min(lowest[cur], lowest[nxt])
        elif nxt!=prev:
            # cur -> v がback-edgeの場合の処理
            lowest[cur]=min(lowest[cur], prenum[nxt])

# 必要な各値の取得
rec(0, -1)

# 間接点
ap=set()
# ルートの子ノードの数
np=0
for i in range(1, N):
    p=parent[i]
    if p==0:
        np+=1
    # 条件2の確認
    elif prenum[p]<=lowest[i]:
        ap.add(p)
# 条件1の確認
if np>1:
    ap.add(0)

ap=sorted(ap)
for a in ap:
    print(a)

