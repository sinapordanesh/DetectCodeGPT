#import math
#import itertools
import numpy as np
#from collections import deque
# sys.setrecursionlimit(10 ** 6)
#MOD = 10 ** 9 + 7
#INF = 10 ** 9
#PI = 3.14159265358979323846

INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))

def do():
    h,w=INTM()
    ban=np.zeros((h,w),dtype=np.int16)
    for i in range(h):
        s=STR()
        for i1 in range(len(s)):
            if s[i1]==".":
                ban[i][i1]=1

    left =np.zeros((h,w),dtype=np.int16)
    right=np.zeros((h,w),dtype=np.int16)
    up   =np.zeros((h,w),dtype=np.int16)
    down =np.zeros((h,w),dtype=np.int16)
    #print(up)
    for i in range(w):
        i2=w-1-i
        if i==0:
            left[:,i]=ban[:,i]
            right[:,i2]=ban[:,i2]
        else:
            left[:,i]=ban[:,i]*(left[:,i-1]+1)
            right[:,i2]=ban[:,i2]*(right[:,i2+1]+1)
    
    for i in range(h):
        i2=h-1-i
        if i==0:
            up[i,:]=ban[i,:]
            down[i2,:]=ban[i2,:]
        else:
            up[i,:]=ban[i,:]*(up[i-1,:]+1)
            down[i2,:]=ban[i2,:]*(down[i2+1,:]+1)
    

    anslist=down+up+right+left
    ans=0
    for i in anslist:
        ans=max(ans,max(i))
    print(ans-3)


if __name__=='__main__':
    do()