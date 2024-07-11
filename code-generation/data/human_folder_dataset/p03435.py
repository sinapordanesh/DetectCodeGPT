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
    c = [i_list() for i in range(3)]

    for i in range(1,3):
        t = c[i][0] - c[0][0]
        if c[i][1] - c[0][1] == t and  c[i][2] - c[0][2] == t:
            pass
        else:
            print("No")
            exit()

    for j in range(1,3):
        t = c[0][i] - c[0][0]
        if c[1][i] - c[1][0] == t and c[2][i] - c[2][0] == t:
            pass
        else:
            print("No")
            exit()
    print("Yes")




if __name__=="__main__":
    main()
