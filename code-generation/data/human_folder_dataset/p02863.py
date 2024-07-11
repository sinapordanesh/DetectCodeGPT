#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N, T = map(int, input().split())
    AB = []
    for _ in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort()

    dp = [0] * (T + 1)
    ans = 0
    for i in range(N-1):
        for j in range(T, -1, -1):
            if j + AB[i][0] <= T:
                dp[j + AB[i][0]] = max(dp[j + AB[i][0]], dp[j] + AB[i][1])
        ans = max(ans, dp[T-1]+AB[i+1][1])
    print(ans)


if __name__ == "__main__":
    main()
