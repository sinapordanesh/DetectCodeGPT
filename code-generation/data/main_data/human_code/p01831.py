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
    n = I()
    s = S()
    a = [2] + [None if s[i] == '>' else 1 for i in range(n)] + [2]

    def f(i):
        if i < 0 or i > n+1:
            return (0, None)
        c = 0
        nl = i-1
        nr = i+1
        ni = i
        while a[ni] != 2:
            if a[ni] is None:
                ni = nr
                nr += 1
            else:
                ni = nl
                nl -= 1
            c += 1
        return (c, ni == 0)

    ma = n+1
    mi = 0
    mm = (ma+mi) // 2
    r = 0
    while ma > mi:
        mm = (ma+mi) // 2
        c,ff = f(mm)
        if r < c:
            r = c
        if ff:
            mi = mm + 1
        else:
            ma = mm
    for i in range(mm-1,mm+2):
        c,ff = f(i)
        if r < c:
            c = r

    return r



print(main())


