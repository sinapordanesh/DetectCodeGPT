def max_erased_optimal_place(n, k, arr):
    max_sum = sum(arr[:k])
    current_sum = max_sum
    max_index = 0
    
    for i in range(1, n-k+1):
        current_sum = current_sum - arr[i-1] + arr[i+k-1]
        if current_sum > max_sum:
            max_sum = current_sum
            max_index = i
    
    return max_index

# Sample input
n = 5
k = 3
arr = [2, 7, 9, 5, 8]
print(max_erased_optimal_place(n, k, arr))