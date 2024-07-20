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
        n,t,l,b = LI()
        if n == 0:
            break
        ls = set([I() for _ in range(l)])
        bs = set([I() for _ in range(b)])
        r = [[0] * (n+1) for _ in range(t+2)]
        r[0][0] = 1
        for i in range(t):
            for j in range(n):
                if r[i][j] == 0:
                    continue
                for k in range(1,7):
                    nj = j+k
                    if nj > n:
                        nj = n - (nj-n)
                    ni = i + 1
                    if nj in ls:
                        ni += 1
                    if nj in bs:
                        nj = 0
                    if nj == n:
                        ni = t
                    r[ni][nj] += r[i][j] / 6.0
        rr.append('{:0.9f}'.format(r[t][n]))

    return '\n'.join(map(str, rr))


print(main())


