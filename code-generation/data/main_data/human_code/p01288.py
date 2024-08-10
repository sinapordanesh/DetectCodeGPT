import sys
sys.setrecursionlimit(10 ** 6)


class UnionFindTree:
    """Disjoint-Set Data Structure
       Union-Find Tree
       complexity:
          init: O(n)
          find, unite, same: O(alpha(n))
       used in SRM505 div.2 900, ATC001 A, DSL1A(AOJ)
    """
    def __init__(self, n):
        self.par = list(range(n))  # parent
        self.rank = [0] * n  # depth of tree

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


while True:
    N, Q = map(int, input().split())
    if N == Q == 0:
        break
    parents = [0] + [int(input()) - 1 for _ in range(N - 1)]
    queries = []
    marked = set()
    for _ in range(Q):
        k, v = input().split()
        v = int(v) - 1
        if k == "Q":
            queries.append((k, v))
        elif k == "M" and v not in marked:
            marked.add(v)
            queries.append((k, v))

    uf = UnionFindTree(N)
    for i in range(1, N):
        if i not in marked:
            p_root = uf.find(parents[i])
            uf.par[i] = p_root
            uf.rank[p_root] = max(uf.rank[p_root], uf.par[i] + 1)
    ans = 0
    for k, v in reversed(queries):
        if k == "Q":
            ans += uf.find(v) + 1
        elif not uf.same(v, parents[v]):
            p_root = uf.find(parents[v])
            uf.par[v] = p_root
            uf.rank[p_root] = max(uf.rank[p_root], uf.par[v] + 1)
    print(ans)

