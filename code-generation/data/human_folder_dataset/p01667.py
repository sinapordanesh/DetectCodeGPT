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
    m,n = LI()
    dp = collections.defaultdict(list)
    dm = collections.defaultdict(list)
    for i in range(m):
        k = I()
        for _ in range(k):
            s, c, t = LS()
            if c == '<=':
                dm[int(s)].append((int(t), i))
            else:
                dp[int(s)].append((int(t), i))

    e = collections.defaultdict(set)
    for k in list(dm.keys()):
        ml = dm[k]
        pl = dp[k]
        for tm, i in ml:
            for tp, j in pl:
                if tm < tp:
                    e[i].add(j)

    v = collections.defaultdict(int)

    def f(i):
        if v[i] == 2:
            return True
        if v[i] == 1:
            return False
        v[i] = 1

        for n in e[i]:
            if not f(n):
                return False
        v[i] = 2
        return True

    for i in range(m):
        if not f(i):
            return 'No'

    return 'Yes'




print(main())

