from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools


import queue
from collections import deque

def check(max_length, left, right, r, index):
    if index == 1000:
        print(left)
        sys.exit()
    half = (left + right) / 2
    if 2 * half <= max_length * (r - half) / r:
        check(max_length, half, right, r, index + 1)
    else:
        check(max_length, left, half, r, index + 1)

def main():
    data = [list(map(int, input().split())) for i in range(3)]
    a = ((data[0][0] - data[1][0]) ** 2 + (data[0][1] - data[1][1]) ** 2) ** 0.5
    b = ((data[1][0] - data[2][0]) ** 2 + (data[1][1] - data[2][1]) ** 2) ** 0.5
    c = ((data[0][0] - data[2][0]) ** 2 + (data[0][1] - data[2][1]) ** 2) ** 0.5

    s = (a + b + c) / 2
    S = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    r = 2 * S / (a + b + c)

    left, right = 0, max(a, b, c)

    check(max(a, b, c), left, right, r, 0)





if __name__ == '__main__':
    main()
    # test()

