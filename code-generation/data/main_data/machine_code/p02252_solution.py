def fractional_knapsack(N, W, items):
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    total_value = 0
    
    for value, weight in items:
        if W == 0:
            break
        amount = min(weight, W)
        total_value += amount * (value/weight)
        W -= amount
    
    return total_value

N, W = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

print(fractional_knapsack(N, W, items))