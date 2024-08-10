import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,h,w = list(map(int, input().split()))
from collections import defaultdict
ns = defaultdict(list)
for i in range(n):
    r,c,a = list(map(int, input().split()))
    r -= 1; c -= 1
    c += h
    ns[r].append((a,c))
    ns[c].append((a,r))
class UnionFindTree:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.size = [1] * n
        self.es = [0]*n

    def root(self, i):
        inter = set()
        while self.parent[i]!=i:
            inter.add(i)
            i = self.parent[i]
        r = i
        for i in inter:
            self.parent[i] = r
        return r

    def connect(self, i, j):
        ri = self.root(i)
        rj = self.root(j)
        if ri==rj:
            self.es[ri] += 1
            return
        if self.size[ri]<self.size[rj]:
            self.parent[ri] = rj
            self.size[rj] += self.size[ri]
            self.es[rj] += self.es[ri] + 1
        else:
            self.parent[rj] = ri
            self.size[ri] += self.size[rj]
            self.es[ri] += self.es[rj] + 1

def selectEdge(ns):
    """各頂点に1本以下の接続枝を割り当てて、重み最大化
    """
    from heapq import heappop as hpp, heappush as hp
    q = []
    for u in ns.keys():
        for a,v in ns[u]:
            if u<v:
                hp(q, (-a,(u,v)))
    # 辺を選択できる = 選択した場合の連結成分において頂点数>=枝数
    uf = UnionFindTree(h+w)
    ans = 0
    while q:
        a, (u,v) = hpp(q)
        a *= -1
        ru = uf.root(u)
        rv = uf.root(v)
        if ru==rv and uf.es[ru]<uf.size[ru]:
            uf.connect(u,v)
            ans += a
        elif ru!=rv and (uf.es[ru]+uf.es[rv]+1) <= (uf.size[ru]+uf.size[rv]):
            uf.connect(u,v)
            ans += a
    return ans,uf
ans,uf = selectEdge(ns)
print(ans)