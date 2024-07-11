#!/usr/bin/env python3

#import
import math
#import numpy as np
N = int(input())
#= input()
#= map(int, input().split())
#= list(map(int, input().split()))
#= [input(), input()]
#= [list(map(int, input().split())) for _ in range(N)]
#= [int(input()) for _ in range(N)]
#= {i:[] for i in range(N)}

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

res = factorization(N)

li = [0] * 101
for i in range(1, 101):
    li[i] = li[i - 1] + i

ans = 0
for r in res:
    if r[0] == 1:
        continue
    i = 0
    while li[i] <= r[1]:
        i += 1
    ans += i - 1

print(ans)

