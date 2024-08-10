'''
N頂点の木があり、i番目の辺は頂点x_iとy_iを結んでいる。
各頂点を白または黒で塗り、どの黒い頂点からどの黒い頂点へも黒い頂点のみをたどって到達できる時、
頂点vが黒であるような頂点の色の組み合わせは何通りか？Mで割ったあまりを求めよ。
graph_i
input:
3 100
1 2
2 3
output:
    3
    4
    3

'''
# region header
import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
import copy
# @lru_cache(maxsize=None)
# sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7
# endregion
# region input function


def inp():
    '''
    一つの整数
    '''
    return int(input())


def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))


def str_inp():
    '''
    文字列をリストとして読み込む
    '''
    return list(input()[:-1])


# endregion

# setting
unit = 1  # 単位元


def merge(a, b):
    # モノイド演算
    return a * b % M


def adj_bu(a, i):
    # bottom up DP
    return a + 1


def adj_td(a, i, p):
    # top down DP
    return a + 1


def adj_fin(a, i):
    # 最終結果
    return a
#####


n, M = inpl()
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = inpl()
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
parent = [-1] * n
root = 0  # 0を根とする
queue = collections.deque([root])
sorted_graph = []  # トポロジカルソート

# トポロジカルソート
while queue:
    i = queue.popleft()
    sorted_graph.append(i)
    for a in graph[i]:
        if a != parent[i]:
            parent[a] = i
            graph[a].remove(i)  # graph：隣接リストから子リストにする
            queue.append(a)

# Bottom up DP

BU = [unit] * n  # acc[i]と対応
res = [0] * n
for i in sorted_graph[1:][::-1]:
    res[i] = adj_bu(BU[i], i)
    p = parent[i]
    BU[p] = merge(BU[p], res[i])
res[sorted_graph[0]] = adj_fin(BU[sorted_graph[0]], sorted_graph[0])  # 根だけ別で


# Top down DP

TD = [unit] * n
for i in sorted_graph:
    # 左からDP
    tmp = TD[i]
    for j in graph[i]:
        TD[j] = tmp
        tmp = merge(tmp, res[j])
    # 右からDP
    tmp = unit
    for j in graph[i][::-1]:
        TD[j] = adj_td(merge(TD[j], tmp), j, i)
        tmp = merge(tmp, res[j])
        res[j] = adj_fin(merge(BU[j], TD[j]), j)
print(*res, sep="\n")
'''
各頂点に対して結果を出力するので全方位木を考える。
全方位木では子→親の木DPと親→子の木DPを使う。
acc[i][p]:ノードiにおける親pを除いた全方向からの累積
res[i][p]:acc[i][p]に調整を加えたもの
acc[i]:ノードiにおけるすべての方向からの集約
'''
