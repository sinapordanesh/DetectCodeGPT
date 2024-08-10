#!/usr/bin python3
# -*- coding: utf-8 -*-

# ワーシャルフロイド法
# 全頂点間最短路
# d[i][j]は2頂点間i, j間の移動コストを格納, Mは頂点数

INF = float("inf")
import copy

def warshall_floyd(d):
    n = len(d)
    wf = copy.deepcopy(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                wf[i][j] = min(wf[i][j], wf[i][k] + wf[k][j])

    return wf #wf[i][j]に頂点i, j間の最短距離を格納

##############################

n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]

if d != warshall_floyd(d):
    print(-1)
else:
    ret = 0
    for i in range(n):
        for j in range(i+1,n):
            if i == j: continue
            ret += d[i][j]
            for mid in range(n):
                if mid in (i, j): continue
                if d[i][mid] + d[mid][j] == d[i][j]:
                    ret -= d[i][j]
                    break
    print(ret)