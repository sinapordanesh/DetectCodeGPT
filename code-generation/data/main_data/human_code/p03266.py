# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
# 
# 
# @stop_watch
def solve(N, K):
    div0 = N // K
    divh = (N + (K // 2)) // K if K % 2 == 0 else 0
    import math
    print(div0 ** 3 + divh ** 3)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, K = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, K)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
