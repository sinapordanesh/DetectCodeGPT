class UnionFind:
    def __init__(self, size):
        self.table = [-1] * size
    
    def find(self, x):
        while self.table[x] >= 0:
            x = self.table[x]
        return x
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.table[x_root] < self.table[y_root]:
                self.table[x_root] += self.table[y_root]
                self.table[y_root] = x_root
            else:
                self.table[y_root] += self.table[x_root]
                self.table[x_root] = y_root
    
    def isDisjoint(self, x, y):
        return self.find(x) != self.find(y)

def solve():
    import sys
    file_input = sys.stdin
    N, M = map(int, file_input.readline().split())
    
    piles = [tuple(map(int, file_input.readline().split())) for i in range(N)]
    
    fences = []
    for i in range(M):
        p, q = map(int, file_input.readline().split())
        p -= 1
        q -= 1
        px, py = piles[p]
        qx, qy = piles[q]
        fence_len = ((px - qx) ** 2 + (py - qy) ** 2) ** 0.5
        fences.append((fence_len, p, q))
    
    fences.sort(reverse=True)
    S = UnionFind(N)
    fences_len = 0
    
    for f_len, p1, p2 in fences:
        if S.isDisjoint(p1, p2):
            S.union(p1, p2)
        else:
            fences_len += f_len
    
    print(fences_len)

solve()
