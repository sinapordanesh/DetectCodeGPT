import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

S = readline().rstrip()
l,r = map(int,read().split())

def double_naive(S):
    L = len(S)
    for i in range(1,L+1):
        T = S[:i] * 2
        if len(T) > L and T[:L] == S:
            return T

def Z_algorithm(S):
    # 共通接頭辞の長さを返す
    N=len(S)
    arr = [0]*N
    arr[0] = N
    i,j = 1,0
    while i<N:
        while i+j<N and S[j]==S[i+j]:
            j += 1
        arr[i]=j
        if not j:
            i += 1
            continue
        k = 1
        while i+k<N and k+arr[k]<j:
            arr[i+k] = arr[k]
            k += 1
        i += k; j -= k
    return arr

def F(S):
    N = len(S)
    opt_len = N
    Z = Z_algorithm(S)
    for x in range(N//2+1,N):
        z = Z[x]
        if x + z >= N:
            opt_len = x
            break
    return S[:opt_len] * 2

S = F(S)
S = F(S)
T = F(S)
S = S[:len(S)//2]
T = T[:len(T)//2]

S = np.array(list(S)) - ord('a')
T = np.array(list(T)) - ord('a')

# S,T,TS,TST,...

L = [len(S), len(T)]
for _ in range(100):
    L.append(L[-1] + L[-2])
ctr = [np.bincount(S,minlength=26), np.bincount(T,minlength=26)]
for _ in range(100):
    ctr.append(ctr[-1] + ctr[-2])

def get_dist(N,R):
    # S_NにおけるR番目以下
    if N == 0:
        return np.bincount(S[:R],minlength=26)
    if N == 1:
        return np.bincount(T[:R],minlength=26)
    if L[N-1] >= R:
        return get_dist(N-1,R)
    return ctr[N-1] + get_dist(N-2,R-L[N-1])

c = get_dist(99,r) - get_dist(99,l-1)

print(*c)