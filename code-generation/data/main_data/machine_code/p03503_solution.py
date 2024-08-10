def max_profit(N, F, P):
    max_profit = float('-inf')
    for i in range(1, 2**10):
        open_periods = [0]*N
        profit = 0
        for j in range(N):
            for k in range(10):
                if (i >> k) & 1 and F[j][k]:
                    open_periods[j] += 1
            profit += P[j][open_periods[j]]
        max_profit = max(max_profit, profit)
    return max_profit

# Sample Input 1
N = 1
F = [[1, 1, 0, 1, 0, 0, 0, 1, 0, 1]]
P = [[3, 4, 5, 6, 7, 8, 9, -2, -3, 4, -2]]
print(max_profit(N, F, P))

# Sample Input 2
N = 2
F = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]]
P = [[0, -2, -2, -2, -2, -2, -1, -1, -1, -1, -1], [0, -2, -2, -2, -2, -2, -1, -1, -1, -1, -1]]
print(max_profit(N, F, P))

# Sample Input 3
N = 3
F = [[1, 1, 1, 1, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]]
P = [[-8, 6, -2, -8, -8, 4, 8, 7, -6, 2, 2], [-9, 2, 0, 1, 7, -5, 0, -2, -6, 5, 5], [6, -6, 7, -9, 6, -5, 8, 0, -9, -7, -7]]
print(max_profit(N, F, P))