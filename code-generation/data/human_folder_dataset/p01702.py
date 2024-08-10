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
    rr = []

    st = string.digits + string.ascii_uppercase

    while True:
        n,m,q = LI()
        if n == 0:
            break

        a = [LS() for _ in range(q)]
        if n == 1:
            rr.append('0'*m)
            continue
        u = [0] * m
        v = [0] * m
        ms = 0
        mk = 2**n - 1
        for t,s in a:
            mt = int(t[::-1],2)
            tu = ms ^ mt
            tv = mk ^ tu
            for i in range(m):
                if s[i] == '1':
                    u[i] |= tu
                    v[i] |= tv
                else:
                    v[i] |= tu
                    u[i] |= tv
            ms = tu

        r = ''
        for i in range(m):
            t = None
            for ti in range(n):
                if (u[i] & 2**ti) > 0 and (v[i] & 2**ti) == 0:
                    if t is None:
                        t = st[ti]
                    else:
                        t = '?'
                        break
            if not t:
                t = '?'
            r += str(t)

        rr.append(r)

    return '\n'.join(map(str, rr))


print(main())


