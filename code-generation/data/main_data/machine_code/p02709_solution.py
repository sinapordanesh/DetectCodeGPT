def max_happiness_points(N, A):
    A.sort(reverse=True)
    max_points = 0
    
    for i in range(N):
        max_points += A[i] * abs(i - (N - 1))
    
    return max_points

# Sample Input
print(max_happiness_points(4, [1, 3, 4, 2])) # Output: 20
print(max_happiness_points(6, [5, 5, 6, 1, 1, 1])) # Output: 58
print(max_happiness_points(6, [8, 6, 9, 1, 2, 1])) # Output: 85