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
    rr = []

    def f(n,m):
        a = [[-1]*(n+3)] + [[-1] + LI() + [-1]*2 for _ in range(n)] + [[-1]*(n+3)]
        aa = [c[:] for c in a]
        d = collections.defaultdict(int)
        def _f(i,j,c):
            if a[i][j] == 0:
                return (0, set([(i,j)]))
            if a[i][j] != c:
                return (0,set())
            a[i][j] = -1
            r = [1, set()]
            for di,dj in [(-1,-1),(-1,0),(0,-1),(0,1),(1,0),(1,1)]:
                t = _f(i+di,j+dj,c)
                r[0] += t[0]
                r[1] |= t[1]
            # print('_f',i,j,c,r)
            return tuple(r)
        for i in range(1,n+1):
            for j in range(1,i+1):
                if a[i][j] != m:
                    continue
                c,s = _f(i,j,a[i][j])
                if len(s) == 1:
                    d[list(s)[0]] = -1
        a = aa
        aa = [c[:] for c in a]
        for i in range(1,n+1):
            for j in range(1,i+1):
                if a[i][j] != 0:
                    continue
                if (i,j) in d:
                    continue
                tf = True
                for di,dj in [(-1,-1),(-1,0),(0,-1),(0,1),(1,0),(1,1)]:
                    if a[i+di][j+dj] in [0,m]:
                        tf = False
                        break
                if tf:
                    d[(i,j)] = -1
                else:
                    d[(i,j)] = 0

        ts = collections.defaultdict(set)
        for i in range(1,n+1):
            for j in range(1,i+1):
                if a[i][j] != m:
                    continue
                cc = a[i][j]
                sf = -1 if a[i][j] == m else 1
                c,s = _f(i,j,a[i][j])
                # print('res',i,j,c,s,sf,len(s))
                if len(s) > 1:
                    for sc in s:
                        ts[sc].add(cc)
                        d[sc] = 0

        a = aa
        # print(d)
        # print('\n'.join("\t".join(map(str,_)) for _ in a))
        for i in range(1,n+1):
            for j in range(1,i+1):
                if a[i][j] < 1:
                    continue
                cc = a[i][j]
                sf = -1 if a[i][j] == m else 1
                c,s = _f(i,j,a[i][j])
                # print('res',i,j,c,s,sf,len(s))
                if len(s) == 1 and cc not in ts[list(s)[0]]:
                    if sf == 1:
                        d[list(s)[0]] += c * sf
                    else:
                        d[list(s)[0]] += c * sf
                # print('\n'.join("\t".join(map(str,_)) for _ in a))
        # print('\n'.join("\t".join(map(str,_)) for _ in a))
        # print(d)
        if len(d) == 0:
            return 0
        return max(d.values())

    while True:
        n,m = LI()
        if n == 0 and m == 0:
            break
        rr.append(f(n,m))

    return '\n'.join(map(str,rr))


print(main())

