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

    while True:
        n = I()
        a = LI()

        l = len(a)
        if l == 1:
            rr.append(a[0]*2)
            break
        r = a[0] * 2
        p = [a[0]]
        for i in range(1,n):
            c = a[i]
            cp = c
            for j in range(i):
                b = a[j]
                bp = p[j]
                t = abs(b-c)
                u = ((b+c)**2 - t**2) ** 0.5
                tp = bp + u
                if cp < tp:
                    cp = tp
            p.append(cp)
            if r < cp + c:
                r = cp + c

        rr.append('{:00.9f}'.format(r))
        break

    return '\n'.join(map(str, rr))


print(main())


