import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)


def main():
    n,m = LI()
    xc = collections.Counter(LI())

    c = collections.defaultdict(int)
    d = collections.defaultdict(int)
    for x,v in xc.items():
        if v % 2 == 1:
            c[x % m] += 1
        d[x % m] += v

    r = d[0] // 2
    if m % 2 == 0:
        r += d[m // 2] // 2

    for i in range(1, (m+1)//2):
        t = min(d[i], d[m-i])
        r += t
        r += (d[i] - max(c[i], t)) // 2
        r += (d[m-i] - max(c[m-i], t)) // 2

    return r

print(main())



