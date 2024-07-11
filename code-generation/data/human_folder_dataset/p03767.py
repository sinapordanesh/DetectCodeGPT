#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import numpy as np

def main():
    numbers=[]
    dp=[]
    n = int(input())
    numbers=np.array(list(map(int,input().split())),dtype=int)
    numbers.sort()
    print(numbers[n::2].sum())

if __name__=="__main__":
    main()