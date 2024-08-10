import sys
from collections import deque
import bisect
import copy
import heapq
import itertools
import math
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def f(A, n):
    L = [0] + sorted([a % n for a in A if a % n != 0])
    R = [n - a for a in L[1:]] + [0]
    for i in range(len(L) - 1):
        L[i + 1] += L[i]
        R[len(L) - i - 2] += R[len(L) - i - 1]

    res = 10 ** 20
    for l, r in zip(L, R):
        res = min(res, max(l, r))
    return res


def main():
    N, K = read_values()
    A = read_list()
    S = sum(A)
    
    res = 0
    for n in range(1, int(S ** 0.5) + 1):
        if S % n != 0:
            continue
        m = S // n
        if f(A, n) <=  K:
            res = max(res, n)
        if f(A, m) <=  K:
            res = max(res, m)
    print(res)
        

if __name__ == "__main__":
    main()
