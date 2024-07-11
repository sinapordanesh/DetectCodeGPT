def main():
    m, n = tuple(map(int, input().split()))
    matrix = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(m):
        tmp = list(map(int, input().split()))
        for j in range(n):
            matrix[i][j] = tmp[j]
            matrix[i][n] += tmp[j]
    
    for j in range(n+1):
        for i in range(m):
            matrix[m][j] += matrix[i][j]

    for i in range(m+1):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print(matrix[i][n])

if __name__ == '__main__':
    main()
