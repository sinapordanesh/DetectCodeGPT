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

    def f(n):
        a = [LI() for _ in range(n)]
        q = []
        d = [0] * 2
        for t,c in a:
            heapq.heappush(q, (0,0,t,c*2))

        while q:
            ct, l, t, c = heapq.heappop(q)
            nx = l ^ 1
            nt = ct + t
            if d[nx] > nt:
                nt = d[nx]
            else:
                d[nx] = nt
            if c > 1:
                heapq.heappush(q, (nt,nx,t,c-1))

        return max(d)


    while 1:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(map(str, rr))


print(main())

