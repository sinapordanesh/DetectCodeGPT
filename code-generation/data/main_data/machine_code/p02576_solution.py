def time_to_make_takoyaki(N, X, T):
    total_time = (N // X) * T
    if N % X != 0:
        total_time += T
    return total_time

N, X, T = map(int, input().split())
print(time_to_make_takoyaki(N, X, T))