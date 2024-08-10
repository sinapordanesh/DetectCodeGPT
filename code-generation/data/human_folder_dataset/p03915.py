import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from operator import itemgetter

N,Q = map(int,readline().split())
m = map(int,read().split())
ABC = list(zip(m,m,m))

INF = 10 ** 18
cyclic_cost = [INF] * N
for a,b,c in ABC:
    if cyclic_cost[a] > c + 1:
        cyclic_cost[a] = c + 1
    if cyclic_cost[b] > c + 2:
        cyclic_cost[b] = c + 2

cyclic_cost += cyclic_cost # 2周分
x = INF
for i in range(N+N):
    x += 2
    if x < cyclic_cost[i]:
        cyclic_cost[i] = x
    x = cyclic_cost[i]
cyclic_cost = [x if x < y else y for x,y in zip(cyclic_cost, cyclic_cost[N:])]

ABC += [(i,i+1,c) for i,c in enumerate(cyclic_cost)]
ABC[-1] = (N-1,0,cyclic_cost[-1])

class UnionFind:
    def __init__(self,N):
        self.root = list(range(N))
        self.size = [1] * (N)
        
    def find_root(self,x):
        root = self.root
        while root[x] != x:
            root[x] = root[root[x]]
            x = root[x]
        return x
    
    def merge(self,x,y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return False
        sx,sy = self.size[x],self.size[y]
        if sx < sy:
            self.root[x] = y
            self.size[y] += sx
        else:
            self.root[y] = x
            self.size[x] += sy
        return True

ABC.sort(key = itemgetter(2))

uf = UnionFind(N)
merge = uf.merge
answer = 0
for a,b,c in ABC:
    if merge(a,b):
        answer += c

print(answer)