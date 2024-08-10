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
    m = 10**6

    a = [inf] * m
    b = [inf] * m
    a[0] = 0
    b[0] = 0
    for i in range(1,200):
        t = i * (i+1) * (i+2) // 6
        mm = min(t*5,m)
        for j in range(t,mm):
            if a[j] > a[j-t] + 1:
                a[j] = a[j-t] + 1
        if t % 2 == 0:
            continue
        for j in range(t,m):
            if b[j] > b[j-t] + 1:
                b[j] = b[j-t] + 1

    while True:
        n = I()
        if n == 0:
            break
        rr.append('{} {}'.format(a[n],b[n]))



    return '\n'.join(map(str, rr))


print(main())


