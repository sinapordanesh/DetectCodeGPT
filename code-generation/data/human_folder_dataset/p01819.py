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
    n,m = LI()
    a = [S() for _ in range(m)]
    b = [0] * (n+1)
    c = [0] * (n+1)
    for i in range(n):
        for j in range(m):
            if a[j][i] == 'W':
                b[i] += 1
            else:
                c[i] += 1

    for i in range(n):
        c[i+1] += c[i]

    for i in range(n-2,-1,-1):
        b[i] += b[i+1]

    m = b[0]
    r = 0
    for i in range(n):
        tm = b[i+1] + c[i]
        if m > tm:
            r = i + 1
            m = tm

    return '{} {}'.format(r,r+1)


print(main())


