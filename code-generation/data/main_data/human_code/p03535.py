from fractions import gcd
from datetime import date, timedelta
from heapq import*
import math
from collections import defaultdict, Counter, deque
import sys
from bisect import *
import itertools
import copy
sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7


def main():
    n = int(input())
    d = list(map(int, input().split()))
    if n == 1:
        print(d[0])
        exit()
    dc = defaultdict(int)
    dc[0] = 1
    for i in range(n):
        v = d[i]
        if dc[v] >= 2 or (dc[v] == 1 and (v == 12 or v == 0)):
            print(0)
            exit()
        dc[v] += 1
    
    dd = []
    ddt = []
    for i in range(0, 13):
        if (i == 0 or i == 12) and dc[i] == 1:
            ddt.append(i)
        elif dc[i] == 1:
            dd.append(i)
        elif dc[i] == 2:
            ddt.append(i)
            ddt.append(24 - i)


    
    ans = 0
    for i in range(1 << len(dd)):
        d3 = []
        for j in range(len(ddt)):
            d3.append(ddt[j])

        for j in range(len(dd)):
            if (i & (1 << j)):
                d3.append(dd[j])
            else:
                d3.append(24 - dd[j])
        
        d3 = sorted(d3)
        t = float("inf")
        for i in range(len(d3) - 1):
            t = min(t, d3[i + 1] - d3[i])
        t = min(t , 24 - d3[-1])
        ans = max(t, ans)
    print(ans)


if __name__ == '__main__':
    main()
