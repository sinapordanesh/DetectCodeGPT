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
    k,r,l = LI()
    p = F()
    e = F()
    t = F()

    def f(k,r,l):
        if abs(r-t) <= e and abs(t-l) <= e:
            return 1
        if t-l > e or r-t > e:
            return 0
        if k == 0:
            if abs(t - (r+l) / 2) <= e:
                return 1
            return 0

        h = (r+l) / 2
        if h >= t:
            return f(k-1,r,h) * (1-p) + f(k-1,h,l) * p
        return f(k-1,r,h) * p + f(k-1,h,l) * (1-p)

    tr = f(k,r,l)

    return '{:0.9f}'.format(tr)



print(main())

