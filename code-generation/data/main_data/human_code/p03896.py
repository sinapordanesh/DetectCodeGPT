import sys
readline = sys.stdin.readline
readlines = sys.stdin.readlines

import numpy as np

N = int(readline())

def F(N):
    if N == 4:
        return np.array([[3,2,4],[3,4,1],[4,1,2],[2,1,3]])
    if N&1:
        x = np.arange(N)[:,None] + np.arange(N)[None,:]
        return (x[:,1:]%N)+1
    M = N//2
    x = F(M)
    arr = np.empty((N,N-1),np.int32)
    arr[0:M,0:M-1] = x
    arr[M:N,0:M-1] = x+M
    for n in range(M-1,N-1):
        arr[0:M,n] = np.arange(M) + n
        arr[M:N,n] = np.arange(M) + (1-n)        
    arr[:M,M-1:] %= M
    arr[:M,M-1:] += M+1
    arr[M:,M-1:] %= M
    arr[M:,M-1:] += 1
    return arr

if N == 2:
    print(-1)
    exit()

x = F(N)
print('\n'.join(' '.join(row) for row in x.astype(str)))