import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
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
    rr = []

    while True:
        n = I()
        if n == 0:
            break
        a = [LI() for _ in range(n)]
        d = collections.defaultdict(lambda: inf)
        d[0] = 0
        cp = 0
        ct = 0
        r = inf
        for i in range(n):
            p,t = a[i]
            e = collections.defaultdict(lambda: inf)
            for k,ck in list(d.items()):
                if k < 3 and abs(cp-p) * (k+1) + ct <= t:
                    if e[k+1] > ck + abs(cp-p):
                        e[k+1] = ck + abs(cp-p)
                if cp * (k+1) + p + ct <= t:
                    if e[1] > ck + cp + p:
                        e[1] = ck + cp + p
            d = e
            if len(e) == 0:
                r = i + 1
                break
            cp = p
            ct = t

        if r < inf:
            rr.append('NG {}'.format(r))
        else:
            for k,ck in d.items():
                if r > ck + cp:
                    r = ck + cp
            rr.append('OK {}'.format(r))

    return '\n'.join(map(str,rr))


print(main())


