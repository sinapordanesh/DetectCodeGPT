def min_displayed_value(N, K):
    if N % 2 == 0:
        return (K * (N // 2)) ** 2
    else:
        return ((K * (N // 2)) + K) ** 2

N, K = map(int, input().split())
print(min_displayed_value(N, K))