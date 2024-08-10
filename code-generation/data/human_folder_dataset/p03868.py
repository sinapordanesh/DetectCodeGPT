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

def main():
    num = int(input())
    data_pc = sorted([int(input()) for i in range(num)])
    data_tap = sorted([int(input()) for i in range(num)])

    ans = 1
    mod = 10 ** 9 + 7

    ind_pc = 0
    ind_tap = 0
    count_pc, count_tap = 0, 0

    while ind_pc < num or ind_tap < num:
        if ind_pc >= num:
            if count_pc > 1:
                ans *= count_pc
                count_pc -= 1
            ind_tap += 1
        elif ind_tap >= num:
            if count_tap >= 1:
                ans *= count_tap
                count_tap -= 1
            ind_pc += 1
        elif data_pc[ind_pc] < data_tap[ind_tap]:
            count_pc += 1
            if count_tap >= 1:
                ans *= count_tap
                count_tap -= 1
                count_pc -= 1
            ind_pc += 1
        else:
            count_tap += 1
            if count_pc >= 1:
                ans *= count_pc
                count_pc -= 1
                count_tap -= 1
            ind_tap += 1
        ans %= mod

    print(ans)





if __name__ == '__main__':
    main()
    # test()

