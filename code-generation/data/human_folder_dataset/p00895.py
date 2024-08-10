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

    dd = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

    while True:
        h,w = LI()
        if h == 0 and w == 0:
            break

        a = [S() for _ in range(h)]

        rs = set()
        r = ''
        rm = -1

        for i in range(h):
            for j in range(w):
                for di,dj in dd:
                    tr = a[i][j]
                    for k in range(1,401):
                        ni = (i+di*k) % h
                        nj = (j+dj*k) % w
                        if ni == i and nj == j:
                            break
                        c = a[ni][nj]
                        tr += c
                        l = len(tr)
                        if tr in rs and (l > rm or (l==rm and r > tr)):
                            r = tr
                            rm = l
                        rs.add(tr)

        if r == '':
            rr.append(0)
        else:
            rr.append(r)


    return '\n'.join(map(str, rr))


print(main())


