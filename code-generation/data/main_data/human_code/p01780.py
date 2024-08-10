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
    n = I()
    if n == 1:
        return 0
    a = LI_()
    b = [0]
    c = [[None] * 18]
    for i in range(n-1):
        t = a[i]
        b.append(b[t] + 1)
        d = [None] * 18
        d[0] = t
        for j in range(1,18):
            if c[d[j-1]][j-1] is None:
                break
            d[j] = c[d[j-1]][j-1]
        c.append(d)

    ii = [2**i for i in range(19)]
    def f(i,j):
        if i == j:
            return 0
        if b[i] > b[j]:
            sa = b[i] - b[j]
            for k in range(1,18):
                if sa < ii[k]:
                    return ii[k-1] + f(c[i][k-1], j)
        if b[i] < b[j]:
            sa = b[j] - b[i]
            for k in range(1,18):
                if sa < ii[k]:
                    return ii[k-1] + f(c[j][k-1], i)
        for k in range(1,18):
            if c[i][k] == c[j][k]:
                return ii[k] + f(c[i][k-1], c[j][k-1])

    ba = sorted(zip(b, range(n)))
    aa = [0]
    aai = {}
    aai[0] = 0
    i = 1
    while i < n:
        j = i + 1
        bi = ba[i][0]
        while j < n and bi == ba[j][0]:
            j += 1
        aa.extend(list(map(lambda x: x[1], sorted([[aai[c[_][0]], _] for k,_ in ba[i:j]]))))
        for k in range(i,j):
            aai[aa[k]] = k
        i = j
    r = 1
    for i in range(1,n-1):
        r += f(aa[i],aa[i+1])

    return r


print(main())

