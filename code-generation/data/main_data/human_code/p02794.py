from copy import deepcopy
from itertools import product

class EulerTour:
    def __init__(self, N):
        self.N = N
        self.G = [[] for _ in range(N)]
    
    def add_edge(self, a, b):
        self.G[a].append(b)
        self.G[b].append(a)
    
    def from_graph(self, G, copy=False):
        if copy: self.G = deepcopy(G)
        else: self.G = G
            
    def build(self, root=0, lca=True):
        self.root = root
        self._dfs(root)
        self.In = [0]*self.N
        self.Out = [0]*self.N
        for i, v in enumerate(self.node_list):
            if self.In[v] == 0:
                self.In[v] = i
            self.Out[v] = i
        if lca:
            self.seg = SegTree(len(self.node_list))
            self.seg.build([self.d[self.node_list[i]] for i in range(len(self.node_list))])
    
    def lca(self, a, b):
        if self.root in (a,b):
            return self.root
        a_out, b_in = self.Out[a], self.In[b]
        if a_out > b_in:
            a_out, b_in = self.Out[b], self.In[a]
        if a_out > b_in:
            a_out, b_in = self.Out[b], self.Out[a]
        if a_out > b_in:
            a_out, b_in = self.Out[a], self.Out[b]
        idx = self.seg.find(a_out, b_in+1)
        return self.node_list[idx]
            
    def _dfs(self, root=0):
        self.idx2edge = {}
        self.edge2idx = {}
        self.node_list = []
        self.edge_list = []
        seen = [0]*len(self.G)
        prev = [0]*len(self.G)
        self.d =[-1]*len(self.G)
        todo = [~root, root]
        count = 0
        while todo:
            a = todo.pop()
            if a >= 0:
                seen[a] = 1
                self.d[a] = self.d[prev[a]] + 1
                edge = (prev[a], a)
                self.idx2edge[count] = edge
                self.edge2idx[edge] = count
                self.edge_list.append(count)
                self.node_list.append(a)
                count += 1
                for b in reversed(self.G[a]):
                    if seen[b]: continue
                    todo.append(~b)
                    todo.append(b)
                    prev[b] = a
            else: 
                edge = (prev[~a], ~a)
                idx = self.edge2idx[edge]
                self.edge_list.append(-idx)
                if ~a != root: self.node_list.append(prev[~a])
                    
class SegTree:
    """ segment tree with point modification and range product. """
    # # https://yukicoder.me/submissions/452850
    def __init__(self, N, data_f = min, data_unit=1<<30):
        self.N = N
        self.data_f = data_f
        self.data_unit = data_unit
        self.data = [self.data_unit] * (N + N)

    def build(self, raw_data):
        data = self.data
        f = self.data_f
        N = self.N
        data[N:] = raw_data[:]
        for i in range(N - 1, 0, -1):
            data[i] = f(data[i << 1], data[i << 1 | 1])

    def set_val(self, i, x):
        data = self.data
        f = self.data_f
        i += self.N
        data[i] = x
        while i > 1:
            data[i >> 1] = f(data[i], data[i ^ 1])
            i >>= 1

    def fold(self, L, R):
        """ compute for [L, R) """
        vL = vR = self.data_unit
        data = self.data
        f = self.data_f
        L += self.N
        R += self.N
        while L < R:
            if L & 1:
                vL = f(vL, data[L])
                L += 1
            if R & 1:
                R -= 1
                vR = f(data[R], vR)
            L >>= 1
            R >>= 1
        return f(vL, vR)
    
    def find(self, L, R):
        x = self.fold(L,R)
        while R-L>1:
            M = (R+L)//2
            if self.fold(L,M)==x: R = M
            else: L = M
        return L

from collections import deque

def bfs(G,s,edge2idx):
    seen = [0]*N
    todo = deque()
    seen[s]=1
    todo.append(s)
    cumedge = [set() for _ in range(N)]
    while len(todo):
      a = todo.popleft()
      for b in G[a]:
        if seen[b] == 0:
          seen[b] = 1
          todo.append(b)
          cumedge[b] = deepcopy(cumedge[a])
          idx = edge2idx[(a,b)]
          cumedge[b].add(idx)
    return cumedge
      
N=int(input())
et = EulerTour(N)
for i in range(N-1):
  a,b=map(int,input().split())
  et.add_edge(a-1,b-1)
  
et.build(0)
cumedge = bfs(et.G,0,et.edge2idx)

M = int(input())
path_list = [0]*M
for i in range(M):
  u,v = map(int,input().split())
  u,v = u-1,v-1
  w = et.lca(u,v)
  path_list[i] = (cumedge[u] - cumedge[w]) | (cumedge[v] - cumedge[w])

ans = 2**(N-1)
for i,p in enumerate(product(range(2),repeat=M)):
  if i == 0: continue
  union = set.union(*[path_list[i] for i in range(M) if p[i]])
  ans += (-1)**sum(p) * 2**(N-1-len(union))

print(ans)