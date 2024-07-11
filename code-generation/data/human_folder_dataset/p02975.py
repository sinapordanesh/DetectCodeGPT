import sys
import itertools
# import numpy as np
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import permutations
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

def solve(N,A):
    if all(x == 0 for x in A):
        return True
    q,r = divmod(N,3)
    if r:
        return False
    counter = Counter(A)
    n = len(counter)
    if n == 1:
        return False
    if n == 2:
        a,b = counter.keys()
        if a > b:
            a,b = b,a
        if a != 0:
            return False
        # 0,b
        if counter[0] != N//3:
            return False
        return True
    if n == 3:
        a,b,c = counter.keys()
        for x in [a,b,c]:
            if counter[x] != q:
                return False
        return a^b^c == 0
    return False
print('Yes' if solve(N, A) else 'No')