def main():
    n, m, l = tuple(map(int, input().split()))
    matA = [[0 for j in range(m)] for i in range(n)]
    matB = [[0 for k in range(l)] for j in range(m)]
    matC = [[0 for k in range(l)] for i in range(n)]

    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(m):
            matA[i][j] = tmp[j]

    for j in range(m):
        tmp = list(map(int, input().split()))
        for k in range(l):
            matB[j][k] = tmp[k]


    for i in range(n):
        for k in range(l):
            for j in range(m):
                matC[i][k] += matA[i][j] * matB[j][k]

    for i in range(n):
        for k in range(l):
            if k == l-1:
                print(matC[i][k])
            else:
                print(matC[i][k], end=' ')

if __name__ == '__main__':
    main()
