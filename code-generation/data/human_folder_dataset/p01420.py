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


nm = {}
def nCr(n, b):
    if b > n - b:
        b = n - b
    key = (n,b)
    if key in nm:
        return nm[key]
    r = 1
    for k in range(n, n-b, -1):
        r = r * k
    d = 1
    for k in range(1, b+1):
        d = d * k
    nm[key] = r / d
    return nm[key]


def main():
    rr = []

    n,m,l = LI()
    ps = [LI() for _ in range(n)]
    ts = []
    rs = []
    us = []

    for p,t,v in ps:
        if v == 0:
            ts.append(0)
            rs.append(0)
            us.append(0)
            continue
        p /= 100
        u = l / v
        ti = []
        ri = []
        for i in range(m+1):
            ti.append(u+t*i)
            k = pow(1-p, m-i) * pow(p, i) * nCr(m, i)
            ri.append(k)
        ts.append(ti)
        rs.append(ri)
        ui = ri[:]
        for i in range(1,m+1):
            ui[i] += ui[i-1]
        us.append(ui)

    for i in range(n):
        r = 0
        if ts[i] == 0:
            rr.append(r)
            continue
        for j in range(m+1):
            tr = rs[i][j]
            tt = ts[i][j] + 1.0 / 10**10
            for k in range(n):
                if i == k or ts[k] == 0:
                    continue
                bi = bisect.bisect_left(ts[k], tt)
                if bi > 0:
                    tr *= 1 - us[k][bi-1]
            r += tr
        rr.append('{:.9f}'.format(r))

    return '\n'.join(map(str,rr))


print(main())

