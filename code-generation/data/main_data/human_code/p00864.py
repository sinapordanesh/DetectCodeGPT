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
        n,w = LI()
        if n == 0:
            break
        a = [I() for _ in range(n)]
        ma = max(a)
        l = (ma // w + 1)
        b = [0] * l
        for c in a:
            b[c//w] += 1
        h = max(b)
        r = 0.01
        for i in range(l):
            bi = b[i]
            d = (l-i-1) / (l-1)
            r += d * bi / h
        rr.append(r)

    return '\n'.join(map(str, rr))


print(main())


