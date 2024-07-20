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

    M = 20000
    s = set()
    for i in range(int(M**0.5)+1):
        for j in range(int(M**0.5)+1):
            t = i**2+j**2
            if t > 1:
                s.add(t)

    n = I()
    ni = 0
    while ni < n:
        ni += 1
        a,b = LI()
        t = a**2 + b**2
        r = 'P'
        for c in s:
            if t % c == 0 and t // c in s:
                r = 'C'
                break

        rr.append(r)

    return '\n'.join(map(str, rr))


print(main())


