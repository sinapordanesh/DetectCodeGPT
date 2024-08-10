def min_distance(A, B, Q, shrines, temples, queries):
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return 0
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if right < 0:
            return abs(arr[left] - target)
        if left >= len(arr):
            return abs(arr[right] - target)
        return min(abs(arr[left] - target), abs(arr[right] - target))

    result = []
    for query in queries:
        min_dist = float('inf')
        for shrine in shrines:
            for temple in temples:
                dist1 = abs(shrine - query)
                dist2 = abs(temple - shrine)
                total_dist = dist1 + dist2
                min_dist = min(min_dist, total_dist)
        result.append(min_dist)
    return result

# Sample Input 1
print(min_distance(2, 3, 4, [100, 600], [400, 900, 1000], [150, 2000, 899, 799]))

# Sample Input 2
print(min_distance(1, 1, 3, [1], [10000000000], [2, 9999999999, 5000000000]))