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

    while True:
        s = S()
        if s == '0':
            break
        d = collections.defaultdict(int)
        r = 0
        for c in s:
            c = int(c)
            nd = collections.defaultdict(int)
            for k,v in d.items():
                nd[(k*10+c) % 11] = v
            if c > 0:
                nd[c] += 1
            r += nd[0]
            d = nd
        rr.append(r)

    return '\n'.join(map(str, rr))



print(main())

