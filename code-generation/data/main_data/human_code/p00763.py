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


class WarshallFloyd():
    def __init__(self, e, n):
        self.E = e
        self.N = n

    def search(self):
        n = self.N
        nl = list(range(n))
        d = [[inf] * n for _ in nl]
        for k,v in self.E.items():
            for b,c in v:
                if d[k][b] > c:
                    d[k][b] = c
        for i in nl:
            for j in nl:
                if i == j:
                    continue
                for k in nl:
                    if i != k and j != k and d[j][k] > d[j][i] + d[i][k]:
                        d[j][k] = d[j][i] + d[i][k]
                        d[j][k] = d[j][i] + d[i][k]
        return d

def main():
    rr = []

    def f(n,m,c,s,g):
        ms = [LI() for _ in range(m)]
        ps = LI()
        qrs = [([0] + LI(),LI()) for _ in range(c)]
        ec = collections.defaultdict(lambda: collections.defaultdict(list))
        for x,y,d,cc in ms:
            ec[cc][x].append((y,d))
            ec[cc][y].append((x,d))
        nl = list(range(n+1))
        ad = [[inf] * (n+1) for _ in nl]
        for cc,v in ec.items():
            q, r = qrs[cc-1]
            wf = WarshallFloyd(v, n+1)
            d = wf.search()
            w = [0]
            for i in range(1, len(q)):
                w.append(w[-1] + (q[i]-q[i-1]) * r[i-1])

            for i in nl:
                for j in nl:
                    dk = d[i][j]
                    if dk == inf:
                        continue
                    ri = bisect.bisect_left(q, dk) - 1
                    dw = w[ri] + r[ri] * (dk - q[ri])
                    if ad[i][j] > dw:
                        ad[i][j] = dw

        ae = collections.defaultdict(list)
        for i in nl:
            ai = ad[i]
            for j in nl:
                if ai[j] < inf:
                    ae[i].append((j, ai[j]))
        awf = WarshallFloyd(ae, n+1)
        awd = awf.search()
        r = awd[s][g]

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

                for uv, ud in ae[u]:
                    if v[uv]:
                        continue
                    vd = k + ud
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))

            return d
        dkr = search(s)[g]
        if r == inf:
            return -1
        return r

    while True:
        n,m,c,s,g = LI()
        if n == 0 and m == 0:
            break
        rr.append(f(n,m,c,s,g))

    return '\n'.join(map(str, rr))



print(main())

