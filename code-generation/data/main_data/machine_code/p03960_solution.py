def minimum_total_cost():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    
    costs = 0
    for i in range(H-1):
        for j in range(W):
            if grid[i][j] == grid[i+1][j]:
                costs += 1
    
    print(costs * 2)

minimum_total_cost()