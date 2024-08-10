def max_gem_value(N, V, C):
    max_value = 0
    for i in range(2 ** N):
        X = 0
        Y = 0
        for j in range(N):
            if (i >> j) & 1:
                X += V[j]
                Y += C[j]
        max_value = max(max_value, X - Y)
    return max_value

# Sample Input 1
N = 3
V = [10, 2, 5]
C = [6, 3, 4]
print(max_gem_value(N, V, C))

# Sample Input 2
N = 4
V = [13, 21, 6, 19]
C = [11, 30, 6, 15]
print(max_gem_value(N, V, C))

# Sample Input 3
N = 1
V = [1]
C = [50]
print(max_gem_value(N, V, C))