import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 998244353

N = int(read())

import numpy as np

def cumprod(arr,MOD):
    L = len(arr); Lsq = int(L**.5+1)
    arr = np.resize(arr,Lsq**2).reshape(Lsq,Lsq)
    for n in range(1,Lsq):
        arr[:,n] *= arr[:,n-1]; arr[:,n] %= MOD
    for n in range(1,Lsq):
        arr[n] *= arr[n-1,-1]; arr[n] %= MOD
    return arr.ravel()[:L]

def make_fact(U,MOD):
    x = np.arange(U,dtype=np.int64); x[0] = 1
    fact = cumprod(x,MOD)
    x = np.arange(U,0,-1,dtype=np.int64); x[0] = pow(int(fact[-1]),MOD-2,MOD)
    fact_inv = cumprod(x,MOD)[::-1]
    return fact,fact_inv

U = 10**7 + 10
fact, fact_inv = make_fact(U,MOD)

x = np.full(U,2,dtype=np.int64); x[0] = 1
pow2 = cumprod(x,MOD)

n = N//2
comb = fact_inv[:n] * fact_inv[N:N-n:-1] % MOD * fact[N] % MOD

x = (comb * pow2[:n] % MOD).sum()
answer = pow(3,N,MOD) - x - x
answer %= MOD
print(answer)
