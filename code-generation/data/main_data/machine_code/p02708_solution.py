def possible_sum_values(N, K):
    MOD = 10**9 + 7
    if K == 1:
        return N+1
    elif K == N+1:
        return 1
    else:
        return (N-K+2)*(N-K+1)//2 + N-K+1

N, K = map(int, input().split())
print(possible_sum_values(N, K) % (10**9 + 7))