def total_length_of_trajectory(N, X):
    return 3 * N - 3 - 2 * abs(N - 2 * X)

N, X = map(int, input().split())
print(total_length_of_trajectory(N, X))