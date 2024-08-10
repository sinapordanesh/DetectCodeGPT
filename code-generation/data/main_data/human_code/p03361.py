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
    H, W = MI()
    D = Init(H, W, -1)
    L = [input().rstrip() for i in range(H)]
    move = [[1,0],[0,1],[-1,0],[0,-1]]
    for i in range(H):
        for j in range(W):
            if L[i][j] == "#" and D[i][j] == -1:
                D[i][j] = 0
                dq = deque([(i, j)])
                while dq:
                    x, y = dq.popleft()
                    for x1, y1 in move:
                        x1+=x
                        y1+=y
                        if x1 >= 0 and x1 <= H-1 and y1 >= 0 and y1 <= W-1 and D[x1][y1] == -1:
                            if L[x1][y1] == "#":
                                D[x1][y1] = D[x][y]+1
                                dq.append((x1, y1))
                if D[x][y] == 0:
                    print("No")
                    exit()
    print("Yes")

if __name__ == "__main__":
    main()