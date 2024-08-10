def height_of_student(matrix):
    row_max = [max(row) for row in matrix]
    col_min = [min(col) for col in zip(*matrix)]
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == row_max[i] and matrix[i][j] == col_min[j]:
                return matrix[i][j]
    return 0

# Read input
def read_input():
    while True:
        n = int(input())
        if n == 0:
            break
        matrix = [list(map(int, input().split())) for _ in range(n)]
        print(height_of_student(matrix))

read_input()