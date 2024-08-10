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

def mod_pow(x,n):
    res = 1
    while n > 0:
        if n & 1:
            res = res * x
            x = x * x
            n >>= 1
    return res


def main():
    S = input().rstrip()
    K = I()
    for i in range(len(S)):
        if int(S[i]) >= 2 or K == 1:
            print(S[i])
            break
        else:
            K -= 1
            
        
    
    
if __name__ == "__main__":
    main()