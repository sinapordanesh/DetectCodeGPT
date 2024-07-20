MODD = 10**9 + 7 

def modinv(a,m)-> int:
    b = m
    u = 1
    v = 0
    while (b):
        t = a // b
        a -= t * b
        a,b= b,a
        u -= t * v
        u,v= v,u
    u %= m
    if (u < 0):
        u += m
    return u


fac=[1]*200001
infac=[1]*200001
aaa=1
for i in range(1,200001):
    aaa=(aaa*i)%MODD
    fac[i]=aaa
    infac[i]=modinv(aaa,MODD)
    #print(fac[i])

import math as m

def perm(x,y,z) -> int:
    #print(fac[x]//(fac[y]*fac[z]))   
    return ((fac[x]*infac[y]*infac[z])%MODD)

h,w,a,b= [int(x) for x in input().split()]
A = h-a
B = b-1
C = h-1
D = w-b-1
j=0
k=B
kl = C
jl = D
ans = 0
for i in range(A):
  ans+=perm(B+i,B,i)*perm(C+D-i,C-i,D)
print(ans%MODD)