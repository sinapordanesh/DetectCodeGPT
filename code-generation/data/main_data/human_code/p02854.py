#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import numpy as np

def main():
    N=[]
    n = int(input())
    N=np.array(list(map(int,input().split())))
    Ncum=N.cumsum()
    L=Ncum[:-1]
    R=Ncum[-1]-L
    ans=np.abs(L-R).min()
    print(ans)

if __name__=="__main__":
    main()