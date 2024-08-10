from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
 
def dfs1(v):
    visited[v] = 1
    for to in graph[v]:
        if not visited[to]:
            dfs1(to)
    order.append(v)
 
def dfs2(v, comp):
    comp.append(v)
    visited[v] = 1
    for to in reversed_graph[v]:
        if not visited[to]:
            dfs2(to, comp)
 
def scc(n, edges):
    for a, b in edges:
        graph[a].append(b)
        reversed_graph[b].append(a)
     
    for i in range(n):
        if not visited[i]:
            dfs1(i)
             
    visited = [0] * n
    components = []
    for i in reversed(order):
        if not visited[i]:
            comp = []
            dfs2(i, comp)
            components.append(comp)
 
    print(len(components))
    for comp in components:
        print(len(comp), *comp)
 
N, M = map(int, input().split())
graph = defaultdict(list)
reversed_graph = defaultdict(list)
visited = [0] * N
order = []
edges = [list(map(int, input().split())) for _ in range(M)]
scc(N, edges)