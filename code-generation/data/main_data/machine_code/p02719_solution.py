def minimum_possible_value(N, K):
    while N >= K:
        N = abs(N - K)
    return N

N, K = map(int, input().split())
print(minimum_possible_value(N, K))