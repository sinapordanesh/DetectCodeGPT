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

    dd = [(1,1),(1,0),(0,1),(0,-1),(-1,0),(-1,-1)]

    while True:
        n,q = LI()
        if n == 0 and q == 0:
            break
        a = [LS() for _ in range(n)]
        a = [[_[0],int(_[1]),int(_[2])] for _ in a]
        b = [I() for _ in range(q)]
        for c in b:
            r = 'Unknown'
            for l,e,w in a:
                if w-e < c <= w:
                    r = '{} {}'.format(l, e-w+c)
            rr.append(r)

    return '\n'.join(map(str, rr))


print(main())


