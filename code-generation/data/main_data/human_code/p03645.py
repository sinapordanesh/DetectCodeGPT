import heapq
import sys
input = lambda :sys.stdin.readline().rstrip()

def INPUT(mode=int):
    return list(map(mode, input().split()))

def Dijkstra_heap(s, edge):
    # 始点sから各頂点への最短距離#始点sから各頂点への最短距離
    d = [10**20] * n
    used = [False] * n
    d[s] = 0
    used[s] = True
    edgelist = []
    for i, j in edge[s]:
        heapq.heappush(edgelist, i+j*(10**6))
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        v = minedge % (10**6)
        # まだ使われてない頂点の中から最小の距離のものを探す
        if used[v]: continue
        d[v] = minedge // (10**6)
        used[v] = True
        for e in edge[v]:
            if not used[e[0]]:
                heapq.heappush(edgelist, e[0]+(e[1]+d[v]) * (10**6))
    return d

n, m = INPUT()
AB = [INPUT() for _ in range(m)]
edge = [[] for _ in range(n)]
for a, b in AB:
    a -= 1
    b -= 1
    edge[a].append((b, 1))
    edge[b].append((a, 1))

dist = Dijkstra_heap(0, edge)
if dist[-1] <= 2:
  print("POSSIBLE")
else:
  print("IMPOSSIBLE")