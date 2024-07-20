def minimum_cost_to_achieve_connectivity(N, rectangles):
    rectangles.sort(key=lambda x: x[0])
    total = 0
    for i in range(N):
        total += rectangles[i][0] - (i+1)
    return total

# Sample Input 1
N = 3
rectangles = [(1, 3), (5, 7), (1, 3)]
print(minimum_cost_to_achieve_connectivity(N, rectangles))

# Sample Input 2
N = 3
rectangles = [(2, 5), (4, 6), (1, 4)]
print(minimum_cost_to_achieve_connectivity(N, rectangles))

# Sample Input 3
N = 5
rectangles = [(999999999, 1000000000), (1, 2), (314, 315), (500000, 500001), (999999999, 1000000000)]
print(minimum_cost_to_achieve_connectivity(N, rectangles))

# Sample Input 4
N = 5
rectangles = [(123456, 789012), (123, 456), (12, 345678901), (123456, 789012), (1, 23)]
print(minimum_cost_to_achieve_connectivity(N, rectangles))

# Sample Input 5
N = 1
rectangles = [(1, 400)]
print(minimum_cost_to_achieve_connectivity(N, rectangles))