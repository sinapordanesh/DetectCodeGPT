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
    a, b, c, d = map(int, input().split())
    print(max(a*c, a*d, b*c, b*d))


if __name__ == '__main__':
    main()