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
    N = int(input())
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        adj[a].append(b)
        adj[b].append(a)

    queue = deque([0])
    visit = [-1] * N
    visit[0] = 0

    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if visit[u] < 0:
                queue.append(u)
                visit[u] = visit[now] + 1

    queue = deque([N-1])
    visit2 = [-1] * N
    visit2[N-1] = 0

    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if visit2[u] < 0:
                queue.append(u)
                visit2[u] = visit2[now] + 1

    cnt = 0
    for i in range(N):
        if visit[i] <= visit2[i]:
            cnt += 1
    print('Fennec') if cnt > N-cnt else print('Snuke')
    # print(visit2)


if __name__ == "__main__":
    main()
