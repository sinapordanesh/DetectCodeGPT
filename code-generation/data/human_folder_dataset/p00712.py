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

    def f(p, q, a, n):
        r = 0
        fr = fractions.Fraction(p,q)
        q = [(fr, 0, 1)]
        if fr.numerator == 1 and fr.denominator <= a:
            r += 1
        n1 = n-1
        for i in range(1, 70):
            nq = []
            ti = fractions.Fraction(1, i)
            i2 = (i+1) ** 2
            for t, c, m in q:
                mik = m
                tt = t
                for k in range(1, n-c):
                    mik *= i
                    tt -= ti
                    if tt <= 0 or a < mik * i:
                        break
                    if tt.numerator == 1 and tt.denominator >= i and mik * tt.denominator <= a:
                        r += 1
                    if c+k < n1 and mik * (i ** max(math.ceil(tt / ti), 2)) < a:
                        nq.append((tt, c+k, mik))
                if m * (i ** max(math.ceil(t / ti), 2)) < a:
                    nq.append((t,c,m))
            if not nq:
                break
            q = nq
        return r

    while True:
        p, q, a, n = LI()
        if p == 0 and q == 0:
            break
        rr.append(f(p, q, a, n))

    return '\n'.join(map(str, rr))



print(main())

