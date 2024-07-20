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
    rr = []

    while True:
        n = I()
        if n == 0:
            break
        ms = []
        for _ in range(n):
            m,l = LI()
            a = [LI() for _ in range(m)]
            b = 0
            for s,e in a:
                for i in range(s,e):
                    b |= 2**(i-6)
            ms.append((l,b))

        d = collections.defaultdict(int)
        d[0] = 0
        for l,b in ms:
            for k,v in list(d.items()):
                if b&k > 0:
                    continue
                if d[b|k] < v + l:
                    d[b|k] = v + l
        rr.append(max(d.values()))

    return '\n'.join(map(str, rr))


print(main())


