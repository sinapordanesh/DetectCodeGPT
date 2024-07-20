def set_levels(N):
    levels = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            levels[i][j] = 1
    for row in levels:
        print(*row) 

# Sample Input
N = 3
set_levels(N)