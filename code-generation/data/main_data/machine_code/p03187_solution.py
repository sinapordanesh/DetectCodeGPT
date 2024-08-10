def longest_distance(L, N, trees):
    trees.sort()
    max_dist = max(trees[0], L - trees[-1])
    
    for i in range(N-1):
        max_dist = max(max_dist, trees[i+1] - trees[i])
    
    return L + max_dist

# Sample Input 1
print(longest_distance(10, 3, [2, 7, 9]))

# Sample Input 2
print(longest_distance(10, 6, [1, 2, 3, 6, 7, 9]))

# Sample Input 3
print(longest_distance(314159265, 7, [21662711, 77271666, 89022761, 156626166, 160332356, 166902656, 298992265]))