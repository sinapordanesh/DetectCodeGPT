def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    dp = [float('inf')] * (N + 5)
    dp[0] = 0
    for i in range(1,N):
        for k in range(1,K+1):
            if i - k >= 0:
                dp[i] = min(dp[i], dp[i-k] + abs(H[i] - H[i-k]))

    print(dp[N-1])

if __name__ == "__main__":
    main()