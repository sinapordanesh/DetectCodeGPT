import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    rr = []
    ii = [2**i for i in range(21)]

    def f(a,b):
        r = 0
        for i in range(3):
            r += (a[i]-b[i]) ** 2
        return r

    while True:
        n,m = LI()
        a = [LF() for _ in range(n)]
        sa = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                sa[i][j] = f(a[i],a[j])

        r = 0
        for i in range(2**n):
            t = [_ for _ in range(n) if i&ii[_]]
            if len(t) != m:
                continue
            tr = 0
            for i in range(m):
                for j in range(i+1,m):
                    tr += sa[t[i]][t[j]]
            if r < tr:
                r = tr

        rr.append(r)
        break

    return '\n'.join(map(str, rr))


print(main())


