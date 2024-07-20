import sys
import copy

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


INF = 10**18


def warshall_floyd(V, cost):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if cost[i][k] < INF and cost[k][j] < INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])


def main():

    V = in_n()
    cost = [[] for _ in range(V)]

    for i in range(V):
        cost[i] = in_nl()

    short_cost = copy.deepcopy(cost)
    warshall_floyd(V, short_cost)

    ans = 0
    for i in range(V):
        for j in range(i + 1, V):
            if short_cost[i][j] < cost[i][j]:
                print(-1)
                exit()
            for k in range(V):
                if i == k or j == k:
                    continue
                if short_cost[i][k] + short_cost[k][j] == cost[i][j]:
                    break
            else:
                ans += cost[i][j]

    print(ans)


if __name__ == '__main__':
    main()
