import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.buffer.readline
in_n = lambda: int(input())
in_nn = lambda: map(int, input().split())
in_s = lambda: input().rstrip().decode('utf-8')
in_map = lambda: [s == ord('.') for s in input() if s != ord('\n')]

MOD = 10**9 + 7
INF = 8 * 10**18


# 最小全域木 O(ElogV)
def prims_algorithm(N, cost):

    used = [False] * N
    used[0] = True
    que = [(c, w) for c, w in cost[0]]
    heapify(que)

    ret = 0
    while que:
        cv, v = heappop(que)
        if used[v]:
            continue
        used[v] = True
        ret += cv
        for c, w in cost[v]:
            if used[w]:
                continue
            heappush(que, (c, w))

    return ret


def main():

    N = in_n()
    x = [0] * N
    y = [0] * N

    for i in range(N):
        x[i], y[i] = in_nn()

    sort_ind_x = sorted(range(N), key=lambda i: x[i])
    sort_ind_y = sorted(range(N), key=lambda i: y[i])

    cost = [[] for _ in range(N)]
    for i in range(N - 1):
        j1, j2 = sort_ind_x[i], sort_ind_x[i + 1]
        c = abs(x[j1] - x[j2])
        cost[j1].append((c, j2))
        cost[j2].append((c, j1))

        j1, j2 = sort_ind_y[i], sort_ind_y[i + 1]
        c = abs(y[j1] - y[j2])
        cost[j1].append((c, j2))
        cost[j2].append((c, j1))

    ans = prims_algorithm(N, cost)
    print(ans)


if __name__ == '__main__':
    main()
