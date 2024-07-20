def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


class UF:
    def __init__(self, N):
        self.state = [-1] * N
        self.rank = [0] * N
        self.num_group = N
    
    def get_parent(self, a):
        p = self.state[a]
        if p < 0:
            return a
        
        q = self.get_parent(p)
        self.state[a] = q
        return q

    def make_pair(self, a, b):
        pa = self.get_parent(a)
        pb = self.get_parent(b)
        if pa == pb:
            return

        if self.rank[pa] > self.rank[pb]:
            pa, pb = pb, pa
            a, b = b, a
        elif self.rank[pa] == self.rank[pb]:
            self.rank[pb] += 1

        self.state[pb] += self.state[pa]
        self.state[pa] = pb
        self.state[a] = pb
        self.num_group -= 1
    
    def is_pair(self, a, b):
        return self.get_parent(a) == self.get_parent(b)

    def get_size(self, a):
        return -self.state[self.get_parent(a)]


N, M = read_values()
A = read_list()
uf = UF(N)
for _ in range(M):
    i, j = read_index()
    uf.make_pair(A[i] - 1, A[j] - 1)

res = 0
for i, a in enumerate(A):
    if uf.is_pair(i, A[i] - 1):
        res += 1

print(res)
