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

    def f(n,m,cap):
        cap *= 10
        s,t = LS()
        e = collections.defaultdict(list)
        for _ in range(n):
            a,b,c = LS()
            c = int(c)
            e[a].append((b,c))
            e[b].append((a,c))
        cs = set([S() for _ in range(m)])

        def search(s,t):
            d = collections.defaultdict(lambda: inf)
            d[(s,cap)] = 0
            q = []
            heapq.heappush(q, (0, (s,cap)))
            v = collections.defaultdict(bool)
            while len(q):
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                v[u] = True
                if u[0] == t:
                    return k

                for uv, ud in e[u[0]]:
                    uc = u[1] - ud
                    if uc < 0:
                        continue
                    if uv in cs:
                        uc = cap
                    uv = (uv, uc)
                    if v[uv]:
                        continue
                    vd = k + ud
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))

            return None

        r = search(s,t)
        if r is None:
            return -1

        return r

    while 1:
        n,m,l = LI()
        if n == 0:
            break
        rr.append(f(n,m,l))
        # print('rr', rr[-1])

    return '\n'.join(map(str,rr))


print(main())

