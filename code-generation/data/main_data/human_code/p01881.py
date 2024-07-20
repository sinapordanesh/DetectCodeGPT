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
    h,w = LI()
    mp = [S() for _ in range(h)]

    def search(ss):
        d = collections.defaultdict(lambda: inf)
        q = []
        for s in ss:
            d[s] = 0
            heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for di,dj in dd:
                ni = u[0] + di
                nj = u[1] + dj
                if ni < 0 or ni >= h or nj < 0 or nj >= w or mp[ni][nj] == '#':
                    continue
                uv = (ni, nj)
                if v[uv]:
                    continue
                vd = k + 1
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return d

    ss = []
    ps = None
    es = None
    for i in range(h):
        for j in range(w):
            if mp[i][j] == '$':
                ss.append((i,j))
            elif mp[i][j] == '@':
                ps = (i,j)
            elif mp[i][j] == '%':
                es = (i,j)
    pd = search(ss)
    d = search([ps])
    if d[es] < pd[es]:
        return 'Yes'

    return 'No'


print(main())


