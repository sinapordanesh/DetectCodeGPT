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
    h,w = LI()
    a = [[c for c in S()] for _ in range(h)]
    s = None
    lc = 0
    for i in range(h):
        for j in range(w):
            c = a[i][j]
            if c == '.':
                continue
            if c == 'o':
                lc += 1
                continue
            s = (i,j,c)

    def f(i,j,c,d):
        if d == lc:
            return (True, '')
        a[i][j] = '.'
        if c != 'U':
            for k in range(i+1,h):
                if a[k][j] == 'o':
                    rf,rs = f(k,j,'D',d+1)
                    if rf:
                        return (True, 'D' + rs)
                    break
        if c != 'D':
            for k in range(i-1,-1,-1):
                if a[k][j] == 'o':
                    rf,rs = f(k,j,'U',d+1)
                    if rf:
                        return (True, 'U' + rs)
                    break
        if c != 'L':
            for k in range(j+1,w):
                if a[i][k] == 'o':
                    rf,rs = f(i,k,'R',d+1)
                    if rf:
                        return (True, 'R' + rs)
                    break
        if c != 'R':
            for k in range(j-1,-1,-1):
                if a[i][k] == 'o':
                    rf,rs = f(i,k,'L',d+1)
                    if rf:
                        return (True, 'L' + rs)
                    break

        a[i][j] = 'o'
        return (False, None)

    rf,rs = f(s[0],s[1],s[2],0)
    return rs


print(main())

