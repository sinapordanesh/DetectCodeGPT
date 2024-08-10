import sys
import math
from collections import defaultdict, deque, Counter
from copy import deepcopy
from bisect import bisect, bisect_right, bisect_left
from heapq import heapify, heappop, heappush
    
input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def TI(): return tuple(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]
    
    
def main():
    N = I()
    L = [1]
    temp = 1
    while temp <= N:
        temp *= 6
        L.append(temp)
    temp = 1
    while temp <= N:
        temp *= 9
        L.append(temp)
    L.sort()
    D = [i for i in range(N+1)]
    for i in L[1:]:
        for j in range(i, N+1):
            D[j] = min(D[j], D[j-i]+1)
    print(D[N])

if __name__ == "__main__":
    main()