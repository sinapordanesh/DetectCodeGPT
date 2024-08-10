def min_money_required(A, B, M, a, b, x, y, c):
    min_cost = min(a) + min(b)
    for i in range(M):
        min_cost = min(min_cost, a[x[i] - 1] + b[y[i] - 1] - c[i])
    
    return min_cost

# Sample Input 1
print(min_money_required(2, 3, 1, [3, 3], [3, 3, 3], [1], [2], [1])) 

# Sample Input 2
print(min_money_required(1, 1, 2, [10], [10], [1, 1], [1, 1], [5, 10])) 

# Sample Input 3
print(min_money_required(2, 2, 1, [3, 5], [3, 5], [2], [2], [2]))