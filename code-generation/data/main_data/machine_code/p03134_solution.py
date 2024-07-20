def possible_sequences(S):
    MOD = 998244353
    N = len(S)
    dp = [[0] * (4 * N + 1) for _ in range(4 * N + 1)]
    dp[0][0] = 1
    for i in range(N):
        s = int(S[i])
        new_dp = [[0] * (4 * N + 1) for _ in range(4 * N + 1)]
        for red in range(2 * N + 1):
            for blue in range(2 * N + 1):
                if dp[red][blue] == 0:
                    continue
                total = dp[red][blue]
                if s == 0:
                    new_dp[red + 1][blue] = (new_dp[red + 1][blue] + total) % MOD
                    new_dp[red][blue + 2] = (new_dp[red][blue + 2] + total) % MOD
                elif s == 1:
                    new_dp[red + 1][blue] = (new_dp[red + 1][blue] + total) % MOD
                    new_dp[red][blue + 1] = (new_dp[red][blue + 1] + total) % MOD
                elif s == 2:
                    new_dp[red][blue + 1] = (new_dp[red][blue + 1] + total) % MOD
                    new_dp[red][blue + 2] = (new_dp[red][blue + 2] + total) % MOD
        dp = new_dp
    result = 0
    for red in range(2 * N + 1):
        for blue in range(2 * N + 1):
            if (red + blue) % 2 == 0:
                result = (result + dp[red][blue]) % MOD
    return result % MOD

S = input()
print(possible_sequences(S))