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
lowest=[0]*(N+1)
ans=[]
def rec(cur, prev):
    global timer
    # curを訪問した直後の処理
    prenum[cur]=lowest[cur]=timer
    timer+=1

    visited[cur]=True
    for nxt in nodes[cur]:
        # 未訪問なら再帰探索する
        if not visited[nxt]:
            rec(nxt, cur)
            # nxtの探索が終了した直後の処理
            lowest[cur]=min(lowest[cur], lowest[nxt])
            # より近い経路を含まないなら橋とする
            if lowest[nxt]==prenum[nxt]:
                # 番号の小さい方から入れる
                ans.append((min(cur, nxt), max(cur, nxt)))
        # 訪問済の場合、親への経路は無視して、他は近い経路となるか確認を取る
        elif nxt!=prev:
            lowest[cur]=min(lowest[cur], lowest[nxt])

rec(0, -1)

ans.sort()
for edge in ans:
    print(*edge)

