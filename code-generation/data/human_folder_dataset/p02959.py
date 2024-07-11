#import math
#import itertools
#import numpy as np
#from collections import deque
# sys.setrecursionlimit(10 ** 6)
#mod = 10 ** 9 + 7
#INF = 10 ** 9
#PI = 3.14159265358979323846

INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))

def do():
    n=INT()
    A=LIST()
    B=LIST()
    ans=0
    ta=A[0]
    for i in range(n):
        tb=B[i]
        ans+=min(ta,tb)
        ta,tb=max(0,ta-tb),max(0,tb-ta)
        ta+=A[i+1]
        ans+=min(ta,tb)
        ta=max(0,ta-tb)
        ta=min(ta,A[i+1])
        #print(ans,ta,tb)
    print(ans)

if __name__=='__main__':
    do()