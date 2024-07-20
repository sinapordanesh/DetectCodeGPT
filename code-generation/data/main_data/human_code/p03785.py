import sys, math
from bisect import bisect_right
sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    N, C, K = mi()
    T = [ii() for i in range(N)]
    T.sort()

    cnt = 0
    i = 0

    while i < N:
        t = T[i]+K
        b = bisect_right(T, t)
        i = min(i+C, b)
        cnt += 1

    print(cnt)



if __name__ == "__main__":
    main()