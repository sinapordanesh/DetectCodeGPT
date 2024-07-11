import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

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
    ii = [2**i for i in range(6)]

    while True:
        t,n = LI()
        if t == 0 and n == 0:
            break

        s = [c for c in str(n)]
        l = len(s)

        r = None
        rm = -1
        rc = 0
        for i in range(2**(l-1)):
            k = []
            c = s[0]
            for j in range(l-1):
                if ii[j] & i:
                    c += s[j+1]
                else:
                    k.append(c)
                    c = s[j+1]
            k.append(c)
            m = sum(map(int,k))
            if m <= t:
                if rm < m:
                    rm = m
                    r = k
                    rc = 1
                elif rm == m:
                    rc += 1
        if rc == 0:
            rr.append('error')
        elif rc > 1:
            rr.append('rejected')
        else:
            rr.append('{} {}'.format(rm, ' '.join(r)))

    return '\n'.join(map(str, rr))


print(main())


