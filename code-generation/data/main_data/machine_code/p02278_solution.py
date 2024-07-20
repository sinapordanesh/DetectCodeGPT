def min_cost_sort(n, arr):
    arr.sort()
    total_cost = 0
    for i in range(n):
        total_cost += arr[i] * (i + 1)
    return total_cost

n = 5
arr = [1, 5, 3, 4, 2]
print(min_cost_sort(n, arr))

n = 4
arr = [4, 3, 2, 1]
print(min_cost_sort(n, arr))