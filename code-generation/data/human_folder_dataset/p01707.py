def main():
    MOD = 10**9 + 7

    while 1:
        N, D, X = map(int, input().split())
        if N == D == X == 0:
            break
        dp = [[0]*(N+1) for i in range(N+1)]
        dp[0][0] = 1
        for i in range(N):
            s = 0
            dpi = dp[i]
            dpj = dp[i+1]
            for j in range(N):
                s += dpi[j]
                if X-1 <= j:
                    s -= dpi[j-X+1]
                dpj[j+1] = s = s % MOD
        ans = 0
        v = 1
        d = D % MOD
        for k in range(1, min(D, N)+1):
            v = v * (d-k+1) * pow(k, MOD-2, MOD) % MOD
            ans += v * dp[k][N] % MOD
        print(ans % MOD)
main()
