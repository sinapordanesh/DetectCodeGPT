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

    def f():
        r,c,m = LI()
        a = [[1] * (c+2)] + [[1] + [None if c == '.' else 1 for c in S()] + [1] for _ in range(r)] + [[1] * (c+2)]
        cost = [[1] * (c+2)] + [[1] + LI() + [1] for _ in range(r)] + [[1] * (c+2)]
        on = [[1] * (c+2)] + [[1] + LI() + [1] for _ in range(r)] + [[1] * (c+2)]
        off = [[1] * (c+2)] + [[1] + LI() + [1] for _ in range(r)] + [[1] * (c+2)]
        ms = [tuple(map(lambda x: x+1, LI())) for _ in range(m)]
        e = collections.defaultdict(list)
        for i in range(1,r+1):
            for j in range(1,c+1):
                if a[i][j]:
                    continue
                for di,dj in dd:
                    if a[i+di][j+dj]:
                        continue
                    e[(i,j)].append(((i+di,j+dj), 1))

        def search(s):
            d = collections.defaultdict(lambda: inf)
            d[s] = 0
            q = []
            heapq.heappush(q, (0, s))
            v = collections.defaultdict(bool)
            while len(q):
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                v[u] = True

                for uv, ud in e[u]:
                    if v[uv]:
                        continue
                    vd = k + ud
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))

            return d

        ad = {}
        for k in ms:
            if k in ad:
                continue
            ad[k] = search(k)
        ti = 0
        td = collections.defaultdict(list)
        c = ms[0]
        td[c].append(0)
        for t in ms[1:]:
            while c != t:
                cc = ad[t][c]
                for di,dj in dd:
                    ni = c[0] + di
                    nj = c[1] + dj
                    n = (ni, nj)
                    if ad[t][n] == cc - 1:
                        ti += 1
                        td[n].append(ti)
                        c = n
                        break

        r = 0
        for k,v in sorted(td.items()):
            i = k[0]
            j = k[1]
            cs = cost[i][j]
            onf = on[i][j] + off[i][j]
            tr = onf
            for vi in range(len(v)-1):
                sa = v[vi+1] - v[vi]
                tr += min(cs * sa, onf)
            r += tr

        return r

    while True:
        rr.append(f())
        break

    return '\n'.join(map(str,rr))


print(main())

