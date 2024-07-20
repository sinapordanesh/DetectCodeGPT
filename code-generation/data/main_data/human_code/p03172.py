#!/usr/bin/env python3

#import
#import math
#import numpy as np
N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

def mod(num):
    return num % MOD

dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    s = [0] * (K + 2)
    for j in range(1, K + 2):
        s[j] = mod(s[j - 1] + dp[i - 1][j - 1])

    for j in range(K + 1):
        dp[i][j] =  mod(s[j + 1] - s[max(0, j - A[i-1])])

print(dp[N][K])

