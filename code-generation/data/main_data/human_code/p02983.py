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
    l,r=INTM()
    mods=[]
    for i in range(l,min(l+3000,r+1)):
        mods.append(i%2019)
    
    ans=2018
    ml=len(mods)
    for i in range(ml-1):
        for j in range(i+1,ml):
            ans=min(ans,(mods[i]*mods[j])%2019)

    print(ans)


if __name__=='__main__':
    do()