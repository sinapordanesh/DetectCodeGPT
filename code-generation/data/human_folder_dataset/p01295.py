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

    def f(n,m):
        n -= 1
        i = 1
        l = 1
        for k in range(1,10):
            if n > 10**(k-1) * 9 * k:
                n -= 10**(k-1) * 9 * k
                i = 10 ** k
                l = k + 1
            else:
                break
        i += n // l
        n %= l
        r = ''
        for j in range(i,i+101):
            r += str(j)
        return r[n:n+m]

    while True:
        n,m = LI()
        if n == 0 and m == 0:
            break
        rr.append(f(n,m))

    return '\n'.join(map(str,rr))


print(main())

