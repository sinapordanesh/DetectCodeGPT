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


class Prime():
    def __init__(self, m):
        self.M = m + 1
        self.A = a = [True] * self.M
        a[0] = a[1] = 0
        self.T = t = []
        sq = int(math.sqrt(self.M))
        q = 0
        for i in range(2, sq + 1):
            if not a[i]:
                a[i] = q
                continue
            t.append(i)
            a[i] = q
            q += 1
            for j in range(i*i,m,i):
                a[j] = False

        for i in range(sq + 1, self.M):
            if a[i]:
                a[i] = q
                q += 1
                t.append(i)
            else:
                a[i] = q

    def is_prime(self, n):
        return self.A[n]


def main():
    rr = []

    M = 7368792
    pr = Prime(M)

    def f(m, n):
        nn = n
        g = [None] * (m*m)
        for i in range(m, m*m):
            if not g[i]:
                if n == 0:
                    return i
                n -= 1
                for j in range(i, m*m, i):
                    g[j] = 1
        d = pr.A[m*m]
        return pr.T[d+n]

    while True:
        m,n = LI()
        if m == 0 and n == 0:
            break
        rr.append(f(m,n))

    return '\n'.join(map(str,rr))




print(main())

