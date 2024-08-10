from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
input = sys.stdin.readline
INF = float("inf")


def func(x, m):
    return x % m


# 処理内容
def main():
    N = int(input())
    z = [0] * N
    w = [0] * N
    for i in range(N):
        x, y = map(int, input().split())
        z[i] = x + y
        w[i] = x - y
    
    ans = max(max(z) - min(z), max(w) - min(w))
    
    print(ans)



if __name__ == '__main__':
    main()