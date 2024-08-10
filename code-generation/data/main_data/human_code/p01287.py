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

# aa
# 1 2 4 5
# 2 3 1 6
# 3 4 2 7
# 4 1 3 8
# 5 8 6 1
# 6 5 7 2
# 7 6 8 3
# 8 7 5 4
#

def main():
    rr = []
    k = [
            [2, 4, 5],
            [3, 1, 6],
            [4, 2, 7],
            [1, 3, 8],
            [8, 6, 1],
            [5, 7, 2],
            [6, 8, 3],
            [7, 5, 4]
        ]
    for i in range(8):
        for j in range(3):
            k[i][j] -= 1
    ptn = []
    for i in range(8):
        for j in range(3):
            t = [-1] * 8
            t[0] = i
            t[1] = k[i][j]
            t[3] = k[i][(j+1)%3]
            for l in range(8):
                if l == i:
                    continue
                if t[1] in k[l] and t[3] in k[l]:
                    t[2] = l
                    break
            for l in range(4):
                kl = k[t[l]]
                for m in range(3):
                    if kl[m] not in t:
                        t[l+4] = kl[m]
                        break
            ptn.append(t)

    def f(a):
        s = set()
        r = 0
        tc = 0
        for t in itertools.permutations(a):
            tc += 1
            if t in s:
                continue
            r += 1
            for p in ptn:
                s.add(tuple(t[p[i]] for i in range(8)))
        return r

    while True:
        a = LS()
        if len(a) == 0:
            break
        rr.append(f(a))

    return '\n'.join(map(str,rr))


print(main())

