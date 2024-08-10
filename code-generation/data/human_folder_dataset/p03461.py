from heapq import *
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

def impossible():
    print("Impossible")
    exit()

def main():
    h, w = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(h)]
    edge = [[0] * 101 for _ in range(101)]

    # XとYをつなぐ辺の作成
    for n_x in range(101):
        for n_y in range(101):
            cost = 0
            for i in range(h):
                for j in range(w):
                    x, y = i + 1, j + 1
                    cur_cost = t[i][j] - x * n_x - y * n_y
                    if cur_cost > cost: cost = cur_cost
            edge[n_x][n_y] = cost
    # p2D(edge)

    # 条件を満たしているかのチェック
    for i in range(h):
        for j in range(w):
            x, y = i + 1, j + 1
            tij = t[i][j]
            min_dist = 1000
            for n_x in range(101):
                for n_y in range(101):
                    dist = x * n_x + y * n_y + edge[n_x][n_y]
                    if dist < min_dist: min_dist = dist
            if tij != min_dist: impossible()

    print("Possible")
    print(202, 101 * 101 + 200)
    for u in range(1, 101):
        print(u, u + 1, "X")
    for u in range(102, 202):
        print(u, u + 1, "Y")
    for n_x in range(101):
        for n_y in range(101):
            print(n_x + 1, 202 - n_y, edge[n_x][n_y])
    print(1, 202)

main()
