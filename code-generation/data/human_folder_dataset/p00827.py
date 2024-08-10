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
        a,b,c = LI()
        if a == 0:
            break
        r = inf
        x = inf
        y = inf
        for i in range(c*5):
            t = a * i
            if t < c and (c - t) % b == 0:
                tr = c
                tx = i
                ty = (c-t) // b
                if x+y > tx+ty or (x+y==tx+ty and r > tr):
                    r = tr
                    x = tx
                    y = ty

            if  t >= c and (t-c) % b == 0:
                tr = t - c + t
                tx = i
                ty = (t-c) // b
                if x+y > tx+ty or (x+y==tx+ty and r > tr):
                    r = tr
                    x = tx
                    y = ty

            if (t+c) % b == 0:
                tr = t + c + t
                tx = i
                ty = (t+c) // b
                if x+y > tx+ty or (x+y==tx+ty and r > tr):
                    r = tr
                    x = tx
                    y = ty

        rr.append('{} {}'.format(x,y))

    return '\n'.join(map(str,rr))


print(main())


