def min_fatigue_level(N, A, B, X):
    min_fatigue = 0
    for i in range(N-1):
        walk_distance = X[i+1] - X[i]
        min_fatigue += min(A * walk_distance, B)
    return min_fatigue

# Sample Input 1
N = 4
A = 2
B = 5
X = [1, 2, 5, 7]
print(min_fatigue_level(N, A, B, X))

# Sample Input 2
N = 7
A = 1
B = 100
X = [40, 43, 45, 105, 108, 115, 124]
print(min_fatigue_level(N, A, B, X))

# Sample Input 3
N = 7
A = 1
B = 2
X = [24, 35, 40, 68, 72, 99, 103]
print(min_fatigue_level(N, A, B, X))