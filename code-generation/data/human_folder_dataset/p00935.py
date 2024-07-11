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

    while True:
        n = I()
        a = []
        while len(a) < n:
            a += LS()
        s = set()
        for i in range(n):
            s.add(int(a[i]))
            for j in range(i+1,min(i+2,n)):
                s.add(int(a[i]+a[j]))
                for k in range(j+1,min(j+2,n)):
                    s.add(int(a[i]+a[j]+a[k]))
        r = -1
        for i in range(1000):
            if not i in s:
                r = i
                break
        rr.append(r)
        break

    return '\n'.join(map(str, rr))


print(main())


