import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

class UnionFind:
    def __init__(self, n):
        self.state = [-1] * n
        self.size_table = [1] * n
        # cntはグループ数
        # self.cnt = n

    def root(self, u):
        v = self.state[u]
        if v < 0: return u
        self.state[u] = res = self.root(v)
        return res

    def merge(self, u, v):
        ru = self.root(u)
        rv = self.root(v)
        if ru == rv: return
        du = self.state[ru]
        dv = self.state[rv]
        if du > dv: ru, rv = rv, ru
        if du == dv: self.state[ru] -= 1
        self.state[rv] = ru
        # self.cnt -= 1
        self.size_table[ru] += self.size_table[rv]
        return

    # グループの要素数
    def size(self, u):
        return self.size_table[self.root(u)]

def ng():
    for u in range(n):
        for v in range(n):
            if v == u: continue
            if to[u][v]: continue
            if uf.root(u)==uf.root(v):return True
    return False

n,m=MI()
to=[[False]*n for _ in range(n)]
for _ in range(m):
    u,v=MI1()
    to[u][v]=to[v][u]=True

uf=UnionFind(n)
uncon=[-1]*n
for u in range(n):
    pv=-1
    for v in range(n):
        if v==u:continue
        if to[u][v]:continue
        if pv==-1:pv=v
        else:uf.merge(pv,v)
    uncon[u]=pv

#print(uf.state)
#print(uf.size_table)
#print(uncon)

if ng():
    print(-1)
    exit()

fin=[False]*n
free=0
ss=[]
for u in range(n):
    if uncon[u]==-1:
        free+=1
        continue
    r0=uf.root(u)
    if fin[r0]:continue
    r1=uf.root(uncon[u])
    fin[r0]=fin[r1]=True
    ss.append(abs(uf.size_table[r0]-uf.size_table[r1]))
cur=1<<1000
for s in ss:cur=cur<<s|cur>>s
cur>>=1000
d=(cur&-cur).bit_length()-1
d=max(0,d-free)
s0=(n-d)//2
s1=n-s0
print(s0*(s0-1)//2+s1*(s1-1)//2)
