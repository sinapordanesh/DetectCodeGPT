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
    def inp():
        s = LS()
        a = []
        for i in range(len(s)-1):
            if i % 2 == 0:
                a.append(s[i])
            else:
                a.append(int(s[i]))
        return a

    def com(a):
        r = a[:2]
        for i in range(2,len(a), 2):
            if a[i] == r[-2]:
                r[-1] += a[i+1]
            else:
                r += a[i:i+2]
        return r

    a = com(inp())
    b = com(inp())
    c = com(inp())

    r = []
    ff = True
    if len(b) == 2:
        b0 = b[0]
        b1 = b[1]
        for i in range(0,len(a),2):
            if a[i] == b0:
                while a[i+1] >= b1 and ff:
                    r += c
                    a[i+1] -= b1
                    ff = False
                if a[i+1] > 0:
                    r += a[i:i+2]
            else:
                r += a[i:i+2]
    else:
        i = 0
        al = len(a)
        bl = len(b)
        be = bl - 2
        while i < al:
            f = True
            for j in range(0,bl,2):
                ii = i + j
                if al <= ii or a[ii] != b[j] or (a[ii+1] < b[j+1] if j in [0, be] else a[ii+1] != b[j+1]) or not ff:
                    f = False
                    break
            if f:
                for j in range(0,bl,2):
                    ii = i + j
                    a[ii+1] -= b[j+1]
            if a[i+1] > 0:
                r += a[i:i+2]
            if f:
                r += c
                ff = False
            i += 2

    r += '$'


    return ' '.join(map(str,com(r)))




print(main())

