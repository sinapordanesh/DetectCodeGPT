def matrix_multiplication():
    n, m, l = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    B = [list(map(int, input().split())) for _ in range(m)]
    
    C = [[0 for _ in range(l)] for _ in range(n)]
    
    for i in range(n):
        for j in range(l):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    
    for row in C:
        print(*row)

matrix_multiplication()