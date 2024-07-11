from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 10)
input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools


import queue
from collections import deque


def main():
    num = int(input())
    data = [int(input()) for i in range(num)]
    now_num = 0
    for i in range(num):
        a = data[i]
        now_num ^= a

    now_num = bin(now_num)[2:]
    now_num = list(now_num)
    now_num = list(map(int, now_num))

    # print(now_num)

    delete_list = [0 for i in range(len(now_num))]
    for i in range(num):
        bin_data = bin(data[i])[2:][::-1]

        for j in range(min(len(bin_data), len(now_num))):
            # print(data[j])
            if bin_data[j] == '1':
                delete_list[j] = 1
                break

    delete_list = delete_list[::-1]

    # print(now_num)
    # print(delete_list)

    ans = 0
    taberu = 0
    for i in range(len(now_num)):
        ele = now_num[i]
        if ele ^ taberu:
            if delete_list[i]:
                taberu ^= 1
                ans += 1
            else:
                print(-1)
                sys.exit()


    if ans > num or num == 1:
        print(-1)
    else:
        print(ans)




if __name__ == '__main__':
    main()
    # test()

