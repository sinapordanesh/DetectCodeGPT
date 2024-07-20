def min_operations(N, x, arr):
    operations = 0
    for i in range(1, N):
        if arr[i] + arr[i-1] > x:
            diff = (arr[i] + arr[i-1]) - x
            operations += diff
            if arr[i] >= diff:
                arr[i] -= diff
            else:
                arr[i-1] -= (diff - arr[i])
                arr[i] = 0
    return operations

# Sample Input 1
print(min_operations(3, 3, [2, 2, 2]))

# Sample Input 2
print(min_operations(6, 1, [1, 6, 1, 2, 0, 4]))

# Sample Input 3
print(min_operations(5, 9, [3, 1, 4, 1, 5]))

# Sample Input 4
print(min_operations(2, 0, [5, 5]))