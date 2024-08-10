def count_patties(N, X):
    if X == 1:
        return 0
    if N == 0:
        return 1
    total_layers = 2**(N+1) - 3
    if X >= total_layers:
        return 2**N
    half_layers = total_layers // 2
    if X == half_layers + 1:
        return 2**N - 1
    if X < half_layers + 1:
        return count_patties(N-1, X-1)
    if X > half_layers + 1:
        return 2**N - 1 + count_patties(N-1, X-half_layers-2) + 1

N, X = map(int, input().split())
print(count_patties(N, X))