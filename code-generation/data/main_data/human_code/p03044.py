import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    from collections import defaultdict, deque
    n = input_int()
    G = defaultdict(dict)
    color = [None] * (n + 1)
    for _ in range(n - 1):
        u, v, w = input_int_list()
        G[u][v] = w
        G[v][u] = w

    # ノード1 を起点にBFSをする
    color[1] = 0
    dq = deque()
    dq.append((1, 0))  # node,cost
    while dq:
        u, cur = dq.popleft()
        for v, cost in G[u].items():
            if color[v] is None:
                if (cur + cost) % 2 == 0:
                    color[v] = 0
                else:
                    color[v] = 1
                dq.append((v, cur + cost))
    for c in color[1:]:
        print(c)

    return


if __name__ == "__main__":
    main()
