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
    L = [LI() for i in range(N)]
    
    for x in range(101):
        for y in range(101):
            max_num = float('inf')
            ans = 0
            res = True
            for xn, yn, hn in L:
                if hn == 0:
                    max_num = min(max_num, abs(x-xn)+abs(y-yn))
                    if max_num == 0:
                        res = False
                        break
                else:
                    temp = abs(x-xn)+abs(y-yn)+hn
                    if ans != 0 and ans != temp:
                        res = False
                        break
                    else:
                        ans = temp
            if (max_num >= 2 and ans == 0) or ans > max_num:
                res = False

            if res:
                if ans != 0:
                    print(x,y,ans)
                else:
                    print(x,y,1)
                exit()
    
    
    
if __name__ == "__main__":
    main()