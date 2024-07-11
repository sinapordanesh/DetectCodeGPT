import sys
input = sys.stdin.readline

import numpy as np

MOD = 998244353  
N,M = map(int,input().split())

def cumprod_mod(arr):
    L = len(arr); Lsq = int((L**.5)+1)
    arr = np.resize(arr,Lsq**2).reshape(Lsq,Lsq)
    for n in range(1,Lsq):
        arr[:,n] *= arr[:,n-1]; arr[:,n] %= MOD
    for n in range(1,Lsq):
        arr[n] *= arr[n-1,-1]; arr[n] %= MOD
    return arr.ravel()[:L]

# x^n = a+bx mod 1-3x+x^2
Nsq = int((N**.5)+1)
a = np.zeros((Nsq,Nsq+1),dtype=np.int64)
b = np.zeros((Nsq,Nsq+1),dtype=np.int64)
a[0,0] = 1
for n in range(1,Nsq+1):
    a[0,n] = -b[0,n-1] % MOD; b[0,n] = (a[0,n-1]+3*b[0,n-1]) % MOD
u,v = a[0,Nsq],b[0,Nsq]
for n in range(1,Nsq):
    a[n] = (a[n-1]*u-b[n-1]*v) % MOD
    b[n] = (a[n-1]*v+b[n-1]*u+3*b[n-1]*v) % MOD
a = a[:,:-1].ravel()
b = b[:,:-1].ravel()
G = (-a-2*b) % MOD
G = G[:N+1]

A,B = -G[N-1],-G[N]+3*G[N-1]
A,B = A+B,-B
A %= MOD; B %= MOD

def fibonacci(n):
    # a+bx mod 1+x-x^2
    if n == 0:
        return 1,0
    a,b = fibonacci(n//2)
    a,b = a*a+b*b,2*a*b+b*b
    a,b = a%MOD,b%MOD
    return (b,a+b) if n&1 else (a,b)

x = (np.arange(N,dtype=np.int64)+M)%MOD
x[0] = 1
num = cumprod_mod(x)

x = np.arange(N,dtype=np.int64)
x[0] = 1
fact = cumprod_mod(x)

x = np.arange(N,0,-1,dtype=np.int64)
x[0] = pow(int(fact[-1]),MOD-2,MOD)
fact_inv = cumprod_mod(x)[::-1]

if N == 1:
    x = 0
else:
    x = ((num * fact_inv % MOD)[:N-1] * G[N-2::-1] % MOD).sum() % MOD
y,z = fibonacci(M+1)
answer = (z*A + y*B + x)%MOD
print(answer)