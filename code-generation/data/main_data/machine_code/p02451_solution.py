def binary_search(n, A, q, queries):
    def binary_search_helper(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return 0
    
    result = []
    for query in queries:
        result.append(binary_search_helper(A, query))
    
    return result

# Sample input
n = 4
A = [1, 2, 2, 4]
q = 3
queries = [2, 3, 5]
print(binary_search(n, A, q, queries))