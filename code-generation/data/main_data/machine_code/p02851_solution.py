def find_contiguous_subsequences(N, K, A):
    count = 0
    prefix_sum_count = {0: 1}
    prefix_sum = 0
    for num in A:
        prefix_sum = (prefix_sum + num) % K
        count += prefix_sum_count.get((prefix_sum - len(prefix_sum_count)) % K, 0)
        prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1
    return count

# Sample Input 1
print(find_contiguous_subsequences(5, 4, [1, 4, 2, 3, 5])) 

# Sample Input 2
print(find_contiguous_subsequences(8, 4, [4, 2, 4, 2, 4, 2, 4, 2])) 

# Sample Input 3
print(find_contiguous_subsequences(10, 7, [14, 15, 92, 65, 35, 89, 79, 32, 38, 46]))