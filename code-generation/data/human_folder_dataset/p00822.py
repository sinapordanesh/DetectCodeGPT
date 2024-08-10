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
    mij = []
    for i in range(3):
        mi = []
        for j in range(3):
            mi.append([i*4+j,i*4+j+1,i*4+j+4,i*4+j+5])
        mij.append(mi)

    def f(n):
        a = [LI() for _ in range(n)]
        fs = set()
        def _f(i,j,d,d1,d4,d13,d16):
            if d >= n:
                return True
            key = (i,j,d,d1,d4,d13,d16)
            if key in fs:
                return False
            if i == 0:
                if j == 0:
                    d1 = d
                elif j == 2:
                    d4 = d
            elif i == 2:
                if j == 0:
                    d13 = d
                elif j == 2:
                    d16 = d
            for mm in mij[i][j]:
                if a[d][mm] > 0:
                    fs.add(key)
                    return False
            if d - min([d1,d4,d13,d16]) >= 7:
                fs.add(key)
                return False

            if _f(i,j,d+1,d1,d4,d13,d16):
                return True
            for ni in range(3):
                if i == ni:
                    continue
                if _f(ni,j,d+1,d1,d4,d13,d16):
                    return True
            for nj in range(3):
                if j == nj:
                    continue
                if _f(i,nj,d+1,d1,d4,d13,d16):
                    return True
            fs.add(key)
            return False

        if _f(1,1,0,-1,-1,-1,-1):
            return 1

        return 0

    while True:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(map(str,rr))


print(main())

