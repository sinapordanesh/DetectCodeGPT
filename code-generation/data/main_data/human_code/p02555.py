from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
INF = float("inf")

MOD = 1000000007
class Combination(object):
    def __init__(self, N):
        self.fac = [0] * (N + 1)
        self.inv = [0] * (N + 1)
        self.finv = [0] * (N + 1)
        self.fac[0] = 1
        self.finv[0] = 1
        if N > 0:
            self.fac[1] = 1
            self.inv[1] = 1
            self.finv[1] = 1
 
        # 前計算
        for i in range(2, N + 1):
            self.fac[i] = self.fac[i - 1] * i % MOD
            self.inv[i] = self.inv[MOD % i] * (MOD - (MOD // i)) % MOD
            self.finv[i] = self.finv[i - 1] * self.inv[i] % MOD
 
    def com(self, N, k):
        return (self.fac[N] * self.finv[k] * self.finv[N - k]) % MOD


# 処理内容
def main():
    S = int(input())
    Com = Combination(S)
    
    ans = 0
    i = 1
    S -= 3
    while S >= 0:
        ans += Com.com(S+i-1, i-1)
        ans %= MOD
        S -= 3
        i += 1
    
    print(ans)


if __name__ == '__main__':
    main()