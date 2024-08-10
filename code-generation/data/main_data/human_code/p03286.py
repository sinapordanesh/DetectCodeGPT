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
    if N == 0:
        print(0)
        exit()
    if N < 0:
        N = -N
        D = defaultdict(int)
        index = 0
        while N >= 1:
            #bitフラグがたっていたら
            if N & 1 == 1:
                #2の倍数の場合D[index]とD[index+1]に1を足す
                if index % 2 == 0:
                    D[index] += 1
                    D[index+1] += 1
                else:
                    D[index] += 1
            else:
                D[index] = D[index]
            N = N>>1
            index += 1
    else:
        D = defaultdict(int)
        if N & 1 == 1:
            D[0] = 1
        else:
            D[0] = 0
        index = 1
        N = N >> 1

        while N >= 1:
            #bitフラグがたっていたら
            if N & 1 == 1:
                #2の倍数の場合D[index]とD[index+1]に1を足す
                if index % 2 == 1:
                    D[index] += 1
                    D[index+1] += 1
                else:
                    D[index] += 1
            else:
                D[index] = D[index]
            N = N>>1
            index += 1
            
            
    index = 0
    while True:
        if not index in D.keys():
            break
        if D[index] <= 1:
            pass
        else:
            temp = D[index]
            D[index] = temp % 2
            D[index+1] += (temp // 2)
            D[index+2] += (temp // 2)
            if D[index+1] >= D[index+2] * 2:
                temp = D[index+2]
                D[index+2] -= temp
                D[index+1] -= temp * 2
        index += 1
    res = True

    for i in reversed(D.values()):
        if res and i == 1:
            res = False
        if not res:
            print(i, end="")
    print()

if __name__ == "__main__":
    main()