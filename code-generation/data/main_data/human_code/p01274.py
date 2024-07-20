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
        h = [I() for _ in range(n)]
        hm = max(h)
        m = I()
        ms = []
        ma = []
        zf = False
        for _ in range(m):
            nama,mp,target,damege = LS()
            mp = int(mp)
            damege = int(damege)
            if damege == 0:
                continue
            if mp == 0:
                zf = True
                continue
            if target == 'All':
                ma.append((mp,damege))
            else:
                ms.append((mp,damege))
        if zf:
            return 0
        ds = [inf] * (hm+1)
        ds[0] = 0
        for mp, dm in ms:
            for i in range(dm,hm+1):
                if ds[i] > mp + ds[i-dm]:
                    ds[i] = mp + ds[i-dm]
            if dm < 2:
                continue
            t = min(ds[-dm+1:])
            if ds[-1] > t + mp:
                ds[-1] = t + mp

        da = [inf] * (hm+1)
        da[0] = 0
        for mp, dm in ma:
            for i in range(dm,hm+1):
                if da[i] > mp + da[i-dm]:
                    da[i] = mp + da[i-dm]
            if dm < 2:
                continue
            t = min(da[-dm+1:])
            if da[-1] > t + mp:
                da[-1] = t + mp
        for i in range(hm-1,-1,-1):
            if ds[i] > ds[i+1]:
                ds[i] = ds[i+1]
            if da[i] > da[i+1]:
                da[i] = da[i+1]
        mm = r = inf
        for i in range(hm,-1,-1):
            if mm <= da[i]:
                continue
            mm = tp = da[i]
            for hi in h:
                if hi > i:
                    tp += ds[hi-i]
            if r > tp:
                r = tp
        return r

    while True:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(map(str,rr))


print(main())

