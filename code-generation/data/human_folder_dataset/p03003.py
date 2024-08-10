import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,M = LI()
    S = LI()
    T = LI()

    dp = [[1]*(M+1) for _ in range(N+1)]

    for i in range(1,N+1):
        for j in range(1,M+1):
            if S[i-1] == T[j-1]:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]) % MOD
    print(dp[-1][-1])

if __name__ == '__main__':
    main()