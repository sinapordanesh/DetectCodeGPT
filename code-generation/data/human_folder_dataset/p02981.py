def main():
    n, a, b = map(int, input().split())
    print(min(n * a, b))
    # import sys
    # sys.setrecursionlimit = 10 ** 7
    # input = sys.stdin.readline
    # rstrip()
    # (int(x) - 1 for x in input().split())
    pass


if __name__ == '__main__':
    main()

# def binary_search(*, ok, ng, func):
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if func(mid):
#             ok = mid
#         else:
#             ng = mid
#     return ok
