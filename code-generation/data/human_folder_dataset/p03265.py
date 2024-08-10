import sys
from collections import deque
import math
#sys.setrecursionlimit(10**6)
def S(): return sys.stdin.readline().rstrip()
def SL(): return map(str,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())
def array(n,val=0):
    return [val]*n
def matrix(row,columns,val):
    return [[val]*columns for _ in range(row)]

def solve():
    dx = x2-x1
    dy = y2-y1

    x3 = x2 - dy
    y3 = y2 + dx
    x4 = x1 - dy
    y4 = y1 + dx
    print(x3,y3,x4,y4)
    return

if __name__=='__main__':
    x1,y1,x2,y2 = IL()
    solve()