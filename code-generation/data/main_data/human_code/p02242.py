# coding: utf-8

import heapq


def dj(adjm, start):
    n = len(adjm)
    d = [float("inf")] * n
    d[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while(q):
        td, v = heapq.heappop(q)
        for k in adjm[v].keys():
            nd = td + adjm[v][k]
            if d[k] > nd:
                d[k] = nd
                heapq.heappush(q, (nd, k))
    return d


def main():
    n = int(input())
    # 隣接行列
    adjm = [{} for _ in range(n)]
    for i in range(n):
        vdata = list(map(int, input().split()))
        for j in range(vdata[1]):
            v, c = vdata[j * 2 + 2], vdata[j * 2 + 3]
            adjm[i][v] = c
    ans = dj(adjm, 0)
    for i, d in enumerate(ans):
        print(i, d)


if __name__ == "__main__":
    main()

