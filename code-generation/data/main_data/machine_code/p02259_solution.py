def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(n-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swaps += 1
    return arr, swaps

# Sample Input 1
arr1 = [5, 3, 2, 4, 1]
print(*bubble_sort(arr1))

# Sample Input 2
arr2 = [5, 2, 4, 6, 1, 3]
print(*bubble_sort(arr2))