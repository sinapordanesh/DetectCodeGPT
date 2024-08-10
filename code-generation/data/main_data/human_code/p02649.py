def popcount(x):
    x = x - ((x >> 1) & 0x55555555)
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    return x & 0x0000007f

cmb=[[0 for i in range(51)] for j in range(51)]
cmb[0][0]=1
for i in range(51):
    for j in range(51):
        if i!=50:
            cmb[i+1][j]+=cmb[i][j]
        if j!=50 and i!=50:
            cmb[i+1][j+1]+=cmb[i][j]


for i in range(1,51):
    for j in range(2,51):
        cmb[i][j]+=cmb[i][j-1]

import random
N,K,T,S=map(int,input().split())
a=list(map(int,input().split()))

must0=[i for i in range(18) if S>>i &1==0]
must1=[i for i in range(18) if T>>i &1==1]

A=[]
for val in a:
    check=True
    for j in must0:
        check=check&(val>>j &1==0)
    for j in must1:
        check=check&(val>>j &1==1)
    if check:
        A.append(val)

if not A:
    print(0)
    exit()

bit=[]
for i in range(18):
    if i not in must0 and i not in must1:
        bit.append(i)

for i in range(len(A)):
    temp=0
    for j in range(len(bit)):
        temp+=(A[i]>>bit[j] &1==1)*2**j
    A[i]=temp

ans=0
n=len(bit)
data=[0]*(2**n)
pc=[popcount(i) for i in range(2**n)]
for i in range(2**n):
    for a in A:
        data[a&i]+=1
    for a in A:
        if data[a&i]:
            ans+=cmb[data[a&i]][min(K,data[a&i])]*(-1)**pc[i]
            data[a&i]=0

print(ans)