def total_accommodation_fee(N, K, X, Y):
    if N <= K:
        return N * X
    else:
        return K * X + (N - K) * Y

N, K, X, Y = map(int, input().split())
print(total_accommodation_fee(N, K, X, Y))