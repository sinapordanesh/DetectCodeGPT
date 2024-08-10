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
    flg=True
    la=len(A)
    bool=[False]*(n+1)
    B=[]
    for i in range(la-1,-1,-1):
        a=A[i]
        s=i+1
        temp=0
        for j in range(n//s+1):
            if j==0:
                continue
            if bool[j*s]:
                temp+=1
        
        if temp%2!=a:
            B.append(s)
            bool[s]=True
    
    B=sorted(B)
    print(len(B))
    if len(B)!=0:
        print(*B)

            

if __name__=='__main__':
    do()