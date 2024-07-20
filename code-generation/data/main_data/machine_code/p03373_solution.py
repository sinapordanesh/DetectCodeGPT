def pizza_cost(A, B, C, X, Y):
    min_cost = float('inf')
    
    for i in range(max(X, Y) + 1):
        cost = C * 2 * i + A * max(0, X - i) + B * max(0, Y - i)
        min_cost = min(min_cost, cost)
    
    return min_cost

A, B, C, X, Y = map(int, input().split())
print(pizza_cost(A, B, C, X, Y))