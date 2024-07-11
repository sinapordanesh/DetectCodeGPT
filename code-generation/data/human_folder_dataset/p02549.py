import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 998244353
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, K = LI()
    LR = [LI() for _ in range(K)]

    dp = [0] * (N + 1)
    dp[0] = 1
    a = [0] * (N + 1)
    a[0] = 1
    a[1] = -1
    for i in range(N):
        for l, r in LR:
            left = min(i + l, N)
            right = min(i + r + 1, N)
            a[left] += dp[i]
            a[right] -= dp[i]
        dp[i+1] += dp[i] + a[i+1]
        dp[i+1] %= MOD
        # print(a)
        # print(dp)

    print(dp[-2])

if __name__ == '__main__':
    resolve()
