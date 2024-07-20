def count_pairs(N):
    MOD = 10**9 + 7
    return (N+2)*(N+3)//2 % MOD

N = int(input())
print(count_pairs(N))