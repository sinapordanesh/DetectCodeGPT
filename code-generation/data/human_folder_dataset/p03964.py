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
    N = i_input()
    t0,a0 = 1,1

    for i in range(N):
        t1,a1 = i_map()
        f0 = t0//t1
        if t0%t1 != 0:
            f0 += 1
        f1 = a0 // a1
        if a0%a1 != 0:
            f1 += 1
        f = max(f0, f1)
        t0, a0 = t1*f, a1*f
    print(t0+a0)

if __name__=="__main__":
    main()
