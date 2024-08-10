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

    def f(n):
        a = LI()
        l = len(a)
        s = set()
        r = 0
        for i in range(l-1):
            if abs(a[i] - a[i+1]) < 2:
                s.add((i,i+1))
        for i in range(4, l+1):
            for j in range(l-i+1):
                k = j + i - 1
                if (j+1, k-1) in s and abs(a[j] - a[k]) < 2:
                    s.add((j,k))
                    continue
                for m in range(j+2,k,2):
                    if (j,m-1) in s and (m,k) in s:
                        s.add((j,k))
                        break

        m = {}
        m[l] = 0
        def _f(i):
            if i in m:
                return m[i]
            r = 0
            for j in range(i,l+1):
                t = _f(j+1)
                if (i,j) in s:
                    t += j - i + 1
                if r < t:
                    r = t
            m[i] = r
            return r
        return _f(0)

    while True:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(map(str, rr))



print(main())

