#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import numpy as np

def main():
    numbers=[]
    n,m = map(int,input().split())
    [numbers.append(int(input())) for _ in range(n)]
    n_numbers=np.array(numbers,dtype=int)
    n_numbers.sort()
    print(min(n_numbers[i+m-1] - n_numbers[i] for i in range(n-m+1)))

if __name__=="__main__":
    main()