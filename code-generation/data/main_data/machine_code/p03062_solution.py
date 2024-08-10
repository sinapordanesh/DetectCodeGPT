def max_sum_after_operations(N, A):
    neg_count = 0
    min_abs = float('inf')
    total_sum = 0
    
    for i in range(N):
        total_sum += abs(A[i])
        if A[i] < 0:
            neg_count += 1
        min_abs = min(min_abs, abs(A[i]))
    
    if neg_count % 2 == 0:
        return total_sum
    else:
        return total_sum - 2 * min_abs

# Input
N = int(input())
A = list(map(int, input().split()))

# Output
print(max_sum_after_operations(N, A))