import sys
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np

MOD = 10**9 + 7

N = int(readline())
C = np.array([line.split() for line in readlines()],np.int8)

def rank(A):
    if (A==0).all():
        return 0
    i = np.nonzero(A[:,0])[0]
    if len(i) == 0:
        return rank(A[:,1:])
    i = i[0]
    temp = A[i].copy()
    A[i] = A[0]
    A[0] = temp
    A[1:] ^= A[1:,0][:,None] * A[0][None,:]
    return 1 + rank(A[1:,1:])

def cumprod(arr,MOD):
    L = len(arr); Lsq = int(L**.5+1)
    arr = np.resize(arr,Lsq**2).reshape(Lsq,Lsq)
    for n in range(1,Lsq):
        arr[:,n] *= arr[:,n-1]; arr[:,n] %= MOD
    for n in range(1,Lsq):
        arr[n] *= arr[n-1,-1]; arr[n] %= MOD
    return arr.ravel()[:L]

def power_mod(a,n,MOD):
    if n == 0:
        return 1
    x = power_mod(a,n//2,MOD)
    x *= x
    x %= MOD
    return (a*x)%MOD if n&1 else x

r = rank(C)

x = np.full(N*N+100,2,np.int64); x[0] = 1
pow2 = cumprod(x,MOD)

G = np.zeros((N+1,N+1),np.int64)
for n in range(N+1):
    G[n,1:] = pow2[n] - pow2[:N]
G[:,0] = 1
for n in range(1,N+1):
    G[:,n] *= G[:,n-1]; G[:,n] %= MOD

Gd = np.diagonal(G)

D = G * power_mod(Gd,MOD-2,MOD)[None,:] % MOD
F = np.zeros((N+1,N+1),np.int64)
for n in range(N+1):
    F[n,:n+1] = Gd[:n+1] * D[n,n::-1] % MOD

B = D[N] * F[N] % MOD

C = D[N,r] * F[:,r] % MOD * pow2[N*N::-N] % MOD

A = (B[r:N+1] * C[r:N+1] % MOD).sum() % MOD

answer = A * pow(int(B[r]),MOD-2,MOD) % MOD
print(answer)