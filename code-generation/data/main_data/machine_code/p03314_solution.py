MOD = 10**9 + 7

def colorful_integer_sequence(N, K, M, A):
    cnt = [0] * (K + 1)
    ans = 0
    total = 0
    for i in range(1, N + 1):
        total += i
    for i in range(1, M + 1):
        cnt[A[i]] += 1
    for i in range(1, K + 1):
        ans += cnt[i] ** 2
    for i in range(1, N - M + 2):
        if sum(cnt) == M:
            ans %= MOD
            ret = (total - (N - M) + 1) * (N - M) // 2
            ans += ret
        cnt[A[i]] -= 1
        cnt[A[i + M]] += 1
    return ans % MOD

# Read inputs
N, K, M = map(int, input().split())
A = [0] + list(map(int, input().split()))

# Call the function and print the result
print(colorful_integer_sequence(N, K, M, A))