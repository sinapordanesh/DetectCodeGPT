def min_colors(N, A):
    colors = {}
    for i in range(N):
        colors[A[i]] = colors.get(A[i], 0) + 1
    return max(colors.values()) 

# Sample Input 1
print(min_colors(5, [2, 1, 4, 5, 3])) 

# Sample Input 2
print(min_colors(4, [0, 0, 0, 0]))