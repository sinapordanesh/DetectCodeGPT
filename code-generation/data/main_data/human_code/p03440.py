#unionfind
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n


    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]


    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)


        if x == y:
            return


        if self.parents[x] > self.parents[y]:
            x, y = y, x


        self.parents[x] += self.parents[y]
        self.parents[y] = x


    def size(self, x):
        return -self.parents[self.find(x)]


    def same(self, x, y):
        return self.find(x) == self.find(y)


    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]


    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


    def group_count(self):
        return len(self.roots())


    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

n,m=map(int,input().split())
a=list(map(int,input().split()))
if n-1==m:
    print(0)
    exit()
if n<2*(n-m-1):
    print("Impossible")
    exit()
uf=UnionFind(n)
for _ in range(m):
    x,y=map(int,input().split())
    uf.union(x,y)
v=[[] for _ in range(n)]
for i in range(n):
    v[uf.find(i)].append((a[i],i))
flag=set()
ans,cnt=0,0
for t in v:
    if t:
        t.sort()
        c,idx=t[0]
        flag.add(idx)
        cnt+=1
        ans+=c
for i in range(n):
    a[i]=(a[i],i)
a.sort()
for i in range(n):
    if cnt==2*(n-m-1):
        break
    c,idx=a[i]
    if idx not in flag:
        ans+=c
        cnt+=1
print(ans)