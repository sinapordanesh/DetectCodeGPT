def min_time_to_reach_destination(N, A, B, C, D, E):
    return (N + min(A, B, C, D, E) - 1) // min(A, B, C, D, E) + 4

N, A, B, C, D, E = map(int, input().split())
print(min_time_to_reach_destination(N, A, B, C, D, E))