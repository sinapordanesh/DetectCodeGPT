# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, XY):
    tmp = 0
    for x, y in XY:
        tmp += (abs(x) + abs(y)) % 2
    if tmp % N != 0:
        print(-1)
        return
    import math
    m = math.ceil(math.log2(2 * 10 ** 9)) + 1
    d = [2 ** (m - i) for i in range(m)] + [1]
    d += [1] if tmp == 0 else []
    m = len(d)
    w = []
    for xi, yi in XY:
        xx = 0
        yy = 0
        W = ''
        for di in d:
            if abs(xi - xx) >= abs(yi - yy):
                if xx <= xi:
                    xx += di
                    W += 'R'
                else:
                    xx -= di
                    W += 'L'
            else:
                if yy <= yi:
                    yy += di
                    W += 'U'
                else:
                    yy -= di
                    W += 'D'
        w.append(W)
    print(m)
    print(' '.join([str(i) for i in d]))
    [print(wi) for wi in w]


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    XY = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, XY)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
