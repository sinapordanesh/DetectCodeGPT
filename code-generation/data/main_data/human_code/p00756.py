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

    while True:
        n = I()
        if n == 0:
            break

        a = [LI() for _ in range(n)]
        s = [set() for _ in range(n)]
        d = collections.defaultdict(list)
        for i in range(n):
            d[a[i][3]].append(i)
            for j in range(i):
                k = (a[i][0] - a[j][0]) ** 2 + (a[i][1] - a[j][1]) ** 2
                l = (a[i][2] + a[j][2]) ** 2
                if k < l:
                    s[i].add(j)

        ps = None
        for v in d.values():
            l = len(v) // 2
            vs = set(map(lambda x: tuple(sorted([tuple(sorted([x[i*2], x[i*2+1]])) for i in range(l)])), itertools.permutations(v)))
            vl = list(vs)
            if ps is None:
                ps = vl
            else:
                ps = list(map(lambda x: list(x[0]) + list(x[1]),itertools.product(ps,vl)))

        r = 0
        for pa in ps:
            f = True
            ts = set(range(n))
            pas = set(pa)
            tr = 0
            while f:
                f = False
                for p in list(pas):
                    if len(ts & s[p[0]]) == 0 and len(ts & s[p[1]]) == 0:
                        ts.remove(p[0])
                        ts.remove(p[1])
                        pas.remove(p)
                        f = True
                        tr += 2
            if r < tr:
                r = tr

        rr.append(r)

    return '\n'.join(map(str, rr))



print(main())

