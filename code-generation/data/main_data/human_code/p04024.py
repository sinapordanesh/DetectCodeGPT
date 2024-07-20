import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

H, W, K = map(int, readline().split())
S = np.frombuffer(read(),'S1').reshape(H,-1)[:,:W] == b'#'

MOD = 10 ** 9 + 7

if K in [0,1]:
    print(1)
    exit()

B = int(S.sum())

if H == 1 or W == 1:
    if B == H * W:
        answer = 1
    else:
        answer = pow(int(B), K-1, MOD)
    print(answer)
    exit()

concat_h = S[:,0] & S[:,-1]
concat_w = S[0] & S[-1]

bl_h = np.any(concat_h)
bl_w = np.any(concat_w)
if bl_h and bl_w:
    print(1)
    exit()
if (not bl_h) and (not bl_w):
    answer = pow(B, K-1, MOD)
    print(answer)
    exit()
if bl_w:
    H, W = W, H
    S = S.T
    concat_h, concat_w = concat_w, concat_h

def power_mat(A,n,MOD):
    k = A.shape[0]
    if n == 0:
        return np.eye(k,dtype=np.int64)
    B = power_mat(A,n//2,MOD)
    B = np.dot(B,B) % MOD
    return np.dot(A,B) % MOD if n & 1 else B

h_edge = (S[:,:-1] & S[:,1:]).sum()
A = np.array([[B, -h_edge], [0, np.count_nonzero(concat_h)]], np.int64)

answer = power_mat(A, K-1, MOD)[0].sum() % MOD
print(answer)