import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353

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

    m = 2**15
    a = [[0]*(m+1) for _ in range(5)]
    a[0][0] = 1
    for i in range(1,m):
        ii = i**2
        if ii > m:
            break
        for k in range(4):
            for j in range(ii,m+1):
                a[k+1][j] += a[k][j-ii]

    def f(n):
        r = 0
        for i in range(5):
            r += a[i][n]
        return r

    while True:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(map(str, rr))


print(main())


