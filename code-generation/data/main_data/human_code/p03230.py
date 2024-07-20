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
    D = [0] * (N+1)
    for i in range(1, N+1):
        D[i] = i*(i+1)//2

    index = bisect_left(D, N)
    if N != D[index]:
        print("No")
    else:
        print("Yes")
        print(index+1)
        D2 = Init(index+1, index,0)
        D2[0] = [i for i in range(1, index+1)]
        num = index
        for i in range(1, index+1):
            for j in range(i):
                D2[i][j] = D2[j][i-1]
            for k in range(j+1, index):
                num += 1
                D2[i][k] = num
        for temp in D2:
            temp = [index]+temp
            temp = [str(i) for i in temp]
            print(" ".join(temp))

if __name__ == "__main__":
    main()