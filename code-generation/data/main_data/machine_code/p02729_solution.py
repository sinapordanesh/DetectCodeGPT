def choose_balls(N, M):
    return min(N, M) * (N + M - min(N, M))

N, M = map(int, input().split())
print(choose_balls(N, M))