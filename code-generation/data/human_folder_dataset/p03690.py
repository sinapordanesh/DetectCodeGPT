class UnionFindVerSize():
    def __init__(self, N):
        self._parent = [n for n in range(0, N)]
        self._size = [1] * N

    def find_root(self, x):
        if self._parent[x] == x: return x
        self._parent[x] = self.find_root(self._parent[x])
        return self._parent[x]

    def unite(self, x, y):
        gx = self.find_root(x)
        gy = self.find_root(y)
        if gx == gy: return

        if self._size[gx] < self._size[gy]:
            self._parent[gx] = gy
            self._size[gy] += self._size[gx]
        else:
            self._parent[gy] = gx
            self._size[gx] += self._size[gy]

    def get_size(self, x):
        return self._size[self.find_root(x)]

    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def calc_group_num(self):
        N = len(self._parent)
        ans = 0
        for i in range(N):
            if self.find_root(i) == i:
                ans += 1
        return ans

from collections import Counter

N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
A=0
for i in range(N):
    A^=a[i]
B=0
for i in range(N):
    B^=b[i]
a.append(A)
b.append(B)

if Counter(a)!=Counter(b):
    exit(print(-1))

val=set([])
for i in range(N+1):
    if a[i]!=b[i]:
        val.add(a[i])

if not val:
    exit(print(0))

val=list(val)
val.sort()
comp={i:e for e,i in enumerate(val)}
n=max(comp[d] for d in comp)+1

uf=UnionFindVerSize(n)
check=False
cnt=0
for i in range(N):
    if a[i]!=b[i]:
        uf.unite(comp[a[i]],comp[b[i]])
        if a[i]==b[-1]:
            check=True
        cnt+=1

print(cnt+uf.calc_group_num()-int(check))
