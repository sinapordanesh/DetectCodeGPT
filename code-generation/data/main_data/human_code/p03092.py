def main():
    import sys
    input = sys.stdin.readline

    N, R, L = map(int, input().split())
    P = list(map(int, input().split()))

    val2idx = [0] * (N+1)
    for i, p in enumerate(P):
        val2idx[p] = i + 1
    bigger = [[0] * (N+1) for _ in range(N+1)]
    for p in range(1, N+1):
        for j in range(N):
            if P[j] > p:
                bigger[p][j+1] = bigger[p][j] + 1
            else:
                bigger[p][j + 1] = bigger[p][j]
    #print(bigger)
    inf = 10**14
    dp = [[inf] * (N+1) for _ in range(N+1)]
    dp[0][0] = 0

    for p in range(1, N+1):
        i = val2idx[p]
        for j in range(N+1):
            if i > j:
                dp[p][j] = min(dp[p][j], dp[p-1][j] + L)
                dp[p][i] = min(dp[p][i], dp[p-1][j] + R * (bigger[p][i] - bigger[p][j]))
            else:
                dp[p][j] = min(dp[p][j], dp[p - 1][j])
    print(min(dp[-1]))
    #[print(i, dp[i]) for i in range(N+1)]


if __name__ == '__main__':
    main()
