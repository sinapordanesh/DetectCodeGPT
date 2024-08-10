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
        w,d = LI()
        if w == 0:
            break
        a = sorted(LI())
        b = sorted(LI())
        ai = 0
        bi = 0
        r = 0
        while ai < w or bi < d:
            if ai >= w:
                r += sum(b[bi:])
                break
            if bi >= d:
                r += sum(a[ai:])
                break
            if a[ai] == b[bi]:
                r += a[ai]
                ai += 1
                bi += 1
            elif a[ai] < b[bi]:
                r += a[ai]
                ai += 1
            else:
                r += b[bi]
                bi += 1
        rr.append(r)

    return '\n'.join(map(str, rr))


print(main())


