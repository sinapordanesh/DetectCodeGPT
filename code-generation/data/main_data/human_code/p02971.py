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
    A=[]
    for i in range(n):
        A.append(INT())
    
    B=sorted(A,reverse=True)
    m1=A.count(B[0])
    m2=A.count(B[1])
    if m1>=2:
        flg=True
    else:
        index=A.index(B[0])
        flg=False

    #print(A,B,index)

    if flg:
        for i in range(n):
            print(B[0])
    else:
        for i in range(n):
            if i!=index:
                print(B[0])
            else:
                print(B[1])


if __name__=='__main__':
    do()