import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
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


def main():
    rr = []

    def f(n):
        a,b = LS()
        if a == b:
            return 0
        a = [int(c) for c in a]
        b = [int(c) for c in b]
        aa = [a]
        ad = set()
        ad.add(tuple(a))
        r = 0
        while True:
            r += 1
            na = []
            for a in aa:
                ti = 0
                for i in range(r-1,n):
                    if a[i] != b[i]:
                        ti = i
                        break
                sa = b[ti] - a[ti]
                for j in range(ti+1, n+1):
                    t = [(a[i] + sa) % 10 if ti <= i < j else a[i] for i in range(n)]
                    k = tuple(t)
                    if k in ad:
                        continue
                    if t == b:
                        return r
                    ad.add(k)
                    na.append(t)
            aa = na

    while True:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(map(str,rr))


print(main())

