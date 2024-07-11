class BinaryIndexedTree:
    def __init__(self, n):
        self.a = [0] * (n + 1)
        self.n = n

    def add(self, i, x):
        while i <= self.n:
            self.a[i] += x
            i += i & -i

    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.a[i]
            i -= i & -i
        return ret


class Solve:
    def __init__(self, n):
        self.n = n
        self.p = BinaryIndexedTree(n + 1)
        self.q = BinaryIndexedTree(n + 1)

    def add(self, s, t, x):
        t += 1
        self.p.add(s, -x * s)
        self.p.add(t, x * t)
        self.q.add(s, x)
        self.q.add(t, -x)

    def get_sum(self, s, t):
        t += 1
        return self.p.sum(t) + self.q.sum(t) * t - \
               self.p.sum(s) - self.q.sum(s) * s

    def dump(self):
        print(*(self.get_sum(i, i) for i in range(self.n + 1)))


n, q = map(int, input().split())
st = Solve(n)
buf = []
for _ in range(q):
    query = input().split()
    if query[0] == '0':
        st.add(*map(int, query[1:]))
    else:
        buf.append(st.get_sum(*map(int, query[1:])))
print('\n'.join(map(str, buf)))