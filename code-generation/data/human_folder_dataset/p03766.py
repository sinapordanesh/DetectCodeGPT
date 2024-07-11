# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

def get(i):
    #if i==-n: return 0
    if i <= 0: return 1
    else: return a[i]


n, = map(int,readline().split())

MOD = 10**9+7

a = [1,n,n*n]
for i in range(3,n+1):
    res = -get(i-n-2) + get(i-3) - get(i-2) + 2*get(i-1)
    a.append(res%MOD)

#print(a)
print(a[-1])











