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

    def f(s):
        d = collections.defaultdict(int)
        ac = {}
        ca = {}
        for i in range(26):
            t = int(2**i)
            c = chr(ord('a') + i)
            ac[t] = c
            ca[c] = t
        a = [ca[c] for c in s]
        z = ca['z']
        d[0] = 1
        for c in a:
            nd = collections.defaultdict(int)
            c2 = c * 2
            for k,v in d.items():
                if k & c or c == 1:
                    nd[k] += v
                if c != z and k & c2 == 0:
                    nd[k|c2] += v
            d = nd
        r = [sum(d.values())]

        ss = set([''])
        for t in s:
            ns = set()
            t2 = chr(ord(t) + 1)
            for si in ss:
                if t in si or t == 'a':
                    ns.add(si + t)
                if t != 'z' and t2 not in si:
                    ns.add(si + t2)
            ss = set(sorted(ns)[:5])
        rs = ss

        ss = set([''])
        for t in s:
            ns = set()
            t2 = chr(ord(t) + 1)
            for si in ss:
                if t in si or t == 'a':
                    ns.add(si + t)
                if t != 'z' and t2 not in si:
                    ns.add(si + t2)
            ss = set(sorted(ns, reverse=True)[:5])
        rs |= ss
        r.extend(sorted(rs))

        return r

    while True:
        s = S()
        if s == '#':
            break
        rr.extend(f(s))

    return '\n'.join(map(str, rr))



print(main())

