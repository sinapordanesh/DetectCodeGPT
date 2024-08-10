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
        a = S()
        if a == '0':
            break
        b = S()
        c = S()
        ml = max([len(a),len(b),len(c)])
        if len(a) < ml:
            a = '0' * (ml-len(a)) + a
        if len(b) < ml:
            b = '0' * (ml-len(b)) + b
        if len(c) < ml:
            c = '0' * (ml-len(c)) + c

        r = [[0,0] for _ in range(ml+1)]
        r[0][0] = 1
        for i in range(ml):
            ai = a[ml-i-1]
            bi = b[ml-i-1]
            ci = c[ml-i-1]
            r0 = [0,0]
            r1 = [0,0]
            si = 0
            if i == ml - 1:
                si = 1
            al = range(si,10)
            if ai != '?':
                al = [int(ai)]
            bl = range(si,10)
            if bi != '?':
                bl = [int(bi)]
            cl = range(si,10)
            if ci != '?':
                cl = [int(ci)]

            for ac,bc,cc in itertools.product(al,bl,cl):
                abc = ac+bc
                if abc % 10 == cc:
                    if abc > 9:
                        r0[1] += 1
                    else:
                        r0[0] += 1
                elif (abc+1) % 10 == cc:
                    if abc > 8:
                        r1[1] += 1
                    else:
                        r1[0] += 1
            r[i+1][0] += r0[0] * r[i][0]
            r[i+1][0] += r1[0] * r[i][1]
            r[i+1][1] += r0[1] * r[i][0]
            r[i+1][1] += r1[1] * r[i][1]

        rr.append(r[ml][0] % mod)


    return '\n'.join(map(str,rr))



print(main())

