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
    n,k = i_map()
    a = i_list()
    dic = {}
    for i in a:
        dic[i] = dic.get(i,0) + 1

    l = len(dic.keys())

    if l <= k:
        print(0)
        exit()
    l = l - k
    ans = 0
    cnt = 0

    for i in sorted(dic.values()):
        ans += i
        cnt += 1
        if cnt == l:
            break
    print(ans)







if __name__=="__main__":
    main()
