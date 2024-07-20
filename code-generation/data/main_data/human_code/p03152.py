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


def main():
    N, M = read_values()
    A = read_list()
    B = read_list()
    P = [[-1, -1] for _ in range(N * M + 1)]
    C = 0
    HC = 0
    WC = 0
   
    for i, a in enumerate(A):
        if P[a][0] != -1:
            print(0)
            return
        P[a][0] = i
    for j, b in enumerate(B):
        if P[b][1] != -1:
            print(0)
            return
        P[b][1] = j

    res = 1
    for k in range(N * M, 0, -1):
        h, w = P[k]
        if h != -1 and w != -1:
            HC += 1
            WC += 1
            C += HC - 1
            C += WC - 1
        elif h != -1:
            res *= WC
            res %= mod
            C += WC - 1
            HC += 1
        elif w != -1:
            res *= HC
            res %= mod
            C += HC - 1
            WC += 1
        else:
            res *= C
            res %= mod
            C -= 1
        #print(f"k: {k}, HC: {HC}, WC: {WC}, C: {C}, res: {res}")
        if res == 0:
            break
    print(res)


if __name__ == "__main__":
    main()
