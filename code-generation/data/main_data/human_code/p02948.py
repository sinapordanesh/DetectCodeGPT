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
    import heapq
    n,m = i_map()
    t = [[] for _ in range(m+1)]
    for i in range(n):
        a,b = i_map()
        if a> m:
            continue
        t[a].append(b)

    ans = 0
    h = []
    for l in t:
        for i in l:
            heapq.heappush(h, -i)
        if h:
            ans -= heapq.heappop(h)
    print(ans)






if __name__=="__main__":
    main()
