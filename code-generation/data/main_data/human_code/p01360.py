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

    while True:
        s = S()
        if s == '#':
            break

        l = True
        lr = 0
        for i in range(1,len(s)):
            c = s[i]
            p = s[i-1]
            cl = int(c) % 3
            if cl == 0:
                cl = 3
            pl = int(p) % 3
            if pl == 0:
                pl = 3

            if l and cl > pl:
                lr += 1
            elif not l and cl < pl:
                lr += 1
            else:
                l = not l
        l = False
        tr = 0
        for i in range(1,len(s)):
            c = s[i]
            p = s[i-1]
            cl = int(c) % 3
            if cl == 0:
                cl = 3
            pl = int(p) % 3
            if pl == 0:
                pl = 3

            if l and cl > pl:
                tr += 1
            elif not l and cl < pl:
                tr += 1
            else:
                l = not l

        rr.append(min(lr,tr))

    return '\n'.join(map(str, rr))


print(main())


