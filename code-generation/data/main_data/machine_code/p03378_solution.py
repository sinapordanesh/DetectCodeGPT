def min_cost_to_goal(N, M, X, tolls):
    tolls.sort()
    left_cost = sum(1 for i in range(X) if i in tolls)
    right_cost = sum(1 for i in range(X+1, N) if i in tolls)
    
    return min(left_cost, right_cost)

# Sample Input 1
print(min_cost_to_goal(5, 3, 3, [1, 2, 4])) # Output: 1

# Sample Input 2
print(min_cost_to_goal(7, 3, 2, [4, 5, 6])) # Output: 0

# Sample Input 3
print(min_cost_to_goal(10, 7, 5, [1, 2, 3, 4, 6, 8, 9])) # Output: 3