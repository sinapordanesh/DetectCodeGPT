def N():
    return int(input())
def L():
    return list(map(int,input().split()))
def NL(n):
    return [list(map(int,input().split())) for i in range(n)]
mod = pow(10,9)+7
#import numpy
k = N()
a,b = L()
for i in range(a,b+1):
    if i%k == 0:
        print("OK")
        exit()
print("NG")