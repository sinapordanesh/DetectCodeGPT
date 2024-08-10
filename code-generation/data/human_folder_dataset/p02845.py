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
    
mod = 1000000007
def main():
    N = I()
    L = LI()
    D = [0]*(N+2)
    D[0] = 3
    ans = 1
    
    for num in L:
        if D[num] == 0 or D[num+1] >= 3:
            print(0)
            sys.exit()
        temp = D[num] - D[num+1]
        D[num+1] += 1
        ans *= temp
        ans = ans % mod
    print(ans)

if __name__ == "__main__":
    main()