def min_distance(N, houses):
    houses.sort()
    return max(houses[-1] - houses[0], (houses[-1] - houses[1]) + (houses[-2] - houses[0]))

# Sample Input 1
print(min_distance(4, [2, 3, 7, 9])) 

# Sample Input 2
print(min_distance(8, [3, 1, 4, 1, 5, 9, 2, 6]))