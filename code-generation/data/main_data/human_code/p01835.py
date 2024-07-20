import sys

class Set:
    __slots__ = ["data", "one", "N", "N0", "size"]

    def __init__(self, N):
        self.data = [0]*(N+1)
        self.one = [0]*(N+1)
        self.N = N
        self.N0 = 2**(N.bit_length()-1)
        self.size = 0

    def __get(self, k):
        s = 0
        data = self.data
        while k:
            s += data[k]
            k -= k & -k
        return s

    def __add(self, k, x):
        N = self.N
        self.one[k] += x
        #assert 0 <= self.one[k]
        data = self.data
        while k <= N:
            data[k] += x
            k += k & -k
        self.size += x

    def __lower_bound(self, x):
        w = i = 0; k = self.N0
        N = self.N; data = self.data
        while k:
            if i+k <= N and w + data[i+k] <= x:
                w += data[i+k]
                i += k
            k >>= 1
        return i

    def add(self, x, y = 1):
        #assert 0 <= x < self.N
        self.__add(x+1, y)

    def remove(self, x, y = 1):
        #assert 0 <= x < self.N
        self.__add(x+1, -y)

    def find(self, x):
        if self.one[x+1] == 0:
            return -1
        return self.__get(x+1)

    def __contains__(self, x):
        return self.one[x+1] > 0

    def __iter__(self):
        x = self.next(0); N = self.N
        while x < N:
            for i in range(self.one[x+1]):
                yield x
            x = self.next(x+1)

    def count(self, x):
        #assert 0 <= x < self.N
        return self.one[x+1]

    def __len__(self):
        return self.size

    def prev(self, x):
        #assert 0 <= x <= self.N
        v = self.__get(x+1) - self.one[x+1] - 1
        if v == -1:
            return -1
        return self.__lower_bound(v)

    def next(self, x):
        #assert 0 <= x <= self.N
        if x == self.N or self.one[x+1]:
            return x
        v = self.__get(x+1)
        return self.__lower_bound(v)

    def at(self, k):
        v = self.__lower_bound(k)
        #assert 0 <= k and 0 <= v < self.N
        return v

    def __getitem__(self, k):
        return self.__lower_bound(k)

def solve():
    readline = sys.stdin.readline
    write = sys.stdout.write

    N, K = map(int, readline().split())
    T = int(readline())
    A = [[] for i in range(N+1)]
    B = [[] for i in range(N+1)]
    X = [0]*T
    s = Set(T)
    for i in range(T):
        l, r, x = map(int, readline().split())
        A[l-1].append(i)
        B[r].append(i)
        X[i] = x
    c = 0
    ans = 0
    for i in range(N):
        for k in A[i]:
            s.add(k)
            p0 = s.prev(k)
            p1 = s.next(k+1)
            if p0 != -1 and p1 < T:
                if X[p0]+1 == X[p1]:
                    c -= 1
            if p0 != -1:
                if X[p0]+1 == X[k]:
                    c += 1
            if p1 < T:
                if X[k]+1 == X[p1]:
                    c += 1
        for k in B[i]:
            s.remove(k)
            p0 = s.prev(k)
            p1 = s.next(k+1)
            if p0 != -1:
                if X[p0]+1 == X[k]:
                    c -= 1
            if p1 < T:
                if X[k]+1 == X[p1]:
                    c -= 1
            if p0 != -1 and p1 < T:
                if X[p0]+1 == X[p1]:
                    c += 1
        if len(s) == K and c == K-1:
            ans += 1
    write("%d\n" % ans)
solve()

