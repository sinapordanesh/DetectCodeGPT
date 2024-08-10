import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
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
        a = [LS() for _ in range(n)]
        s = S()
        k = S()
        l = len(k)
        if s == k:
            rr.append(0)
            continue
        u = set([s])
        c = set([s])
        t = 0
        r = -1
        while c:
            t += 1
            ns = set()
            for cs in c:
                for d,e in a:
                    nt = cs.replace(d,e)
                    if len(nt) > l:
                        continue
                    ns.add(nt)
            if k in ns:
                r = t
                break
            c = ns - u
            u |= ns
        rr.append(r)

    return '\n'.join(map(str,rr))


print(main())


