import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
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

#     13
#   12  11
# 13  06  13
#   05  04
# 10  03  09
#   02  01
# 13  00  13
#   08  07
#     13

def main():
    rr = []

    tt = [
            [13, 7, 8, 0, 1, 2, 3],
            [7, 13, 0, 1, 9, 3, 4],
            [8, 0, 13, 2, 3, 10, 5],
            [0, 1, 2, 3, 4, 5, 6],
            [1, 9, 3, 4, 13, 6, 11],
            [2, 3, 10, 5, 6, 13, 12],
            [3, 4, 5, 6, 11, 12, 13]
    ]

    while True:
        s = S()
        if s == '#':
            break

        fil = [int(c) for c in s]
        i2 = [2**i for i in range(128)]
        f3 = {}
        for k in range(3**7):
            a = []
            kk = k
            for _ in range(7):
                a.append(k%3)
                k //= 3
            if 2 in a:
                continue
            a.reverse()
            e = 0
            for c in a:
                e *= 2
                e += c
            f3[kk] = fil[e]

        for k in range(3**7):
            a = []
            kk = k
            for _ in range(7):
                a.append(k%3)
                k //= 3
            if 2 not in a:
                continue
            a.reverse()
            ki = a.index(2)
            e = 0
            y = 0
            for i in range(7):
                e *= 3
                y *= 3
                if i == ki:
                    y += 1
                else:
                    e += a[i]
                    y += a[i]

            fe = f3[e]
            fy = f3[y]
            if fe == fy:
                f3[kk] = fe
            else:
                f3[kk] = 2

        f = True
        for k in range(2**13):
            ba = [1 if i2[i] & k else 0 for i in range(13)] + [2]
            ca = []
            for i in range(7):
                ti = tt[i]
                e = 0
                for c in ti:
                    e *= 3
                    e += ba[c]
                ca.append(f3[e])
            y = 0
            for c in ca:
                y *= 3
                y += c
            if ca[3] != f3[y]:
                f = False
                break

        if f:
            rr.append('yes')
        else:
            rr.append('no')

    return '\n'.join(rr)




print(main())

