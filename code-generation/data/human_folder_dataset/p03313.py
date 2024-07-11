def merge(x, y, z, w):
    P = [x, y, z, w]
    P.sort()
    return P[-1], P[-2]


def main():
    N = int(input())
    a = list(map(int, input().split()))
    dp = [0]*(2*(N+1)*((1 << N)))

    def calc(i, j, k):
        return (2*N + 2) * i + (N+1)*k + j
    for i in range(1 << N):
        dp[calc(i, 0, 0)] = a[i]
    for j in range(1, N+1):
        for i in range(1 << N):
            x = calc(i, j, 0)
            y = calc(i & ~(1 << (j-1)), j - 1, 0)          
            if (i & (1 << (j-1))):
                dp[x], dp[x+N+1] = merge(dp[y], dp[y+N+1], dp[x-1], dp[x+N])
            else:
                dp[x], dp[x+N+1] = dp[x-1], dp[x+N]
    result = [0]*(1 << N)
    for k in range(1, 1 << N):
        result[k] = max(result[k-1], dp[calc(k, N, 0)]+dp[calc(k, N, 1)])
        print(result[k])
    return


if __name__ == "__main__":
    main()

