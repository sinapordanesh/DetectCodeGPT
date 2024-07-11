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

    def f(n,m,l):
        a = [[c for c in S()] for _ in range(n)]
        s = (-1,-1)
        g = (-1,-1)
        kh = set()
        for i in range(n):
            for j in range(m):
                c = a[i][j]
                if c == 'S':
                    s = (i,j)
                    a[i][j] = '.'
                if c == 'G':
                    g = (i,j)
                    a[i][j] = '.'
                if a[i][j] == '.':
                    kh.add((i,j))

        if (s[0]+1, s[1]) not in kh:
            return -1

        def search():
            d = collections.defaultdict(lambda: (inf,0,0))
            ss = ((s[0]+1, s[1]), 2)
            d[ss] = (0,0,0)
            q = []
            heapq.heappush(q, ((0,0,0), ss))
            v = collections.defaultdict(bool)
            while len(q):
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                v[u] = True

                if u[0] == g:
                    return k[0]

                if u == (s, 0) or (k[0]>0 and u == (s,2)):
                    continue

                for di in range(4):
                    if abs(di - u[1]) == 2:
                        continue
                    if (u[0][0]+dd[di][0], u[0][1]+dd[di][1]) not in kh:
                        continue
                    uv = ((u[0][0]+dd[di][0], u[0][1]+dd[di][1]), di)
                    if v[uv]:
                        continue
                    if di == u[1]:
                        if d[uv] > k:
                            d[uv] = k
                            heapq.heappush(q, (k, uv))
                        continue

                    if u[0] == s:
                        continue

                    ti = (0,0)
                    if u[1] % 2 == 1:
                        if u[1] - 1 == di:
                            ti = (1,0)
                        else:
                            ti = (0,1)
                    else:
                        if u[1] - 1 == di:
                            ti = (0,1)
                        else:
                            ti = (1,0)

                    ud = (k[0]+1,k[1]+ti[0],k[2]+ti[1])
                    if ud[1] > l or ud[2] > l or d[uv] <= ud:
                        continue
                    d[uv] = ud
                    heapq.heappush(q, (ud, uv))

            return -1

        return search()

    while 1:
        n,m,l = LI()
        if n == 0:
            break
        rr.append(f(n,m,l))
        break

    return '\n'.join(map(str, rr))


print(main())

