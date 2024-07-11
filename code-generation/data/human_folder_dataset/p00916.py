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


# 二次元累積和
class Ruiwa():
    def __init__(self, a):
        self.H = h = len(a)
        self.W = w = len(a[0])
        self.R = r = a
        for i in range(h):
            for j in range(1,w):
                r[i][j] += r[i][j-1]

        for i in range(1,h):
            for j in range(w):
                r[i][j] += r[i-1][j]

    def search(self, x1, y1, x2, y2):
        if x1 > x2 or y1 > y2:
            return 0

        r = self.R
        rr = r[y2][x2]
        if x1 > 0 and y1 > 0:
            return rr - r[y1-1][x2] - r[y2][x1-1] + r[y1-1][x1-1]
        if x1 > 0:
            rr -= r[y2][x1-1]
        if y1 > 0:
            rr -= r[y1-1][x2]

        return rr

def main():
    rr = []

    def f(n):
        a = [LI() for _ in range(n)]
        xs = set()
        ys = set()
        for l,t,r,b in a:
            xs.add(l)
            xs.add(r)
            ys.add(t)
            ys.add(b)
        xd = {}
        for x,i in zip(sorted(xs), range(len(xs))):
            xd[x] = i
        yd = {}
        for y,i in zip(sorted(ys), range(len(ys))):
            yd[y] = i
        z = []
        for l,t,r,b in a:
            z.append([xd[l],yd[t],xd[r],yd[b]])
        xx = len(xs) + 3
        yy = len(ys) + 3
        aa = [[0]*xx for _ in range(yy)]
        ii = [2**i for i in range(n)]
        for i in range(n):
            l,t,r,b = map(lambda x: x+1, z[i])
            aa[b][l] += ii[i]
            aa[t][l] -= ii[i]
            aa[b][r] -= ii[i]
            aa[t][r] += ii[i]
        rui = Ruiwa(aa)
        t = rui.R
        def _f(i,j,k):
            if i < 0 or i >= yy or j < 0 or j >= xx:
                return
            if t[i][j] != k:
                return
            t[i][j] = -1
            for di,dj in dd:
                _f(i+di,j+dj,k)
        r = 0
        for i in range(yy):
            for j in range(xx):
                if t[i][j] >= 0:
                    _f(i,j,t[i][j])
                    r += 1
        return r

    while True:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(map(str,rr))


print(main())

