def min_total_cost(N, balls):
    min_cost = float('inf')
    for i in range(N):
        for j in range(N):
            p = balls[j][0] - balls[i][0]
            q = balls[j][1] - balls[i][1]
            cost = 0
            for k in range(N):
                x = balls[k][0]
                y = balls[k][1]
                if (x - p, y - q) not in balls:
                    cost += 1
            min_cost = min(min_cost, cost)
    return min_cost

# Sample Input
print(min_total_cost(2, [(1, 1), (2, 2)])) # Output: 1
print(min_total_cost(3, [(1, 4), (4, 6), (7, 8)])) # Output: 1
print(min_total_cost(4, [(1, 1), (1, 2), (2, 1), (2, 2)])) # Output: 2