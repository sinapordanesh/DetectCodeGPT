def count_pairs(N, M, grid):
    result = 0
    MOD = 998244353
    
    for i in range(1 << N):
        for j in range(1 << M):
            temp = 0
            for x in range(N):
                for y in range(M):
                    if i & (1 << x) and j & (1 << y):
                        temp += grid[x][y]
            if temp % 2 == 1:
                result += 1
                
    return result % MOD

# Sample Input 1
N1 = 2
M1 = 2
grid1 = [[0, 1], [1, 0]]
print(count_pairs(N1, M1, grid1))

# Sample Input 2
N2 = 2
M2 = 3
grid2 = [[0, 0, 0], [0, 1, 0]]
print(count_pairs(N2, M2, grid2))