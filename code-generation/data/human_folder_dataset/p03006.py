import sys, math, re
from itertools import accumulate
sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def main():
    N = ii()
    if N == 1:
        print(1)
        return
        
    x, y = i2(N)
    d = {}

    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            pair = (x[i]-x[j], y[i]-y[j])
            if not pair in d:
                d[pair] = 0
            
            d[pair] += 1

    print(N-max(d.values()))


if __name__ == "__main__":
    main()