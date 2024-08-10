class Tree():
    def __init__(self, n, decrement=1):
        self.n = n
        self.edges = [[] for _ in range(n)]
        self.root = None
        self.size = [1]*n       # number of nodes in subtree
        self.decrement = decrement

    def add_edge(self, u, v):
        u, v = u-self.decrement, v-self.decrement
        self.edges[u].append(v)
        self.edges[v].append(u)

    def add_edges(self, edges):
        for u, v in edges:
            u, v = u-self.decrement, v-self.decrement
            self.edges[u].append(v)
            self.edges[v].append(u)

    def set_root(self, root):
        root -= self.decrement
        self.depth = [-1]*self.n
        self.root = root
        self.par = [-1]*self.n
        self.depth[root] = 0
        self.order = [root]
        next_set = [root]
        while next_set:
            p = next_set.pop()
            for q in self.edges[p]:
                if self.depth[q] != -1: continue
                self.par[q] = p
                self.depth[q] = self.depth[p]+1
                self.order.append(q)
                next_set.append(q)
        for p in self.order[::-1]:
            for q in self.edges[p]:
                if self.par[p] == q: continue
                self.size[p] += self.size[q]

    def rerooting(self, op, merge, id):
        # assert self.root is not None
        dp1 = [id] * self.n
        dp2 = [id] * self.n
        for p in self.order[::-1]:
            t = id
            for q in self.edges[p]:
                if self.par[p] == q: continue
                dp2[q] = t
                t = merge(t, op(dp1[q], p, q))
            t = id
            for q in self.edges[p][::-1]:
                if self.par[p] == q: continue
                dp2[q] = merge(t, dp2[q])
                t = merge(t, op(dp1[q], p, q))
            dp1[p] = t
        for q in self.order[1:]:
            pq = self.par[q]
            dp2[q] = op(merge(dp2[q], dp2[pq]), q, pq)
            dp1[q] = merge(dp1[q], dp2[q])
        return dp1

#########################################################################################################
import sys
input = sys.stdin.readline


# edges = make_tree(10,show=True)
# N = len(edges)+1

# example()

N = int(input())
T = Tree(N)
for _ in range(N-1):
    x, y = map(int, input().split())
    T.add_edge(x,y)
T.set_root(1)

##########################################################
def op(a, p, q):
    # define how the dp[q] is determined by children of q if setting (p, q) = (parent, child)
    # Cation: p, q are now defined by 0-indexed
    return a/(len(T.edges[q])-1) + 1 if a != 0 else 1

def merge(a, b):
    # define how the O(N) info. {r in ch(q)} in op({r in ch(q)}, p, q) の {r in ch(q)} is reduced to O(1) info.
    return a + b

# identity elem. of merge
id = 0
##########################################################

dp = T.rerooting(op, merge, id)
res = [""]*N
for i in range(N):
    res[i] = str(dp[i]/len(T.edges[i]))
print("\n".join(res))