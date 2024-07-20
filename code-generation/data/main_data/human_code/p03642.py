import sys
input = sys.stdin.readline

import itertools
from collections import defaultdict
import numpy as np

N = int(input())
X = set(int(x) for x in input().split())

# 2は素数でないとして扱って
U = 10**7 + 100
is_prime = np.zeros(U,dtype=np.bool)
is_prime[3::2] = 1
for p in range(3,U,2):
    if p*p > U:
        break
    if is_prime[p]:
        is_prime[p*p::p+p] = 0

# imosで値を入れないといけない場所
X ^= set(x+1 for x in X)

EV = set(x for x in X if x%2 == 0)
OD = set(x for x in X if x%2 == 1)

# 1手でとれるペアを見つける：最大マッチング
# 奇点から偶点に辺を貼る
source = -1
sink = -2
graph = defaultdict(dict)
for x in EV:
    graph[x][sink] = 1
    graph[sink][x] = 0
for x in OD:
    graph[source][x] = 1
    graph[x][source] = 0
for x,y in itertools.product(OD,EV):
    if is_prime[abs(x-y)]:
        graph[x][y] = 1
        graph[y][x] = 0

def bfs():
    level = defaultdict(int)
    q = [source]
    level[source] = 1
    d = 1
    while q:
        d += 1
        if level[sink] != 0:
            break
        qq = []
        for x in q:
            for y,cap in graph[x].items():
                if cap==0 or level[y]!=0:
                    continue
                level[y] = d
                qq.append(y)
        q = qq
    return level

def dfs(v,f,level,itr):
    if v == sink:
        return f
    for w,cap in itr[v]:
        if cap==0 or level[w]!=level[v]+1:
            continue
        d = dfs(w,min(f,cap),level,itr)
        if d:
            graph[v][w] -= d
            graph[w][v] += d
            return d
    return 0

def max_flow():
    flow = 0
    while True:
        level = bfs()
        if level[sink] == 0:
            return flow
        itr = {v:iter(graph[v].items()) for v in graph}
        while True:
            f = dfs(source,10**9,level,itr)
            if f == 0:
                break
            flow += f

f = max_flow()

od = len(OD); ev = len(EV)
answer = f
od -= f; ev -= f
answer += 2*(od//2); od %= 2
answer += 2*(ev//2); ev %= 2
if od:
    answer += 3
print(answer)