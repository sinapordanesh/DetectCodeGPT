def expected_total_distance(N, d1, x):
    return d1 + x * (N ** 2 + N) / 2 + (x / 2) * ((N - 1) * N * (2 * N + 1) - 2 * N + 1) / 3 - N

N, d1, x = map(int, input().split())
print(expected_total_distance(N, d1, x))