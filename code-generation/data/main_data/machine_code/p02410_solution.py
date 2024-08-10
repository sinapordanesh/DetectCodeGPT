def matrix_vector_multiplication():
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    b = [int(input()) for _ in range(m)]
    
    for i in range(n):
        c_i = sum(A[i][j] * b[j] for j in range(m))
        print(c_i)

matrix_vector_multiplication()