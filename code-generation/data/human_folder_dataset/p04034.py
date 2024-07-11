import sys, math
from functools import lru_cache
sys.setrecursionlimit(10**9)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

N, M = mi()
x, y = i2(M)

boxes = [1]*N
red = [False for i in range(N)]
red[0] = True

for i in range(M):
    boxes[x[i]-1] -= 1
    boxes[y[i]-1] += 1

    if red[x[i]-1]:
        red[y[i]-1] = True
    if boxes[x[i]-1] == 0:
        red[x[i]-1] = False

print(red.count(True))

