def min_money_needed(N, M, X, books):
    min_cost = float('inf')
    
    for i in range(1, 1 << N):
        understanding_levels = [0] * M
        total_cost = 0
        
        for j in range(N):
            if i >> j & 1:
                total_cost += books[j][0]
                for k in range(M):
                    understanding_levels[k] += books[j][k+1]
        
        if all(level >= X for level in understanding_levels):
            min_cost = min(min_cost, total_cost)
    
    return min_cost if min_cost != float('inf') else -1

# Input
N, M, X = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(N)]

# Output
print(min_money_needed(N, M, X, books))