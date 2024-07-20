def zigzag_path(N):
    if N == 0:
        return
    
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    num = 1
    
    for i in range(2*N-1):
        if i < N:
            start_col = 0
            start_row = i
        else:
            start_col = i - N + 1
            start_row = N - 1
        
        while start_row >= 0 and start_col < N:
            matrix[start_row][start_col] = num
            num += 1
            start_row -= 1
            start_col += 1
    
    print(f"Case {N}:")
    for row in matrix:
        print(" ".join(str(x).rjust(3) for x in row))

# Read input test cases
while True:
    N = int(input())
    if N == 0:
        break
    zigzag_path(N)