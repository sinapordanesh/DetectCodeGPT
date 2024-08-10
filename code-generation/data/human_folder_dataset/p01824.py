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
    a,b,c,n = LI()
    aa = [LI() for _ in range(n)]
    r = (a*b+b*c+c*a) * 2

    for d,e,f in aa:
        r += 6
        if d == 0:
            r -= 2
        if e == 0:
            r -= 2
        if f == 0:
            r -= 2
        if d == a-1:
            r -= 2
        if e == b-1:
            r -= 2
        if f == c-1:
            r -= 2

    def k(a,b):
        return sum(map(lambda x: abs(a[x]-b[x]), range(3)))

    for i in range(n):
        ai = aa[i]
        for j in range(i+1,n):
            if k(ai, aa[j]) == 1:
                r -= 2

    return r




print(main())

