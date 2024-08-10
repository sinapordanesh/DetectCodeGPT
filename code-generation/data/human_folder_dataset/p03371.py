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
    A,B,C,X,Y = i_map()

    Z = max(X,Y)

    ans = INF
    C *= 2

    for i in range(0,Z+1):
        trial = i*C
        At = X - i
        Bt = Y - i
        if At > 0:
            trial += At*A
        if Bt > 0:
            trial += Bt*B
        ans = min(ans, trial)
    print(ans)

  
  
 
  
if __name__=="__main__":
    main()
