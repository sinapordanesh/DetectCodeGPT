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

    while True:
        n,m,k = LI()
        if n == 0:
            break
        r = [[0] * (n*m+1) for _ in range(n+1)]
        r[0][0] = 1
        for i in range(n):
            for j in range(i,n*m):
                if r[i][j] == 0:
                    break
                for kk in range(1,m+1):
                    r[i+1][j+kk] += r[i][j] / m
        t = 0
        for kk in range(n*m+1):
            c = max(kk-k,1)
            t += c * r[n][kk]
        rr.append('{:0.9f}'.format(t))

    return '\n'.join(map(str, rr))


print(main())


