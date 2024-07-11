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
    n = I()
    ni = 0
    t = 0

    while ni < n:
        ni += 1
        a = LS()
        if a[1] == '(':
            t -= int(a[2])
        else:
            t += int(a[2])

        if t == 0:
            rr.append('Yes')
        else:
            rr.append('No')


    return '\n'.join(map(str, rr))


print(main())


