def min_absolute_diff(N, A):
    A = [0] + A
    sums = [0] * (N+1)
    for i in range(1, N+1):
        sums[i] = sums[i-1] + A[i]
    
    result = float('inf')
    for i in range(1, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                sum1 = sums[i]
                sum2 = sums[j] - sums[i]
                sum3 = sums[k] - sums[j]
                sum4 = sums[N] - sums[k]
                result = min(result, max(sum1, sum2, sum3, sum4) - min(sum1, sum2, sum3, sum4))
    
    return result

# Sample Input
print(min_absolute_diff(5, [3, 2, 4, 1, 2])) # Output: 2
print(min_absolute_diff(10, [10, 71, 84, 33, 6, 47, 23, 25, 52, 64])) # Output: 36
print(min_absolute_diff(7, [1, 2, 3, 1000000000, 4, 5, 6])) # Output: 999999994