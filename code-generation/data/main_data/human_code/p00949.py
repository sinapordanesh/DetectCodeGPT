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
    mod2 = 10**9+9
    sa = [S() for _ in range(2)]
    ml = min(map(len, sa))
    ss = []
    r = 0
    for si in range(2):
        s = sa[si]
        a = [0]
        a2 = [0]
        b = [set() for _ in range(ml)]
        b2 = [set() for _ in range(ml)]
        for c in s:
            k = 97 ** (ord(c) - ord('a'))
            a.append((a[-1] + k) % mod)
            a2.append((a2[-1] + k) % mod2)
        if si == 1:
            for i in range(len(a)):
                for j in range(i+1,len(a)):
                    if j - i > ml:
                        break
                    if j - i <= r:
                        continue
                    if (a[j]-a[i]) % mod in ss[0][j-i-1] and (a2[j]-a2[i]) % mod2 in ss[1][j-i-1]:
                        r = j-i

        else:
            for i in range(len(a)):
                for j in range(i+1,len(a)):
                    if j - i > ml:
                        break
                    b[j-i-1].add((a[j]-a[i]) % mod)
                    b2[j-i-1].add((a2[j]-a2[i]) % mod2)
            ss = [b,b2]

    return r


print(main())

