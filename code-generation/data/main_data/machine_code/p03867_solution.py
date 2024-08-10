def count_sequences(N, K):
    MOD = 10**9 + 7
    if N == 1:
        return K
    if N == 2:
        return K*K
    return K * pow(K-1, (N+1)//2, MOD) % MOD

N, K = map(int, input().split())
print(count_sequences(N, K))