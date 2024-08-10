# from sys import stdin
# input = stdin.readline
from collections import Counter

MOD = 10**9 + 7
MAX = 2000001
def solve():
    k = int(input())
    s = input().strip()
    ns = len(s)
    res = 0
    fac = [1,1] + [0] * MAX
    inv = [1,1] + [0] * MAX
    for i in range(2,MAX+1):
        fac[i] = fac[i-1] * i % MOD
    inv[MAX] = pow(fac[MAX],MOD-2,MOD)
    for i in range(MAX-1,1,-1):
        inv[i] = inv[i+1]*(i+1)%MOD

    def c(a,b):
        return fac[b]*inv[a]*inv[b-a] % MOD



    for left in range(0,k+1):
        right = k - left
        temp = pow(25,left,MOD) * pow(26,right,MOD)
        temp *= c(ns - 1, left + ns -1)
        temp %= MOD
        res += temp
        res %= MOD
    print(res)







if __name__ == '__main__':
    solve()
