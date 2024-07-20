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
        n,l = LI()
        if n == 0:
            break
        a = []
        b = []
        for _ in range(n):
            d,p = LS()
            if int(p) % 2 == 0:
                a.append((d,int(p),_+1))
            else:
                b.append((d,int(p),_+1))

        lc = 0
        rm = 0
        rf = False
        for d,p,i in a:
            if d == 'L':
                lc += 1
            m = int(p)
            if d == 'R':
                m = l - m
            if rm < m or (rm == m and d == 'L'):
                rm = m
                rf = d == 'R'
        ri = lc
        if rf:
            ri = lc + 1
        ari = -1
        if a:
            ari = a[ri-1][2]

        lc = 0
        rf = False
        af = True
        for d,p,i in b:
            if d == 'L':
                lc += 1
            m = int(p)
            if d == 'R':
                m = l - m
            if rm < m or (rm == m and d == 'L'):
                rm = m
                rf = d == 'R'
                af = False
        ri = lc
        if rf:
            ri = lc + 1
        bri = -1
        if b:
            bri = b[ri-1][2]

        if af:
            rr.append('{} {}'.format(rm, ari))
        else:
            rr.append('{} {}'.format(rm, bri))

    return '\n'.join(map(str, rr))


print(main())


