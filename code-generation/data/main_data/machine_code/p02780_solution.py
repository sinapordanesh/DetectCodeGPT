def max_expected_value(N, K, P):
    total_sum = sum(P[:K])
    max_sum = total_sum
    
    for i in range(K, N):
        total_sum = total_sum - P[i-K] + P[i]
        max_sum = max(max_sum, total_sum)
    
    return max_sum

# Sample Input 1
print(max_expected_value(5, 3, [1, 2, 2, 4, 5]))

# Sample Input 2
print(max_expected_value(4, 1, [6, 6, 6, 6]))

# Sample Input 3
print(max_expected_value(10, 4, [17, 13, 13, 12, 15, 20, 10, 13, 17, 11]))