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

    def f(n,m):
        a = [LI() for _ in range(n*2-1)]
        e = collections.defaultdict(set)
        ds = []
        for i in range(n):
            for j in range(m):
                if i < n - 1 and a[i*2+1][j] == 0:
                    e[(i,j)].add((i+1,j))
                    e[(i+1,j)].add((i,j))
                    ds.append(set([(i,j),(i+1,j)]))
                if j < m - 1 and a[i*2][j] == 0:
                    e[(i,j)].add((i,j+1))
                    e[(i,j+1)].add((i,j))
                    ds.append(set([(i,j),(i,j+1)]))

        def search(s, ns):
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

                for uv in e[u]:
                    if v[uv]:
                        continue
                    if uv in ns and u in ns:
                        continue
                    vd = k + 1
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))

            return d

        nd = collections.defaultdict(lambda: -1)
        for ns in ds:
            td = search((n-1,m-1), ns)
            for k in ns:
                if nd[k] < td[k]:
                    nd[k] = td[k]

        def ff(mx):
            def search2(s):
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

                    for uv in e[u]:
                        if v[uv]:
                            continue
                        vd = k + 1
                        if vd + nd[uv] >= mx:
                            continue
                        if d[uv] > vd:
                            d[uv] = vd
                            heapq.heappush(q, (vd, uv))

                return d

            fd = search2((0,0))
            return fd[(n-1,m-1)] >= mx

        mm = n*m*3
        r = bs(ff,0,mm)

        if r >= mm:
            return -1

        return r - 1

    while True:
        n,m = LI()
        if n == 0:
            break
        rr.append(f(n,m))

    return '\n'.join(map(str, rr))


print(main())

