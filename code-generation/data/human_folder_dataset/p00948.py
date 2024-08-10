import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    n,q = LI()
    qa = sorted([LI() for _ in range(q)])
    u = [0] * (n+2)
    d = [0] * (n+2)

    for x,i in qa:
        u[i+1] = u[i] + 1
        d[i] = d[i+1] + 1
    rr = []
    for i in range(1,n+1):
        rr.append(u[i]+d[i]+1)


    return ' '.join(map(str,rr))


print(main())


