def sum_of_scores(N):
    MOD = 10**9 + 7
    ans = 0
    for i in range(1, N):
        ans += i * (N - i) * (N - i + 1) // 2
        ans %= MOD
    return ans

N = int(input())
print(sum_of_scores(N))