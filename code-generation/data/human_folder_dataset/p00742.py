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
    rr = []

    def f(n):
        ss = [S() for _ in range(n)]
        cs = set()
        nz = set()
        for s in ss:
            cs |= set([c for c in s])
            if len(s) > 1:
                nz.add(s[0])
        l = len(cs)
        ci = {}
        cw = [0] * l
        for c,i in zip(sorted(list(cs), key=lambda x: 0 if x in nz else 1), range(l)):
            if c in nz:
                nz.add(i)
            ci[c] = i
        for s in ss[:-1]:
            w = 1
            for c in s[::-1]:
                cw[ci[c]] += w
                w *= 10
        w = 1
        for c in ss[-1][::-1]:
            cw[ci[c]] -= w
            w *= 10
        r = 0
        al = l // 2
        bl = l - al
        cwa = cw[:al]
        cwb = cw[al:]
        for _a in itertools.combinations(range(1, 10), al):
            ad = collections.defaultdict(int)
            bd = collections.defaultdict(int)
            for a in itertools.permutations(_a, al):
                tw = 0
                for i in range(al):
                    tw += cwa[i] * a[i]
                ad[tw] += 1
            _b = [_ for _ in range(1, 10) if _ not in _a]
            for b in itertools.permutations(_b, bl):
                tw = 0
                for i in range(bl):
                    tw += cwb[i] * b[i]
                bd[tw] += 1
            aa = sorted(ad.items())
            ba = sorted(bd.items(), reverse=True)
            aal = len(aa)
            bal = len(ba)
            ai = bi = 0
            while ai < aal and bi < bal:
                t = aa[ai][0] + ba[bi][0]
                if t == 0:
                    r += aa[ai][1] * ba[bi][1]
                    ai += 1
                    bi += 1
                elif t < 0:
                    ai += 1
                else:
                    bi += 1
        # print('ci', ci)
        # print('cw', cw)
        zl = [_ for _ in range(l) if _ not in nz][::-1]
        al = l - len(zl)
        bl = l - al
        if al == 0 or bl < 2:
            cws = [cw[i+1] - cw[i] for i in range(l-1)]
            for a in itertools.permutations(range(1, 10), l-1):
                tw = 0
                for i in range(l-1):
                    tw += cw[i] * a[i]
                zz = l - 1
                for zi in zl:
                    while zz > zi:
                        zz -= 1
                        tw += cws[zz] * a[zz]
                    if tw == 0:
                        r += 1
        else:
            cwa = cw[:al]
            cwb = cw[al:]
            # print('cwa', cwa)
            # print('cwb', cwb)
            zl = [_ - al for _ in zl]
            for _a in itertools.combinations(range(1, 10), al):
                ad = collections.defaultdict(int)
                bd = collections.defaultdict(int)
                for a in itertools.permutations(_a):
                    tw = 0
                    for i in range(al):
                        tw += cwa[i] * a[i]
                    ad[tw] += 1
                _b = [_ for _ in range(1, 10) if _ not in _a]
                cws = [cwb[i+1] - cwb[i] for i in range(bl-1)]
                for b in itertools.permutations(_b, bl-1):
                    tw = 0
                    for i in range(bl-1):
                        tw += cwb[i] * b[i]
                    zz = bl - 1
                    for zi in zl:
                        while zz > zi:
                            zz -= 1
                            tw += cws[zz] * b[zz]
                        bd[tw] += 1
                aa = sorted(ad.items())
                ba = sorted(bd.items(), reverse=True)
                aal = len(aa)
                bal = len(ba)
                ai = bi = 0
                while ai < aal and bi < bal:
                    t = aa[ai][0] + ba[bi][0]
                    if t == 0:
                        r += aa[ai][1] * ba[bi][1]
                        ai += 1
                        bi += 1
                    elif t < 0:
                        ai += 1
                    else:
                        bi += 1
        return r

    while True:
        n = I()
        if n == 0:
            break
        rr.append(f(n))
        # print(rr[-1])

    return '\n'.join(map(str, rr))



print(main())

