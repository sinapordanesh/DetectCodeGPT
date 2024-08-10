def select_max_combination(n, a):
    max_comb = 0
    max_a_i = -1
    max_a_j = -1
    
    for i in range(n):
        for j in range(i+1, n):
            comb = (a[i] * (a[i]-1)) // 2
            if comb > max_comb:
                max_comb = comb
                max_a_i = a[i]
                max_a_j = a[j]
    
    return max_a_i, max_a_j

# Sample Input 1
n = 5
a = [6, 9, 4, 2, 11]
print(*select_max_combination(n, a))

# Sample Input 2
n = 2
a = [100, 0]
print(*select_max_combination(n, a))