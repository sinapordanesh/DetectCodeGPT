def max_profit(n, arr):
    max_profit = 0
    min_val = arr[0]
    
    for i in range(1, n):
        if arr[i] - min_val > max_profit:
            max_profit = arr[i] - min_val
        if arr[i] < min_val:
            min_val = arr[i]
    
    return max_profit

# Sample Input
n = 6
arr = [5, 3, 1, 3, 4, 3]
print(max_profit(n, arr))

n = 3
arr = [4, 3, 2]
print(max_profit(n, arr))