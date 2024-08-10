import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
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
        p,q = LI()
        if p == 0:
            break

        a = [S() for _ in range(p)]
        b = [S() for _ in range(q)]
        aa = [[0,0,0,0]]
        mc = 0
        for c in a:
            d = collections.Counter(c)
            t = aa[-1][:]
            t[0] += d['(']
            t[0] -= d[')']
            t[1] += d['{']
            t[1] -= d['}']
            t[2] += d['[']
            t[2] -= d[']']
            t[3] = 0
            for ct in c:
                if ct != '.':
                    break
                t[3] += 1
                if mc < t[3]:
                    mc = t[3]
            aa.append(t)
        k = []
        for c1,c2,c3 in itertools.product(range(1,min(mc+1,21)), repeat=3):
            f = True
            for ci in range(p):
                c = aa[ci]
                if c[0] * c1 + c[1] * c2 + c[2] * c3 != aa[ci+1][3]:
                    f = False
                    break
            if f:
                k.append((c1,c2,c3))
        bb = [[0,0,0]]
        for c in b:
            d = collections.Counter(c)
            t = bb[-1][:]
            t[0] += d['(']
            t[0] -= d[')']
            t[1] += d['{']
            t[1] -= d['}']
            t[2] += d['[']
            t[2] -= d[']']
            bb.append(t)

        r = [0]
        for c in bb[1:-1]:
            s = set()
            for c1,c2,c3 in k:
                s.add(c[0]*c1+c[1]*c2+c[2]*c3)
            if len(s) == 1:
                r.append(list(s)[0])
            elif sum(c) == 0:
                r.append(0)
            else:
                r.append(-1)

        rr.append(' '.join(map(str,r)))


    return '\n'.join(map(str,rr))


print(main())


