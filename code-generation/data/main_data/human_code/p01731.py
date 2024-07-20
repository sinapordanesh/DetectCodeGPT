import sys
sys.setrecursionlimit(10000)
n=int(input())
a=[]
b=[[]for _ in [0]*n]

def f(i,x):
    print('.'*x+a[i])
    for j in b[i]:
        f(j,x+1)

for i in range(n):
    c=int(input())
    a+=[input()]
    if c!=0:b[c-1]+=[i]
f(0,0)