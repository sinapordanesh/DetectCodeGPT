#!/usr/bin/env python3
# atcoder 
# Türkler var mı?
# Herkese memnün oldum
import sys
#from heapq import heapify, heappush, heappop
#from heapq import nlargest, nsmallest

iimr = lambda: map(int, sys.stdin.readline().rstrip().split())
readline = sys.stdin.readline
# puorquoi le sys.stdin.buffer.readline() ne fonctionne plus sur atcoder?
#sys.setrecursionlimit(10 ** 7)
#INF = 1 << 30 # 大体 1e9


def debug(*x):
    print(*x, file=sys.stderr)


# s == self
class atcoder():
    def __init__(s):
        f = open(0)
        s.N = int(f.readline())
        s.A = list(map(int, f.readline().split()))

    def çözmek(s):
        res = []
        res.append(s.関数(s.N, s.A))
        print(*res)	
    
    def 関数(self, n, a):
        guusuu = True
        cnt = 0
        while(guusuu):
            for i in range(n):
                if(a[i] % 2 != 0):
                    guusuu = False
                    break;
                else:
                    a[i] /= 2
            if(guusuu): cnt += 1
        return cnt 

if __name__ == "__main__":
    ima = atcoder()
    ima.çözmek()
