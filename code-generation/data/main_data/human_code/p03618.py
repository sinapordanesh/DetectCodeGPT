import sys
import math
import copy
import random
import itertools
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)



def solve(n=None, s1=None, s2=None):
    s = getS()
    cnt = Counter(s)
    n = len(s)
    ans = 0
    for k, v in cnt.items():
        ans += v * (n - v)
        

    ans //= 2
    ans += 1

    print(ans)


def main():
    for _ in range(n):
        solve()
    return


if __name__ == "__main__":
    # main()
    solve()
