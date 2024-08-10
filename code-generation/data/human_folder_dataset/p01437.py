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


def main():
    rr = []
    did = {}
    did['N'] = 0
    did['E'] = 1
    did['S'] = 2
    did['W'] = 3

    while True:
        h,w,l = LI()
        if h == 0:
            break

        a = [[c for c in S()] for _ in range(h)]
        s = None
        for i in range(h):
            for j in range(w):
                if a[i][j] in 'NEWS':
                    s = (i,j,did[a[i][j]])
                    break

        i = 0
        t = s
        td = {}
        tt = 0
        i,j,dk = t
        while tt < l:
            tt += 1
            for ddi in range(4):
                di,dj = dd[(dk+ddi) % 4]
                ni = i + di
                nj = j + dj
                if ni < 0 or ni >= h or nj < 0 or nj >= w or a[ni][nj] == '#':
                    continue
                dk = (dk + ddi) % 4
                i = ni
                j = nj
                break
            if (i,j,dk) in td:
                tt += (l-tt) // (tt - td[(i,j,dk)]) * (tt - td[(i,j,dk)])
            else:
                td[(i,j,dk)] = tt
        rr.append('{} {} {}'.format(i+1,j+1,'NESW'[dk]))

    return '\n'.join(map(str,rr))



print(main())

