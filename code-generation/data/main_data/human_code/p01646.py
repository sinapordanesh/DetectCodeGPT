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

    while True:
        n = I()
        if n == 0:
            break

        a = [S() for _ in range(n)]
        e = collections.defaultdict(set)
        for c in string.ascii_lowercase:
            e[''].add(c)

        f = True
        for i in range(n):
            ai = a[i]
            for j in range(i+1,n):
                aj = a[j]
                for k in range(len(ai)):
                    if len(aj) <= k:
                        f = False
                        break
                    if ai[k] == aj[k]:
                        continue
                    e[ai[k]].add(aj[k])
                    break
        if not f:
            rr.append('no')
            continue

        v = collections.defaultdict(bool)
        v[''] = True

        def g(c):
            if v[c] == 2:
                return True
            if v[c] == 1:
                return False
            v[c] = 1
            for nc in e[c]:
                if not g(nc):
                    return False
            v[c] = 2
            return True

        for c in list(e.keys()):
            if v[c]:
                continue
            if not g(c):
                f = False
                break

        if f:
            rr.append('yes')
        else:
            rr.append('no')


    return '\n'.join(map(str,rr))



print(main())

