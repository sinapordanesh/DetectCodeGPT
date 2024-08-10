class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i&-i
        return s
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i&-i
n, q = map(int, input().split())
c = list(map(int, input().split()))
last = [-1]*n
foradd = [[] for i in range(n)]
for i in range(n):
    if last[c[i]-1] != -1: foradd[last[c[i]-1]].append(i)
    last[c[i]-1] = i
forsum = [[] for i in range(n)]
for i in range(q):
    l, r = map(int, input().split()); l -= 1; r -= 1
    forsum[l].append([r, i])
bit = Bit(n); ans = [-1]*q
for i in range(n-1, -1, -1):
    for j in foradd[i]: bit.add(j, 1)
    for j in forsum[i]: ans[j[1]] = j[0]-i+1-bit.sum(j[0])
print(*ans, sep="\n")