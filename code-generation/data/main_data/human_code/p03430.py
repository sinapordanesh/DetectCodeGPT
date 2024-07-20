import sys
input = sys.stdin.buffer.readline

S = list(input().rstrip())
K = int(input())

L = len(S)

def main():
    if K >= L//2:
        ans = L
    else:
        dp = [[[0]*(K+1) for _ in range(L+1)] for _ in range(L+1)]

        ans = 0
        for ind in reversed(range(L)):
            # [0, ind), [ind, L-1]
            s = S[ind]
            for i in range(ind):
                for k in reversed(range(K+1)):
                    if S[i] == s:
                        dp[i+1][L-ind][k] = dp[i][L-ind-1][k] + 1
                    else:
                        dp[i+1][L-ind][k] = max(dp[i][L-ind][k], dp[i+1][L-ind-1][k])
                        dp[i+1][L-ind][k] = min(dp[i+1][L-ind][k], min(i+1, L-ind))
                        if k < K and dp[i+1][L-ind][k] == dp[i][L-ind-1][k]:
                            dp[i+1][L-ind][k+1] = max(dp[i+1][L-ind][k+1], dp[i+1][L-ind][k]+1)
                            dp[i+1][L-ind][k+1] = min(dp[i+1][L-ind][k+1], min(i+1, L-ind))
            for k in range(K+1):
                ans = max(ans, 2*dp[ind][L-ind][k])
                ans = max(ans, 2*dp[ind][L-ind-1][k] + 1)
            dp.pop()
    print(ans)


if __name__ == "__main__":
    main()