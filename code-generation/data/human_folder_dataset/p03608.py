class WarshallFloyd:
    #O(V^3)で任意２頂点の最短距離
    def __init__(self,n,_first_index=0):
        self.v = n
        self._first_idx=_first_index
        self.d = [[float("INF")]*(n) for _ in range(n)]
        for i in range(n):
            self.d[i][i] = 0

    def path(self,x,y,c):
        if x == y:
            return False
        f=self._first_idx
        self.d[x-f][y-f] = c
        self.d[y-f][x-f] = c
        return True

    def build(self):
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    self.d[i][j] = min(self.d[i][j], self.d[i][k] + self.d[k][j])
        return self.d
n,m,r=map(int,input().split())
rs=[x-1 for x in map(int,input().split())]
w=WarshallFloyd(n,1)
for i in range(m):w.path(*map(int,input().split()))
v=w.build()
from itertools import permutations as pe
print(min(sum(v[f][t]for f,t in zip(i,i[1:]))for i in pe(rs)))
