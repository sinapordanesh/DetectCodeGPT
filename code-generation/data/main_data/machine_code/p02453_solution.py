def lower_bound(n, arr, q, queries):
    result = []
    for k in queries:
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < k:
                left = mid + 1
            else:
                right = mid
        result.append(left)
    return result

# Sample Input
n = 4
arr = [1, 2, 2, 4]
q = 3
queries = [2, 3, 5]

# Sample Output
print(lower_bound(n, arr, q, queries))