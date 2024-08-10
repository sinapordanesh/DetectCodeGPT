N, W = map(int, input().split())
INF, V = 1 << 40, 100
dp = [[INF for j in range(N*V+1)] for i in range(N+1)]


def main():
    v, w = [0 for i in range(N)], [0 for i in range(N)]
    for i in range(N):
        v[i], w[i] = map(int, input().split())

    dp[0][0] = 0
    for i in range(1, N+1):
        for j in range(N*V+1):
            if j < v[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-v[i-1]]+w[i-1])

    ans = 0
    for i in range(N*V+1):
        if dp[N][i] <= W:
            ans = i

    print(ans)


if __name__ == '__main__':
    main()

