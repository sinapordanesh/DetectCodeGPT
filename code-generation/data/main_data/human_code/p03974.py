import sys
readline = sys.stdin.readline
class Node:
    def __init__(self, sigma, depth):
        self.end = False
        self.child = [None] * sigma
        self.depth = depth
        self.count = 0
    def __setitem__(self, i, x):
        self.child[i] = x
    def __getitem__(self, i):
        return self.child[i]

class Trie():
    def __init__(self, sigma):
        self.sigma = sigma
        self.root = Node(sigma, 0)
    
    def add(self, S):
        vn = self.root
        vn.count += 1
        for cs in S:
            if vn[cs] is None:
                vn[cs] = Node(self.sigma, vn.depth + 1)
            vn = vn[cs]
            vn.count += 1
        vn.end = True

T = Trie(26)
N = int(readline())
Di = [None]*N

for i in range(N):
    S = list(map(lambda x: ord(x)-97, readline().strip()))
    Di[i] = S
    T.add(S)

Q = int(readline())
Ans = [None]*Q
Query = [[] for _ in range(N)]
for qu in range(Q):
    k, p = readline().strip().split()
    k = int(k)-1
    p = list(map(lambda x:ord(x)-97, p))
    pinv = [None]*26
    for i in range(26):
        pinv[p[i]] = i
    Query[k].append((qu, pinv))

for k in range(N):
    if not Query[k]:
        continue
    cost = [[0]*26 for _ in range(26)]
    geta = 0
    vn = T.root
    for si in Di[k]:        
        for ti in range(26):
            if si != ti and vn[ti] is not None:
                cost[si][ti] += vn[ti].count
        vn = vn[si]
        if vn.end:
            geta += 1
    L, P = map(list, zip(*Query[k]))
    M = len(P)
    for idx in range(M):
        res = 0
        invp = P[idx]
        for i in range(26):
            for j in range(26):
                if invp[i] > invp[j]:
                    res += cost[i][j]
        Ans[L[idx]] = res+geta
        
print('\n'.join(map(str, Ans)))     
