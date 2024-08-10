import sys
import os
import math
import bisect
import itertools
import collections
import heapq
import queue
import array

# 時々使う
# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
# from decimal import Decimal
# from collections import defaultdict, deque

# 再帰の制限設定
sys.setrecursionlimit(10000000)


def ii(): return int(sys.stdin.buffer.readline().rstrip())
def il(): return list(map(int, sys.stdin.buffer.readline().split()))
def fl(): return list(map(float, sys.stdin.buffer.readline().split()))
def iln(n): return [int(sys.stdin.buffer.readline().rstrip())
                    for _ in range(n)]


def iss(): return sys.stdin.buffer.readline().decode().rstrip()
def sl(): return list(map(str, sys.stdin.buffer.readline().decode().split()))
def isn(n): return [sys.stdin.buffer.readline().decode().rstrip()
                    for _ in range(n)]


def lcm(x, y): return (x * y) // math.gcd(x, y)


MOD = 10 ** 9 + 7
INF = float('inf')


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    S = iss()
    T = iss()

    ret = set()
    for i in range(len(S)-len(T)+1):
        for s, t in zip(S[i:i+len(T)], T):
            if s == t or s == '?': continue
            else: break
        else:
            tmp = ''
            if i != 0: tmp += S[:i]
            tmp += T
            if i+len(T) < len(S): tmp += S[i+len(T):]
            ret.add(tmp.replace('?', 'a'))

    if len(ret) == 0:
        print('UNRESTORABLE')
    else:
        print(sorted(list(ret))[0])


if __name__ == '__main__':
    main()
