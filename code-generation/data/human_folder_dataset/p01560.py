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


def main():
    n,m = LI()
    a = LI()
    p = [c / 100.0 for c in LI()]
    d = collections.defaultdict(lambda: 1.0)
    e = collections.defaultdict(lambda: 1)

    r = 0
    for k in range(1,1<<n):
        t = [i for i in range(n) if k & (1 << i)]
        l = k & (k-1)
        d[k] = d[l] * p[t[0]]
        e[k] = e[l] * a[t[0]] // fractions.gcd(a[t[0]], e[l])
        o = m // e[k]
        if len(t) % 2 == 1:
            r += o * d[k]
        else:
            r -= o * d[k]


    return '{:0.8f}'.format(r)


print(main())

