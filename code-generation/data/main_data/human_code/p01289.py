import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)


# 陝ｻ譛ｬ 4-1
# Ax=b繧定ｧ｣縺・ A縺ｯ豁｣譁ｹ陦悟・, 隗｣縺後↑縺・r荳諢上〒縺ｪ縺・ｴ蜷医・None繧定ｿ斐☆
def gauss_jordan(A, b):
    n = len(A)
    B = [A[i][:] for i in range(n)]
    for i in range(n):
        B[i].append(b[i])

    for i in range(n):
        pivot = i
        abp = abs(B[i][i])
        for j in range(i+1, n):
            if abp < abs(B[j][i]):
                abp = abs(B[j][i])
                pivot = j
        B[i],B[pivot] = B[pivot],B[i]
        if abp < eps:
            return

        for j in range(i+1, n+1):
            B[i][j] /= B[i][i]
        for j in range(n):
            if j == i:
                continue
            for k in range(i+1, n+1):
                B[j][k] -= B[j][i] * B[i][k]

    return list(map(lambda x: x[-1], B))

def main():
    def f():
        n,s,t = LI()
        if n < 1:
            return None

        s -= 1
        t -= 1
        p = LI()
        aa = [LI() for _ in range(n)]

        e = collections.defaultdict(list)
        for i in range(n):
            ai = aa[i]
            for j in range(n):
                if ai[j] == 0:
                    continue
                e[i].append((j, ai[j]))

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

        d = search(t)
        if d[s] == inf:
            return "impossible"

        A = [[0]*n for _ in range(n)]
        b = [0] * n
        for i in range(n):
            if i == t or d[i] == inf:
                A[i][i] = 1
                b[i] = 0
                continue

            mv = 0
            mk = 0
            di = d[i]
            ai = aa[i]
            for j in range(n):
                if ai[j] < 1 or (p[i] == 1 and d[j] + ai[j] != di):
                    continue
                mv += 1
                mk += ai[j]
                A[i][j] = -1

            A[i][i] = mv
            b[i] = mk

        r = gauss_jordan(A, b)
        if r is None:
            return "impossible"

        return "{:0.9f}".format(r[s])

    rr = []
    while True:
        r = f()
        if r is None:
            break
        rr.append(r)

    return JA(rr, "\n")

# start = time.time()
print(main())
# pe(time.time() - start)




