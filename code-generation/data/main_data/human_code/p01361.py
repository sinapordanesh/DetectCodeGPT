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

def bs(f, mi, ma):
    mm = -1
    while ma > mi:
        mm = (ma+mi) // 2
        if f(mm):
            mi = mm + 1
        else:
            ma = mm
    if f(mm):
        return mm + 1
    return mm

def main():
    rr = []

    def f(hi,hm):
        n,m = LI()
        a = [S() for _ in range(n)]
        t = I()
        d = {}
        for _ in range(t):
            c,i = LS()
            d[c] = int(i)
        t = I()
        mv = [LS() for _ in range(t)]
        t = I()
        p = [I() for _ in range(t)]
        b = [[d[c] for c in s] for s in a]
        cu = [0,0]
        dms = []
        for c,i in mv:
            i = int(i)
            for _ in range(i):
                if c == 'D':
                    cu[0] += 1
                elif c == 'U':
                    cu[0] -= 1
                elif c == 'R':
                    cu[1] += 1
                else:
                    cu[1] -= 1
                dm = b[cu[0]][cu[1]]
                if dm > 0:
                    dms.append(dm)
        dl = len(dms)
        fm = {}
        sh = hi
        si = dl
        for i in range(dl):
            if dms[i] >= sh:
                si = i
                break
            sh -= dms[i]

        pl = len(p)

        def ff(k):
            if k == 0:
                return (si,sh)
            if k in fm:
                return fm[k]
            r = (0,sh)
            for i in range(pl):
                if k & (1<<i):
                    ti,th = ff(k-(1<<i))
                    th += p[i]
                    if th > hm:
                        th = hm
                    tj = dl
                    for j in range(ti,dl):
                        if dms[j] >= th:
                            tj = j
                            break
                        th -= dms[j]
                    t = (tj,th)
                    if r < t:
                        r = t
            fm[k] = r
            return r

        r = ff(2**pl-1)

        # print('b',b)
        # print('hi,hm',hi,hm)
        # print('dms',dms)
        # print('p',p)
        # print('fm',fm)

        if r[0] == dl:
            return 'YES'

        return 'NO'

    while True:
        n,m = LI()
        if n == 0:
            break
        rr.append(f(n,m))

    return '\n'.join(map(str, rr))


print(main())

