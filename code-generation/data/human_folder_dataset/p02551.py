from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
input = sys.stdin.readline
INF = float("inf")


# 処理内容
def main():
    N, Q = map(int, input().split())
    
    h = N
    w = N
    a = [N]*N
    b = [N]*N
    ans = (N-2)**2
    for _ in range(Q):
        q, x = map(int, input().split())
        if q == 1:
            if x < w:
                for i in range(x, w):
                    b[i] = h
                w = x
            ans -= b[x] - 2
        elif q == 2:
            if x < h:
                for i in range(x, h):
                    a[i] = w
                h = x
            ans -= a[x] - 2
    
    print(ans)


if __name__ == '__main__':
    main()