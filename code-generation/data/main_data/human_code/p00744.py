import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

class Flow():
    def __init__(self, e, N):
        self.E = e
        self.N = N
        self.nl = list(range(N))

    def max_flow(self, s, t):
        r = 0
        e = self.E
        v = None

        def f(c):
            v[c] = 1
            if c == t:
                return 1
            for i in e[c]:
                if v[i] is None and f(i):
                    e[c].remove(i)
                    e[i].add(c)
                    return 1
            return

        while True:
            v = [None] * self.N
            if f(s) is None:
                break
            r += 1

        return r

def main():
    rr = []

    def f(m, n):
        b = LI()
        while len(b) < m:
            b += LI()
        r = LI()
        while len(r) < n:
            r += LI()
        s = m + n + 2
        e = collections.defaultdict(set)
        for i in range(m):
            e[0].add(i+1)
        for i in range(n):
            e[m+i+1].add(s-1)

        for i in range(m):
            for j in range(n):
                if fractions.gcd(b[i], r[j]) > 1:
                    e[i+1].add(m+j+1)

        fl = Flow(e, s)

        return fl.max_flow(0, s-1)

    while True:
        m, n = LI()
        if m == 0 and n == 0:
            break
        rr.append(f(m,n))

    return '\n'.join(map(str, rr))



print(main())

