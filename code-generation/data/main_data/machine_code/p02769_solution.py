def possible_combinations(n, k):
    MOD = 10**9 + 7
    ans = 1
    for i in range(1, n+1):
        ans = (ans * (k + i - 1) % MOD) 
        ans //= i
    return ans

n, k = map(int, input().split())
print(possible_combinations(n, k))