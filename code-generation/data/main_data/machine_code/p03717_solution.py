MOD = 10**9+7

def paint_squares(N, M, conditions):
    dp = [[[0] * 8 for _ in range(1<<N)] for _ in range(N+1)]
    dp[0][0][0] = 1
    
    for i in range(1, N+1):
        for bit in range(1<<N):
            for j in range(8):
                dp[i][bit][j] = dp[i-1][bit][j]
                
        for bit in range(1<<N):
            for j in range(8):
                if dp[i-1][bit][j] == 0:
                    continue
                
                for l, r, x in conditions:
                    color = 0
                    for k in range(l-1, r):
                        color |= 1 << k
                    
                    if bin(bit & color).count('1') == x:
                        dp[i][bit|color][j|color] += dp[i-1][bit][j]
                        dp[i][bit|color][j|color] %= MOD
    
    ans = 0
    for bit in range(1<<N):
        if bin(bit).count('1') == N:
            ans += sum(dp[N][bit])
            ans %= MOD
    
    return ans

# Sample Input
N = 3
M = 1
conditions = [[1, 3, 3]]

print(paint_squares(N, M, conditions))

N = 4
M = 2
conditions = [[1, 3, 1], [2, 4, 2]]

print(paint_squares(N, M, conditions))

N = 1
M = 3
conditions = [[1, 1, 1], [1, 1, 2], [1, 1, 3]]

print(paint_squares(N, M, conditions))

N = 8
M = 10
conditions = [[2, 6, 2], [5, 5, 1], [3, 5, 2], [4, 7, 3], [4, 4, 1], [2, 3, 1], [7, 7, 1], [1, 5, 2], [1, 7, 3], [3, 4, 2]]

print(paint_squares(N, M, conditions))