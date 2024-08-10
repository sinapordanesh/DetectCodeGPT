import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**3
eps = 1.0 / 10**10
mod = 10**9+7

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
        n,q = LI()
        if n == 0:
            break
        a = [LI() for _ in range(n)]
        d = collections.defaultdict(int)
        for c in a:
            for cc in c[1:]:
                d[cc] += 1
        t = sorted([[-v,k] for k,v in d.items() if v >= q])
        if len(t) == 0:
            rr.append(0)
        else:
            rr.append(t[0][1])

    return '\n'.join(map(str, rr))


print(main())


