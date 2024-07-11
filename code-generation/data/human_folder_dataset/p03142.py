
class Graph:
    def __init__(self, n_vertices, edges, directed=True):
        self.n_vertices = n_vertices
        self.edges = edges
        self.directed = directed

    @property
    def adj(self):
        try:
            return self._adj
        except AttributeError:
            adj = [[] for _ in range(self.n_vertices)]
            if self.directed:
                for u,v in self.edges:
                    adj[u].append(v)
            else:
                for u,v in self.edges:
                    adj[u].append(v)
                    adj[v].append(u)
            self._adj = adj
            return adj

max2 = lambda x,y: x if x > y else y
min2 = lambda x,y: x if x < y else y

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

def solve(N, edges):
    adj = Graph(N, edges, directed=True).adj
    parent = [-1]*N
    
    # find root
    deg = [0]*N
    for u,v in edges:
        deg[v] += 1

    root = next(v for v,d in enumerate(deg) if d==0)

    topo = [-1]*N
    stack = [root]
    for i in range(N):
        v = stack.pop()
        topo[i] = v
        for u in adj[v]:
            deg[u] -= 1
            if deg[u] == 0:
                stack.append(u)

    dist = [0]*N
    for v in topo:
        d = dist[v]
        for u in adj[v]:
            dist[u] = max2(dist[u], d+1)

    parent = [-1]*N
    for v,l in enumerate(adj):
        d = dist[v]+1
        for u in l:
            if d == dist[u]:
                parent[u] = v
    return (p+1 for p in parent)




if __name__ == '__main__':
    N,M = map(int,readline().split())
    m = map(lambda x: int(x)-1, read().split())
    edges = list(zip(m,m))
    print(*solve(N,edges), sep='\n')