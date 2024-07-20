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
    n = i_input()
    a = i_list()

    one = 0
    b = []
    for i in a:
        if i %2 == 0:
            one += 1
            b.append(i//2)
    two = 0
    for i in b:
        if i % 2 == 0:
            two += 1
    zero = n - one
    one = n - zero - two
    if zero <= two or one == 0 and zero - two == 1:
        print("Yes")
    else:
        print("No")







if __name__=="__main__":
    main()
