def count_sequences(N, M):
    MOD = 10**9 + 7
    ans = 1
    i = 2
    while i * i <= M:
        cnt = 0
        while M % i == 0:
            cnt += 1
            M //= i
        ans = (ans * (cnt + 1)) % MOD
        i += 1
    if M != 1:
        ans = (ans * 2) % MOD
    return ans

N, M = map(int, input().split())
print(count_sequences(N, M))