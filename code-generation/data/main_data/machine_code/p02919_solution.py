def second_largest_sum(N, P):
    sum_LR = 0
    for L in range(1, N):
        for R in range(L+1, N+1):
            X_LR = sorted(P[L-1:R])[-2]
            sum_LR += X_LR
    return sum_LR

N = int(input())
P = list(map(int, input().split()))

print(second_largest_sum(N, P))