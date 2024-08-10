def max_desires(N, K, desires):
    black = [[0] * (K + 1) for _ in range(K + 1)]
    white = [[0] * (K + 1) for _ in range(K + 1)]
    
    for x, y, c in desires:
        if c == 'B':
            black[x % K][y % K] += 1
        else:
            white[x % K][y % K] += 1
    
    for i in range(K):
        for j in range(1, K):
            black[i][j] += black[i][j-1]
            white[i][j] += white[i][j-1]
    
    for j in range(K):
        for i in range(1, K):
            black[i][j] += black[i-1][j]
            white[i][j] += white[i-1][j]
            
    res = 0
    for i in range(K):
        for j in range(K):
            res = max(res, black[K-1][K-1] - black[i][K-1] - black[K-1][j] + 2 * black[i][j])
            res = max(res, white[K-1][K-1] - white[i][K-1] - white[K-1][j] + 2 * white[i][j])
    
    return res

# Sample Input 1
print(max_desires(4, 3, [(0, 1, 'W'), (1, 2, 'W'), (5, 3, 'B'), (5, 4, 'B')]))

# Sample Input 2
print(max_desires(2, 1000, [(0, 0, 'B'), (0, 1, 'W')]))

# Sample Input 3
print(max_desires(6, 2, [(1, 2, 'B'), (2, 1, 'W'), (2, 2, 'B'), (1, 0, 'B'), (0, 6, 'W'), (4, 5, 'W')]))