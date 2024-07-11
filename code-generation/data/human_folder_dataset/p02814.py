import math
from math import gcd,pi,sqrt
INF = float("inf")
MOD = 10**9 + 7

import sys
sys.setrecursionlimit(10**6)
import itertools
import bisect
from collections import Counter,deque
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]


def main():
    n,M = i_map()
    a = i_list()

    cd = []
    new_a = []
    for i in a:
        cd.append(i//2)
        new_a.append((i//2))

    def pow2(x):
        ret = 0
        while x%2 == 0:
            ret += 1
            x//=2
        return ret

    P = []
    for a in new_a:
        P.append(pow2(a))

    if len(set(P)) != 1:
        print(0)
    else:
        m = 1
        for a in new_a:
            m = (m*a)//gcd(m,a)
        print(-(-(M//m)//2))









if __name__=="__main__":
    main()
